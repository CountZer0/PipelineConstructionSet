"""
A node and corresponding command to expose transform information about one
transform node with respect to another.

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

\namespace AM_ExposeTransform
"""

import math, sys, re
import maya.OpenMaya as OM
import maya.OpenMayaMPx as OMMPx

## current version of the plug-in
kVersionNumber = '1.01'

# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------
## a dictionary of possible rotation order values
kRotateOrderMapping = {
    'xyz': OM.MEulerRotation.kXYZ,
    'yzx': OM.MEulerRotation.kYZX,
    'zxy': OM.MEulerRotation.kZXY,
    'xzy': OM.MEulerRotation.kXZY,
    'yxz': OM.MEulerRotation.kYXZ,
    'zyx': OM.MEulerRotation.kZYX,
    '0': OM.MEulerRotation.kXYZ,
    '1': OM.MEulerRotation.kYZX,
    '2': OM.MEulerRotation.kZXY,
    '3': OM.MEulerRotation.kXZY,
    '4': OM.MEulerRotation.kYXZ,
    '5': OM.MEulerRotation.kZYX
}

# -----------------------------------------------------------------------------
# Command Definition
# -----------------------------------------------------------------------------
class AM_ExposeTransformCmd(OMMPx.MPxCommand):
    """
	A command to quickly create, edit, or query an am_exposeTransform node.
	"""

    ## the name of the command
    kPluginCmdName = 'am_exposeTransform'

    ## specifies a name for the am_exposeTransform node (CE)
    kNameFlag = '-n'
    kNameFlagLong = '-name'
    ## specifies an exposed object (CEQ)
    kExposedObjectFlag = '-o'
    kExposedObjectFlagLong = '-object'
    ## specifies a reference object; otherwise the node exposes world-space info (CEQ)
    kReferenceObjectFlag = '-ref'
    kReferenceObjectFlagLong = '-referenceObject'
    ## specifies Euler rotation order that the node should use (CEQ)
    kRotateOrderFlag = '-ro'
    kRotateOrderFlagLong = '-rotateOrder'
    ## specifies whether incoming axes should be normalized for computation of dot products (CEQ)
    kNormalizeFlag = '-na'
    kNormalizeFlagLong = '-normalizeAxes'
    ## specifies an axis on the object for computing dot and angle (CEQ)
    kObjectAxisFlag = '-a'
    kObjectAxisFlagLong = '-axis'
    ## specifies an axis on the reference for computing dot and angle (CEQ)
    kReferenceAxisFlag = '-ra'
    kReferenceAxisFlagLong = '-referenceAxis'

    def __init__(self):
        OMMPx.MPxCommand.__init__(self)
        self.__isQueryUsed = True  # initialize to True so command is not added to queue if argument parsing fails
        self.__isEditUsed = False  # if the edit flag has been set, then undo will be enabled

        self.__exposeNodeArg = OM.MObject()  # the am_exposeTransform node selected for edit and query modes
        self.__exposeNodeFn = OM.MFnDependencyNode()
        self.__exposeNodeName = ''

        self.__exposedObjectArg = OM.MDagPath()  # the exposed object
        self.__referenceObjectArg = OM.MDagPath()  # the reference object
        self.__rotateOrderArg = kRotateOrderMapping['xyz']  # the Euler rotation order to use
        self.__normalizeArg = True  # should the incoming axes be normalized for computation of dot product?
        self.__objectAxisArg = OM.MVector(0, 0, 1)  # axis on the selected objects to use for dot and angle
        self.__referenceAxisArg = OM.MVector(0, 0, 1)  # axis on the reference object to use for dot and angle

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
                # if in create mode, use the argument specified with the -object flag as the exposed object
                if not argData.isEdit() and not argData.isQuery() and argData.isFlagSet(
                        AM_ExposeTransformCmd.kExposedObjectFlag):
                    sel.add(argData.flagArgumentString(AM_ExposeTransformCmd.kExposedObjectFlag, 0))
                    sel.getDagPath(sel.length() - 1, self.__exposedObjectArg)
                else:
                    raise Exception(
                        'This command requires exactly 1 argument to be specified or selected;  found %i.' % sel.length())
            else:
                iter = OM.MItSelectionList(sel, OM.MFn.kDependencyNode)
                selectedObject = OM.MObject()
                while not iter.isDone():
                    # in edit or query mode, the object must be an am_exposeTransform node
                    if argData.isEdit() or argData.isQuery():
                        iter.getDependNode(self.__exposeNodeArg)
                        if not (self.__exposeNodeFn.typeId() == AM_ExposeTransformNode.kPluginNodeId):
                            raise Exception('The provided dependency node %s is not of type %s.' % (
                                self.__exposeNodeFn.name(), AM_ExposeTransformNode.kPluginNodeTypeName))
                    # in create mode, only a transform node is accepted
                    else:
                        iter.getDependNode(selectedObject)
                        if selectedObject.hasFn(OM.MFn.kTransform):
                            OM.MDagPath.getAPathTo(selectedObject, self.__exposedObjectArg)
                        else:
                            selectedObjectFn = OM.MFnDependencyNode(selectedObject)
                            raise Exception('%s is not a valid transform node.' % selectedObjectFn.name())
                    iter.next()

            # perform the query
            if argData.isQuery():
                self.__exposedObjectArg = argData.isFlagSet(AM_ExposeTransformCmd.kExposedObjectFlag)
                self.__referenceObjectArg = argData.isFlagSet(AM_ExposeTransformCmd.kReferenceObjectFlag)
                self.__rotateOrderArg = argData.isFlagSet(AM_ExposeTransformCmd.kRotateOrderFlag)
                self.__normalizeArg = argData.isFlagSet(AM_ExposeTransformCmd.kNormalizeFlag)
                self.__objectAxisArg = argData.isFlagSet(AM_ExposeTransformCmd.kObjectAxisFlag)
                self.__referenceAxisArg = argData.isFlagSet(AM_ExposeTransformCmd.kReferenceAxisFlag)
                self.doItQuery()
            # set up other arguments and call redoIt() for create or edit mode
            else:
                # validate the name flag
                if argData.isFlagSet(AM_ExposeTransformCmd.kNameFlag):
                    self.__exposeNodeName = argData.flagArgumentString(AM_ExposeTransformCmd.kNameFlag, 0)
                    if (len(self.__exposeNodeName) < 1 or self.__exposeNodeName[0].isalpha() is False or len(
                            re.split('\W+', self.__exposeNodeName)) > 1):
                        raise Exception(
                            '%s is not a valid node name. Did you type it correctly?' % self.__exposeNodeName)

                # manually specifying an object to expose using an argument will trump selection
                if argData.isFlagSet(AM_ExposeTransformCmd.kExposedObjectFlag):
                    sel = OM.MSelectionList()
                    sel.add(argData.flagArgumentString(AM_ExposeTransformCmd.kExposedObjectFlag, 0))
                    sel.getDagPath(0, self.__exposedObjectArg)
                if argData.isFlagSet(AM_ExposeTransformCmd.kReferenceObjectFlag):
                    sel = OM.MSelectionList()
                    sel.add(argData.flagArgumentString(AM_ExposeTransformCmd.kReferenceObjectFlag, 0))
                    sel.getDagPath(0, self.__referenceObjectArg)
                if argData.isFlagSet(AM_ExposeTransformCmd.kRotateOrderFlag):
                    rotateOrderStr = argData.flagArgumentString(AM_ExposeTransformCmd.kRotateOrderFlag, 0)
                    try:
                        self.__rotateOrderArg = kRotateOrderMapping[rotateOrderStr.lower()]
                    except:
                        OM.MGlobal.displayWarning('%s is not a valid rotate order. %s is being used instead.' % (
                            rotateOrderStr, kRotateOrderMapping[self.__rotateOrderArg]))
                else:
                    self.__rotateOrderArg = None
                if argData.isFlagSet(AM_ExposeTransformCmd.kNormalizeFlag):
                    self.__normalizeArg = argData.flagArgumentBool(AM_ExposeTransformCmd.kNormalizeFlag, 0)
                else:
                    self.__normalizeArg = None
                if argData.isFlagSet(AM_ExposeTransformCmd.kObjectAxisFlag):
                    self.__objectAxisArg = OM.MVector(
                        argData.flagArgumentDouble(AM_ExposeTransformCmd.kObjectAxisFlag, 0),
                        argData.flagArgumentDouble(AM_ExposeTransformCmd.kObjectAxisFlag, 1),
                        argData.flagArgumentDouble(AM_ExposeTransformCmd.kObjectAxisFlag, 2))
                if argData.isFlagSet(AM_ExposeTransformCmd.kReferenceAxisFlag):
                    self.__referenceAxisArg = OM.MVector(
                        argData.flagArgumentDouble(AM_ExposeTransformCmd.kReferenceAxisFlag, 0),
                        argData.flagArgumentDouble(AM_ExposeTransformCmd.kReferenceAxisFlag, 1),
                        argData.flagArgumentDouble(AM_ExposeTransformCmd.kReferenceAxisFlag, 2))
                # set the isEditUsed flag only after all arguments have been stored to ensure command is not added to queue before it has done anything
                self.__isEditUsed = argData.isEdit()
                self.__isQueryUsed = False
                self.redoIt()

    def doItQuery(self):
        # query mode typically only supports one argument at a time
        # this principle ensures that the result will be given in a way that can be stored in a variable
        path = OM.MDagPath()
        doubleArray = OM.MScriptUtil()
        if self.__exposedObjectArg:
            plug = OM.MPlug(self.__exposeNodeFn.findPlug(AM_ExposeTransformNode.kObjectMatrixAttrName, True))
            iter = OM.MItDependencyGraph(plug, OM.MFn.kTransform, OM.MItDependencyGraph.kUpstream)
            while not iter.isDone():
                OM.MDagPath.getAPathTo(iter.currentItem(), path)
                iter.next()
            self.setResult(path.partialPathName())
        elif self.__referenceObjectArg:
            plug = OM.MPlug(self.__exposeNodeFn.findPlug(AM_ExposeTransformNode.kReferenceMatrixAttrName, True))
            iter = OM.MItDependencyGraph(plug, OM.MFn.kTransform, OM.MItDependencyGraph.kUpstream)
            while not iter.isDone():
                OM.MDagPath.getAPathTo(iter.currentItem(), path)
                iter.next()
            self.setResult(path.partialPathName())
        elif self.__rotateOrderArg:
            self.setResult(
                OM.MPlug(self.__exposeNodeFn.findPlug(AM_ExposeTransformNode.kRotateOrderAttrName, True)).asInt())
        elif self.__normalizeArg:
            self.setResult(
                OM.MPlug(self.__exposeNodeFn.findPlug(AM_ExposeTransformNode.kNormalizeAttrName, True)).asBool())
        elif self.__objectAxisArg:
            doubleArray.createFromDouble(
                OM.MPlug(
                    self.__exposeNodeFn.findPlug('%s0' % AM_ExposeTransformNode.kObjectAxisAttrName, True)).asDouble(),
                OM.MPlug(
                    self.__exposeNodeFn.findPlug('%s1' % AM_ExposeTransformNode.kObjectAxisAttrName, True)).asDouble(),
                OM.MPlug(
                    self.__exposeNodeFn.findPlug('%s2' % AM_ExposeTransformNode.kObjectAxisAttrName, True)).asDouble())
            self.setResult(OM.MDoubleArray(doubleArray.asDoublePtr(), 3))
        elif self.__referenceAxisArg:
            doubleArray.createFromDouble(
                OM.MPlug(self.__exposeNodeFn.findPlug('%s0' % AM_ExposeTransformNode.kReferenceAxisAttrName,
                                                      True)).asDouble(),
                OM.MPlug(self.__exposeNodeFn.findPlug('%s1' % AM_ExposeTransformNode.kReferenceAxisAttrName,
                                                      True)).asDouble(),
                OM.MPlug(self.__exposeNodeFn.findPlug('%s2' % AM_ExposeTransformNode.kReferenceAxisAttrName,
                                                      True)).asDouble())
            self.setResult(OM.MDoubleArray(doubleArray.asDoublePtr(), 3))

    def redoIt(self):
        # clear out the modifier so it doesn't accumulate old object names
        self.__dgModify = OM.MDGModifier()

        # create a new node if the command is in create mode
        if not self.__isEditUsed:
            self.__exposeNodeArg = OM.MObject(self.__dgModify.createNode(AM_ExposeTransformNode.kPluginNodeId))
            self.__exposeNodeFn.setObject(self.__exposeNodeArg)
            fn = OM.MFnDagNode(self.__exposedObjectArg)
            self.__dgModify.renameNode(self.__exposeNodeArg,
                                       '%s_exposeTransform' % fn.name())  # use fn.name() instead of partialPathName(), as the latter may contain invalid characters

        # assign the -name argument if provided
        if len(self.__exposeNodeName) > 0:
            self.__dgModify.renameNode(self.__exposeNodeArg, self.__exposeNodeName)
        # WARNING: must tell the DGModifier to doIt() now in order to let Maya's auto-rename kick in and ensure the name is unique
        # otherwise attempts to use commandToExecute below may end up using some other object
        self.__dgModify.doIt()

        # set the attributes on the node
        plug = OM.MPlug()
        if self.__exposedObjectArg.isValid():
            # connect the exposed object's worldMatrix attribute
            self.__dgModify.commandToExecute('connectAttr -f %s.worldMatrix %s.%s' % (
                self.__exposedObjectArg.fullPathName(), self.__exposeNodeFn.name(),
                AM_ExposeTransformNode.kObjectMatrixAttrName))
        if self.__referenceObjectArg.isValid():
            # connect the reference object's worldMatrix attribute
            self.__dgModify.commandToExecute('connectAttr -f %s.worldMatrix %s.%s' % (
                self.__referenceObjectArg.fullPathName(), self.__exposeNodeFn.name(),
                AM_ExposeTransformNode.kReferenceMatrixAttrName))
        if self.__rotateOrderArg is not None:
            # set the rotateOrder attribute if it is not connected
            plug = self.__exposeNodeFn.findPlug(AM_ExposeTransformNode.kRotateOrderAttrName, True)
            if not plug.isConnected():
                self.__dgModify.commandToExecute('setAttr %s.%s %i' % (
                    self.__exposeNodeFn.name(), AM_ExposeTransformNode.kRotateOrderAttrName,
                    self.__rotateOrderArg))
        if self.__normalizeArg is not None:
            plug = self.__exposeNodeFn.findPlug(AM_ExposeTransformNode.kNormalizeAttrName, True)
            if not plug.isConnected():
                self.__dgModify.commandToExecute('setAttr %s.%s %s' % (
                    self.__exposeNodeFn.name(), AM_ExposeTransformNode.kNormalizeAttrName,
                    self.__normalizeArg.__str__().lower()))
        if self.__objectAxisArg:
            # set the objectAxis attribute if it is not connected
            plug = self.__exposeNodeFn.findPlug(AM_ExposeTransformNode.kObjectAxisAttrName, True)
            if not plug.isConnected():
                self.__dgModify.commandToExecute('setAttr %s.%s %f %f %f' % (
                    self.__exposeNodeFn.name(), AM_ExposeTransformNode.kObjectAxisAttrName,
                    self.__objectAxisArg.x, self.__objectAxisArg.y, self.__objectAxisArg.z))
        if self.__referenceAxisArg:
            # set the refAxis attribute if it is not connected
            plug = self.__exposeNodeFn.findPlug(AM_ExposeTransformNode.kReferenceAxisAttrName, True)
            if not plug.isConnected():
                self.__dgModify.commandToExecute('setAttr %s.%s %f %f %f' % (
                    self.__exposeNodeFn.name(), AM_ExposeTransformNode.kReferenceAxisAttrName,
                    self.__referenceAxisArg.x, self.__referenceAxisArg.y, self.__referenceAxisArg.z))
        # following Maya convention, select the newly created node if the command is in create mode
        if not self.__isEditUsed:
            self.__dgModify.commandToExecute('select %s' % self.__exposeNodeFn.name())
        self.__dgModify.doIt()
        self.setResult(self.__exposeNodeFn.name())

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
        syntax.addFlag(cls.kExposedObjectFlag, cls.kExposedObjectFlagLong, OM.MSyntax.kSelectionItem)
        syntax.addFlag(cls.kReferenceObjectFlag, cls.kReferenceObjectFlagLong, OM.MSyntax.kSelectionItem)
        syntax.addFlag(cls.kRotateOrderFlag, cls.kRotateOrderFlagLong, OM.MSyntax.kString)
        syntax.addFlag(cls.kNormalizeFlag, cls.kNormalizeFlagLong, OM.MSyntax.kBoolean)
        syntax.addFlag(cls.kObjectAxisFlag, cls.kObjectAxisFlagLong, OM.MSyntax.kDouble, OM.MSyntax.kDouble,
                       OM.MSyntax.kDouble)
        syntax.addFlag(cls.kReferenceAxisFlag, cls.kReferenceAxisFlagLong, OM.MSyntax.kDouble, OM.MSyntax.kDouble,
                       OM.MSyntax.kDouble)
        syntax.useSelectionAsDefault(True)
        syntax.setObjectType(OM.MSyntax.kSelectionList)
        return syntax


