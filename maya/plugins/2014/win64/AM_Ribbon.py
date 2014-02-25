"""
A node and corresponding command for building ribbon meshes along NURBS curves
using supplied parameters.

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

\namespace AM_Ribbon
"""

import sys, math, re
import maya.OpenMaya as OM
import maya.OpenMayaAnim as OMA
import maya.OpenMayaMPx as OMMPx

## current version of the plug-in
kVersionNumber = '1.01'

## a dictionary of possible uv group scale values
kUVScaleGroupMapping = {
	'individual' : 0, 
	'longest' : 1, 
	'shortest' : 2, 
	'0' : 0, 
	'1' : 1, 
	'2' : 2
}
## a dictionary of possible uv pinning values
kUVPinMapping = {
	'top' : 0, 
	'bottom' : 1, 
	'0' : 0, 
	'1' : 1, 
}

# -----------------------------------------------------------------------------
# Command Definition
# -----------------------------------------------------------------------------
class AM_RibbonsCmd(OMMPx.MPxCommand):
	"""
	A command to quickly create, edit, or query an am_ribbon node.
	"""
	
	## the name of the command
	kPluginCmdName = 'am_ribbon'
	
	## specifies a name for the new objects (CQ)
	kNameFlag = '-n'
	kNameFlagLong = '-name'
	## specifies the inputCurve attribute (CE)
	kCurveFlag = '-c'
	kCurveFlagLong = '-curve'
	## specifies the width of the ribbons (CEQ)
	kWidthFlag = '-w'
	kWidthFlagLong = '-width'
	## specifies an absolute number of divisions (CEQ)
	kDivisionsFlag = '-d'
	kDivisionsFlagLong = '-divisions'
	## specifies the number of divisions per centimeter (CEQ)
	kDivisionsPerUnitFlag = '-dp'
	kDivisionsPerUnitFlagLong = '-divisionsPerUnit'
	## specifies the amount of taper (CEQ)
	kTaperFlag = '-t'
	kTaperFlagLong = '-taper'
	## specifies the amount of twist at the base (CEQ)
	kTwistBaseFlag = '-tb'
	kTwistBaseFlagLong = '-twistBase'
	## specifies the amount of twist at the end (CEQ)
	kTwistLengthFlag = '-tl'
	kTwistLengthFlagLong = '-twistLength'
	## specifies the up-vector at the base (CEQ)
	kUpVectorFlag = '-up'
	kUpVectorFlagLong = '-upVector'
	## specifies the uv scale factor (CEQ)
	kUVScaleFlag = '-uv'
	kUVScaleFlagLong = '-uvScale'
	## specifies a scale override for all new ribbons  (C)
	kUVScaleGroupFlag = '-uvg'
	kUVScaleGroupFlagLong = '-uvGroupScale'
	## specifies the uv pinning location  (CEQ)
	kUVPinFlag = '-uvp'
	kUVPinFlagLong = '-uvPin'
	
	def __init__(self):
		OMMPx.MPxCommand.__init__(self)
		self.__isQueryUsed = True # initialize to True so command is not added to queue if argument parsing fails
		self.__isEditUsed = False
		
		self.__ribbonNodeFn = OM.MFnDependencyNode() # the am_ribbon node selected for edit and query modes
		
		self.__selectedCurves = OM.MSelectionList() # selection list containing only nurbs curves in the object list
		
		self.__baseNameArg = '' # base name for the newly created ribbon meshes
		self.__widthArg = None # width of the ribbon in centimeters
		self.__divisionsArg = None # divisions along the ribbon
		self.__divisionsPerUnitArg = None # optional parameter to specify a rate of divisions to get similar-sized faces when multiple curves are selected
		self.__taperArg = None # scale at the end of the ribbon
		self.__twistBaseArg = None # rotation around the curve at the start of the ribbon
		self.__twistLengthArg = None # rotation around the curve at the end of the ribbon
		self.__upVectorArg = None # base up-vector at the start of the ribbon
		self.__uvScaleArg = None # scale factor of new uvs
		self.__uvScaleGroupArg = None # scaling method to apply to the whole group of newly-created ribbons--only in create mode
		self.__uvPinArg = None # uv pinning location
		
		self.__dagModify = OM.MDagModifier() # Dag modifier used to create new shapes/transforms
		self.__dgModify = OM.MDGModifier() # DG modifier used to create and modify new ribbon nodes
	
	def doIt(self, args):
		# parse the arguments
		try: argData = OM.MArgDatabase(self.syntax(), args) # if this fails, it will raise its own exception...
		except: pass # ...so we can just pass here
		else:
			# read all of the arguments and store them to the appropriate data attributes
			# manually confirm the object list
			selection = OM.MSelectionList()
			argData.getObjects(selection)
			
			# ordinarily, the command is requires that at least one object be selected
			if selection.length() < 1:
				# if in create mode, use the argument specified with the -curve flag as the selected curve
				if not argData.isQuery() and not argData.isEdit() and argData.isFlagSet(AM_RibbonsCmd.kCurveFlag):
					selection.add(argData.flagArgumentString(AM_RibbonsCmd.kCurveFlag, 0))
				else: raise Exception('This command requires at least 1 object to be specified or selected;  found %i.'%selection.length())
			
			# in edit or query mode, the object must be a single am_ribbon node
			if argData.isEdit() or argData.isQuery():
				if selection.length() is not 1:
					raise Exception('This command requires exactly 1 %s node to be specified or selected;  found %i.'%(AM_RibbonsNode.kPluginNodeTypeName, selection.length()))
				else:
					ribbonNode = OM.MObject()
					selection.getDependNode(0, ribbonNode)
					self.__ribbonNodeFn.setObject(ribbonNode)
					if not self.__ribbonNodeFn.typeId() == AM_RibbonsNode.kPluginNodeId:
						raise Exception('The provided dependency node %s is not of type %s.\n'%(self.__ribbonNodeFn.name(), AM_RibbonsNode.kPluginNodeTypeName))
			
			# confirm specified or selected curves
			if not argData.isQuery():
				# manually specifying a -curve argument will override the selection list in create mode
				if argData.isFlagSet(AM_RibbonsCmd.kCurveFlag):
					selection.clear()
					selection.add(argData.flagArgumentString(AM_RibbonsCmd.kCurveFlag, 0))
				# store the curves if command is in create mode or -curve has been specified
				if not argData.isEdit() or (argData.isEdit() and argData.isFlagSet(AM_RibbonsCmd.kCurveFlag)):
					curve = OM.MObject()
					iter = OM.MItSelectionList(selection, OM.MFn.kNurbsCurve)
					while not iter.isDone():
						iter.getDependNode(curve)
						self.__selectedCurves.add(curve)
						iter.next()
					# early out if there are no nurbs curves selected
					if self.__selectedCurves.length() == 0:
						raise Exception('This command requires at least 1 NURBS curve to be specified or selected;  found 0.')
			
			# perform the query
			if argData.isQuery():
				self.__curveArg = argData.isFlagSet(AM_RibbonsCmd.kCurveFlag)
				self.__widthArg = argData.isFlagSet(AM_RibbonsCmd.kWidthFlag)
				self.__divisionsArg = argData.isFlagSet(AM_RibbonsCmd.kDivisionsFlag)
				self.__divisionsPerUnitArg = argData.isFlagSet(AM_RibbonsCmd.kDivisionsPerUnitFlag)
				self.__taperArg = argData.isFlagSet(AM_RibbonsCmd.kTaperFlag)
				self.__twistBaseArg = argData.isFlagSet(AM_RibbonsCmd.kTwistBaseFlag)
				self.__twistLengthArg = argData.isFlagSet(AM_RibbonsCmd.kTwistLengthFlag)
				self.__upVectorArg = argData.isFlagSet(AM_RibbonsCmd.kUpVectorFlag)
				self.__uvScaleArg = argData.isFlagSet(AM_RibbonsCmd.kUVScaleFlag)
				self.__uvPinArg = argData.isFlagSet(AM_RibbonsCmd.kUVPinFlag)
				self.doItQuery()
				
			# set up other arguments and call redoIt() for create or edit mode
			else:
				# validate the name flag
				if argData.isFlagSet(AM_RibbonsCmd.kNameFlag):
					self.__baseNameArg = argData.flagArgumentString(AM_RibbonsCmd.kNameFlag, 0)
					if(len(self.__baseNameArg) < 1 or self.__baseNameArg[0].isalpha() is False or len(re.split('\W+', self.__baseNameArg)) > 1):
						raise Exception('%s is not a valid node name. Did you type it correctly?'%self.__baseNameArg)
				
				# manually specifying a divisions will trump the divisionsPerUnit flag
				if argData.isFlagSet(AM_RibbonsCmd.kDivisionsFlag):
					self.__divisionsArg = argData.flagArgumentInt(AM_RibbonsCmd.kDivisionsFlag, 0)
				elif argData.isFlagSet(AM_RibbonsCmd.kDivisionsPerUnitFlag): # only use divisions per unit if a manual divisions value is not specified
					self.__divisionsPerUnitArg = argData.flagArgumentDouble(AM_RibbonsCmd.kDivisionsPerUnitFlag, 0)
				
				# remaining data attributes
				if argData.isFlagSet(AM_RibbonsCmd.kWidthFlag):
					self.__widthArg = argData.flagArgumentDouble(AM_RibbonsCmd.kWidthFlag, 0)
				if argData.isFlagSet(AM_RibbonsCmd.kTaperFlag):
					self.__taperArg = argData.flagArgumentDouble(AM_RibbonsCmd.kTaperFlag, 0)
				if argData.isFlagSet(AM_RibbonsCmd.kTwistBaseFlag):
					self.__twistBaseArg = argData.flagArgumentDouble(AM_RibbonsCmd.kTwistBaseFlag, 0)
				if argData.isFlagSet(AM_RibbonsCmd.kTwistLengthFlag):
					self.__twistLengthArg = argData.flagArgumentDouble(AM_RibbonsCmd.kTwistLengthFlag, 0)
				if argData.isFlagSet(AM_RibbonsCmd.kUpVectorFlag):
					self.__upVectorArg = OM.MVector(
						argData.flagArgumentDouble(AM_RibbonsCmd.kUpVectorFlag, 0), 
						argData.flagArgumentDouble(AM_RibbonsCmd.kUpVectorFlag, 1), 
						argData.flagArgumentDouble(AM_RibbonsCmd.kUpVectorFlag, 2))
				if argData.isFlagSet(AM_RibbonsCmd.kUVScaleFlag):
					self.__uvScaleArg = argData.flagArgumentDouble(AM_RibbonsCmd.kUVScaleFlag, 0)
				if argData.isFlagSet(AM_RibbonsCmd.kUVScaleGroupFlag):
					self.__uvScaleGroupArg = kUVScaleGroupMapping[argData.flagArgumentString(AM_RibbonsCmd.kUVScaleGroupFlag, 0).lower()]
				if argData.isFlagSet(AM_RibbonsCmd.kUVPinFlag):
					self.__uvPinArg = kUVPinMapping[argData.flagArgumentString(AM_RibbonsCmd.kUVPinFlag, 0).lower()]
				
				self.__isEditUsed = argData.isEdit()
				self.__isQueryUsed = False
				
				self.redoIt()
	
	def doItQuery(self):
		# query mode typically only supports one argument at a time
		# this principle ensures that the result will be given in a way that can be stored in a variable
		doubleArray = OM.MScriptUtil()
		if self.__widthArg:
			self.setResult(OM.MPlug(self.__ribbonNodeFn.findPlug(AM_RibbonsNode.kInputWidthAttrName, True)).asDouble())
		elif self.__divisionsArg:
			self.setResult(OM.MPlug(self.__ribbonNodeFn.findPlug(AM_RibbonsNode.kInputDivisionsAttrName, True)).asInt())
		elif self.__divisionsPerUnitArg:
			self.__divisionsArg = OM.MPlug(self.__ribbonNodeFn.findPlug(AM_RibbonsNode.kInputDivisionsAttrName, True)).asInt()
			# find the curve upstream
			plug = OM.MPlug(self.__ribbonNodeFn.findPlug(AM_RibbonsNode.kInputCurveAttrName, True))
			iter = OM.MItDependencyGraph(plug, OM.MFn.kShape, OM.MItDependencyGraph.kUpstream)
			curve = OM.MDagPath()
			while not iter.isDone():
				if not curve.isValid(): # ignore everything beyond the first valid hit
					OM.MDagPath.getAPathTo(iter.currentItem(), curve)
				iter.next()
			if curve.isValid():
				curveFn = OM.MFnNurbsCurve(curve)
				self.setResult(self.__divisionsArg/curveFn.length())
			else:
				OM.MGlobal.displayError('No NURBS curve is attached to %s.%s;  unable to compute divisions per unit.\n'%(
					self.__ribbonNodeFn.name(), AM_RibbonsNode.kInputCurveAttrName))
		elif self.__taperArg:
			self.setResult(OM.MPlug(self.__ribbonNodeFn.findPlug(AM_RibbonsNode.kInputTaperAttrName, True)).asDouble())
		elif self.__twistBaseArg:
			self.setResult(OM.MPlug(self.__ribbonNodeFn.findPlug(AM_RibbonsNode.kInputTwistBaseAttrName, True)).asDouble())
		elif self.__twistLengthArg:
			self.setResult(OM.MPlug(self.__ribbonNodeFn.findPlug(AM_RibbonsNode.kInputTwistLengthAttrName, True)).asDouble())
		elif self.__upVectorArg:
			doubleArray.createFromDouble(
				OM.MPlug(self.__ribbonNodeFn.findPlug('%s0'%AM_RibbonsNode.kInputUpVectorAttrName, True)).asDouble(),
				OM.MPlug(self.__ribbonNodeFn.findPlug('%s1'%AM_RibbonsNode.kInputUpVectorAttrName, True)).asDouble(),
				OM.MPlug(self.__ribbonNodeFn.findPlug('%s2'%AM_RibbonsNode.kInputUpVectorAttrName, True)).asDouble())
			self.setResult(OM.MDoubleArray(doubleArray.asDoublePtr(), 3))
		elif self.__uvScaleArg:
			self.setResult(OM.MPlug(self.__ribbonNodeFn.findPlug(AM_RibbonsNode.kInputUVScaleAttrName, True)).asDouble())
		elif self.__uvPinArg:
			self.setResult(OM.MPlug(self.__ribbonNodeFn.findPlug(AM_RibbonsNode.kInputUVPinAttrName, True)).asInt())
		
	def redoIt(self):
		# clear out the modifiers to they don't store old object names
		self.__dagModify = OM.MDagModifier()
		self.__dgModify = OM.MDGModifier()
		
		# create new nodes if the command is in create mode
		newObjects = OM.MObjectArray()
		pathToCurve = OM.MDagPath()
		curve = OM.MObject()
		curveFn = OM.MFnNurbsCurve()
		shapeFn = OM.MFnDagNode()
		pathToShape = OM.MDagPath()
		curveStartPoint = OM.MPoint()
		transformFn = OM.MFnTransform()
		pathToNewObject = OM.MDagPath()
		newRibbonNodes = OM.MObjectArray()
		if not self.__isEditUsed:
			if len(self.__baseNameArg) < 1:
				self.__baseNameArg = 'pRibbon'
			for i in range(self.__selectedCurves.length()):
				newMesh = self.__dagModify.createNode('mesh')
				newObjects.append(newMesh)
				self.__dagModify.renameNode(newMesh, '%s%s'%(self.__baseNameArg, i+1))
			self.__dagModify.doIt()
			
			# position the new meshes' transform nodes on their respective curves' starting points
			for i in range(self.__selectedCurves.length()):
				self.__selectedCurves.getDependNode(i, curve)
				##curveFn.setObject(curve)
				##curveFn.getPath(pathToCurve)
				OM.MDagPath.getAPathTo(curve, pathToCurve)
				curveFn.setObject(pathToCurve) # initialize using a dagpath so world-space can be used
				curveFn.getPointAtParam(0.0, curveStartPoint, OM.MSpace.kWorld)
				##transformFn.setObject(newObjects[i])
				##transformFn.getPath(pathToNewObject)
				OM.MDagPath.getAPathTo(newObjects[i], pathToNewObject)
				transformFn.setObject(pathToNewObject) # initialize using a dagpath so world-space can be used
				transformFn.setTranslation(OM.MVector(curveStartPoint), OM.MSpace.kWorld)
				
			# create new ribbon nodes
			for i in range(newObjects.length()):
				transformFn.setObject(newObjects[i])
				# create the new ribbon node
				newRibbonNode = self.__dgModify.createNode(AM_RibbonsNode.kPluginNodeId)
				newRibbonNodes.append(newRibbonNode)
				self.__dgModify.renameNode(newRibbonNode, '%s_ribbon'%transformFn.partialPathName())
				# a little sloppy, but use this opportunity to rename the shape nodes for the new meshes too
				transformFn.getPath(pathToShape)
				pathToShape.extendToShape()
				shapeFn.setObject(pathToShape)
				self.__dgModify.renameNode(shapeFn.object(), '%sShape%s'%(self.__baseNameArg, (transformFn.name()).lstrip(self.__baseNameArg)))
					
		# if in edit mode, then simply rename the ribbon node
		else:
			newObjects.append(self.__ribbonNodeFn.object()) # sloppy, but it gets the job done
			if len(self.__baseNameArg) > 0:
				self.__dgModify.renameNode(self.__ribbonNodeFn.object(), self.__baseNameArg)
				newObjects.append(self.__ribbonNodeFn.object())
					
		self.__dgModify.doIt()
		
		# connect the ribbon nodes and set their attributes
		plug = OM.MPlug()
		for i in range(newObjects.length()):
			# establish parameters for create mode
			if not self.__isEditUsed:
				##transformFn.setObject(newObjects[i])
				##transformFn.getPath(pathToShape)
				OM.MDagPath.getAPathTo(newObjects[i], pathToShape)
				pathToShape.extendToShape()
				shapeFn.setObject(pathToShape)
				self.__selectedCurves.getDependNode(i, curve)
				##curveFn.setObject(curve)
				##curveFn.getPath(pathToCurve)
				OM.MDagPath.getAPathTo(curve, pathToCurve)
				self.__ribbonNodeFn.setObject(newRibbonNodes[i])
			
			# establish optional parameters for edit mode
			else:
				# if the ribbon node is attached to a curve, then the user can edit divisions per unit
				pathToCurve = OM.MDagPath()
				if self.__divisionsPerUnitArg or self.__selectedCurves.length() > 0:
					plug = self.__ribbonNodeFn.findPlug(AM_RibbonsNode.kInputCurveAttrName, True)
					iter = OM.MItDependencyGraph(plug, OM.MFn.kShape, OM.MItDependencyGraph.kUpstream)
					pathToCurve = OM.MDagPath()
					while not iter.isDone():
						if not pathToCurve.isValid(): # stop at the first one we find
							##OM.MFnDagNode(iter.currentItem()).getPath(pathToCurve)
							OM.MDagPath.getAPathTo(iter.currentItem(), pathToCurve)
						iter.next()
					if pathToCurve.isValid():
						curveFn = OM.MFnNurbsCurve(pathToCurve)
					else:
						curveFn = False
					# if the -curve argument was specified, then store its value
					if self.__selectedCurves.length() > 0:
						self.__selectedCurves.getDependNode(0, curve)
						##shapeFn.setObject(curve)
						##shapeFn.getPath(pathToCurve)
						OM.MDagPath.getAPathTo(curve, pathToCurve)
					else:
						pathToCurve = OM.MDagPath()
			
			# set attributes on the new ribbon node
			if self.__widthArg is not None:
				plug = self.__ribbonNodeFn.findPlug(AM_RibbonsNode.kInputWidthAttrName, True)
				if not plug.isConnected():
					self.__dgModify.commandToExecute('setAttr %s.%s %f'%(
						self.__ribbonNodeFn.name(), AM_RibbonsNode.kInputWidthAttrName,
						self.__widthArg))
			if self.__divisionsArg is not None or self.__divisionsPerUnitArg is not None:
				if self.__divisionsPerUnitArg and curveFn:
					self.__divisionsArg = int(round(self.__divisionsPerUnitArg * curveFn.length()))
				plug = self.__ribbonNodeFn.findPlug(AM_RibbonsNode.kInputDivisionsAttrName, True)
				if not plug.isConnected():
					self.__dgModify.commandToExecute('setAttr %s.%s %i'%(
						self.__ribbonNodeFn.name(), AM_RibbonsNode.kInputDivisionsAttrName,
						self.__divisionsArg))
			if self.__taperArg is not None:
				plug = self.__ribbonNodeFn.findPlug(AM_RibbonsNode.kInputTaperAttrName, True)
				if not plug.isConnected():
					self.__dgModify.commandToExecute('setAttr %s.%s %f'%(
						self.__ribbonNodeFn.name(), AM_RibbonsNode.kInputTaperAttrName,
						self.__taperArg))
			if self.__twistBaseArg is not None:
				plug = self.__ribbonNodeFn.findPlug(AM_RibbonsNode.kInputTwistBaseAttrName, True)
				if not plug.isConnected():
					self.__dgModify.commandToExecute('setAttr %s.%s %f'%(
						self.__ribbonNodeFn.name(), AM_RibbonsNode.kInputTwistBaseAttrName,
						self.__twistBaseArg))
			if self.__twistLengthArg is not None:
				plug = self.__ribbonNodeFn.findPlug(AM_RibbonsNode.kInputTwistLengthAttrName, True)
				if not plug.isConnected():
					self.__dgModify.commandToExecute('setAttr %s.%s %f'%(
						self.__ribbonNodeFn.name(), AM_RibbonsNode.kInputTwistLengthAttrName,
						self.__twistLengthArg))
			if self.__upVectorArg:
				plug = self.__ribbonNodeFn.findPlug(AM_RibbonsNode.kInputUpVectorAttrName, True)
				if not plug.isConnected():
					self.__dgModify.commandToExecute('setAttr %s.%s %f %f %f'%(
						self.__ribbonNodeFn.name(), AM_RibbonsNode.kInputUpVectorAttrName,
						self.__upVectorArg.x, self.__upVectorArg.y, self.__upVectorArg.z))
			if self.__uvPinArg is not None:
				plug = self.__ribbonNodeFn.findPlug(AM_RibbonsNode.kInputUVPinAttrName, True)
				if not plug.isConnected():
					self.__dgModify.commandToExecute('setAttr %s.%s %i'%(
						self.__ribbonNodeFn.name(), AM_RibbonsNode.kInputUVPinAttrName,
						self.__uvPinArg))
			
			# connect the curve to the ribbon node if specified
			if pathToCurve.isValid():
				self.__dgModify.commandToExecute('connectAttr -f %s.worldSpace[0] %s.%s'%(
					pathToCurve.fullPathName(),
					self.__ribbonNodeFn.name(), AM_RibbonsNode.kInputCurveAttrName))
				# if in edit mode, assume that the user also wants to move the object to the curve's start position
				if self.__isEditUsed:
					curveFn.setObject(pathToCurve)
					curveFn.getPointAtParam(0.0, curveStartPoint)
					plug = self.__ribbonNodeFn.findPlug(AM_RibbonsNode.kOutputAttrName, True)
					iter = OM.MItDependencyGraph(plug, OM.MFn.kShape, OM.MItDependencyGraph.kDownstream)
					pathToNewObject = OM.MDagPath()
					while not iter.isDone():
						if not pathToNewObject.isValid(): # stop at the first one we find
							##OM.MFnDagNode(iter.currentItem()).getPath(pathToNewObject)
							OM.MDagPath.getAPathTo(iter.currentItem(), pathToNewObject)
						iter.next()
					##transformFn.setObject(pathToNewObject.transform())
					##transformFn.getPath(pathToNewObject)
					OM.MDagPath.getAPathTo(pathToNewObject.transform(), pathToNewObject)
					transformFn.setObject(pathToNewObject) # initialize using a dagpath so world-space can be used
					transformFn.setTranslation(OM.MVector(curveStartPoint), OM.MSpace.kWorld)
			
			# if in create mode, connect the ribbon node to the shape
			if not self.__isEditUsed:
				# connect the ribbon node to the shape node
				self.__dgModify.commandToExecute('connectAttr %s.%s %s.inMesh'%(
					self.__ribbonNodeFn.name(), AM_RibbonsNode.kOutputAttrName,
					shapeFn.name()))
		
		self.__dgModify.doIt()
		
		# if in create mode, handle group uv layout if needed
		if not self.__isEditUsed and self.__uvScaleGroupArg: # this will not trigger if the flag has not been set, nor if the flag is set to individual
			ribbonLengths = []
			divisionsInCurrentRibbonNode = 0
			for i in range(newRibbonNodes.length()):
				self.__ribbonNodeFn.setObject(newRibbonNodes[i])
				divisionsInCurrentRibbonNode = OM.MPlug(self.__ribbonNodeFn.findPlug(AM_RibbonsNode.kInputDivisionsAttrName, True)).asInt()
				ribbonLengths.append(divisionsInCurrentRibbonNode)
			longestRibbon = max(ribbonLengths)
			shortestRibbon = min(ribbonLengths)
			targetUVScale = 0.0
			for i in range(newRibbonNodes.length()):
				self.__ribbonNodeFn.setObject(newRibbonNodes[i])
				if self.__uvScaleGroupArg == 1: # normalize all new ribbons against the longest
					targetUVScale = float(ribbonLengths[i])/longestRibbon
				else: # normalize all new ribbons against the shortest
					targetUVScale = float(ribbonLengths[i])/shortestRibbon
				self.__dgModify.commandToExecute('setAttr %s.%s %f'%(
					self.__ribbonNodeFn.name(), AM_RibbonsNode.kInputUVScaleAttrName,
					targetUVScale))
		
		# otherwise set uv scale normally
		elif self.__uvScaleArg:
			for i in range(newObjects.length()):
				if not self.__isEditUsed:
					self.__ribbonNodeFn.setObject(newRibbonNodes[i])
				plug = self.__ribbonNodeFn.findPlug(AM_RibbonsNode.kInputUVScaleAttrName, True)
				if not plug.isConnected():
					self.__dgModify.commandToExecute('setAttr %s.%s %f'%(
						self.__ribbonNodeFn.name(), AM_RibbonsNode.kInputUVScaleAttrName, 
						self.__uvScaleArg))
					
		
		# select the new mesh transforms and output the new ribbon nodes
		if not self.__isEditUsed:
			newMeshListAsString = ''
			newSelectionListAsString = ''
			for i in range(newObjects.length()):
				transformFn.setObject(newObjects[i])
				self.__ribbonNodeFn.setObject(newRibbonNodes[i])
				newMeshListAsString += ' %s'%transformFn.fullPathName()
				#self.appendToResult(transformFn.partialPathName())
				newSelectionListAsString += ' %s'%self.__ribbonNodeFn.name()
				self.appendToResult(self.__ribbonNodeFn.name())
			self.__dgModify.commandToExecute('select%s'%newMeshListAsString)
			# assign the default material to the new objects
			self.__dgModify.commandToExecute('hyperShade -assign lambert1')
		
		self.__dgModify.doIt()
	
	def undoIt(self):
		self.__dgModify.undoIt()
		self.__dagModify.undoIt()
		
	def isUndoable(self):
		# the command should only be undoable if edit or create mode was used
		return not self.__isQueryUsed
	
	@classmethod
	def cmdCreator(cls):
		return OMMPx.asMPxPtr(cls())
	
	@classmethod
	def syntaxCreator(cls):
		syntax = OM.MSyntax()
		syntax.enableQuery() # BUG: including these modes has benefits, but it also breaks object parsing
		syntax.enableEdit()
		syntax.addFlag(cls.kNameFlag, cls.kNameFlagLong, OM.MSyntax.kString)
		syntax.addFlag(cls.kCurveFlag, cls.kCurveFlagLong, OM.MSyntax.kSelectionItem)
		syntax.addFlag(cls.kWidthFlag, cls.kWidthFlagLong, OM.MSyntax.kDouble)
		syntax.addFlag(cls.kDivisionsFlag, cls.kDivisionsFlagLong, OM.MSyntax.kLong)
		syntax.addFlag(cls.kDivisionsPerUnitFlag, cls.kDivisionsPerUnitFlagLong, OM.MSyntax.kDouble)
		syntax.addFlag(cls.kTaperFlag, cls.kTaperFlagLong, OM.MSyntax.kDouble)
		syntax.addFlag(cls.kTwistBaseFlag, cls.kTwistBaseFlagLong, OM.MSyntax.kDouble)
		syntax.addFlag(cls.kTwistLengthFlag, cls.kTwistLengthFlagLong, OM.MSyntax.kDouble)
		syntax.addFlag(cls.kUpVectorFlag, cls.kUpVectorFlagLong, OM.MSyntax.kDouble, OM.MSyntax.kDouble, OM.MSyntax.kDouble)
		syntax.addFlag(cls.kUVScaleFlag, cls.kUVScaleFlagLong, OM.MSyntax.kDouble)
		syntax.addFlag(cls.kUVScaleGroupFlag, cls.kUVScaleGroupFlagLong, OM.MSyntax.kString)
		syntax.addFlag(cls.kUVPinFlag, cls.kUVPinFlagLong, OM.MSyntax.kString)
		syntax.useSelectionAsDefault(True)
		syntax.setObjectType(OM.MSyntax.kSelectionList)
		return syntax

