"""
A node and corresponding command to constrain the first twist joint in a hip.
The node also outputs the hip's pelvis-space elevation angle for other nodes to
use.

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

\namespace AM_HipConstraint
"""

import math, re, sys
import maya.OpenMaya as OM
import maya.OpenMayaMPx as OMMPx

## current version of the plug-in
kVersionNumber = '1.04'

# ----------------------------------------------------------------
# Command Definition
# ----------------------------------------------------------------
class AM_HipConstraintCmd(OMMPx.MPxCommand):
    """
    A command to quickly create, edit, or query an am_hipConstraint node.
    """

    ## the name of the command
    kPluginCmdName = 'am_hipConstraint'

    ## specifies a name for the am_hipConstraint node (CE)
    kNameFlag = '-n'
    kNameFlagLong = '-name'
    ## the hip object (CEQ)
    kHipObjectFlag = '-h'
    kHipObjectFlagLong = '-hipObject'
    ## the pelvis object (CEQ)
    kPelvisObjectFlag = '-p'
    kPelvisObjectFlagLong = '-pelvisObject'
    ## local axis of the hip that aims at the knee (CEQ)
    kHipAimFlag = '-ha'
    kHipAimFlagLong = '-hipAim'
    ## local axis of the hip that points toward the character's front (CEQ)
    kHipFrontFlag = '-hf'
    kHipFrontFlagLong = '-hipFront'
    ## local axis of the pelvis that points up toward the head (CEQ)
    kPelvisAimFlag = '-pa'
    kPelvisAimFlagLong = '-pelvisAim'
    ## local axis of the pelvis that points toward the character's front (CEQ)
    kPelvisFrontFlag = '-pf'
    kPelvisFrontFlagLong = '-pelvisFront'

    def __init__(self):
        OMMPx.MPxCommand.__init__(self)
        self.__isQueryUsed = True  # initialize to True so command is not added to queue if argument parsing fails
        self.__isEditUsed = False  # if the edit flag has been set, then undo will be enabled

        self.__hipConstraintNodeArg = OM.MObject()  # the am_exposeTransform node selected for edit and query modes
        self.__hipConstraintNodeFn = OM.MFnDependencyNode()
        self.__hipConstraintNodeName = ''

        self.__constrainedObjectArg = OM.MDagPath()  # the helper joint whose rotation is constrained
        self.__hipObjectArg = OM.MDagPath()  # the hip object to which the helper joint is constrained
        self.__pelvisObjectArg = OM.MDagPath()  # the pelvis object (ribcage)

        self.__hipAimAxisArg = OM.MVector(1, 0, 0)
        self.__hipFrontAxisArg = OM.MVector(0, 0, 1)
        self.__pelvisAimAxisArg = OM.MVector(0, 1, 0)
        self.__pelvisFrontAxisArg = OM.MVector(0, 0, 1)

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
                    isHipSpecified = argData.isFlagSet(AM_HipConstraintCmd.kHipObjectFlag)
                    isPelvisSpecified = argData.isFlagSet(AM_HipConstraintCmd.kPelvisObjectFlag)
                    # selection list is either [pelvis, constraintObject] with hip flag, or [hip, constrainedObject] with pelvis flag
                    if sel.length() == 2:
                        if not (isHipSpecified or isPelvisSpecified):
                            raise Exception(
                                'Selection list of length 2 requires either a pelvis or a hip be specified with a flag.')
                        else:
                            if isPelvisSpecified:
                                sel.add(argData.flagArgumentString(AM_HipConstraintCmd.kPelvisObjectFlag, 0))
                                sel.getDagPath(sel.length() - 1, self.__pelvisObjectArg)
                            else:
                                sel.getDagPath(0, self.__pelvisObjectArg)
                            if isHipSpecified:
                                sel.add(argData.flagArgumentString(AM_HipConstraintCmd.kHipObjectFlag, 0))
                                sel.getDagPath(sel.length() - 1, self.__hipObjectArg)
                            else:
                                sel.getDagPath(0, self.__hipObjectArg)
                            sel.getDagPath(1, self.__constrainedObjectArg)
                    # selection list is either [pelvis, hip, constraintObject], or has pelvis or hip specified with flags
                    elif sel.length() == 3:
                        if isPelvisSpecified:
                            sel.add(argData.flagArgumentString(AM_HipConstraintCmd.kPelvisObjectFlag, 0))
                            sel.getDagPath(sel.length() - 1, self.__pelvisObjectArg)
                        else:
                            sel.getDagPath(0, self.__pelvisObjectArg)
                        if isHipSpecified:
                            sel.add(argData.flagArgumentString(AM_HipConstraintCmd.kPelvisObjectFlag, 0))
                            sel.getDagPath(sel.length() - 1, self.__hipObjectArg)
                        else:
                            sel.getDagPath(1, self.__hipObjectArg)
                        sel.getDagPath(2, self.__constrainedObjectArg)
                    else:
                        raise Exception(
                            'This command requires 3 or fewer arguments to be specified or selected;  found %i.' % sel.length())
            else:
                iter = OM.MItSelectionList(sel, OM.MFn.kDependencyNode)
                while not iter.isDone():
                    # in edit or query mode, the object must be an am_hipConstraint node
                    if argData.isEdit() or argData.isQuery():
                        iter.getDependNode(self.__hipConstraintNodeArg)
                        self.__hipConstraintNodeFn.setObject(self.__hipConstraintNodeArg)
                        if not (self.__hipConstraintNodeFn.typeId() == AM_HipConstraintNode.kPluginNodeId):
                            raise Exception('The provided dependency node %s is not of type %s.' % (
                                self.__hipConstraintNodeFn.name(), AM_HipConstraintNode.kPluginNodeTypeName))
                    # in create mode, only a transform node is accepted
                    else:
                        selectedObject = OM.MObject()
                        iter.getDependNode(selectedObject)
                        if selectedObject.hasFn(OM.MFn.kTransform):
                            OM.MDagPath.getAPathTo(selectedObject, self.__constrainedObjectArg)
                        else:
                            selectedObjectFn = OM.MFnDependencyNode(selectedObject)
                            raise Exception('%s is not a valid transform node.' % selectedObjectFn.name())
                    iter.next()

            # perform the query
            if argData.isQuery():
                self.__hipObjectArg = argData.isFlagSet(AM_HipConstraintCmd.kHipObjectFlag)
                self.__pelvisObjectArg = argData.isFlagSet(AM_HipConstraintCmd.kPelvisObjectFlag)
                self.__hipAimAxisArg = argData.isFlagSet(AM_HipConstraintCmd.kHipAimFlag)
                self.__hipFrontAxisArg = argData.isFlagSet(AM_HipConstraintCmd.kHipFrontFlag)
                self.__pelvisAimAxisArg = argData.isFlagSet(AM_HipConstraintCmd.kPelvisAimFlag)
                self.__pelvisFrontAxisArg = argData.isFlagSet(AM_HipConstraintCmd.kPelvisFrontFlag)
                self.doItQuery()
            # set up other arguments and call redoIt() for create or edit mode
            else:
                # validate the name flag
                if argData.isFlagSet(AM_HipConstraintCmd.kNameFlag):
                    self.__hipConstraintNodeName = argData.flagArgumentString(AM_HipConstraintCmd.kNameFlag, 0)
                    if (len(self.__hipConstraintNodeName) < 1 or self.__hipConstraintNodeName[
                        0].isalpha() is False or len(re.split('\W+', self.__hipConstraintNodeName)) > 1):
                        raise Exception(
                            '%s is not a valid node name. Did you type it correctly?' % self.__hipConstraintNodeName)
                # validate dagpaths
                sel = OM.MSelectionList()
                if argData.isFlagSet(AM_HipConstraintCmd.kHipObjectFlag):
                    sel.clear()
                    try:
                        sel.add(argData.flagArgumentString(AM_HipConstraintCmd.kHipObjectFlag, 0))
                        sel.getDagPath(0, self.__hipObjectArg)
                    except:
                        raise Exception(
                            '%s is not a valid node name. Did you type it correctly?' % argData.flagArgumentString(
                                AM_HipConstraintCmd.kHipObjectFlag, 0))
                if argData.isFlagSet(AM_HipConstraintCmd.kPelvisObjectFlag):
                    sel.clear()
                    try:
                        sel.add(argData.flagArgumentString(AM_HipConstraintCmd.kPelvisObjectFlag, 0))
                        sel.getDagPath(0, self.__pelvisObjectArg)
                    except:
                        raise Exception(
                            '%s is not a valid node name. Did you type it correctly?' % argData.flagArgumentString(
                                AM_HipConstraintCmd.kPelvisObjectFlag, 0))
                # get vector args
                if argData.isFlagSet(AM_HipConstraintCmd.kHipAimFlag):
                    self.__hipAimAxisArg = OM.MVector(
                        argData.flagArgumentDouble(AM_HipConstraintCmd.kHipAimFlag, 0),
                        argData.flagArgumentDouble(AM_HipConstraintCmd.kHipAimFlag, 1),
                        argData.flagArgumentDouble(AM_HipConstraintCmd.kHipAimFlag, 2))
                if argData.isFlagSet(AM_HipConstraintCmd.kHipFrontFlag):
                    self.__hipFrontAxisArg = OM.MVector(
                        argData.flagArgumentDouble(AM_HipConstraintCmd.kHipFrontFlag, 0),
                        argData.flagArgumentDouble(AM_HipConstraintCmd.kHipFrontFlag, 1),
                        argData.flagArgumentDouble(AM_HipConstraintCmd.kHipFrontFlag, 2))
                if argData.isFlagSet(AM_HipConstraintCmd.kPelvisAimFlag):
                    self.__pelvisAimAxisArg = OM.MVector(
                        argData.flagArgumentDouble(AM_HipConstraintCmd.kPelvisAimFlag, 0),
                        argData.flagArgumentDouble(AM_HipConstraintCmd.kPelvisAimFlag, 1),
                        argData.flagArgumentDouble(AM_HipConstraintCmd.kPelvisAimFlag, 2))
                if argData.isFlagSet(AM_HipConstraintCmd.kPelvisFrontFlag):
                    self.__pelvisFrontAxisArg = OM.MVector(
                        argData.flagArgumentDouble(AM_HipConstraintCmd.kPelvisFrontFlag, 0),
                        argData.flagArgumentDouble(AM_HipConstraintCmd.kPelvisFrontFlag, 1),
                        argData.flagArgumentDouble(AM_HipConstraintCmd.kPelvisFrontFlag, 2))
                # set the isEditUsed flag only after all arguments have been stored to ensure command is not added to queue before it has done anything
                self.__isEditUsed = argData.isEdit()
                self.__isQueryUsed = False
                self.redoIt()

    def doItQuery(self):
        # query mode typically only supports one argument at a time
        # this principle ensures that the result will be given in a way that can be stored in a variable
        path = OM.MDagPath()
        doubleArray = OM.MScriptUtil()
        if self.__hipObjectArg:
            plug = OM.MPlug(self.__hipConstraintNodeFn.findPlug(AM_HipConstraintNode.kHipObjectAttrName, True))
            iter = OM.MItDependencyGraph(plug, OM.MFn.kTransform, OM.MItDependencyGraph.kUpstream)
            while not iter.isDone():
                OM.MDagPath.getAPathTo(iter.currentItem(), path)
                iter.next()
            self.setResult(path.partialPathName())
        elif self.__pelvisObjectArg:
            plug = OM.MPlug(self.__hipConstraintNodeFn.findPlug(AM_HipConstraintNode.kPelvisObjectAttrName, True))
            iter = OM.MItDependencyGraph(plug, OM.MFn.kTransform, OM.MItDependencyGraph.kUpstream)
            while not iter.isDone():
                OM.MDagPath.getAPathTo(iter.currentItem(), path)
                iter.next()
            self.setResult(path.partialPathName())
        elif self.__hipAimAxisArg:
            doubleArray.createFromDouble(
                OM.MPlug(
                    self.__hipConstraintNodeFn.findPlug('%s0' % AM_HipConstraintNode.kHipAimAttrName, True)).asDouble(),
                OM.MPlug(
                    self.__hipConstraintNodeFn.findPlug('%s1' % AM_HipConstraintNode.kHipAimAttrName, True)).asDouble(),
                OM.MPlug(
                    self.__hipConstraintNodeFn.findPlug('%s2' % AM_HipConstraintNode.kHipAimAttrName, True)).asDouble())
            self.setResult(OM.MDoubleArray(doubleArray.asDoublePtr(), 3))
        elif self.__hipFrontAxisArg:
            doubleArray.createFromDouble(
                OM.MPlug(self.__hipConstraintNodeFn.findPlug('%s0' % AM_HipConstraintNode.kHipFrontAttrName,
                                                             True)).asDouble(),
                OM.MPlug(self.__hipConstraintNodeFn.findPlug('%s1' % AM_HipConstraintNode.kHipFrontAttrName,
                                                             True)).asDouble(),
                OM.MPlug(self.__hipConstraintNodeFn.findPlug('%s2' % AM_HipConstraintNode.kHipFrontAttrName,
                                                             True)).asDouble())
            self.setResult(OM.MDoubleArray(doubleArray.asDoublePtr(), 3))
        elif self.__pelvisAimAxisArg:
            doubleArray.createFromDouble(
                OM.MPlug(self.__hipConstraintNodeFn.findPlug('%s0' % AM_HipConstraintNode.kPelvisAimAttrName,
                                                             True)).asDouble(),
                OM.MPlug(self.__hipConstraintNodeFn.findPlug('%s1' % AM_HipConstraintNode.kPelvisAimAttrName,
                                                             True)).asDouble(),
                OM.MPlug(self.__hipConstraintNodeFn.findPlug('%s2' % AM_HipConstraintNode.kPelvisAimAttrName,
                                                             True)).asDouble())
            self.setResult(OM.MDoubleArray(doubleArray.asDoublePtr(), 3))
        elif self.__pelvisFrontAxisArg:
            doubleArray.createFromDouble(
                OM.MPlug(self.__hipConstraintNodeFn.findPlug('%s0' % AM_HipConstraintNode.kPelvisFrontAttrName,
                                                             True)).asDouble(),
                OM.MPlug(self.__hipConstraintNodeFn.findPlug('%s1' % AM_HipConstraintNode.kPelvisFrontAttrName,
                                                             True)).asDouble(),
                OM.MPlug(self.__hipConstraintNodeFn.findPlug('%s2' % AM_HipConstraintNode.kPelvisFrontAttrName,
                                                             True)).asDouble())
            self.setResult(OM.MDoubleArray(doubleArray.asDoublePtr(), 3))

    def redoIt(self):
        # clear out the modifier so it doesn't store old object names
        self.__dgModify = OM.MDGModifier()

        # create a new node if the command is in create mode
        if not self.__isEditUsed:
            self.__hipConstraintNodeArg = OM.MObject(self.__dgModify.createNode(AM_HipConstraintNode.kPluginNodeId))
            self.__hipConstraintNodeFn.setObject(self.__hipConstraintNodeArg)
            fn = OM.MFnDagNode(self.__constrainedObjectArg)
            self.__dgModify.renameNode(self.__hipConstraintNodeArg, '%s_hipConstraint' % fn.name())
        # assign the -name argument if provided
        if len(self.__hipConstraintNodeName) > 0:
            self.__dgModify.renameNode(self.__hipConstraintNodeArg, self.__hipConstraintNodeName)
        # WARNING: must tell the DGModifier to doIt() now in order to let Maya's auto-rename kick in and ensure the name is unique
        # otherwise attempts to use commandToExecute below may end up using some other object
        self.__dgModify.doIt()

        # set the attributes on the node
        plug = OM.MPlug()
        if self.__constrainedObjectArg.isValid():
            self.__dgModify.commandToExecute('connectAttr -f %s.%s %s.rotate' % (
                self.__hipConstraintNodeFn.name(), AM_HipConstraintNode.kRotateAttrName,
                self.__constrainedObjectArg.partialPathName()))
            self.__dgModify.commandToExecute('connectAttr -f %s.rotateOrder %s.%s' % (
                self.__constrainedObjectArg.partialPathName(),
                self.__hipConstraintNodeFn.name(), AM_HipConstraintNode.kRotateOrderAttrName))
            self.__dgModify.commandToExecute('connectAttr -f %s.parentInverseMatrix %s.%s' % (
                self.__constrainedObjectArg.partialPathName(),
                self.__hipConstraintNodeFn.name(), AM_HipConstraintNode.kParentInvMatrixAttrName))
        if self.__hipObjectArg.isValid():
            self.__dgModify.commandToExecute('connectAttr -f %s.worldMatrix %s.%s' % (
                self.__hipObjectArg.partialPathName(),
                self.__hipConstraintNodeFn.name(), AM_HipConstraintNode.kHipObjectAttrName))
            if not self.__hipObjectArg.hasFn(OM.MFn.kJoint):
                self.__dgModify.commandToExecute('connectAttr -f %s.rotatePivot %s.%s' % (
                    self.__hipObjectArg.partialPathName(),
                    self.__hipConstraintNodeFn.name(), AM_HipConstraintNode.kHipRotatePivotAttrName))
        if self.__pelvisObjectArg.isValid():
            self.__dgModify.commandToExecute('connectAttr -f %s.worldMatrix %s.%s' % (
                self.__pelvisObjectArg.partialPathName(),
                self.__hipConstraintNodeFn.name(), AM_HipConstraintNode.kPelvisObjectAttrName))
            if not self.__pelvisObjectArg.hasFn(OM.MFn.kJoint):
                self.__dgModify.commandToExecute('connectAttr -f %s.rotatePivot %s.%s' % (
                    self.__pelvisObjectArg.partialPathName(),
                    self.__hipConstraintNodeFn.name(), AM_HipConstraintNode.kPelvisRotatePivotAttrName))
        # set vector attribute values
        vectorArgs = {
            self.__hipAimAxisArg: AM_HipConstraintNode.kHipAimAttrName,
            self.__hipFrontAxisArg: AM_HipConstraintNode.kHipFrontAttrName,
            self.__pelvisAimAxisArg: AM_HipConstraintNode.kPelvisAimAttrName,
            self.__pelvisFrontAxisArg: AM_HipConstraintNode.kPelvisFrontAttrName
        }
        for vArg in vectorArgs:
            if not vArg:
                continue
            # set the vector attribute if it is not connected
            plug = self.__hipConstraintNodeFn.findPlug(vectorArgs[vArg], True)
            if not plug.isConnected():
                self.__dgModify.commandToExecute('setAttr %s.%s %s %s %s' % (
                    self.__hipConstraintNodeFn.name(),
                    vectorArgs[vArg], vArg.x, vArg.y, vArg.z))

        # following Maya convention, select the newly created node if the command is in create mode
        if not self.__isEditUsed:
            self.__dgModify.commandToExecute('select %s' % self.__hipConstraintNodeFn.name())
        self.__dgModify.doIt()
        self.setResult(self.__hipConstraintNodeFn.name())

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
        syntax.addFlag(cls.kPelvisObjectFlag, cls.kPelvisObjectFlagLong, OM.MSyntax.kSelectionItem)
        syntax.addFlag(cls.kHipObjectFlag, cls.kHipObjectFlagLong, OM.MSyntax.kSelectionItem)
        syntax.addFlag(cls.kHipAimFlag, cls.kHipAimFlagLong, OM.MSyntax.kDouble, OM.MSyntax.kDouble, OM.MSyntax.kDouble)
        syntax.addFlag(cls.kHipFrontFlag, cls.kHipFrontFlagLong, OM.MSyntax.kDouble, OM.MSyntax.kDouble,
                       OM.MSyntax.kDouble)
        syntax.addFlag(cls.kPelvisAimFlag, cls.kPelvisAimFlagLong, OM.MSyntax.kDouble, OM.MSyntax.kDouble,
                       OM.MSyntax.kDouble)
        syntax.addFlag(cls.kPelvisFrontFlag, cls.kPelvisFrontFlagLong, OM.MSyntax.kDouble, OM.MSyntax.kDouble,
                       OM.MSyntax.kDouble)
        syntax.useSelectionAsDefault(True)
        syntax.setObjectType(OM.MSyntax.kSelectionList, 1, 3)
        return syntax


