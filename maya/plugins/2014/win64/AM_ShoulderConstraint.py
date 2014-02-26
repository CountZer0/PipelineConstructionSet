"""
A node and corresponding command to constrain the first twist joint in a
shoulder. The node also outputs the shoulder's spine-space elevation angle for
other nodes to use.

\b Creation \b Info:

\b Donations: http://adammechtley.com/donations/

\b License: The MIT License

Copyright (c) 2011 Adam Mechtley (http://adammechtley.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the 'Software'), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

\b Usage:
Add this file to your plug-in path and load it in Maya from the Plug-in
Manager (Window -> Settings/Preferences -> Plug-in Manager).

\namespace AM_ShoulderConstraint
"""

import math, re, sys
import maya.OpenMaya as OM
import maya.OpenMayaMPx as OMMPx

## current version of the plug-in
kVersionNumber = '1.06'

# ----------------------------------------------------------------
# Command Definition
# ----------------------------------------------------------------
class AM_ShoulderConstraintCmd(OMMPx.MPxCommand):
    """
	A command to quickly create, edit, or query an am_shoulderConstraint node.
	"""

    ## the name of the command
    kPluginCmdName = 'am_shoulderConstraint'

    ## specifies a name for the am_shoulderConstraint node (CE)
    kNameFlag = '-n'
    kNameFlagLong = '-name'
    ## the shoulder object (CEQ)
    kShoulderObjectFlag = '-sh'
    kShoulderObjectFlagLong = '-shoulderObject'
    ## the spine object (CEQ)
    kSpineObjectFlag = '-sp'
    kSpineObjectFlagLong = '-spineObject'
    ## twist offset when the arm is raised (CEQ)
    kRaisedAngleFlag = '-rao'
    kRaisedAngleFlagLong = '-raisedAngleOffset'
    ## local axis of the shoulder that aims at the elbow (CEQ)
    kShoulderAimFlag = '-sha'
    kShoulderAimFlagLong = '-shoulderAim'
    ## local axis of the shoulder that points toward the character's front (CEQ)
    kShoulderFrontFlag = '-shf'
    kShoulderFrontFlagLong = '-shoulderFront'
    ## local axis of the spine that points up toward the head (CEQ)
    kSpineAimFlag = '-spa'
    kSpineAimFlagLong = '-spineAim'
    ## local axis of the spine that points toward the character's front (CEQ)
    kSpineFrontFlag = '-spf'
    kSpineFrontFlagLong = '-spineFront'

    def __init__(self):
        OMMPx.MPxCommand.__init__(self)
        self.__isQueryUsed = True  # initialize to True so command is not added to queue if argument parsing fails
        self.__isEditUsed = False  # if the edit flag has been set, then undo will be enabled

        self.__shoulderConstraintNodeArg = OM.MObject()  # the am_exposeTransform node selected for edit and query modes
        self.__shoulderConstraintNodeFn = OM.MFnDependencyNode()
        self.__shoulderConstraintNodeName = ''

        self.__constrainedObjectArg = OM.MDagPath()  # the helper joint whose rotation is constrained
        self.__shoulderObjectArg = OM.MDagPath()  # the shoulder object to which the helper joint is constrained
        self.__spineObjectArg = OM.MDagPath()  # the spine object (ribcage)

        self.__raisedAngleArg = 45.0  # amount up-vector rotates back from lateral direction when arm is raised

        self.__shoulderAimAxisArg = OM.MVector(1, 0, 0)
        self.__shoulderFrontAxisArg = OM.MVector(0, 0, 1)
        self.__spineAimAxisArg = OM.MVector(1, 0, 0)
        self.__spineFrontAxisArg = OM.MVector(0, 0, 1)

        self.__dgModify = OM.MDGModifier()  # DG modifier used to create and modify nodes

    def doIt(self, args):
        # parse the arguments
        try:
            argData = OM.MArgDatabase(self.syntax(), args)  # if this fails, it will raise its own exception...
        except:
            pass  # ...so we can just pass here
        else:
            # read all of the arguments and store them to the appropriate data attributes
            # manually confirm the object list
            sel = OM.MSelectionList()
            argData.getObjects(sel)
            # ordinarily, the command is designed to only operate on a single object at a time
            if not sel.length() == 1:
                # edit and query mode require one object
                if argData.isEdit() or argData.isQuery():
                    raise Exception(
                        'This command requires exactly 1 argument to be specified or selected;  found %i.' % sel.length())
                # create mode supports a variety of patterns
                else:
                    isShoulderSpecified = argData.isFlagSet(AM_ShoulderConstraintCmd.kShoulderObjectFlag)
                    isSpineSpecified = argData.isFlagSet(AM_ShoulderConstraintCmd.kSpineObjectFlag)
                    # selection list is either [spine, constraintObject] with shoulder flag, or [shoulder, constrainedObject] with spine flag
                    if sel.length() == 2:
                        if not (isShoulderSpecified or isSpineSpecified):
                            raise Exception(
                                'Selection list of length 2 requires either a spine or a shoulder be specified with a flag.')
                        else:
                            if isSpineSpecified:
                                sel.add(argData.flagArgumentString(AM_ShoulderConstraintCmd.kSpineObjectFlag, 0))
                                sel.getDagPath(sel.length() - 1, self.__spineObjectArg)
                            else:
                                sel.getDagPath(0, self.__spineObjectArg)
                            if isShoulderSpecified:
                                sel.add(argData.flagArgumentString(AM_ShoulderConstraintCmd.kShoulderObjectFlag, 0))
                                sel.getDagPath(sel.length() - 1, self.__shoulderObjectArg)
                            else:
                                sel.getDagPath(0, self.__shoulderObjectArg)
                            sel.getDagPath(1, self.__constrainedObjectArg)
                    # selection list is either [spine, shoulder, constraintObject], or has spine or shoulder specified with flags
                    elif sel.length() == 3:
                        if isSpineSpecified:
                            sel.add(argData.flagArgumentString(AM_ShoulderConstraintCmd.kSpineObjectFlag, 0))
                            sel.getDagPath(sel.length() - 1, self.__spineObjectArg)
                        else:
                            sel.getDagPath(0, self.__spineObjectArg)
                        if isShoulderSpecified:
                            sel.add(argData.flagArgumentString(AM_ShoulderConstraintCmd.kSpineObjectFlag, 0))
                            sel.getDagPath(sel.length() - 1, self.__shoulderObjectArg)
                        else:
                            sel.getDagPath(1, self.__shoulderObjectArg)
                        sel.getDagPath(2, self.__constrainedObjectArg)
                    else:
                        raise Exception(
                            'This command requires 3 or fewer arguments to be specified or selected;  found %i.' % sel.length())
            else:
                iter = OM.MItSelectionList(sel, OM.MFn.kDependencyNode)
                while not iter.isDone():
                    # in edit or query mode, the object must be an am_shoulderConstraint node
                    if argData.isEdit() or argData.isQuery():
                        iter.getDependNode(self.__shoulderConstraintNodeArg)
                        self.__shoulderConstraintNodeFn.setObject(self.__shoulderConstraintNodeArg)
                        if not (self.__shoulderConstraintNodeFn.typeId() == AM_ShoulderConstraintNode.kPluginNodeId):
                            raise Exception('The provided dependency node %s is not of type %s.' % (
                                self.__shoulderConstraintNodeFn.name(), AM_ShoulderConstraintNode.kPluginNodeTypeName))
                    # in create mode, only a transform node is accepted
                    else:
                        selectedObject = OM.MObject()
                        iter.getDependNode(selectedObject)
                        if selectedObject.hasFn(OM.MFn.kTransform):
                            OM.MDagPath.getAPathTo(selectedObject, self.__constrainedObjectArg)
                        else:
                            selectedObjectFn = OM.MFnDependencyNode(selectedObject)
                            raise Exception('%s is not a valid transform node.' % selectedObjectFn.name())
                        # verify that a shoulder and spine have been specified
                        if not argData.isFlagSet(AM_ShoulderConstraintCmd.kShoulderObjectFlag) or not argData.isFlagSet(
                                AM_ShoulderConstraintCmd.kSpineObjectFlag):
                            raise Exception(
                                'When only one argument is specified in create mode, shoulder and spine flags must be present.')
                    iter.next()

            # perform the query
            if argData.isQuery():
                self.__shoulderObjectArg = argData.isFlagSet(AM_ShoulderConstraintCmd.kShoulderObjectFlag)
                self.__spineObjectArg = argData.isFlagSet(AM_ShoulderConstraintCmd.kSpineObjectFlag)
                self.__raisedAngleArg = argData.isFlagSet(AM_ShoulderConstraintCmd.kRaisedAngleFlag)
                self.__shoulderAimAxisArg = argData.isFlagSet(AM_ShoulderConstraintCmd.kShoulderAimFlag)
                self.__shoulderFrontAxisArg = argData.isFlagSet(AM_ShoulderConstraintCmd.kShoulderFrontFlag)
                self.__spineAimAxisArg = argData.isFlagSet(AM_ShoulderConstraintCmd.kSpineAimFlag)
                self.__spineFrontAxisArg = argData.isFlagSet(AM_ShoulderConstraintCmd.kSpineFrontFlag)
                self.doItQuery()
            # set up other arguments and call redoIt() for create or edit mode
            else:
                # validate the name flag
                if argData.isFlagSet(AM_ShoulderConstraintCmd.kNameFlag):
                    self.__shoulderConstraintNodeName = argData.flagArgumentString(AM_ShoulderConstraintCmd.kNameFlag,
                                                                                   0)
                    if (len(self.__shoulderConstraintNodeName) < 1 or self.__shoulderConstraintNodeName[
                        0].isalpha() is False or len(re.split('\W+', self.__shoulderConstraintNodeName)) > 1):
                        raise Exception(
                            '%s is not a valid node name. Did you type it correctly?' % self.__shoulderConstraintNodeName)
                # validate dagpaths
                sel = OM.MSelectionList()
                if argData.isFlagSet(AM_ShoulderConstraintCmd.kShoulderObjectFlag):
                    sel.clear()
                    try:
                        sel.add(argData.flagArgumentString(AM_ShoulderConstraintCmd.kShoulderObjectFlag, 0))
                        sel.getDagPath(0, self.__shoulderObjectArg)
                    except:
                        raise Exception(
                            '%s is not a valid node name. Did you type it correctly?' % argData.flagArgumentString(
                                AM_ShoulderConstraintCmd.kShoulderObjectFlag, 0))
                if argData.isFlagSet(AM_ShoulderConstraintCmd.kSpineObjectFlag):
                    sel.clear()
                    try:
                        sel.add(argData.flagArgumentString(AM_ShoulderConstraintCmd.kSpineObjectFlag, 0))
                        sel.getDagPath(0, self.__spineObjectArg)
                    except:
                        raise Exception(
                            '%s is not a valid node name. Did you type it correctly?' % argData.flagArgumentString(
                                AM_ShoulderConstraintCmd.kSpineObjectFlag, 0))
                # get raised angle arg
                if argData.isFlagSet(AM_ShoulderConstraintCmd.kRaisedAngleFlag):
                    self.__raisedAngleArg = argData.flagArgumentString(AM_ShoulderConstraintCmd.kRaisedAngleFlag, 0)
                else:
                    self.__raisedAngleArg = None
                # get vector args
                if argData.isFlagSet(AM_ShoulderConstraintCmd.kShoulderAimFlag):
                    self.__shoulderAimAxisArg = OM.MVector(
                        argData.flagArgumentDouble(AM_ShoulderConstraintCmd.kShoulderAimFlag, 0),
                        argData.flagArgumentDouble(AM_ShoulderConstraintCmd.kShoulderAimFlag, 1),
                        argData.flagArgumentDouble(AM_ShoulderConstraintCmd.kShoulderAimFlag, 2))
                if argData.isFlagSet(AM_ShoulderConstraintCmd.kShoulderFrontFlag):
                    self.__shoulderFrontAxisArg = OM.MVector(
                        argData.flagArgumentDouble(AM_ShoulderConstraintCmd.kShoulderFrontFlag, 0),
                        argData.flagArgumentDouble(AM_ShoulderConstraintCmd.kShoulderFrontFlag, 1),
                        argData.flagArgumentDouble(AM_ShoulderConstraintCmd.kShoulderFrontFlag, 2))
                if argData.isFlagSet(AM_ShoulderConstraintCmd.kSpineAimFlag):
                    self.__spineAimAxisArg = OM.MVector(
                        argData.flagArgumentDouble(AM_ShoulderConstraintCmd.kSpineAimFlag, 0),
                        argData.flagArgumentDouble(AM_ShoulderConstraintCmd.kSpineAimFlag, 1),
                        argData.flagArgumentDouble(AM_ShoulderConstraintCmd.kSpineAimFlag, 2))
                if argData.isFlagSet(AM_ShoulderConstraintCmd.kSpineFrontFlag):
                    self.__spineFrontAxisArg = OM.MVector(
                        argData.flagArgumentDouble(AM_ShoulderConstraintCmd.kSpineFrontFlag, 0),
                        argData.flagArgumentDouble(AM_ShoulderConstraintCmd.kSpineFrontFlag, 1),
                        argData.flagArgumentDouble(AM_ShoulderConstraintCmd.kSpineFrontFlag, 2))
                # set the isEditUsed flag only after all arguments have been stored to ensure command is not added to queue before it has done anything
                self.__isEditUsed = argData.isEdit()
                self.__isQueryUsed = False
                self.redoIt()

    def doItQuery(self):
        # query mode typically only supports one argument at a time
        # this principle ensures that the result will be given in a way that can be stored in a variable
        path = OM.MDagPath()
        doubleArray = OM.MScriptUtil()
        if self.__shoulderObjectArg:
            plug = OM.MPlug(
                self.__shoulderConstraintNodeFn.findPlug(AM_ShoulderConstraintNode.kShoulderObjectAttrName, True))
            iter = OM.MItDependencyGraph(plug, OM.MFn.kTransform, OM.MItDependencyGraph.kUpstream)
            while not iter.isDone():
                OM.MDagPath.getAPathTo(iter.currentItem(), path)
                iter.next()
            self.setResult(path.partialPathName())
        elif self.__spineObjectArg:
            plug = OM.MPlug(
                self.__shoulderConstraintNodeFn.findPlug(AM_ShoulderConstraintNode.kSpineObjectAttrName, True))
            iter = OM.MItDependencyGraph(plug, OM.MFn.kTransform, OM.MItDependencyGraph.kUpstream)
            while not iter.isDone():
                OM.MDagPath.getAPathTo(iter.currentItem(), path)
                iter.next()
            self.setResult(path.partialPathName())
        elif self.__raisedAngleArg:
            self.setResult(OM.MPlug(
                self.__shoulderConstraintNodeFn.findPlug(AM_ShoulderConstraintNode.kRaisedAngleAttrName,
                                                         True)).asDouble())
        elif self.__shoulderAimAxisArg:
            doubleArray.createFromDouble(
                OM.MPlug(
                    self.__shoulderConstraintNodeFn.findPlug('%s0' % AM_ShoulderConstraintNode.kShoulderAimAttrName,
                                                             True)).asDouble(),
                OM.MPlug(
                    self.__shoulderConstraintNodeFn.findPlug('%s1' % AM_ShoulderConstraintNode.kShoulderAimAttrName,
                                                             True)).asDouble(),
                OM.MPlug(
                    self.__shoulderConstraintNodeFn.findPlug('%s2' % AM_ShoulderConstraintNode.kShoulderAimAttrName,
                                                             True)).asDouble())
            self.setResult(OM.MDoubleArray(doubleArray.asDoublePtr(), 3))
        elif self.__shoulderFrontAxisArg:
            doubleArray.createFromDouble(
                OM.MPlug(
                    self.__shoulderConstraintNodeFn.findPlug('%s0' % AM_ShoulderConstraintNode.kShoulderFrontAttrName,
                                                             True)).asDouble(),
                OM.MPlug(
                    self.__shoulderConstraintNodeFn.findPlug('%s1' % AM_ShoulderConstraintNode.kShoulderFrontAttrName,
                                                             True)).asDouble(),
                OM.MPlug(
                    self.__shoulderConstraintNodeFn.findPlug('%s2' % AM_ShoulderConstraintNode.kShoulderFrontAttrName,
                                                             True)).asDouble())
            self.setResult(OM.MDoubleArray(doubleArray.asDoublePtr(), 3))
        elif self.__spineAimAxisArg:
            doubleArray.createFromDouble(
                OM.MPlug(self.__shoulderConstraintNodeFn.findPlug('%s0' % AM_ShoulderConstraintNode.kSpineAimAttrName,
                                                                  True)).asDouble(),
                OM.MPlug(self.__shoulderConstraintNodeFn.findPlug('%s1' % AM_ShoulderConstraintNode.kSpineAimAttrName,
                                                                  True)).asDouble(),
                OM.MPlug(self.__shoulderConstraintNodeFn.findPlug('%s2' % AM_ShoulderConstraintNode.kSpineAimAttrName,
                                                                  True)).asDouble())
            self.setResult(OM.MDoubleArray(doubleArray.asDoublePtr(), 3))
        elif self.__spineFrontAxisArg:
            doubleArray.createFromDouble(
                OM.MPlug(self.__shoulderConstraintNodeFn.findPlug('%s0' % AM_ShoulderConstraintNode.kSpineFrontAttrName,
                                                                  True)).asDouble(),
                OM.MPlug(self.__shoulderConstraintNodeFn.findPlug('%s1' % AM_ShoulderConstraintNode.kSpineFrontAttrName,
                                                                  True)).asDouble(),
                OM.MPlug(self.__shoulderConstraintNodeFn.findPlug('%s2' % AM_ShoulderConstraintNode.kSpineFrontAttrName,
                                                                  True)).asDouble())
            self.setResult(OM.MDoubleArray(doubleArray.asDoublePtr(), 3))

    def redoIt(self):
        # clear out the modifier so it doesn't store old object names
        self.__dgModify = OM.MDGModifier()

        # create a new node if the command is in create mode
        if not self.__isEditUsed:
            self.__shoulderConstraintNodeArg = OM.MObject(
                self.__dgModify.createNode(AM_ShoulderConstraintNode.kPluginNodeId))
            self.__shoulderConstraintNodeFn.setObject(self.__shoulderConstraintNodeArg)
            fn = OM.MFnDagNode(self.__constrainedObjectArg)
            self.__dgModify.renameNode(self.__shoulderConstraintNodeArg, '%s_shoulderConstraint' % fn.name())
        # assign the -name argument if provided
        if len(self.__shoulderConstraintNodeName) > 0:
            self.__dgModify.renameNode(self.__shoulderConstraintNodeArg, self.__shoulderConstraintNodeName)
        # WARNING: must tell the DGModifier to doIt() now in order to let Maya's auto-rename kick in and ensure the name is unique
        # otherwise attempts to use commandToExecute below may end up using some other object
        self.__dgModify.doIt()

        # set the attributes on the node
        plug = OM.MPlug()
        if self.__constrainedObjectArg.isValid():
            self.__dgModify.commandToExecute('connectAttr -f %s.%s %s.rotate' % (
                self.__shoulderConstraintNodeFn.name(), AM_ShoulderConstraintNode.kRotateAttrName,
                self.__constrainedObjectArg.partialPathName()))
            self.__dgModify.commandToExecute('connectAttr -f %s.rotateOrder %s.%s' % (
                self.__constrainedObjectArg.partialPathName(),
                self.__shoulderConstraintNodeFn.name(), AM_ShoulderConstraintNode.kRotateOrderAttrName))
            self.__dgModify.commandToExecute('connectAttr -f %s.parentInverseMatrix %s.%s' % (
                self.__constrainedObjectArg.partialPathName(),
                self.__shoulderConstraintNodeFn.name(), AM_ShoulderConstraintNode.kParentInvMatrixAttrName))
        if self.__shoulderObjectArg.isValid():
            self.__dgModify.commandToExecute('connectAttr -f %s.worldMatrix %s.%s' % (
                self.__shoulderObjectArg.partialPathName(),
                self.__shoulderConstraintNodeFn.name(), AM_ShoulderConstraintNode.kShoulderObjectAttrName))
            if not self.__shoulderObjectArg.hasFn(OM.MFn.kJoint):
                self.__dgModify.commandToExecute('connectAttr -f %s.rotatePivot %s.%s' % (
                    self.__shoulderObjectArg.partialPathName(),
                    self.__shoulderConstraintNodeFn.name(), AM_ShoulderConstraintNode.kShoulderRotatePivotAttrName))
        if self.__spineObjectArg.isValid():
            self.__dgModify.commandToExecute('connectAttr -f %s.worldMatrix %s.%s' % (
                self.__spineObjectArg.partialPathName(),
                self.__shoulderConstraintNodeFn.name(), AM_ShoulderConstraintNode.kSpineObjectAttrName))
            if not self.__spineObjectArg.hasFn(OM.MFn.kJoint):
                self.__dgModify.commandToExecute('connectAttr -f %s.rotatePivot %s.%s' % (
                    self.__spineObjectArg.partialPathName(),
                    self.__shoulderConstraintNodeFn.name(), AM_ShoulderConstraintNode.kSpineRotatePivotAttrName))
        if self.__raisedAngleArg is not None:
            # set the raisedAngleOffset attribute if it is not connected
            plug = self.__shoulderConstraintNodeFn.findPlug(AM_ShoulderConstraintNode.kRaisedAngleAttrName, True)
            if not plug.isConnected():
                self.__dgModify.commandToExecute('setAttr %s.%s %s' % (
                    self.__shoulderConstraintNodeFn.name(), AM_ShoulderConstraintNode.kRaisedAngleAttrName,
                    self.__raisedAngleArg))
        # set vector attribute values
        vectorArgs = {
            self.__shoulderAimAxisArg: AM_ShoulderConstraintNode.kShoulderAimAttrName,
            self.__shoulderFrontAxisArg: AM_ShoulderConstraintNode.kShoulderFrontAttrName,
            self.__spineAimAxisArg: AM_ShoulderConstraintNode.kSpineAimAttrName,
            self.__spineFrontAxisArg: AM_ShoulderConstraintNode.kSpineFrontAttrName
        }
        for vArg in vectorArgs:
            if not vArg:
                continue
            # set the vector attribute if it is not connected
            plug = self.__shoulderConstraintNodeFn.findPlug(vectorArgs[vArg], True)
            if not plug.isConnected():
                self.__dgModify.commandToExecute('setAttr %s.%s %s %s %s' % (
                    self.__shoulderConstraintNodeFn.name(),
                    vectorArgs[vArg], vArg.x, vArg.y, vArg.z))

        # following Maya convention, select the newly created node if the command is in create mode
        if not self.__isEditUsed:
            self.__dgModify.commandToExecute('select %s' % self.__shoulderConstraintNodeFn.name())
        self.__dgModify.doIt()
        self.setResult(self.__shoulderConstraintNodeFn.name())

    def undoIt(self):
        self.__dgModify.undoIt()

    def isUndoable(self):
        # the command should only be undoable if edit or create mode was used
        return not self.__isQueryUsed

    @classmethod
    def cmdCreator(cls):
        return OMMPx.asMPxPtr(cls())

    @classmethod
    def syntaxCreator(cls):
        syntax = OM.MSyntax()
        syntax.enableQuery()  # BUG: including these modes has benefits, but it also breaks built-in object parsing
        syntax.enableEdit()
        syntax.addFlag(cls.kNameFlag, cls.kNameFlagLong, OM.MSyntax.kString)
        syntax.addFlag(cls.kSpineObjectFlag, cls.kSpineObjectFlagLong, OM.MSyntax.kSelectionItem)
        syntax.addFlag(cls.kShoulderObjectFlag, cls.kShoulderObjectFlagLong, OM.MSyntax.kSelectionItem)
        syntax.addFlag(cls.kRaisedAngleFlag, cls.kRaisedAngleFlagLong, OM.MSyntax.kDouble)
        syntax.addFlag(cls.kShoulderAimFlag, cls.kShoulderAimFlagLong, OM.MSyntax.kDouble, OM.MSyntax.kDouble,
                       OM.MSyntax.kDouble)
        syntax.addFlag(cls.kShoulderFrontFlag, cls.kShoulderFrontFlagLong, OM.MSyntax.kDouble, OM.MSyntax.kDouble,
                       OM.MSyntax.kDouble)
        syntax.addFlag(cls.kSpineAimFlag, cls.kSpineAimFlagLong, OM.MSyntax.kDouble, OM.MSyntax.kDouble,
                       OM.MSyntax.kDouble)
        syntax.addFlag(cls.kSpineFrontFlag, cls.kSpineFrontFlagLong, OM.MSyntax.kDouble, OM.MSyntax.kDouble,
                       OM.MSyntax.kDouble)
        syntax.useSelectionAsDefault(True)
        syntax.setObjectType(OM.MSyntax.kSelectionList, 1, 3)
        return syntax