# -----------------------------------------------------------------------------
# Node Definition
# -----------------------------------------------------------------------------
class AM_RibbonsNode(OMMPx.MPxNode):
	"""
	A node for building ribbon meshes along NURBS curves using supplied
	parameters.
	\par Input Attributes:
		- \em inputCurve: The worldSpace attribute of a NURBS curve.
		- \em width: The width of the ribbon at its base.
		- \em divisions: The number of faces down the ribbon's length.
		- \em taper: The scale of the ribbon's end, linearly interpolated down
			the length.
		- \em twistBase: The twist rotation of the ribbon at the base.
		- \em twistLength: The twist rotation at the ribbon's end, linearly
			interpolated down the length.
		- \em upVector: The world space up-vector to determine the ribbon's
			orientation at the base.
		- \em uvScale: The homogenized length of the ribbon in uv space.
		- \em uvPin: Specifies whether the uvs should be pinned at the bottom
			at v=0 or at the top at v=1.
	\par Output Attributes:
		- \em output: Mesh data to pipe into the inMesh attribute of a shape
			node.
	"""
	## the name of the nodeType
	kPluginNodeTypeName = 'am_ribbon'
	## the unique MTypeId for the node
	kPluginNodeId = OM.MTypeId(0x001138C3)

	# input attributes
	## nurbs curve to define the flow of the ribbon
	inputCurve = OM.MObject()
	kInputCurveAttrName = 'in'
	kInputCurveAttrLongName = 'input'
	## width of the ribbon in centimeters
	inputWidth = OM.MObject()
	kInputWidthAttrName = 'w'
	kInputWidthAttrLongName = 'width'
	## number of divisions along the ribbon
	inputDivisions = OM.MObject()
	kInputDivisionsAttrName = 'd'
	kInputDivisionsAttrLongName = 'divisions'
	## amount of taper at the far end of the ribbon
	inputTaper = OM.MObject()
	kInputTaperAttrName = 't'
	kInputTaperAttrLongName = 'taper'
	## amount of twisting of the ribbon at its base
	inputTwistBase = OM.MObject()
	kInputTwistBaseAttrName = 'tb'
	kInputTwistBaseAttrLongName = 'twistBase'
	## amount of twisting of the ribbon at its far end
	inputTwistLength = OM.MObject()
	kInputTwistLengthAttrName = 'tl'
	kInputTwistLengthAttrLongName = 'twistLength'
	## up-vector for the ribbon at its base
	inputUpVector = OM.MObject()
	kInputUpVectorAttrName = 'up'
	kInputUpVectorAttrLongName = 'upVector'
	## scale factor applied to the default uv layout
	inputUVScale = OM.MObject()
	kInputUVScaleAttrName = 'uv'
	kInputUVScaleAttrLongName = 'uvScale'
	## pin location for the default uv layout
	inputUVPin = OM.MObject()
	kInputUVPinAttrName = 'uvp'
	kInputUVPinAttrLongName = 'uvPin'
	
	# output attributes
	## the output mesh
	output = OM.MObject()
	kOutputAttrName = 'out'
	kOutputAttrLongName = 'output'
	
	def __init__(self):
		OMMPx.MPxNode.__init__(self)
	
	def compute(self, plug, dataBlock):
		"""Use a NURBS curve and other input parameters to generate mesh data to be piped into a shape node."""
		if (plug == AM_RibbonsNode.output):
			# get the incoming data
			# the input nurbs curve
			dataHandle = OM.MDataHandle(dataBlock.inputValue(AM_RibbonsNode.inputCurve))
			curve = OM.MObject(dataHandle.asNurbsCurve())
			# early out if there is no curve data
			if curve.isNull(): return OM.kUnknownParameter
			# width of the ribbon in centimeters
			dataHandle = OM.MDataHandle(dataBlock.inputValue(AM_RibbonsNode.inputWidth))
			width = dataHandle.asDouble()
			# number of divisions along the ribbon
			dataHandle = OM.MDataHandle(dataBlock.inputValue(AM_RibbonsNode.inputDivisions))
			divisions = dataHandle.asInt()
			# the ribbon must have at least one division
			if divisions < 1:
				divisions = 1
				dataHandle.setInt(1)
				dataHandle.setClean()
			# amount of taper at the far end of the ribbon
			dataHandle = OM.MDataHandle(dataBlock.inputValue(AM_RibbonsNode.inputTaper))
			taper = dataHandle.asDouble()
			# amount of twisting of the ribbon at its base
			dataHandle = OM.MDataHandle(dataBlock.inputValue(AM_RibbonsNode.inputTwistBase))
			twistBase = dataHandle.asDouble()
			# amount of twisting of the ribbon at its far end
			dataHandle = OM.MDataHandle(dataBlock.inputValue(AM_RibbonsNode.inputTwistLength))
			twistLength = dataHandle.asDouble()
			# up-vector for the ribbon at its base
			dataHandle = OM.MDataHandle(dataBlock.inputValue(AM_RibbonsNode.inputUpVector))
			upVector = OM.MVector(dataHandle.asVector())
			upVector.normalize()
			if upVector.length() == 0: upVector = OM.MVector(0.0,1.0,0.0)
			# scale factor applied to the default uv layout
			dataHandle = OM.MDataHandle(dataBlock.inputValue(AM_RibbonsNode.inputUVScale))
			uvScale = dataHandle.asDouble()
			# pin location for the default uv layout
			dataHandle = OM.MDataHandle(dataBlock.inputValue(AM_RibbonsNode.inputUVPin))
			uvPin = dataHandle.asShort()
			
			# create data for the output mesh
			dataCreator = OM.MFnMeshData()
			outputData = dataCreator.create()
			numVertices = 2 + divisions * 2
			numPolygons = divisions
			newMeshVertices = OM.MPointArray()
			newMeshPolyCount = OM.MIntArray()
			newMeshPolyConnects = OM.MIntArray()
			newMeshUVCounts = OM.MIntArray()
			newMeshUVIDs = OM.MIntArray()
			meshFn = OM.MFnMesh()
			
			# find the points and tangents at each division along the curve
			pointsOnCurve = OM.MPointArray()
			tangentsOnCurve = OM.MVectorArray()
			curveFn = OM.MFnNurbsCurve(curve)
			maxParam = curveFn.findParamFromLength(curveFn.length())
			paramStep = maxParam / divisions
			startPoint = OM.MPoint()
			currentPoint = OM.MPoint()
			curveFn.getPointAtParam(0.0, startPoint)
			for i in range(divisions+1):
				curveFn.getPointAtParam(i*paramStep, currentPoint)
				pointsOnCurve.append(OM.MPoint(currentPoint-startPoint))
				tangentsOnCurve.append(curveFn.tangent(i*paramStep).normal())
			
			# determine the amount of twisting to apply at the base and per division
			twistBaseRotation = OM.MQuaternion(math.radians(twistBase), tangentsOnCurve[0])
			twistStepAngle = math.radians(twistLength/divisions)
			# if the first tangent is roughly the same as the up-vector, then simply override the up-vector to be the z-axis
			upVector = upVector.rotateBy(twistBaseRotation)
			if upVector * tangentsOnCurve[0] > 0.999999999999999:
				upVector = OM.MVector(0.0, 0.0, 1.0)
			# orthonormalize the up-vector and first tangent
			rightVector = OM.MVector(upVector ^ tangentsOnCurve[0]).normal()
			upVector = tangentsOnCurve[0] ^ rightVector
			
			# create the points along the curve
			for i in range(pointsOnCurve.length()):
				if i is not 0:
					upVector = upVector.rotateBy(OM.MQuaternion(tangentsOnCurve[i-1], tangentsOnCurve[i]))
					upVector = upVector.rotateBy(OM.MQuaternion(twistStepAngle, tangentsOnCurve[i]))
					newMeshPolyCount.append(4)
					newMeshUVCounts.append(4)
				rightVector = upVector ^ tangentsOnCurve[i]
				newMeshVertices.append(OM.MPoint(pointsOnCurve[i] + rightVector * 0.5 * width * (1.0 + (taper-1.0)/pointsOnCurve.length() * (i+1))))
				newMeshVertices.append(OM.MPoint(pointsOnCurve[i] + rightVector * -0.5 * width * (1.0 + (taper-1.0)/pointsOnCurve.length() * (i+1))))
			
			# connect the points in the new mesh and assign uv values to the faces
			for i in range(newMeshPolyCount.length()):
				newMeshPolyConnects.append(i*2+0)
				newMeshPolyConnects.append(i*2+1)
				newMeshPolyConnects.append(i*2+3)
				newMeshPolyConnects.append(i*2+2)
				newMeshUVIDs.append(i*2+0)
				newMeshUVIDs.append(i*2+1)
				newMeshUVIDs.append(i*2+3)
				newMeshUVIDs.append(i*2+2)
			
			# establish other parameters for the new mesh data
			numVertices = newMeshVertices.length()
			numPolygons = divisions
			
			# create the new mesh from all of the data
			mesh = meshFn.create(numVertices, numPolygons, newMeshVertices, newMeshPolyCount, newMeshPolyConnects, outputData)
			
			# set and assign uv values
			for i in range(pointsOnCurve.length()):
				meshFn.setUV(i*2+0, 1.0, 1.0-uvScale*(float(i)/(pointsOnCurve.length()-1))-uvPin*(1.0-uvScale))
				meshFn.setUV(i*2+1, 0.0, 1.0-uvScale*(float(i)/(pointsOnCurve.length()-1))-uvPin*(1.0-uvScale))
			meshFn.assignUVs(newMeshUVCounts, newMeshUVIDs)
			
			# set the outgoing plug
			outputHandle = dataBlock.outputValue(AM_RibbonsNode.output)
			outputHandle.setMObject(outputData)
			dataBlock.setClean(plug)
			
		else:
			return OM.kUnknownParameter
	
	@classmethod
	def nodeCreator(cls):
		return OMMPx.asMPxPtr(cls())
	
	@classmethod
	def nodeInitializer(cls):
		# input attributes
		# nurbs curve to define the flow of the ribbon
		typedAttr = OM.MFnTypedAttribute()
		cls.inputCurve = typedAttr.create(AM_RibbonsNode.kInputCurveAttrLongName, AM_RibbonsNode.kInputCurveAttrName, OM.MFnNurbsCurveData.kNurbsCurve)
		# width of the ribbon in centimeters
		numAttr = OM.MFnNumericAttribute()
		cls.inputWidth = numAttr.create(AM_RibbonsNode.kInputWidthAttrLongName, AM_RibbonsNode.kInputWidthAttrName, OM.MFnNumericData.kDouble, 3.0)
		numAttr.setWritable(True)
		numAttr.setStorable(True)
		numAttr.setReadable(True)
		numAttr.setKeyable(True)
		# number of divisions along the ribbon
		cls.inputDivisions = numAttr.create(AM_RibbonsNode.kInputDivisionsAttrLongName, AM_RibbonsNode.kInputDivisionsAttrName, OM.MFnNumericData.kInt, 10)
		numAttr.setWritable(True)
		numAttr.setStorable(True)
		numAttr.setReadable(True)
		numAttr.setKeyable(True)
		# amount of taper at the far end of the ribbon
		cls.inputTaper = numAttr.create(AM_RibbonsNode.kInputTaperAttrLongName, AM_RibbonsNode.kInputTaperAttrName, OM.MFnNumericData.kDouble, 1.0)
		numAttr.setWritable(True)
		numAttr.setStorable(True)
		numAttr.setReadable(True)
		numAttr.setKeyable(True)
		# amount of twisting of the ribbon at its base
		cls.inputTwistBase = numAttr.create(AM_RibbonsNode.kInputTwistBaseAttrLongName, AM_RibbonsNode.kInputTwistBaseAttrName, OM.MFnNumericData.kDouble, 0.0)
		numAttr.setWritable(True)
		numAttr.setStorable(True)
		numAttr.setReadable(True)
		numAttr.setKeyable(True)
		# amount of twisting of the ribbon at its far end
		cls.inputTwistLength = numAttr.create(AM_RibbonsNode.kInputTwistLengthAttrLongName, AM_RibbonsNode.kInputTwistLengthAttrName, OM.MFnNumericData.kDouble, 0.0)
		numAttr.setWritable(True)
		numAttr.setStorable(True)
		numAttr.setReadable(True)
		numAttr.setKeyable(True)
		# up-vector for the ribbon at its base
		cls.inputUpVector = numAttr.create(AM_RibbonsNode.kInputUpVectorAttrLongName, AM_RibbonsNode.kInputUpVectorAttrName, OM.MFnNumericData.k3Double, 0.0)
		numAttr.setWritable(True)
		numAttr.setStorable(True)
		numAttr.setReadable(True)
		numAttr.setKeyable(False)
		# scale factor applied to the default uv layout
		cls.inputUVScale = numAttr.create(AM_RibbonsNode.kInputUVScaleAttrLongName, AM_RibbonsNode.kInputUVScaleAttrName, OM.MFnNumericData.kDouble, 1.0)
		numAttr.setWritable(True)
		numAttr.setStorable(True)
		numAttr.setReadable(True)
		numAttr.setKeyable(True)
		# pin location for the default uv layout
		eAttr = OM.MFnEnumAttribute()
		cls.inputUVPin = eAttr.create(AM_RibbonsNode.kInputUVPinAttrLongName, AM_RibbonsNode.kInputUVPinAttrName, 0)
		eAttr.addField('Top', 0)
		eAttr.addField('Bottom', 1)
		eAttr.setWritable(True)
		eAttr.setStorable(True)
		eAttr.setReadable(True)
		eAttr.setKeyable(True)
		
		# output attributes
		# the output mesh
		cls.output = typedAttr.create(AM_RibbonsNode.kOutputAttrLongName, AM_RibbonsNode.kOutputAttrName, OM.MFnData.kMesh)
		typedAttr.setWritable(False)
		typedAttr.setStorable(True) # TODO: ??
		typedAttr.setReadable(True)
		
		# add the attributes
		cls.addAttribute(cls.inputCurve)
		cls.addAttribute(cls.inputWidth)
		cls.addAttribute(cls.inputDivisions)
		cls.addAttribute(cls.inputTaper)
		cls.addAttribute(cls.inputTwistBase)
		cls.addAttribute(cls.inputTwistLength)
		cls.addAttribute(cls.inputUpVector)
		cls.addAttribute(cls.inputUVScale)
		cls.addAttribute(cls.inputUVPin)
		cls.addAttribute(cls.output)
		
		# establish effects on output
		cls.attributeAffects(cls.inputCurve, cls.output)
		cls.attributeAffects(cls.inputWidth, cls.output)
		cls.attributeAffects(cls.inputDivisions, cls.output)
		cls.attributeAffects(cls.inputTaper, cls.output)
		cls.attributeAffects(cls.inputTwistBase, cls.output)
		cls.attributeAffects(cls.inputTwistLength, cls.output)
		cls.attributeAffects(cls.inputUpVector, cls.output)
		cls.attributeAffects(cls.inputUVScale, cls.output)
		cls.attributeAffects(cls.inputUVPin, cls.output)