# -----------------------------------------------------------------------------
# Node Definition
# -----------------------------------------------------------------------------
class AM_ExposeTransformNode(OMMPx.MPxNode):
    """
	A node to expose transform information about one transform node with
	respect to another.
	\par Input Attributes:
		- \em object: The worldMatrix attribute of the object being exposed.
		- \em reference: The worldMatrix attribute of the reference object.
		- \em rotateOrder: The rotation order for Euler output.
		- \em axis: An axis on the exposed object to use for dot and angle.
		- \em refAxis: An axis on the reference to use for dot and angle.
	\par Output Attributes:
		- \em position: Position of the exposed object relative to the
			reference.
		- \em distance: Distance between the exposed and reference objects.
		- \em rotation: Euler rotation of the exposed object in the space of
			the reference.
		- \em dot: Dot-product of the specified axes on the exposed object and
			the reference.
		- \em angle: Angle between the specified axes on the exposed object and
			the reference.
		- \em dotToTarget: Dot-product of the specified axis on the exposed
			object and the direction to the reference.
		- \em angleToTarget: Angle between the specified axis on the exposed
			object and the direction to the reference.
	"""
    ## the name of the nodeType
    kPluginNodeTypeName = 'am_exposeTransform'
    ## the unique MTypeId for the node
    kPluginNodeId = OM.MTypeId(0x001138C2)

    # input attributes
    ## rotation order for Euler output
    rotateOrder = OM.MObject()
    kRotateOrderAttrName = 'rotateOrder'
    kRotateOrderAttrLongName = 'eulerOutputRotateOrder'
    ## should incoming axes be normalized for computing dot products?
    normalize = OM.MObject()
    kNormalizeAttrName = 'normalize'
    kNormalizeAttrLongName = 'nomalizeAxes'
    ## axis on the object for computing dot product and angle
    objectAxis = OM.MObject()
    kObjectAxisAttrName = 'axis'
    kObjectAxisAttrLongName = 'objectAxis'
    ## axis on the reference object for computing dot product and angle
    referenceAxis = OM.MObject()
    kReferenceAxisAttrName = 'refAxis'
    kReferenceAxisAttrLongName = 'referenceAxis'
    ## worldMatrix of the object
    objectMatrix = OM.MObject()
    kObjectMatrixAttrName = 'object'
    kObjectMatrixAttrLongName = 'objectWorldMatrix'
    ## worldMatrix of the reference object
    referenceMatrix = OM.MObject()
    kReferenceMatrixAttrName = 'reference'
    kReferenceMatrixAttrLongName = 'referenceWorldMatrix'

    # output attributes
    ## position of the object with respect to the reference
    position = OM.MObject()
    kPositionAttrName = 'position'
    kPositionAttrLongName = 'position'
    ## distance between the two objects
    distance = OM.MObject()
    kDistanceAttrName = 'distance'
    kDistanceAttrLongName = 'distance'
    ## rotation of the object with respect to the reference
    rotation = OM.MObject()
    kRotationAttrName = 'rotation'
    kRotationAttrLongName = 'eulerRotation'
    ## dot product of specified axes on object and reference
    dot = OM.MObject()
    kDotAttrName = 'dotProduct'
    kDotAttrLongName = 'dot'
    ## angle between specified axes on object and reference
    angle = OM.MObject()
    kAngleAttrName = 'angle'
    kAngleAttrLongName = 'angle'
    ## dot product of specified axes on object and direction to reference
    dotToTarget = OM.MObject()
    kDotToTargetAttrName = 'dotTo'
    kDotToTargetAttrLongName = 'dotToTarget'
    ## angle between specified axes on object and direction to reference
    angleToTarget = OM.MObject()
    kAngleToTargetAttrName = 'angleToTarget'
    kAngleToTargetAttrLongName = 'angleTo'

    def __init__(self):
        OMMPx.MPxNode.__init__(self)

    def compute(self, plug, dataBlock):
        """Compute an exposed object's transformations with respect to a reference object."""
        if (plug == AM_ExposeTransformNode.position or
                (
                            plug.isChild() and plug.parent() == AM_ExposeTransformNode.position) or  # WARNING: without this, position always initializes to 0, 0, 0 when connection is made
                    plug == AM_ExposeTransformNode.distance or
                    plug == AM_ExposeTransformNode.rotation or
                (
                            plug.isChild() and plug.parent() == AM_ExposeTransformNode.rotation) or  # WARNING: without this, setting rotateOrder attribute manually won't push a compute()
                    plug == AM_ExposeTransformNode.dot or
                    plug == AM_ExposeTransformNode.angle or
                    plug == AM_ExposeTransformNode.dotToTarget or
                    plug == AM_ExposeTransformNode.angleToTarget):
            # get the incoming data
            # rotation order for Euler output
            dataHandle = OM.MDataHandle(dataBlock.inputValue(AM_ExposeTransformNode.rotateOrder))
            eRotateOrder = dataHandle.asShort()
            # should the incoming axes be normalized for computing dot products?
            dataHandle = OM.MDataHandle(dataBlock.inputValue(AM_ExposeTransformNode.normalize))
            bNormalizeInputAxes = dataHandle.asBool()
            # axis on the object for computing dot product and angle
            dataHandle = OM.MDataHandle(dataBlock.inputValue(AM_ExposeTransformNode.objectAxis))
            vObjectAxis = OM.MVector(dataHandle.asVector())
            if bNormalizeInputAxes:
                vObjectAxis.normalize()
            # axis on the reference object for computing dot product and angle
            dataHandle = OM.MDataHandle(dataBlock.inputValue(AM_ExposeTransformNode.referenceAxis))
            vReferenceAxis = OM.MVector(dataHandle.asVector())
            if bNormalizeInputAxes:
                vReferenceAxis.normalize()
            # worldMatrix of the object
            dataHandle = OM.MDataHandle(dataBlock.inputValue(AM_ExposeTransformNode.objectMatrix))
            mObjectMatrix = OM.MMatrix(dataHandle.asMatrix())
            # worldMatrix of the reference
            dataHandle = OM.MDataHandle(dataBlock.inputValue(AM_ExposeTransformNode.referenceMatrix))
            mReferenceMatrix = OM.MMatrix(dataHandle.asMatrix())

            # compute the output values
            mOutputMatrix = OM.MTransformationMatrix(mObjectMatrix * mReferenceMatrix.inverse())
            vOutPosition = OM.MVector(mOutputMatrix.getTranslation(OM.MSpace.kTransform))
            vOutRotation = OM.MEulerRotation(mOutputMatrix.eulerRotation().reorder(eRotateOrder))
            vObjectAxis *= mObjectMatrix  # rotate objectAxis into world space
            vReferenceAxis *= mReferenceMatrix  # rotate referenceAxis into world space
            vToTarget = OM.MVector(
                mReferenceMatrix(3, 0) - mObjectMatrix(3, 0),
                mReferenceMatrix(3, 1) - mObjectMatrix(3, 1),
                mReferenceMatrix(3, 2) - mObjectMatrix(3,
                                                       2))  # the vector from the object's axis to the reference object's position
            if bNormalizeInputAxes:
                vObjectAxis.normalize()
                vReferenceAxis.normalize()
                vToTarget.normalize()

            # set the outgoing plugs
            outputHandle = dataBlock.outputValue(AM_ExposeTransformNode.position)
            outputHandle.set3Double(vOutPosition.x, vOutPosition.y, vOutPosition.z)
            outputHandle = dataBlock.outputValue(AM_ExposeTransformNode.distance)
            outputHandle.setDouble(vOutPosition.length())
            outputHandle = dataBlock.outputValue(AM_ExposeTransformNode.rotation)
            outputHandle.set3Double(math.degrees(vOutRotation.x), math.degrees(vOutRotation.y),
                                    math.degrees(vOutRotation.z))
            outputHandle = dataBlock.outputValue(AM_ExposeTransformNode.dot)
            outputHandle.setDouble(vObjectAxis * vReferenceAxis)
            outputHandle = dataBlock.outputValue(AM_ExposeTransformNode.angle)
            outputHandle.setDouble(math.degrees(vObjectAxis.angle(vReferenceAxis)))
            outputHandle = dataBlock.outputValue(AM_ExposeTransformNode.dotToTarget)
            outputHandle.setDouble(vObjectAxis * vToTarget)
            outputHandle = dataBlock.outputValue(AM_ExposeTransformNode.angleToTarget)
            outputHandle.setDouble(math.degrees(vObjectAxis.angle(vToTarget)))
            dataBlock.setClean(plug)

        else:
            return OM.kUnknownParameter

    # -----------------------------------------------------------------------------
    # Node Creator
    # -----------------------------------------------------------------------------
    @classmethod
    def nodeCreator(cls):
        return OMMPx.asMPxPtr(cls())

    # -----------------------------------------------------------------------------
    # Node Initializer
    # -----------------------------------------------------------------------------
    @classmethod
    def nodeInitializer(cls):
        # input attributes
        # rotation order for Euler output
        eAttr = OM.MFnEnumAttribute()
        cls.rotateOrder = eAttr.create(cls.kRotateOrderAttrLongName, cls.kRotateOrderAttrName, 0)
        field0 = 'xyz'
        field1 = 'yzx'
        field2 = 'zxy'
        field3 = 'xzy'
        field4 = 'yxz'
        field5 = 'zyx'
        eAttr.addField(field0, kRotateOrderMapping[field0.lower()])
        eAttr.addField(field1, kRotateOrderMapping[field1.lower()])
        eAttr.addField(field2, kRotateOrderMapping[field2.lower()])
        eAttr.addField(field3, kRotateOrderMapping[field3.lower()])
        eAttr.addField(field4, kRotateOrderMapping[field4.lower()])
        eAttr.addField(field5, kRotateOrderMapping[field5.lower()])
        eAttr.setWritable(True)
        eAttr.setStorable(True)
        eAttr.setReadable(True)
        eAttr.setKeyable(True)
        # should incoming axes be normalized for computing dot products?
        nAttr = OM.MFnNumericAttribute()
        cls.normalize = nAttr.create(cls.kNormalizeAttrLongName, cls.kNormalizeAttrName, OM.MFnNumericData.kBoolean,
                                     True)
        nAttr.setWritable(True)
        nAttr.setStorable(True)
        nAttr.setReadable(True)
        nAttr.setKeyable(True)
        # axis on the object for computing dot product and angle
        cls.objectAxis = nAttr.create(cls.kObjectAxisAttrLongName, cls.kObjectAxisAttrName, OM.MFnNumericData.k3Double)
        nAttr.setWritable(True)
        nAttr.setStorable(True)
        nAttr.setReadable(True)
        nAttr.setKeyable(True)
        # axis on the reference object for computing dot product and angle
        cls.referenceAxis = nAttr.create(cls.kReferenceAxisAttrLongName, cls.kReferenceAxisAttrName,
                                         OM.MFnNumericData.k3Double)
        nAttr.setWritable(True)
        nAttr.setStorable(True)
        nAttr.setReadable(True)
        nAttr.setKeyable(True)
        # worldMatrix of the object
        mAttr = OM.MFnMatrixAttribute()
        cls.objectMatrix = mAttr.create(cls.kObjectMatrixAttrLongName, cls.kObjectMatrixAttrName,
                                        OM.MFnMatrixAttribute.kDouble)
        mAttr.setWritable(True)
        mAttr.setStorable(True)
        mAttr.setReadable(True)
        mAttr.setKeyable(False)
        mAttr.setHidden(False)
        # worldMatrix of the reference object
        cls.referenceMatrix = mAttr.create(cls.kReferenceMatrixAttrLongName, cls.kReferenceMatrixAttrName,
                                           OM.MFnMatrixAttribute.kDouble)
        mAttr.setWritable(True)
        mAttr.setStorable(True)
        mAttr.setReadable(True)
        mAttr.setKeyable(False)
        mAttr.setHidden(False)

        # output attributes
        # position of the object with respect to the reference
        nAttr = OM.MFnNumericAttribute()
        cls.position = nAttr.create(cls.kPositionAttrLongName, cls.kPositionAttrName, OM.MFnNumericData.k3Double)
        nAttr.setWritable(True)
        nAttr.setStorable(False)
        nAttr.setReadable(True)
        nAttr.setChannelBox(True)
        # distance between the two objects
        cls.distance = nAttr.create(cls.kDistanceAttrLongName, cls.kDistanceAttrName, OM.MFnNumericData.kDouble)
        nAttr.setWritable(True)
        nAttr.setStorable(False)
        nAttr.setReadable(True)
        nAttr.setChannelBox(True)
        # rotation of the object with respect to the reference
        cls.rotation = nAttr.create(cls.kRotationAttrLongName, cls.kRotationAttrName, OM.MFnNumericData.k3Double)
        nAttr.setWritable(True)
        nAttr.setStorable(False)
        nAttr.setReadable(True)
        nAttr.setChannelBox(True)
        # dot product of specified axes on object and reference
        cls.dot = nAttr.create(cls.kDotAttrLongName, cls.kDotAttrName, OM.MFnNumericData.kDouble)
        nAttr.setWritable(True)
        nAttr.setStorable(False)
        nAttr.setReadable(True)
        nAttr.setChannelBox(True)
        # angle between specified axes on object and reference
        cls.angle = nAttr.create(cls.kAngleAttrLongName, cls.kAngleAttrName, OM.MFnNumericData.kDouble)
        nAttr.setWritable(True)
        nAttr.setStorable(False)
        nAttr.setReadable(True)
        nAttr.setChannelBox(True)
        # dot product of specified axes on object and direction to reference
        cls.dotToTarget = nAttr.create(cls.kDotToTargetAttrLongName, cls.kDotToTargetAttrName,
                                       OM.MFnNumericData.kDouble)
        nAttr.setWritable(True)
        nAttr.setStorable(False)
        nAttr.setReadable(True)
        nAttr.setChannelBox(True)
        # angle between specified axes on object and direction to reference
        cls.angleToTarget = nAttr.create(cls.kAngleToTargetAttrLongName, cls.kAngleToTargetAttrName,
                                         OM.MFnNumericData.kDouble)
        nAttr.setWritable(True)
        nAttr.setStorable(False)
        nAttr.setReadable(True)
        nAttr.setChannelBox(True)

        # add the attributes
        cls.addAttribute(cls.objectMatrix)
        cls.addAttribute(cls.referenceMatrix)
        cls.addAttribute(cls.position)
        cls.addAttribute(cls.distance)
        cls.addAttribute(cls.rotateOrder)
        cls.addAttribute(cls.rotation)
        cls.addAttribute(cls.normalize)
        cls.addAttribute(cls.objectAxis)
        cls.addAttribute(cls.referenceAxis)
        cls.addAttribute(cls.dot)
        cls.addAttribute(cls.angle)
        cls.addAttribute(cls.dotToTarget)
        cls.addAttribute(cls.angleToTarget)
        # establish effects on position output
        cls.attributeAffects(cls.objectMatrix, cls.position)
        cls.attributeAffects(cls.referenceMatrix, cls.position)
        # establish effects on distance output
        cls.attributeAffects(cls.objectMatrix, cls.distance)
        cls.attributeAffects(cls.referenceMatrix, cls.distance)
        # establish effects on rotation output
        cls.attributeAffects(cls.objectMatrix, cls.rotation)
        cls.attributeAffects(cls.referenceMatrix, cls.rotation)
        cls.attributeAffects(cls.rotateOrder, cls.rotation)
        # establish effects on dot product output
        cls.attributeAffects(cls.objectMatrix, cls.dot)
        cls.attributeAffects(cls.referenceMatrix, cls.dot)
        cls.attributeAffects(cls.normalize, cls.dot)
        cls.attributeAffects(cls.objectAxis, cls.dot)
        cls.attributeAffects(cls.referenceAxis, cls.dot)
        # establish effects on angle output
        cls.attributeAffects(cls.objectMatrix, cls.angle)
        cls.attributeAffects(cls.referenceMatrix, cls.angle)
        cls.attributeAffects(cls.objectAxis, cls.angle)
        cls.attributeAffects(cls.referenceAxis, cls.angle)
        # establish effects on dot product to target output
        cls.attributeAffects(cls.objectMatrix, cls.dotToTarget)
        cls.attributeAffects(cls.referenceMatrix, cls.dotToTarget)
        cls.attributeAffects(cls.normalize, cls.dotToTarget)
        cls.attributeAffects(cls.objectAxis, cls.dotToTarget)
        cls.attributeAffects(cls.referenceAxis, cls.dotToTarget)
        # establish effects on angle to target output
        cls.attributeAffects(cls.objectMatrix, cls.angleToTarget)
        cls.attributeAffects(cls.referenceMatrix, cls.angleToTarget)
        cls.attributeAffects(cls.objectAxis, cls.angleToTarget)
        cls.attributeAffects(cls.referenceAxis, cls.angleToTarget)


