"""
Utility functions for working with GUI elements in the Maya cmds module.

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

\namespace amTools.utilities.ui
"""

import re
import maya.cmds as cmds
import amTools as am

## optional flag for text command in versions of Maya with support
__wordWrap__ = ''
## optional flag for frameLayout command in versions of Maya with support
__frameAlignBottom__ = ''
## optional flag for frameLayout command in versions of Maya with support
__frameAlignCenter__ = ''
if am.__mayaVersion__ < 2011.0:
	__frameAlignBottom__ = ', la="bottom"'
	__frameAlignCenter__ = ', la="center"'
else:
	__wordWrap__ = ', ww=True'

def aboutDialog(title='About Dialog', message='About Message'):
	"""
	Create a simple About dialog box with the given title and message.
	@param title Custom about dialog title
	@param message Custom about dialog message
	"""
	cmds.confirmDialog(title = title, message = message, button='OK', defaultButton='OK', cancelButton='OK', dismissString='OK')

def aboutMenuItem(toolName, versionNumber, versionDate):
	"""
	Create a menu item for an about dialog.
	@param toolName Name of the tool
	@param versionNumber Version number of the tool
	@param versionDate Date of the current version
	"""
	cmds.menuItem(label='About', command='amTools.utilities.ui.aboutDialog("About %s Options", "Version %s\\n%s\\nby Adam D. Mechtley\\nhttp://adammechtley.com")'%(toolName, versionNumber, versionDate))

def helpMenuItem(toolName, file):
	"""
	Create a menu item that links to the appropriate page in the online docs.
	@param toolName Name of the tool
	@param file The __file__ string for the tool
	"""
	cmds.menuItem(label='Help on %s Options'%toolName, 
		command='cmds.launch(web="http://adammechtley.com/downloads/python/documentation/amtools/%s/namespace%s.html")'%(am.kVersionNumber,
		re.sub('[A-Z]', '_\g<0>', re.search('amTools.*(?<=[.])', file[file.rfind('amTools'):]).group(0)[:-1]).lower().replace('/', '_1_1')))
	
def threeButtonLayout(mainForm, windowName, cmd_create):
	"""
	Create the standard three button layout used in Maya tools: Create, Apply, and Close.
	@param mainForm The main form of the options window
	@param windowName The name of the options window
	@param cmd_create The command to execute when the Create or Apply button is pressed.
	"""
	cmd_closeWindow = '%s.deleteUI("%s")' % (am.__kCmdsGlobalName__, windowName) # this command is called outside the module, so cmds must exist in the Maya session
	# create the buttons
	btn_create = cmds.button(h=26, label='Create', command='%s\n%s'%(cmd_create, cmd_closeWindow))
	btn_apply = cmds.button(h=26, label='Apply', command=cmd_create)
	btn_close = cmds.button(h=26, label='Close', command=cmd_closeWindow)
	# position the buttons
	cmds.formLayout(mainForm, edit=True, attachForm=[(btn_create, 'left', 5), (btn_create, 'bottom', 5)], attachPosition=[(btn_create, 'right', 1, 33)], attachNone=[(btn_create, 'top')])
	cmds.formLayout(mainForm, edit=True, attachForm=[(btn_apply, 'bottom', 5)], attachPosition=[(btn_apply, 'left', 3, 33), (btn_apply, 'right', 3, 67)], attachNone=[(btn_apply, 'top')])
	cmds.formLayout(mainForm, edit=True, attachForm=[(btn_close, 'right', 5), (btn_close, 'bottom', 5)], attachPosition=[(btn_close, 'left', 1, 67)], attachNone=[(btn_apply, 'top')])