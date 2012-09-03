"""
A GUI for inserting an in-place locator parent for each object in the selection
list.

\b Requirements:
AM_InsertParentsCmd.py

To use this tool, select one or more transform nodes and enter the desired data
into the option fields before pressing either the Create or Apply button.

\par Insert Parents Options:
- \b Prefix \b of \b New \b Parents:
The base naming prefix to apply to the newly created parent locators. Their
stems will match the name of the transform for which they will become the new
parent.
- \b Suffix \b of \b New \b Parents:
The base naming suffix to apply to the newly created parent locators. Their
stems will match the name of the transform for which they will become the new
parent.
- \b Parent \b Locator \b Scale
The scale value for the shape node of the newly created parent locators.

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

\namespace amTools.rigging.insertParents
"""

import sys
import maya.cmds as cmds
import maya.OpenMaya as OM
import amTools.utilities as utils
import amTools.utilities.ui as amui

# verify requirements
utils.plugins.verifyPlugin('AM_InsertParentsCmd', __file__)

## options window name
kInsertOptionsWindow = 'am_insertParentsOptionsWindow'
## name of the tool
kToolName = 'Insert Parents'
## current version of the tool
kVersionNumber = '1.03'
## date of current version
kVersionDate = '2011.03.27'

def menuItem(*args):
	"""This function calls optionsWindow() from a menu item"""
	optionsWindow()

def optionsWindow():
	"""This function creates an options window for inserting parents above all items in the selection list."""
	# create the main interface
	if cmds.window(kInsertOptionsWindow, q=True, ex=True):
		cmds.deleteUI(kInsertOptionsWindow)
	mainWindow = cmds.window(kInsertOptionsWindow, title='%s Options' % kToolName, menuBar=True, wh=(545,350))
	
	# build the menu bar
	cmds.menu(label='Help')
	amui.helpMenuItem(kToolName, __file__)
	amui.aboutMenuItem(kToolName, kVersionNumber, kVersionDate)
	
	mainForm = cmds.formLayout(nd=100)
	
	# build the section to get information about the new parents
	if_prefixName = cmds.textFieldGrp(text='', label='Prefix of New Parents:')
	if_suffixName = cmds.textFieldGrp(text='_xForm', label='Suffix of New Parents:')
	if_locatorScale = cmds.floatSliderGrp(v=1.0, min=0.0, max=10.0, fmn=0.0, fmx=100.0, label='Parent Locator Scale:', field=True)
	
	# position the input fields for the new parents
	cmds.formLayout(mainForm, edit=True, attachForm=[(if_prefixName, 'left', 30), (if_prefixName, 'top', 5)], attachNone=[(if_prefixName, 'right'), (if_prefixName, 'bottom')])
	cmds.formLayout(mainForm, edit=True, attachForm=[(if_suffixName, 'left', 30)], attachNone=[(if_suffixName, 'right'), (if_suffixName, 'bottom')], attachControl=[(if_suffixName, 'top', 5, if_prefixName)])
	cmds.formLayout(mainForm, edit=True, attachForm=[(if_locatorScale, 'left', 30)], attachNone=[(if_locatorScale, 'right'), (if_locatorScale, 'bottom')], attachControl=[(if_locatorScale, 'top', 5, if_suffixName)])
	
	# create the buttons to execute the script
	cmd_create='amTools.rigging.insertParents.doOptions (\"%s\", \"%s\", \"%s\")' % (if_prefixName, if_suffixName, if_locatorScale)
	amui.threeButtonLayout(mainForm, mainWindow, cmd_create)
	
	cmds.showWindow(mainWindow)

def doOptions(input_prefix, input_suffix, input_locatorScale):
	"""This is the function called when the apply or create button is clicked"""
	try:
		utils.dg.validateSelection(type='transform', min=1)
		
		# get the affixes
		prefix = cmds.textFieldGrp(input_prefix, q=True, tx=True)
		suffix = cmds.textFieldGrp(input_suffix, q=True, tx=True)
		
		# no call to utils.dg.validateAffix is necessary, as the command has its own validation built in
		if (len(prefix) == 0 and len(suffix) == 0):
			OM.MGlobal.displayWarning('A prefix or a suffix is required in order to ensure the newly created parent names will be unique. Using _xForm suffix.')
			suffix = '_xForm'
		
		# get the scale
		scale = cmds.floatSliderGrp(input_locatorScale, q=True, v=True)
		
		# call the command
		cmds.am_insertParents(pre=prefix, suf=suffix, scale=(scale, scale, scale))
	except: raise