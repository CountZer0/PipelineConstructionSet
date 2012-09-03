"""
Utility functions for working with the Maya dependency graph (DG).

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

\namespace amTools.utilities.dg
"""

import inspect, re, sys
import maya.cmds as cmds
import maya.OpenMaya as OM
import amTools.python as ampy

def raiseExceptionWithMessage(msg, i):
	"""
	Raise an exception with a custom message and information about where the call originated.
	@param msg Custom exception message to display
	@param i The index of the caller in the inspect stack
	"""
	raise Exception('%s \n(called from %s() in file %s line %s)'%(msg, inspect.stack()[i+1][3], inspect.stack()[i+1][1], inspect.stack()[i+1][2]))

def getFilteredRelatives(sel, objectType, asType=True):
	"""Return a new selection list containing only specific types of relatives or objects containing specific types of relatives."""
	newList = []
	for obj in sel:
		relatives = cmds.listRelatives(obj)
		for relative in relatives:
			if cmds.objectType(relative, isType=objectType):
				if asType:
					newList.append(relative)
				else:
					newList.append(obj)
					break
	return newList
	
def getShapesFromTransforms(sel):
	"""Return a new selection list that contains the shapes for the selected objects."""
	newList = []
	for obj in sel:
		shapes = cmds.listRelatives(obj, shapes=True)
		if not shapes:
			continue
		for shape in shapes:
			newList.append(shape)
	return newList

def validateAffix(affix, min=0):
	"""Verify if a given affix is valid."""
	if len(affix) < min or len(re.split('\W+', affix)) > 1:
		msg = '%s is not a valid affix. Did you type it correctly?'%affix
		raiseExceptionWithMessage(msg, 1)

def validateNodeName(nodeName):
	"""Verify if a given node name is valid."""
	if (len(nodeName) < 1) or (not nodeName[0].isalpha()) or (len(re.split('\W+', nodeName)) > 1):
		msg = '%s is not a valid node name. Did you type it correctly?'%nodeName
		raiseExceptionWithMessage(msg, 1)

def validateSelection(**keywords):
	"""
	Verify that the current selection is valid and return it.
	@param type String corresponding to the object type the selection should filter.
	@param msg A custom error message to override in all cases.
	@param name A custom object name for default error messages.
	@param exact Specifies that an exact number of objects must be selected.
	@param min The minimum number of objects that must be selected.
	@param max tThe maximum number of objects that may be selected.
	"""
	selection = ''
	msg = keywords.setdefault('msg')
	name = keywords.setdefault('name', 'object(s)')
	try: selection = cmds.ls(sl=True, l=True, type=keywords['type'])
	except: selection = cmds.ls(sl=True, l=True)

	# if the exact key is provided, then it takes precedence
	isException = False
	if 'exact' in keywords and len(selection) is not keywords['exact']:
		if not msg: msg = 'Please select exactly %s %s'%(keywords['exact'], name)		
		isException = True
	else:
		if 'min' in keywords and len(selection) < keywords['min']:
			if not msg: msg = 'Error: You must select at least %s %s'%(keywords['min'], name)
			isException = True
		if 'max' in keywords and len(selection) > keywords['max']:
			if not msg: msg = 'Error: You may select no more than %s %s'%(keywords['max'], name)
			isException = True
	
	# raise an exception or return the selection list
	if isException: raiseExceptionWithMessage(msg, 1)
	else: return selection

def verifyNode(nodeName):
	"""Verify the existence of a DG node, primarily for validating user input."""
	allObjects = cmds.ls()
	if ampy.indexOf(nodeName, allObjects) == None:
		# if nodeName is a DAG node then we need to test further possibilities
		# if nodeName exists but is not unique, then a full path must be provided
		msg = None
		for node in allObjects:
			if node.find('|%s'%nodeName) > -1:
				raiseExceptionWithMessage('%s is not a unique object name. Please specify the complete DAG path.'%nodeName, 1)
		# see if nodeName is a full path for a unique object, in which case it won't look the same as that returned by cmds.ls
		for node in allObjects:
			if nodeName[nodeName.rfind(node):nodeName.rfind(node)+len(node)] == node: return True
		raiseExceptionWithMessage('%s is not a valid object name. Please ensure that you have entered it correctly.'%nodeName, 1)

def verifyPlug(plugName):
	"""Verify the existence of a plug, primarily for validating user input."""
	# TODO: Add functionality
	pass