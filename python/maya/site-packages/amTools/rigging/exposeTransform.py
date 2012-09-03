"""
A GUI for creating a node to compute information about one transform node with
respect to another.

\b Requirements:
AM_ExposeTransform.py

To use this tool, select a transform node to expose and enter the desired data
into the option fields before pressing either the Create or Apply button.

\par Expose Transform Options:
- \b Reference \b Object:
Specifies another transform node to be the frame of reference for the
exposed object. World matrix is used if none is specified.
- \b Output \b Rotate \b Order:
Specifies how to compute Euler rotation in the new am_exposeTransform node.
- \b Axis \b on \b Object:
Specifies an axis on the exposed object used to compute dot, angle,
dotToTarget, and angleToTarget.
- \b Axis \b on \b Reference:
Specifies an axis on the reference object used to compute dot and angle.
- \b Normalize \b Axes:
Specifies whether the input axes should be normalized internally in the new
am_exposeTransform node when computing dot and dotToTarget.

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

\namespace amTools.rigging.exposeTransform
"""

import sys
import maya.cmds as cmds
import amTools.utilities as utils
import amTools.utilities.ui as amui

# verify requirements
utils.plugins.verifyPlugin('AM_ExposeTransform', __file__)

## options window name
kExposeTransformOptionsWindow = 'am_exposeTransformOptionsWindow'
## name of the tool
kToolName = 'Expose Transform'
## current version of the tool
kVersionNumber = '1.02'
## date of current version
kVersionDate = '2011.03.27'

def menuItem(*args):
	"""This function calls optionsWindow() from a menu item"""
	optionsWindow()

def optionsWindow():
	"""This function creates an options window for making ribbons along selected hair curves."""
	# create the main interface
	if cmds.window(kExposeTransformOptionsWindow, q=True, ex=True):
		cmds.deleteUI(kExposeTransformOptionsWindow)
	mainWindow = cmds.window(kExposeTransformOptionsWindow, title='%s Options'%kToolName, menuBar=True, wh=(545,350))
	
	# build the menu bar
	cmds.menu(label='Help')
	amui.helpMenuItem(kToolName, __file__)
	amui.aboutMenuItem(kToolName, kVersionNumber, kVersionDate)
	
	mainForm = cmds.formLayout(nd=100)
	
	# build the section to get information about the new expose transform node
	if_referenceObject = cmds.textFieldGrp(label='Reference Object:')
	if_rotateOrder = cmds.optionMenuGrp(label='Output Rotate Order:')
	cmds.menuItem(label='xyz')
	cmds.menuItem(label='yzx')
	cmds.menuItem(label='zxy')
	cmds.menuItem(label='xzy')
	cmds.menuItem(label='yxz')
	cmds.menuItem(label='zyx')
	if_axis = cmds.floatFieldGrp(v1=0, v2=0, v3=1, nf=3, pre=4, label='Axis on Object:')
	if_referenceAxis = cmds.floatFieldGrp(v1=0, v2=0, v3=1, nf=3, pre=4, label='Axis on Reference:')
	if_normalizeAxes = cmds.checkBoxGrp(v1=1, label='Normalize Axes:')
	
	# position the input fields for the new parents
	cmds.formLayout(mainForm, edit=True, attachForm=[(if_referenceObject, 'left', 30), (if_referenceObject, 'top', 5)], attachNone=[(if_referenceObject, 'right'), (if_referenceObject, 'bottom')])
	cmds.formLayout(mainForm, edit=True, attachForm=[(if_rotateOrder, 'left', 30)], attachNone=[(if_rotateOrder, 'right'), (if_rotateOrder, 'bottom')], attachControl=[(if_rotateOrder, 'top', 5, if_referenceObject)])
	cmds.formLayout(mainForm, edit=True, attachForm=[(if_axis, 'left', 30)], attachNone=[(if_axis, 'right'), (if_axis, 'bottom')], attachControl=[(if_axis, 'top', 5, if_rotateOrder)])
	cmds.formLayout(mainForm, edit=True, attachForm=[(if_referenceAxis, 'left', 30)], attachNone=[(if_referenceAxis, 'right'), (if_referenceAxis, 'bottom')], attachControl=[(if_referenceAxis, 'top', 5, if_axis)])
	cmds.formLayout(mainForm, edit=True, attachForm=[(if_normalizeAxes, 'left', 30)], attachNone=[(if_normalizeAxes, 'right'), (if_normalizeAxes, 'bottom')], attachControl=[(if_normalizeAxes, 'top', 5, if_referenceAxis)])
	
	# create the buttons to execute the script
	cmd_create = 'amTools.rigging.exposeTransform.doOptions ("%s", "%s", "%s", "%s", "%s")'%(if_referenceObject, if_rotateOrder, if_axis, if_referenceAxis, if_normalizeAxes)
	amui.threeButtonLayout(mainForm, mainWindow, cmd_create)
	
	cmds.showWindow(mainWindow)

def doOptions(input_referenceObject, input_rotateOrder, input_axis, input_referenceAxis, input_normalizeAxes):
	"""This is the function called when the apply or create button is clicked"""
	try:
		# validate selection
		utils.dg.validateSelection(type='transform', exact=1)
		
		# validate reference object
		referenceObject = cmds.textFieldGrp(input_referenceObject, q=True, tx=True)
		if len(referenceObject) > 0: utils.dg.verifyNode(referenceObject)
		
		# call the command
		if len(referenceObject) > 0:
			cmds.am_exposeTransform(
				ref=referenceObject, 
				ro=utils.kRotateOrderMapping[cmds.optionMenuGrp(input_rotateOrder, q=True, v=True)], 
				a=cmds.floatFieldGrp(input_axis, q=True, v=True), 
				ra=cmds.floatFieldGrp(input_referenceAxis, q=True, v=True), 
				na=cmds.checkBoxGrp(input_normalizeAxes, q=True, v1=True))
		else:
			cmds.am_exposeTransform(
				ro=utils.kRotateOrderMapping[cmds.optionMenuGrp(input_rotateOrder, q=True, v=True)], 
				a=cmds.floatFieldGrp(input_axis, q=True, v=True), 
				ra=cmds.floatFieldGrp(input_referenceAxis, q=True, v=True), 
				na=cmds.checkBoxGrp(input_normalizeAxes, q=True, v1=True))
	except: raise