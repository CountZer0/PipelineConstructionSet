"""
Utility functions requires by the amTools.unity package.

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

\namespace amTools.utilities.unity
"""

import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMaya as OM
import math, re

## a delimeter to use in user property names
kUserPropertyDelimeter = "__"

def generateUserPropertyName(nodeName, attributeName):
	"""Generate a user property name"""
	return '%s%s%s%s%s'%(cmds.nodeType(nodeName), kUserPropertyDelimeter, nodeName, kUserPropertyDelimeter, re.sub('\[', '', re.sub('\]', '', re.sub('\.', '', attributeName))))

def addAttributeValues(targetObject, sourceNode, attributeList, **keywords):
	"""
	Copies the values of attributes on targetObject specified in attributeList
	to user properties on targetObject
	@param targetObject The object to which the user property will be added
	@param sourceNode The object whose attributes are to be read
	@param attributeList A list of all attributes on sourceNode to store
	@param eulerAttributes An optional list of any Euler angle attributes to convert to left-handed
	"""
	# store all of the extant attributes on the targetObject
	existingAttributes = cmds.listAttr(targetObject)
	for attribute in attributeList:
		# determine the type for the attribute on the source node
		attrType = cmds.getAttr('%s.%s'%(sourceNode, attribute), type=True)
		# generate a name for the custom attribute that will store the necessary data
		userPropertyName = generateUserPropertyName(sourceNode, attribute)
		
		# skip if the attrType is none, such as e.g., worldUpMatrix with no incoming connection
		if attrType == None: continue
		
		# determine the type for the corresponding userProperty
		userPropertyType = attrType
		# convert unsupported types into strings
		unsupportedTypes = ['enum', 'matrix']
		if attrType in unsupportedTypes: userPropertyType = 'string'
		# add the attribute if it does not already exist
		if not userPropertyName in existingAttributes:
			if userPropertyType == 'string': mel.eval('addAttr -ln %s -dt "%s" %s;'%(userPropertyName, userPropertyType, targetObject))
			else: mel.eval('addAttr -ln %s -at "%s" %s;'%(userPropertyName, userPropertyType, targetObject))
		
		# determine the value to apply to the custom attribute
		attrValue = ''
		
		# check if attribute is a vector
		if attrType == 'double3':
			# add children attributes
			if not userPropertyName in existingAttributes:
				cmds.addAttr(targetObject, ln='%sX'%userPropertyName, p=userPropertyName, at='double')
				cmds.addAttr(targetObject, ln='%sY'%userPropertyName, p=userPropertyName, at='double')
				cmds.addAttr(targetObject, ln='%sZ'%userPropertyName, p=userPropertyName, at='double')
			# determine the attribute value and convert to left-handed result
			attrValue = cmds.getAttr('%s.%s'%(sourceNode, attribute))[0]
			attrValue = (-1*attrValue[0], attrValue[1], attrValue[2])
			# reorder Euler angles if this is an Euler angle attribute such as e.g., orientConstraint offset
			if ('eulerAttributes' in keywords and attribute in keywords['eulerAttributes']):
				# Euler offset attributes use the rotation order of the target (constrained) object
				euler = OM.MEulerRotation(-math.radians(attrValue[0]), -math.radians(attrValue[1]), -math.radians(attrValue[2]), cmds.getAttr('%s.rotateOrder'%targetObject))
				# BUG: aimConstraint offset does not work the same way, and I have no idea what it is doing; it will only work correctly if the object has rotateOrder XYZ
				euler.reorderIt(OM.MEulerRotation.kZXY)
				attrValue = (math.degrees(euler.x), math.degrees(euler.y), math.degrees(euler.z))
		
		# check if attribute is a transform node
		elif attrType == 'matrix':
			attrValue = cmds.listConnections('%s.%s'%(sourceNode, attribute))
			if attrValue: attrValue = attrValue[0]
		
		# otherwise assume it is a simple type such as long, double, int, or enum
		else: attrValue = cmds.getAttr('%s.%s'%(sourceNode, attribute))
		
		# delete the attribute if no value could be obtained
		if attrValue == None: cmds.deleteAttr('%s.%s'%(targetObject, userPropertyName))
		
		# otherwise set the attribute value
		else:
			# string needs to specify type
			if userPropertyType == 'string': cmds.setAttr('%s.%s'%(targetObject, userPropertyName), attrValue, type='string')
			# compound attributes must specify each element as a separate argument
			elif userPropertyType =='double3': cmds.setAttr('%s.%s'%(targetObject, userPropertyName), attrValue[0], attrValue[1], attrValue[2])
			# other simple types can be set as-is
			else: cmds.setAttr('%s.%s'%(targetObject, userPropertyName), attrValue)