"""
Add custom attributes to objects to describe various different types of
constraints. These user properties are stored in a way that they are to be
parsed by Unity's AssetPostprocessor in order to transport a rig into Unity for
evaluation at run-time.

\b Requirements: Unity Pro with ImportMayaRigs.cs editor script and all its
dependencies.

\par Supported constraint types:
	- aimConstraint
	- orientConstraint
	- pointConstraint

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

\namespace amTools.unity.rigs.constraints
"""

import re
import maya.cmds as cmds
import maya.mel as mel
import amTools.utilities.unity as util
reload(util)

def exportConstraints():
	"""Add user properties for all supported node types."""
	doConstraints('aimConstraint')
	doConstraints('orientConstraint')
	doConstraints('pointConstraint')

def doConstraints(constraintType):
	"""Adds user properties to objects controlled by constraints."""
	# determine the outgoing plug name and attribute lists based on the constraint type
	outPlug = ''
	attributeList = []
	if (constraintType == 'aimConstraint'):
		outPlug = 'constraintRotate'
		attributeList = ['offset', 'aimVector', 'upVector', 'worldUpVector', 'worldUpMatrix', 'worldUpType']
	elif (constraintType == 'orientConstraint'):
		outPlug = 'constraintRotate'
		attributeList = ['offset', 'interpType']
	elif (constraintType == 'pointConstraint'):
		outPlug = 'constraintTranslate'
		attributeList = ['offset', 'constraintOffsetPolarity']
	
	# set up each constraint
	constraints = cmds.ls(type=constraintType)
	for constraint in constraints:
		# first resolve naming conflicts in case any exist
		constraint = cmds.rename(constraint, constraint)
		# NOTE: Unity implementation does not allow per-child-plug behavior, so just check first child plug
		constrainedObjects = cmds.listConnections('%s.%sX'%(constraint, outPlug), source=False)
		if not constrainedObjects: continue
		for obj in constrainedObjects:
			if constraintType == 'pointConstraint': util.addAttributeValues(obj, constraint, attributeList)
			else: util.addAttributeValues(obj, constraint, attributeList, eulerAttributes=['offset'])
			util.addAttributeValues(obj, constraint, mel.eval('%s -q -wal %s'%(constraintType, constraint)))
			try:
				targets = ['target[%s].targetParentMatrix'%re.search('\d+$', t).group(0) for t in mel.eval('%s -q -wal %s'%(constraintType, constraint))]
				util.addAttributeValues(obj, constraint, targets)
			except: pass