# ----------------------------------------------------------------
# Node definition
# ----------------------------------------------------------------
class AM_HipConstraintNode(OMMPx.MPxNode):
    """
    A node to constrain the first twist joint in a hip. The node also outputs
    the hip's pelvis-space elevation angle for other nodes to use.
    \par Input Attributes:
        - \em rotateOrder: The rotateOrder attribute of the constrained object.
        - \em hipAimAxis: Axis in the upper leg's local space that aims toward
            the knee joint.
        - \em hipFrontAxis: Axis in the upper leg's local space that points
            toward the character's front.
        - \em pelvisAimAxis: Axis in the specified pelvis joint's local space
            that aims toward the next vertebra (up).
        - \em pelvisFrontAxis: Axis in the specified pelvis joint's local space
            that aims toward the character's front.
        - \em rotatePivot: The rotatePivot attribute of the upper leg.
        - \em jointOrient: The jointOrient attribute of the constrained object
            if it is a joint. If there is no connection (i.e., the constrained
            object is not a joint), then it is initialized to identity and has
            no effect.
        - \em pelvisWorldMatrix: The worldMatrix attribute of the object to use
            for computing the hip's elevation angle. The hip constraint is
            designed with the expectation that this is the the first common
            parent of both of the upper legs (usually the ribcage). Although
            this joint will produce perfectly valid values if any intermediate
            joints exist (collar bone, scapula), such an intermediate joint
            could be used instead, provided that the axes given for the pelvis
            node (above) are transformed into the intermediate joint's local
            space.
        - \em hipWorldMatrix: The worldMatrix attribute of the upper leg object
            along whose aim axis (above) the constrained object is twisting.
        - \em parentInverseMatrix: The parentInverseMatrix attribute of the
            constrained object.
    \par Output Attributes:
        - \em rotate: The local Euler rotation piped to the constrained object.
        - \em elevationAngle: The elevation angle of the hip in pelvis space.
    """

    ## the name of the nodeType
    kPluginNodeTypeName = 'am_hipConstraint'
    ## the unique MTypeId for the node
    kPluginNodeId = OM.MTypeId(0x001138C1)

    # input attributes
    ## the constrained node's rotateOrder attribute
    rotateOrder = OM.MObject()
    kRotateOrderAttrName = 'rotateOrder'
    kRotateOrderAttrLongName = 'constraintRotateOrder'
    ## local axis of the hip that aims at the knee
    hipAim = OM.MObject()
    kHipAimAttrName = 'hipAim'
    kHipAimAttrLongName = 'hipAimAxis'
    ## local axis of the hip that points toward the character's front
    hipFront = OM.MObject()
    kHipFrontAttrName = 'hipFront'
    kHipFrontAttrLongName = 'hipFrontAxis'
    ## local axis of the pelvis that points up toward the head
    pelvisAim = OM.MObject()
    kPelvisAimAttrName = 'pelvisAim'
    kPelvisAimAttrLongName = 'pelvisAimAxis'
    ## local axis of the pelvis that points toward the character's front
    pelvisFront = OM.MObject()
    kPelvisFrontAttrName = 'pelvisFront'
    kPelvisFrontAttrLongName = 'pelvisFrontAxis'
    ## the rotatePivot attribute of the hip object
    hipPivot = OM.MObject()
    kHipRotatePivotAttrName = 'hipPivot'
    kHipRotatePivotAttrLongName = 'hipRotatePivot'
    ## the rotatePivot attribute of the pelvis object
    pelvisPivot = OM.MObject()
    kPelvisRotatePivotAttrName = 'pelvisPivot'
    kPelvisRotatePivotAttrLongName = 'pelvisRotatePivot'
    ## the jointOrient (XYZ Euler offset) attribute of the constrained object
    jointOrient = OM.MObject()
    kJointOrientAttrName = 'orient'
    kJointOrientAttrLongName = 'jointOrient'
    ## the hip object
    hip = OM.MObject()
    kHipObjectAttrName = 'hip'
    kHipObjectAttrLongName = 'hipWorldMatrix'
    ## the pelvis object
    pelvis = OM.MObject()
    kPelvisObjectAttrName = 'pelvis'
    kPelvisObjectAttrLongName = 'pelvisWorldMatrix'
    ## parentInverseMatrix of the constrained transform
    parentInverseMatrix = OM.MObject()
    kParentInvMatrixAttrName = 'parent'
    kParentInvMatrixAttrLongName = 'parentInverseMatrix'

    # output attributes
    # local rotation for constrained object
    rotate = OM.MObject()
    kRotateAttrName = 'rotate'
    kRotateAttrLongName = 'constraintRotate'
    # elevation angle of the hip
    angle = OM.MObject()
    kElevationAngleAttrName = 'angle'
    kElevationAngleAttrLongName = 'elevationAngle'

    def __init__(self):
        OMMPx.MPxNode.__init__(self)

    def compute(self, plug, dataBlock):
        """Compute the upper leg's elevation angle as well as the orientation for the first twist joint in the hip."""
        if (plug == AM_HipConstraintNode.rotate or plug == AM_HipConstraintNode.angle):
            # ----------------------------------------------------------------
            # Get the incoming data
            # ----------------------------------------------------------------
            # the constrained node's rotateOrder attribute
            dataHandle = dataBlock.inputValue(AM_HipConstraintNode.rotateOrder)
            eRotateOrder = dataHandle.asShort()
            # axis pointing down the length of the upper leg
            dataHandle = dataBlock.inputValue(AM_HipConstraintNode.hipAim)
            vHipForward = (dataHandle.asVector()).normal()
            # axis pointing to the character's front
            dataHandle = dataBlock.inputValue(AM_HipConstraintNode.hipFront)
            vHipUp = (dataHandle.asVector()).normal()
            # axis pointing to the character's the pelvis
            dataHandle = dataBlock.inputValue(AM_HipConstraintNode.pelvisAim)
            vPelvisForward = (dataHandle.asVector()).normal()
            # axis pointing to the character's front
            dataHandle = dataBlock.inputValue(AM_HipConstraintNode.pelvisFront)
            vPelvisUp = (dataHandle.asVector()).normal()
            # the rotatePivot attribute of the upper leg
            dataHandle = dataBlock.inputValue(AM_HipConstraintNode.hipPivot)
            vHipPivot = dataHandle.asVector()
            # the rotatePivot attribute of the pelvis
            dataHandle = dataBlock.inputValue(AM_HipConstraintNode.pelvisPivot)
            vPelvisPivot = dataHandle.asVector()
            # the jointOrient attribute (Euler XYZ offset) of the constrained node
            dataHandle = dataBlock.inputValue(AM_HipConstraintNode.jointOrient)
            vJointOrient = dataHandle.asVector()
            eJointOrient = OM.MEulerRotation(math.radians(vJointOrient.x), math.radians(vJointOrient.y),
                                             math.radians(vJointOrient.z), 0)
            qJointOrient = eJointOrient.asQuaternion()
            qJointOrient.conjugateIt()
            # the pelvis's worldMatrix attribute
            dataHandle = dataBlock.inputValue(AM_HipConstraintNode.pelvis)
            mPelvis = dataHandle.asMatrix()
            mPelvis = OM.MTransformationMatrix(mPelvis)
            qPelvis = mPelvis.rotation()
            # the hip's worldMatrix attribute
            dataHandle = dataBlock.inputValue(AM_HipConstraintNode.hip)
            mHip = dataHandle.asMatrix()
            mHip = OM.MTransformationMatrix(mHip)
            qHip = mHip.rotation()
            # the constrained node's parentInverseMatrix attribute
            dataHandle = dataBlock.inputValue(AM_HipConstraintNode.parentInverseMatrix)
            mParent = dataHandle.asMatrix()
            mParent = OM.MTransformationMatrix(mParent)
            qParent = mParent.rotation()

            # ----------------------------------------------------------------
            # Orthonormalize provided axes for the hip and pelvis
            # ----------------------------------------------------------------
            vHipRight = OM.MVector(vHipUp ^ vHipForward).normal()
            vHipUp = vHipForward ^ vHipRight
            vPelvisRight = OM.MVector(vPelvisUp ^ vPelvisForward).normal()
            vPelvisUp = vPelvisForward ^ vPelvisRight

            # ----------------------------------------------------------------
            # Interpolate the target up-vector based on hip's orientation
            # ----------------------------------------------------------------
            # rotate the pelvis and hip vectors into their respective spaces to get the current elevation angle
            vPelvisForwardRotated = vPelvisForward.rotateBy(qPelvis)
            vPelvisUpRotated = vPelvisUp.rotateBy(qPelvis)
            vHipForwardRotated = vHipForward.rotateBy(qHip)
            dDotPitch = vPelvisForwardRotated * vHipForwardRotated
            dDotYaw = vPelvisUpRotated * (vHipForwardRotated - vPelvisForwardRotated * dDotPitch).normal()
            dAngle = math.degrees(math.acos(min(max(-1.0, -dDotPitch), 1.0)))

            # compute interpolation factor
            dInterpAmt = (2.0 - (1.0 - dDotPitch)) * abs(dDotYaw)
            # interpolate up-vector
            vTargetUp = vPelvisUp.rotateBy(OM.MQuaternion(cmp(dDotYaw, 0.0) * dInterpAmt * math.pi * 0.5, vPelvisRight))

            # rotate the target up-vector into world space
            vTargetUp = vTargetUp.rotateBy(qPelvis)

            # ----------------------------------------------------------------
            # Compute the local orientation for the constrained node
            # ----------------------------------------------------------------
            # orthonormalize target axes and get target normal orientation for constrained object
            vTargetRight = (vTargetUp ^ vHipForwardRotated).normal()
            vTargetUp = vHipForwardRotated ^ vTargetRight
            mList = [vTargetRight.x, vTargetRight.y, vTargetRight.z, 0.0,
                     vTargetUp.x, vTargetUp.y, vTargetUp.z, 0.0,
                     vHipForwardRotated.x, vHipForwardRotated.y, vHipForwardRotated.z, 0.0,
                     0.0, 0.0, 0.0, 1.0]
            mTarget = OM.MMatrix()
            OM.MScriptUtil.createMatrixFromList(mList, mTarget)
            qTarget = OM.MQuaternion(OM.MTransformationMatrix(mTarget).rotation())

            # get offset orientation of the constrained object (from z-forward, y-up)
            mList = [vHipRight.x, vHipRight.y, vHipRight.z, 0.0,
                     vHipUp.x, vHipUp.y, vHipUp.z, 0.0,
                     vHipForward.x, vHipForward.y, vHipForward.z, 0.0,
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
            outputHandle = dataBlock.outputValue(AM_HipConstraintNode.rotate)
            outputHandle.set3Double(math.degrees(eFinal.x), math.degrees(eFinal.y), math.degrees(eFinal.z))
            outputHandle = dataBlock.outputValue(AM_HipConstraintNode.angle)
            outputHandle.setDouble(dAngle)
            dataBlock.setClean(plug)

        else:
            return OM.kUnknownParameter

    @classmethod
    def nodeCreator(cls):
        return OMMPx.asMPxPtr(cls())

    # noinspection PyCallByClass
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
        # local axis of the hip that aims at the knee
        nAttr = OM.MFnNumericAttribute()
        cls.hipAim = nAttr.create(cls.kHipAimAttrLongName, cls.kHipAimAttrName, OM.MFnNumericData.k3Double)
        nAttr.setWritable(1)
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setKeyable(0)
        # local axis of the hip that points toward the character's front
        cls.hipFront = nAttr.create(cls.kHipFrontAttrLongName, cls.kHipFrontAttrName, OM.MFnNumericData.k3Double)
        nAttr.setWritable(1)
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setKeyable(0)
        # axis on the pelvis joint pointing toward the head
        cls.pelvisAim = nAttr.create(cls.kPelvisAimAttrLongName, cls.kPelvisAimAttrName, OM.MFnNumericData.k3Double)
        nAttr.setWritable(1)
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setKeyable(0)
        # axis on the pelvis joint pointing toward the front
        cls.pelvisFront = nAttr.create(cls.kPelvisFrontAttrLongName, cls.kPelvisFrontAttrName,
                                       OM.MFnNumericData.k3Double)
        nAttr.setWritable(1)
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setKeyable(0)
        # rotatePivot attribute of the upper leg
        cls.hipPivot = nAttr.create(cls.kHipRotatePivotAttrLongName, cls.kHipRotatePivotAttrName,
                                    OM.MFnNumericData.k3Double)
        nAttr.setWritable(1)
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setKeyable(0)
        nAttr.setHidden(1)
        # rotatePivot attribute of the pelvis
        cls.pelvisPivot = nAttr.create(cls.kPelvisRotatePivotAttrLongName, cls.kPelvisRotatePivotAttrName,
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
        # worldMatrix of the pelvis joint
        mAttr = OM.MFnMatrixAttribute()
        cls.pelvis = mAttr.create(cls.kPelvisObjectAttrLongName, cls.kPelvisObjectAttrName,
                                  OM.MFnMatrixAttribute.kDouble)
        mAttr.setWritable(1)
        mAttr.setStorable(1)
        mAttr.setReadable(1)
        mAttr.setKeyable(0)
        mAttr.setHidden(1)
        # worldMatrix of the hip joint
        cls.hip = mAttr.create(cls.kHipObjectAttrLongName, cls.kHipObjectAttrName, OM.MFnMatrixAttribute.kDouble)
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
        # elevation angle of the hip
        cls.angle = nAttr.create(cls.kElevationAngleAttrLongName, cls.kElevationAngleAttrName,
                                 OM.MFnNumericData.kDouble)
        nAttr.setWritable(1)
        nAttr.setStorable(0)
        nAttr.setReadable(1)

        # ----------------------------------------------------------------
        # Add attributes
        # ----------------------------------------------------------------
        cls.addAttribute(cls.rotateOrder)
        cls.addAttribute(cls.hipAim)
        cls.addAttribute(cls.hipFront)
        cls.addAttribute(cls.pelvisAim)
        cls.addAttribute(cls.pelvisFront)
        cls.addAttribute(cls.hipPivot)
        cls.addAttribute(cls.pelvisPivot)
        cls.addAttribute(cls.jointOrient)
        cls.addAttribute(cls.pelvis)
        cls.addAttribute(cls.hip)
        cls.addAttribute(cls.parentInverseMatrix)
        cls.addAttribute(cls.rotate)
        cls.addAttribute(cls.angle)
        # establish effect upon rotate output
        cls.attributeAffects(cls.rotateOrder, cls.rotate)
        cls.attributeAffects(cls.hipAim, cls.rotate)
        cls.attributeAffects(cls.hipFront, cls.rotate)
        cls.attributeAffects(cls.pelvisAim, cls.rotate)
        cls.attributeAffects(cls.pelvisFront, cls.rotate)
        cls.attributeAffects(cls.hipPivot, cls.rotate)
        cls.attributeAffects(cls.pelvisPivot, cls.rotate)
        cls.attributeAffects(cls.jointOrient, cls.rotate)
        cls.attributeAffects(cls.pelvis, cls.rotate)
        cls.attributeAffects(cls.hip, cls.rotate)
        cls.attributeAffects(cls.parentInverseMatrix, cls.rotate)
        # establish effect upon angle output
        cls.attributeAffects(cls.rotateOrder, cls.angle)
        cls.attributeAffects(cls.hipAim, cls.angle)
        cls.attributeAffects(cls.hipFront, cls.angle)
        cls.attributeAffects(cls.pelvisAim, cls.angle)
        cls.attributeAffects(cls.pelvisFront, cls.angle)
        cls.attributeAffects(cls.hipPivot, cls.angle)
        cls.attributeAffects(cls.pelvisPivot, cls.angle)
        cls.attributeAffects(cls.jointOrient, cls.angle)
        cls.attributeAffects(cls.pelvis, cls.angle)
        cls.attributeAffects(cls.hip, cls.angle)
        cls.attributeAffects(cls.parentInverseMatrix, cls.angle)


# ----------------------------------------------------------------
# Initialize the plug-in
# ----------------------------------------------------------------
def initializePlugin(mobject):
    plugin = OMMPx.MFnPlugin(mobject, 'Adam Mechtley', kVersionNumber, 'Any')
    # dependency node
    try:
        plugin.registerNode(AM_HipConstraintNode.kPluginNodeTypeName, AM_HipConstraintNode.kPluginNodeId,
                            AM_HipConstraintNode.nodeCreator, AM_HipConstraintNode.nodeInitializer)
    except:
        sys.stderr.write('Failed to register node: %s\n' % AM_HipConstraintNode.kPluginNodeTypeName)
        raise
    # command
    try:
        plugin.registerCommand(AM_HipConstraintCmd.kPluginCmdName, AM_HipConstraintCmd.cmdCreator,
                               AM_HipConstraintCmd.syntaxCreator)
    except:
        sys.stderr.write('Failed to register command: %s\n' % AM_HipConstraintCmd.kPluginCmdName)
        raise


# ----------------------------------------------------------------
# Uninitialize the plug-in
# ----------------------------------------------------------------
def uninitializePlugin(mobject):
    plugin = OMMPx.MFnPlugin(mobject)
    # dependency node
    try:
        plugin.deregisterNode(AM_HipConstraintNode.kPluginNodeId)
    except:
        sys.stderr.write('Failed to deregister node: %s\n' % AM_HipConstraintNode.kPluginNodeTypeName)
        raise
    # command
    try:
        plugin.deregisterCommand(AM_HipConstraintCmd.kPluginCmdName)
    except:
        sys.stderr.write('Failed to unregister command: %s\n' % AM_HipConstraintCmd.kPluginCmdName)
        raise