# -----------------------------------------------------------------------------
# Initialize
# -----------------------------------------------------------------------------
def initializePlugin(mobject):
	plugin = OMMPx.MFnPlugin(mobject, 'Adam Mechtley', kVersionNumber, 'Any')
	# dependency node
	try:
		plugin.registerNode(AM_RibbonsNode.kPluginNodeTypeName, AM_RibbonsNode.kPluginNodeId, AM_RibbonsNode.nodeCreator, AM_RibbonsNode.nodeInitializer)
	except:
		sys.stderr.write('Failed to register node: %s\n'%AM_RibbonsNode.kPluginNodeTypeName)
		raise
	# command
	try:
		plugin.registerCommand(AM_RibbonsCmd.kPluginCmdName, AM_RibbonsCmd.cmdCreator, AM_RibbonsCmd.syntaxCreator)
	except:
		sys.stderr.write('Failed to register command: %s\n'%AM_RibbonsCmd.kPluginCmdName)
		raise

# -----------------------------------------------------------------------------
# Uninitialize
# -----------------------------------------------------------------------------
def uninitializePlugin(mobject):
	plugin = OMMPx.MFnPlugin(mobject)
	# dependency node
	try:
		plugin.deregisterNode(AM_RibbonsNode.kPluginNodeId)
	except:
		sys.stderr.write('Failed to unregister node: %s\n'%AM_RibbonsNode.kPluginNodeTypeName)
		raise
	# command
	try:
		plugin.deregisterCommand(AM_RibbonsCmd.kPluginCmdName)		
	except:
		sys.stderr.write('Failed to unregister command: %s\n'%AM_RibbonsCmd.kPluginCmdName)
		raise