# ----------------------------------------------------------------
# Node definition
# ----------------------------------------------------------------
class AM_ShoulderConstraintNode(OMMPx.MPxNode):
    """
	A node to constrain the first twist joint in a shoulder. The node also
	outputs the shoulder's spine-space elevation angle for other nodes to use.
	\par Input Attributes:
		- \em rotateOrder: The rotateOrder attribute of the constrained object.
		- \em raisedAngleOffset: The amount that the constrained object's
			up-vector rotates back when the shoulder is raised. A value between
			0 and 90 is ideal and should eliminate flipping in a normal human
			range of motion. A value of 45 is recommended in most cases.
		- \em shoulderAimAxis: Axis in the upper arm's local space that aims
			toward the elbow joint.
		- \em shoulderFrontAxis: Axis in the upper arm's local space that
			points toward the character's front.
		- \em spineAimAxis: Axis in the specified spine joint's local space
			that aims toward the next vertebra (up).
		- \em spineFrontAxis: Axis in the specified spine joint's local space
			that aims toward the character's front.
		- \em rotatePivot: The rotatePivot attribute of the upper arm.
		- \em jointOrient: The jointOrient attribute of the constrained object
			if it is a joint. If there is no connection (i.e., the constrained
			object is not a joint), then it is initialized to identity and has
			no effect.
		- \em spineWorldMatrix: The worldMatrix attribute of the object to use
			for computing the shoulder's elevation angle. The shoulder
			constraint is designed with the expectation that this is the the
			first common parent of both of the upper arms (usually the
			ribcage). Although this joint will produce perfectly valid values
			if any intermediate joints exist (collar bone, scapula), such an
			intermediate joint could be used instead, provided that the axes
			given for the spine node (above) are transformed into the
			intermediate joint's local space.
		- \em shoulderWorldMatrix: The worldMatrix attribute of the upper arm
			object along whose aim axis (above) the constrained object is
			twisting.
		- \em parentInverseMatrix: The parentInverseMatrix attribute of the
			constrained object.
	\par Output Attributes:
		- \em rotate: The local Euler rotation piped to the constrained object.
		- \em elevationAngle: The elevation angle of the shoulder in spine
			space.
	"""

    ## the name of the nodeType
    kPluginNodeTypeName = 'am_shoulderConstraint'
    ## the unique MTypeId for the node
    kPluginNodeId = OM.MTypeId(0x001138C0)

    # input attributes
    ## the constrained node's rotateOrder attribute
    rotateOrder = OM.MObject()
    kRotateOrderAttrName = 'rotateOrder'
    kRotateOrderAttrLongName = 'constraintRotateOrder'
    ## twist offset when the arm is raised
    raisedAngleOffset = OM.MObject()
    kRaisedAngleAttrName = 'raisedOffset'
    kRaisedAngleAttrLongName = 'raisedAngleOffset'
    ## local axis of the shoulder that aims at the elbow
    shoulderAim = OM.MObject()
    kShoulderAimAttrName = 'shoulderAim'
    kShoulderAimAttrLongName = 'shoulderAimAxis'
    ## local axis of the shoulder that points toward the character's front
    shoulderFront = OM.MObject()
    kShoulderFrontAttrName = 'shoulderFront'
    kShoulderFrontAttrLongName = 'shoulderFrontAxis'
    ## local axis of the spine that points up toward the head
    spineAim = OM.MObject()
    kSpineAimAttrName = 'spineAim'
    kSpineAimAttrLongName = 'spineAimAxis'
    ## local axis of the spine that points toward the character's front
    spineFront = OM.MObject()
    kSpineFrontAttrName = 'spineFront'
    kSpineFrontAttrLongName = 'spineFrontAxis'
    ## the rotatePivot attribute of the shoulder object
    shoulderPivot = OM.MObject()
    kShoulderRotatePivotAttrName = 'shoulderPivot'
    kShoulderRotatePivotAttrLongName = 'shoulderRotatePivot'
    ## the rotatePivot attribute of the spine object
    spinePivot = OM.MObject()
    kSpineRotatePivotAttrName = 'spinePivot'
    kSpineRotatePivotAttrLongName = 'spineRotatePivot'
    ## the jointOrient (XYZ Euler offset) attribute of the constrained object
    jointOrient = OM.MObject()
    kJointOrientAttrName = 'orient'
    kJointOrientAttrLongName = 'jointOrient'
    ## the shoulder object
    shoulder = OM.MObject()
    kShoulderObjectAttrName = 'shoulder'
    kShoulderObjectAttrLongName = 'shoulderWorldMatrix'
    ## the spine object
    spine = OM.MObject()
    kSpineObjectAttrName = 'spine'
    kSpineObjectAttrLongName = 'spineWorldMatrix'
    ## parentInverseMatrix of the constrained transform
    parentInverseMatrix = OM.MObject()
    kParentInvMatrixAttrName = 'parent'
    kParentInvMatrixAttrLongName = 'parentInverseMatrix'

    # output attributes
    # local rotation for constrained object
    rotate = OM.MObject()
    kRotateAttrName = 'rotate'
    kRotateAttrLongName = 'constraintRotate'
    # elevation angle of the shoulder
    angle = OM.MObject()
    kElevationAngleAttrName = 'angle'
    kElevationAngleAttrLongName = 'elevationAngle'

    def __init__(self):
        OMMPx.MPxNode.__init__(self)

    def compute(self, plug, dataBlock):
        """Compute the upper arm's elevation angle as well as the orientation for the first twist joint in the shoulder."""
        if (plug == AM_ShoulderConstraintNode.rotate or plug == AM_ShoulderConstraintNode.angle):
            # ----------------------------------------------------------------
            # Get the incoming data
            # ----------------------------------------------------------------
            # the constrained node's rotateOrder attribute
            dataHandle = dataBlock.inputValue(AM_ShoulderConstraintNode.rotateOrder)
            eRotateOrder = dataHandle.asShort()
            # angular offset for the raised orientation
            dataHandle = dataBlock.inputValue(AM_ShoulderConstraintNode.raisedAngleOffset)
            dRaisedAngleOffset = dataHandle.asDouble()
            dRaisedAngleOffset = math.radians(dRaisedAngleOffset)
            # axis pointing down the length of the upper arm
            dataHandle = dataBlock.inputValue(AM_ShoulderConstraintNode.shoulderAim)
            vShoulderForward = (dataHandle.asVector()).normal()
            # axis pointing to the character's front
            dataHandle = dataBlock.inputValue(AM_ShoulderConstraintNode.shoulderFront)
            vShoulderRight = (dataHandle.asVector()).normal()
            # axis pointing to the character's the head
            dataHandle = dataBlock.inputValue(AM_ShoulderConstraintNode.spineAim)
            vSpineForward = (dataHandle.asVector()).normal()
            # axis pointing to the character's front
            dataHandle = dataBlock.inputValue(AM_ShoulderConstraintNode.spineFront)
            vSpineUp = (dataHandle.asVector()).normal()
            # the rotatePivot attribute of the upper arm
            dataHandle = dataBlock.inputValue(AM_ShoulderConstraintNode.shoulderPivot)
            vShoulderPivot = dataHandle.asVector()
            # the rotatePivot attribute of the spine
            dataHandle = dataBlock.inputValue(AM_ShoulderConstraintNode.spinePivot)
            vSpinePivot = dataHandle.asVector()
            # the jointOrient attribute (Euler XYZ offset) of the constrained node
            dataHandle = dataBlock.inputValue(AM_ShoulderConstraintNode.jointOrient)
            vJointOrient = dataHandle.asVector()
            eJointOrient = OM.MEulerRotation(math.radians(vJointOrient.x), math.radians(vJointOrient.y),
                                             math.radians(vJointOrient.z), 0)
            qJointOrient = eJointOrient.asQuaternion()
            qJointOrient.conjugateIt()
            # the spine's worldMatrix attribute
            dataHandle = dataBlock.inputValue(AM_ShoulderConstraintNode.spine)
            mSpine = dataHandle.asMatrix()
            mSpine = OM.MTransformationMatrix(mSpine)
            qSpine = mSpine.rotation()
            # the shoulder's worldMatrix attribute
            dataHandle = dataBlock.inputValue(AM_ShoulderConstraintNode.shoulder)
            mShoulder = dataHandle.asMatrix()
            mShoulder = OM.MTransformationMatrix(mShoulder)
            qShoulder = mShoulder.rotation()
            # the constrained node's parentInverseMatrix attribute
            dataHandle = dataBlock.inputValue(AM_ShoulderConstraintNode.parentInverseMatrix)
            mParent = dataHandle.asMatrix()
            mParent = OM.MTransformationMatrix(mParent)
            qParent = mParent.rotation()

            # ----------------------------------------------------------------
            # Orthonormalize provided axes for the shoulder and spine
            # ----------------------------------------------------------------
            vShoulderUp = OM.MVector(vShoulderForward ^ vShoulderRight).normal()
            vShoulderRight = vShoulderUp ^ vShoulderForward
            vSpineRight = OM.MVector(vSpineUp ^ vSpineForward).normal()
            vSpineUp = vSpineForward ^ vSpineRight

            # ----------------------------------------------------------------
            # Determine the side of the body the shoulder is on: right is negative, left is positive
            # (assumes that the shoulder's pivot point will never cross over the spine object's central axis)
            # ----------------------------------------------------------------
            mSpine.addTranslation(-vSpinePivot, OM.MSpace.kObject)
            mShoulder.addTranslation(-vShoulderPivot, OM.MSpace.kObject)
            vSpinePosition = mSpine.getTranslation(OM.MSpace.kWorld)
            vShoulderPosition = mShoulder.getTranslation(OM.MSpace.kWorld)
            dBodySideScalar = cmp((vSpinePosition - vShoulderPosition) * vSpineRight.rotateBy(qSpine), 0.0)

            # ----------------------------------------------------------------
            # Define each of the target up-vectors corresponding to different elevations in spine space
            # ----------------------------------------------------------------
            # target up vector at rest
            vRest = vSpineForward * -dBodySideScalar
            # target up vector when lowered
            vLowered = -(vSpineForward ^ vSpineUp)
            # target up vector when raised
            vRaised = -vSpineRight.rotateBy(OM.MQuaternion(dRaisedAngleOffset, vSpineForward * -dBodySideScalar))

            # ----------------------------------------------------------------
            # Interpolate the target up-vector
            # ----------------------------------------------------------------
            # rotate the spine and shoulder vectors into their respective spaces to get the current elevation angle
            vSpineForwardRotated = vSpineForward.rotateBy(qSpine)
            vShoulderForwardRotated = vShoulderForward.rotateBy(qShoulder)
            dAngle = math.degrees(math.pi - vSpineForwardRotated.angle(vShoulderForwardRotated))

            # interpolate the up-vector based on the shoulder's angle of elevation
            dDot = vSpineForwardRotated * vShoulderForwardRotated
            vTargetUp = OM.MVector()
            if (dDot < 0):
                vTargetUp = vRest + (vLowered - vRest) * -dDot
            else:
                vTargetUp = vRest + (vRaised - vRest) * dDot

            # rotate the target up-vector into world space
            vTargetUp = vTargetUp.rotateBy(qSpine).normal()

            # ----------------------------------------------------------------
            # Compute the local orientation for the constrained node
            # ----------------------------------------------------------------
            # orthonormalize target axes and get target normal orientation for constrained object
            vTargetRight = vTargetUp ^ vShoulderForwardRotated
            vTargetUp = vShoulderForwardRotated ^ vTargetRight
            mList = [vTargetRight.x, vTargetRight.y, vTargetRight.z, 0.0,
                     vTargetUp.x, vTargetUp.y, vTargetUp.z, 0.0,
                     vShoulderForwardRotated.x, vShoulderForwardRotated.y, vShoulderForwardRotated.z, 0.0,
                     0.0, 0.0, 0.0, 1.0]
            mTarget = OM.MMatrix()
            OM.MScriptUtil.createMatrixFromList(mList, mTarget)
            qTarget = OM.MQuaternion(OM.MTransformationMatrix(mTarget).rotation())

            # get offset orientation of the constrained object (from z-forward, y-up)
            mList = [vShoulderRight.x, vShoulderRight.y, vShoulderRight.z, 0.0,
                     vShoulderUp.x, vShoulderUp.y, vShoulderUp.z, 0.0,
                     vShoulderForward.x, vShoulderForward.y, vShoulderForward.z, 0.0,
                     0.0, 0.0, 0.0, 1.0]
            mFromNormal = OM.MMatrix()
            OM.MScriptUtil.createMatrixFromList(mList, mFromNormal)
            qFromNormal = OM.MQuaternion(OM.MTransformationMatrix(mFromNormal).rotation())
            if (qFromNormal.w > 0.0):
                qFromNormal.invertIt()

            # composite final quaternion to get local-space value
            qFinal = OM.MQuaternion(qFromNormal * qTarget * qParent * qJointOrient)

            # output as Euler angles for the constrained node
            eFinal = qFinal.asEulerRotation()
            eFinal.reorderIt(eRotateOrder)

            # ----------------------------------------------------------------
            # Set the outgoing plugs
            # ----------------------------------------------------------------
            outputHandle = dataBlock.outputValue(AM_ShoulderConstraintNode.rotate)
            outputHandle.set3Double(math.degrees(eFinal.x), math.degrees(eFinal.y), math.degrees(eFinal.z))
            outputHandle = dataBlock.outputValue(AM_ShoulderConstraintNode.angle)
            outputHandle.setDouble(dAngle)
            dataBlock.setClean(plug)

        else:
            return OM.kUnknownParameter

    @classmethod
    def nodeCreator(cls):
        return OMMPx.asMPxPtr(cls())

    @classmethod
    def nodeInitializer(cls):
        # ----------------------------------------------------------------
        # Input
        # ----------------------------------------------------------------
        # the constrained node's rotateOrder attribute
        eAttr = OM.MFnEnumAttribute()
        cls.rotateOrder = eAttr.create(cls.kRotateOrderAttrLongName, cls.kRotateOrderAttrName, 0)
        eAttr.addField('xyz', 0)
        eAttr.addField('yzx', 1)
        eAttr.addField('zxy', 2)
        eAttr.addField('xzy', 3)
        eAttr.addField('yxz', 4)
        eAttr.addField('zyx', 5)
        eAttr.setWritable(1)
        eAttr.setStorable(1)
        eAttr.setReadable(1)
        eAttr.setKeyable(0)
        eAttr.setHidden(1)
        # twist offset when the arm is raised
        nAttr = OM.MFnNumericAttribute()
        cls.raisedAngleOffset = nAttr.create(cls.kRaisedAngleAttrLongName, cls.kRaisedAngleAttrName,
                                             OM.MFnNumericData.kDouble, 45.0)
        nAttr.setWritable(1)
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setKeyable(1)
        # local axis of the shoulder that aims at the elbow
        cls.shoulderAim = nAttr.create(cls.kShoulderAimAttrLongName, cls.kShoulderAimAttrName,
                                       OM.MFnNumericData.k3Double)
        nAttr.setWritable(1)
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setKeyable(0)
        # local axis of the shoulder that points toward the character's front
        cls.shoulderFront = nAttr.create(cls.kShoulderFrontAttrLongName, cls.kShoulderFrontAttrName,
                                         OM.MFnNumericData.k3Double)
        nAttr.setWritable(1)
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setKeyable(0)
        # axis on the spine joint pointing toward the head
        cls.spineAim = nAttr.create(cls.kSpineAimAttrLongName, cls.kSpineAimAttrName, OM.MFnNumericData.k3Double)
        nAttr.setWritable(1)
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setKeyable(0)
        # axis on the spine joint pointing toward the front
        cls.spineFront = nAttr.create(cls.kSpineFrontAttrLongName, cls.kSpineFrontAttrName, OM.MFnNumericData.k3Double)
        nAttr.setWritable(1)
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setKeyable(0)
        # rotatePivot attribute of the upper arm
        cls.shoulderPivot = nAttr.create(cls.kShoulderRotatePivotAttrLongName, cls.kShoulderRotatePivotAttrName,
                                         OM.MFnNumericData.k3Double)
        nAttr.setWritable(1)
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setKeyable(0)
        nAttr.setHidden(1)
        # rotatePivot attribute of the spine
        cls.spinePivot = nAttr.create(cls.kSpineRotatePivotAttrLongName, cls.kSpineRotatePivotAttrName,
                                      OM.MFnNumericData.k3Double)
        nAttr.setWritable(1)
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setKeyable(0)
        nAttr.setHidden(1)
        # joint orient (Euler XYZ offset) of the constrained transform
        cls.jointOrient = nAttr.create(cls.kJointOrientAttrLongName, cls.kJointOrientAttrName,
                                       OM.MFnNumericData.k3Double)
        nAttr.setWritable(1)
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setKeyable(0)
        nAttr.setHidden(1)
        # worldMatrix of the spine joint
        mAttr = OM.MFnMatrixAttribute()
        cls.spine = mAttr.create(cls.kSpineObjectAttrLongName, cls.kSpineObjectAttrName, OM.MFnMatrixAttribute.kDouble)
        mAttr.setWritable(1)
        mAttr.setStorable(1)
        mAttr.setReadable(1)
        mAttr.setKeyable(0)
        mAttr.setHidden(1)
        # worldMatrix of the shoulder joint
        cls.shoulder = mAttr.create(cls.kShoulderObjectAttrLongName, cls.kShoulderObjectAttrName,
                                    OM.MFnMatrixAttribute.kDouble)
        mAttr.setWritable(1)
        mAttr.setStorable(1)
        mAttr.setReadable(1)
        mAttr.setKeyable(0)
        mAttr.setHidden(1)
        # parentInverseMatrix of the constrained transform
        cls.parentInverseMatrix = mAttr.create(cls.kParentInvMatrixAttrLongName, cls.kParentInvMatrixAttrName,
                                               OM.MFnMatrixAttribute.kDouble)
        mAttr.setWritable(1)
        mAttr.setStorable(1)
        mAttr.setReadable(1)
        mAttr.setKeyable(0)
        mAttr.setHidden(1)

        # ----------------------------------------------------------------
        # Output
        # ----------------------------------------------------------------
        nAttr = OM.MFnNumericAttribute()
        # local rotation for constrained object
        cls.rotate = nAttr.create(cls.kRotateAttrLongName, cls.kRotateAttrName, OM.MFnNumericData.k3Double)
        nAttr.setWritable(1)
        nAttr.setStorable(0)
        nAttr.setReadable(1)
        # elevation angle of the shoulder
        cls.angle = nAttr.create(cls.kElevationAngleAttrLongName, cls.kElevationAngleAttrName,
                                 OM.MFnNumericData.kDouble)
        nAttr.setWritable(1)
        nAttr.setStorable(0)
        nAttr.setReadable(1)

        # ----------------------------------------------------------------
        # Add attributes
        # ----------------------------------------------------------------
        cls.addAttribute(cls.rotateOrder)
        cls.addAttribute(cls.raisedAngleOffset)
        cls.addAttribute(cls.shoulderAim)
        cls.addAttribute(cls.shoulderFront)
        cls.addAttribute(cls.spineAim)
        cls.addAttribute(cls.spineFront)
        cls.addAttribute(cls.shoulderPivot)
        cls.addAttribute(cls.spinePivot)
        cls.addAttribute(cls.jointOrient)
        cls.addAttribute(cls.spine)
        cls.addAttribute(cls.shoulder)
        cls.addAttribute(cls.parentInverseMatrix)
        cls.addAttribute(cls.rotate)
        cls.addAttribute(cls.angle)
        # establish effect upon rotate output
        cls.attributeAffects(cls.rotateOrder, cls.rotate)
        cls.attributeAffects(cls.raisedAngleOffset, cls.rotate)
        cls.attributeAffects(cls.shoulderAim, cls.rotate)
        cls.attributeAffects(cls.shoulderFront, cls.rotate)
        cls.attributeAffects(cls.spineAim, cls.rotate)
        cls.attributeAffects(cls.spineFront, cls.rotate)
        cls.attributeAffects(cls.shoulderPivot, cls.rotate)
        cls.attributeAffects(cls.spinePivot, cls.rotate)
        cls.attributeAffects(cls.jointOrient, cls.rotate)
        cls.attributeAffects(cls.spine, cls.rotate)
        cls.attributeAffects(cls.shoulder, cls.rotate)
        cls.attributeAffects(cls.parentInverseMatrix, cls.rotate)
        # establish effect upon angle output
        cls.attributeAffects(cls.rotateOrder, cls.angle)
        cls.attributeAffects(cls.raisedAngleOffset, cls.angle)
        cls.attributeAffects(cls.shoulderAim, cls.angle)
        cls.attributeAffects(cls.shoulderFront, cls.angle)
        cls.attributeAffects(cls.spineAim, cls.angle)
        cls.attributeAffects(cls.spineFront, cls.angle)
        cls.attributeAffects(cls.shoulderPivot, cls.angle)
        cls.attributeAffects(cls.spinePivot, cls.angle)
        cls.attributeAffects(cls.jointOrient, cls.angle)
        cls.attributeAffects(cls.spine, cls.angle)
        cls.attributeAffects(cls.shoulder, cls.angle)
        cls.attributeAffects(cls.parentInverseMatrix, cls.angle)