# -----------------------------------------------------------------------------
# Initialize
# -----------------------------------------------------------------------------
def initializePlugin(mobject):
    plugin = OMMPx.MFnPlugin(mobject, 'Adam Mechtley', kVersionNumber, 'Any')
    # dependency node
    try:
        plugin.registerNode(AM_ExposeTransformNode.kPluginNodeTypeName, AM_ExposeTransformNode.kPluginNodeId,
                            AM_ExposeTransformNode.nodeCreator, AM_ExposeTransformNode.nodeInitializer)
    except:
        sys.stderr.write('Failed to register node: %s\n' % AM_ExposeTransformNode.kPluginNodeTypeName)
        raise
    # command
    try:
        plugin.registerCommand(AM_ExposeTransformCmd.kPluginCmdName, AM_ExposeTransformCmd.cmdCreator,
                               AM_ExposeTransformCmd.syntaxCreator)
    except:
        sys.stderr.write('Failed to register command: %s\n' % AM_ExposeTransformCmd.kPluginCmdName)
        raise


# -----------------------------------------------------------------------------
# Uninitialize
# -----------------------------------------------------------------------------
def uninitializePlugin(mobject):
    plugin = OMMPx.MFnPlugin(mobject)
    # dependency node
    try:
        plugin.deregisterNode(AM_ExposeTransformNode.kPluginNodeId)
    except:
        sys.stderr.write('Failed to unregister node: %s\n' % AM_ExposeTransformNode.kPluginNodeTypeName)
        raise
    # command
    try:
        plugin.deregisterCommand(AM_ExposeTransformCmd.kPluginCmdName)
    except:
        sys.stderr.write('Failed to unregister command: %s\n' % AM_ExposeTransformCmd.kPluginCmdName)
        raise