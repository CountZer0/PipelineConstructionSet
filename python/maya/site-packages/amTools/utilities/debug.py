"""
Utility functions for debugging.

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

\namespace amTools.utilities.debug
"""

import math
import maya.mel as mel
import maya.cmds as cmds
import maya.OpenMaya as OM

## the name of a global boolean for MEL to designate whether or not API Debug Mode is enabled
kGlobalAPIDebug = "$gAMToolsAPIDebugMode"
mel.eval('%s = false' % kGlobalAPIDebug)

def menuItem(*args):
	"""A function to call debugAll() from a menu item."""
	debugAll(not mel.eval('%s = %s' % (kGlobalAPIDebug, kGlobalAPIDebug)))

def debugAll(isEnabled):
	"""Toggle all API debugging, which overrides the str() functionality of
	various API classes to print more useful information."""
	if isEnabled:
		for apiClass in overrideFunctions:
			apiClass.__str__ = overrideFunctions[apiClass]
	else:
		for apiClass in apiFunctions:
			apiClass.__str__ = apiFunctions[apiClass]
	mel.eval('%s = !%s' % (kGlobalAPIDebug, kGlobalAPIDebug))

def printAPIType(self):
	"""Print the apiType of an MObject"""
	return self.apiTypeStr()

def printDagPath(self):
	"""Print fullPathName()"""
	if self.isValid():
		return self.partialPathName()
	else:
		return None.__str__()

def printMatrix(self):
	"""Print matrix elements in a 4x4 grid."""
	return ("[%f,%f,%f,%f]\n[%f,%f,%f,%f]\n[%f,%f,%f,%f]\n[%f,%f,%f,%f]" % 
		(self(0,0), self(0,1), self(0,2), self(0,3), 
		self(1,0), self(1,1), self(1,2), self(1,3), 
		self(2,0), self(2,1), self(2,2), self(2,3), 
		self(3,0), self(3,1), self(3,2), self(3,3)))

def printTransformMatrix(self):
	"""Print transform matrix elements in a 4x4 grid."""
	return ("[%f,%f,%f,%f]\n[%f,%f,%f,%f]\n[%f,%f,%f,%f]\n[%f,%f,%f,%f]" % 
	        (self.asMatrix()(0,0), self.asMatrix()(0,1), self.asMatrix()(0,2), self.asMatrix()(0,3), 
	        self.asMatrix()(1,0), self.asMatrix()(1,1), self.asMatrix()(1,2), self.asMatrix()(1,3), 
	        self.asMatrix()(2,0), self.asMatrix()(2,1), self.asMatrix()(2,2), self.asMatrix()(2,3), 
	        self.asMatrix()(3,0), self.asMatrix()(3,1), self.asMatrix()(3,2), self.asMatrix()(3,3)))

def printXYZ(self):
	"""Print X, Y, and Z components."""
	return ("[%f, %f, %f]" % (self.x, self.y, self.z))

def printXYZDegrees(self):
	"""Print X, Y, and Z components in degrees."""
	return ("[%f, %f, %f]" % (math.degrees(self.x), math.degrees(self.y), math.degrees(self.z)))

def printXYZW(self):
	"""Print X, Y, Z, and W components."""
	return ("[%f, %f, %f, %f]" % (self.x, self.y, self.z, self.w))

## dictionary to store all of the original str() functions of overridden API classes
apiFunctions = {
	OM.MDagPath:OM.MDagPath.__str__,
	OM.MEulerRotation:OM.MEulerRotation.__str__,
	OM.MFloatMatrix:OM.MFloatMatrix.__str__,
	OM.MFloatPoint:OM.MFloatPoint.__str__,
	OM.MFloatVector:OM.MFloatVector.__str__,
	OM.MMatrix:OM.MMatrix.__str__,
	OM.MObject:OM.MObject.__str__,
	OM.MPoint:OM.MPoint.__str__,
	OM.MQuaternion:OM.MQuaternion.__str__,
	OM.MTransformationMatrix:OM.MTransformationMatrix.__str__,
	OM.MVector:OM.MVector.__str__
}

## dictionary to map all of the overriden API classes to their debug str() functions
overrideFunctions = {
	OM.MDagPath:printDagPath,
	OM.MEulerRotation:printXYZDegrees,
	OM.MFloatMatrix:printMatrix,
	OM.MFloatPoint:printXYZW,
	OM.MFloatVector:printXYZ,
	OM.MMatrix:printMatrix,
	OM.MObject:printAPIType,
	OM.MPoint:printXYZW,
	OM.MQuaternion:printXYZW,
	OM.MTransformationMatrix:printTransformMatrix,
	OM.MVector:printXYZ
}

def reloadPlugin(pluginName, **keywords):
	"""
	Quickly reload a plug-in during testing
	@param reload Specifies whether or not to close and reopen the current file
	"""
	file = cmds.file(q=True, sn=True)
	if keywords.setdefault('reload') == True: cmds.file(f=True, new=True)
	cmds.flushUndo()
	cmds.unloadPlugin(pluginName)
	cmds.loadPlugin(pluginName)
	if keywords.setdefault('reload') == True: cmds.file(file, o=True)