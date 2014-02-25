"""
A command that automatically creates an intermediate locator parent for each
transform node in the selection at that node's location, allowing the quick
creation of 'zero' transforms.

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

\namespace AM_InsertParentsCmd
"""

import sys, re
import maya.OpenMaya as OM
import maya.OpenMayaMPx as OMMPx

## current version of the plug-in
kVersionNumber = '1.03'

# -----------------------------------------------------------------------------
# Command Definition
# -----------------------------------------------------------------------------
class AM_InsertParentsCmd(OMMPx.MPxCommand):
	"""
	A command that automatically creates an intermediate locator parent for
	each transform node in the selection at that node's location, allowing the
	quick creation of 'zero' transforms.
	"""
	
	## the name of the command
	kPluginCmdName = 'am_insertParents'
	
	## specifies a prefix for all new locators
	kPrefixFlag = '-pre'
	kPrefixFlagLong = '-prefix'
	## specifies a suffix for all new locators
	kSuffixFlag = '-suf'
	kSuffixFlagLong = '-suffix'
	## specifies the local scale value for the new locator shape node
	kScaleFlag = '-s'
	kScaleFlagLong = '-scale'
	
	def __init__(self):
		OMMPx.MPxCommand.__init__(self)
		self.__selection = OM.MSelectionList()
		self.__prefix = ''
		self.__suffix = '_xForm'
		self.__scale = OM.MVector(1.0, 1.0, 1.0)
		self.__pickedObjects = OM.MDagPathArray() # all valid transform nodes in the selection
		self.__newLocators = OM.MDagPathArray() # any new locators created by the command
		self.__dagModify = OM.MDagModifier() # modifier to create and modify the new nodes
	
	def validateAffix(self, affix):
		"""Verify if a given affix is valid."""
		if len(re.split('\W+', affix)) > 1:
			raise Exception('%s is not a valid affix. Did you type it correctly?\n'%affix)
	
	def doIt(self, args):
		# parse the arguments
		try: argData = OM.MArgDatabase(self.syntax(), args) # if this fails, it will raise its own exception...
		except: pass # ...so we can just pass here
		else:
			# read all of the arguments and store them to the appropriate data attributes
			# build a new selection list from the provided one to make sure there are no duplicated DAG paths
			argData.getObjects(self.__selection)
			# containers for use inside the iterator
			newSelectionList = OM.MSelectionList()
			selectedObject = OM.MObject()
			selectedObjectFn = OM.MFnDagNode()
			selectedObjectPath = OM.MDagPath()
			iter = OM.MItSelectionList(self.__selection, OM.MFn.kTransform) # use kTransform instead of kDagNode in order to exclude shapes
			while not iter.isDone():
				iter.getDependNode(selectedObject)
				selectedObjectFn.setObject(selectedObject)
				selectedObjectFn.getPath(selectedObjectPath) # if the selected object is a plug, this is the path to the transform
				newSelectionList.add(selectedObjectPath.fullPathName()) # this version of the method automatically ensures no duplicates
				iter.next()
			self.__selection = newSelectionList # at this point, the selection list consists of only DAG nodes
			if argData.isFlagSet(AM_InsertParentsCmd.kPrefixFlag):
				self.__suffix = ''
				self.__prefix = argData.flagArgumentString(AM_InsertParentsCmd.kPrefixFlag, 0)
				self.validateAffix(self.__prefix)
			if argData.isFlagSet(AM_InsertParentsCmd.kSuffixFlag):
				self.__suffix = argData.flagArgumentString(AM_InsertParentsCmd.kSuffixFlag, 0)
				self.validateAffix(self.__suffix)
			if argData.isFlagSet(AM_InsertParentsCmd.kScaleFlag):
				self.__scale.x = argData.flagArgumentDouble(AM_InsertParentsCmd.kScaleFlag, 0)
				self.__scale.y = argData.flagArgumentDouble(AM_InsertParentsCmd.kScaleFlag, 1)
				self.__scale.z = argData.flagArgumentDouble(AM_InsertParentsCmd.kScaleFlag, 2)
			self.redoIt()

	def redoIt(self):
		# clear out the modifier and arrays so they don't store old object names
		self.__oldTransformationMatrices = []
		self.__newLocators = OM.MDagPathArray()
		self.__pickedObjects = OM.MDagPathArray()
		self.__dagModify = OM.MDagModifier()
		
		# iterate through the list of selected transform nodes and create a locator for each one
		iter = OM.MItSelectionList(self.__selection, OM.MFn.kTransform)
		# containers for use inside the iterator
		currentObject = OM.MObject()
		currentObjectFn = OM.MFnDagNode()
		currentDagPath = OM.MDagPath()
		currentPlug = OM.MPlug()
		currentParent = OM.MObject()
		currentObjectFn = OM.MFnTransform()
		newLocator = OM.MObject()
		newLocFn = OM.MFnTransform()
		newLocatorPath = OM.MDagPath()
		while not iter.isDone():
			# append the current object to the array of picked objects
			iter.getDagPath(currentDagPath)
			self.__pickedObjects.append(currentDagPath)
			# create the new locator
			newLocator = self.__dagModify.createNode('locator')
			# insert the locator sibling to the object
			currentObjectFn.setObject(currentDagPath)
			currentParent = currentObjectFn.parent(0)
			self.__dagModify.reparentNode(newLocator, currentParent)
			# move the new locator to the same location as its corresponding object, parent, and name appropriately
			newLocFn.setObject(newLocator)
			newLocFn.set(currentObjectFn.transformation()) # align the new locator to the object
			self.__dagModify.reparentNode(currentDagPath.node(), newLocator) # the object is now a child of the new locator
			currentObjectFn.set(OM.MTransformationMatrix()) # set the object's local matrix to identity
			self.__dagModify.renameNode(newLocator, self.__prefix + currentObjectFn.partialPathName() + self.__suffix)
			# append the new locator to the array
			newLocFn.getPath(newLocatorPath)
			self.__newLocators.append(newLocatorPath)
			iter.next()
		# WARNING: must tell the MDagModifier to doIt() now in order to let Maya's auto-rename kick in and ensure the names are unique
		# otherwise attempts to use setAttr below may end up using some other object
		self.__dagModify.doIt()
		
		# now set the attributes and reparent the selected objects
		selectionString = '' # the selection list needs to be formatted for MEL
		for i in range (0, self.__newLocators.length()):
			newLocFn.setObject(self.__newLocators[i])
			selectionString += ' %s'%newLocFn.fullPathName()
			# resize the new locator
			self.__dagModify.commandToExecute('setAttr %s.localScaleX %f'%(newLocFn.fullPathName(), self.__scale.x))
			self.__dagModify.commandToExecute('setAttr %s.localScaleY %f'%(newLocFn.fullPathName(), self.__scale.y))
			self.__dagModify.commandToExecute('setAttr %s.localScaleZ %f'%(newLocFn.fullPathName(), self.__scale.z))
		
		# select the new locators
		self.__dagModify.commandToExecute('select%s'%selectionString)
		self.__dagModify.doIt()

	def undoIt(self):
		# store the locators' transform matrices
		objectMatrices = []
		locFn = OM.MFnTransform()
		for i in range (0, self.__newLocators.length()):
			locFn.setObject(self.__newLocators[i])
			objectMatrices.append(locFn.transformation())
		# undo the modifier
		self.__dagModify.undoIt()
		# reset the objects' transform matrices
		objectFn = OM.MFnTransform()
		for i in range (0, self.__pickedObjects.length()):
			objectFn.setObject(self.__pickedObjects[i])
			objectFn.set(objectMatrices[i])

	def isUndoable(self):
		return True
	
	@classmethod
	def cmdCreator(cls):
		return OMMPx.asMPxPtr(cls())
	
	@classmethod
	def syntaxCreator(cls):
		syntax = OM.MSyntax()
		syntax.addFlag(cls.kPrefixFlag, cls.kPrefixFlagLong, OM.MSyntax.kString)
		syntax.addFlag(cls.kSuffixFlag, cls.kSuffixFlagLong, OM.MSyntax.kString)
		syntax.addFlag(cls.kScaleFlag, cls.kScaleFlagLong, OM.MSyntax.kDouble, OM.MSyntax.kDouble, OM.MSyntax.kDouble)
		syntax.useSelectionAsDefault(True)
		syntax.setObjectType(OM.MSyntax.kSelectionList, 1)
		return syntax

# -----------------------------------------------------------------------------
# Initialize the scripted plug-in
# -----------------------------------------------------------------------------
def initializePlugin(mobject):
	plugin = OMMPx.MFnPlugin(mobject, 'Adam Mechtley', kVersionNumber, 'Any')
	try:
		plugin.registerCommand(AM_InsertParentsCmd.kPluginCmdName, AM_InsertParentsCmd.cmdCreator, AM_InsertParentsCmd.syntaxCreator)
	except:
		sys.stderr.write('Failed to register command: %s\n'%AM_InsertParentsCmd.kPluginCmdName)

# -----------------------------------------------------------------------------
# Uninitialize the scripted plug-in
# -----------------------------------------------------------------------------
def uninitializePlugin(mobject):
	plugin = OMMPx.MFnPlugin(mobject)
	try:
		plugin.deregisterCommand(AM_InsertParentsCmd.kPluginCmdName)		
	except:
		sys.stderr.write('Failed to unregister command: %s\n'%AM_InsertParentsCmd.kPluginCmdName)