# ----------------------------------------------------------------
# Initialize the plug-in
# ----------------------------------------------------------------
def initializePlugin(mobject):
    plugin = OMMPx.MFnPlugin(mobject, 'Adam Mechtley', kVersionNumber, 'Any')
    # dependency node
    try:
        plugin.registerNode(AM_ShoulderConstraintNode.kPluginNodeTypeName, AM_ShoulderConstraintNode.kPluginNodeId,
                            AM_ShoulderConstraintNode.nodeCreator, AM_ShoulderConstraintNode.nodeInitializer)
    except:
        sys.stderr.write('Failed to register node: %s\n' % AM_ShoulderConstraintNode.kPluginNodeTypeName)
        raise
    # command
    try:
        plugin.registerCommand(AM_ShoulderConstraintCmd.kPluginCmdName, AM_ShoulderConstraintCmd.cmdCreator,
                               AM_ShoulderConstraintCmd.syntaxCreator)
    except:
        sys.stderr.write('Failed to register command: %s\n' % AM_ShoulderConstraintCmd.kPluginCmdName)
        raise


# ----------------------------------------------------------------
# Uninitialize the plug-in
# ----------------------------------------------------------------
def uninitializePlugin(mobject):
    plugin = OMMPx.MFnPlugin(mobject)
    # dependency node
    try:
        plugin.deregisterNode(AM_ShoulderConstraintNode.kPluginNodeId)
    except:
        sys.stderr.write('Failed to deregister node: %s\n' % AM_ShoulderConstraintNode.kPluginNodeTypeName)
        raise
    # command
    try:
        plugin.deregisterCommand(AM_ShoulderConstraintCmd.kPluginCmdName)
    except:
        sys.stderr.write('Failed to unregister command: %s\n' % AM_ShoulderConstraintCmd.kPluginCmdName)
        raise