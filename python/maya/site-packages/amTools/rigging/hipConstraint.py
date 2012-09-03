"""
A GUI for applying a hip constraint.

\b Requirements:
AM_HipConstraint.py

To use this tool, first select your hip object, then add the constrained object
(your hip hip twist joint) to your selection and enter the desired data
into the option fields before pressing either the Create or Apply button.

\par Hip Constraint Options:
- \b Pelvis \b Object:
Specifies the name of the object to use for computing the hip's elevation
angle. The hip constraint is designed with the expectation that this is the
transform node that is the most direct parent of the hip joints (i.e. the
root). Though this will produce perfectly valid values if any intermediate
joints exist, such an intermediate joint could be used instead, provided that
the axes given for the pelvis node (below) are transformed into the
intermediate joint's local space.'
- \b Hip \b Aim \b Axis:
Corresponds to the axis in the upper leg's local space that aims toward the
knee joint.
- \b Hip \b Front \b Axis:
Corresponds to the axis in the upper leg's local space that points toward the
character's front.
- \b Pelvis \b Aim \b Axis:
Corresponds to the axis in the specified pelvis joint's local space that aims
toward the next vertebra (up).
- \b Pelvis \b Front \b Axis:
Corresponds to the axis in the specified pelvis joint's local space that aims
toward the character's front.

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

\namespace amTools.rigging.hipConstraint
"""

import sys
import maya.cmds as cmds
import amTools.utilities as utils
import amTools.utilities.ui as amui

# verify requirements
utils.plugins.verifyPlugin('AM_HipConstraint', __file__)

## options window name
kConstraintOptionsWindow = 'am_hipConstraintOptionsWindow'
## name of the tool
kToolName = 'Hip Constraint'
## current version of the tool
kVersionNumber = '1.04'
## date of current version
kVersionDate = '2011.03.27'

def menuItem(*args):
	"""This function calls optionsWindow() from a menu item"""
	optionsWindow()

def optionsWindow():
	"""This function creates an options window for the am_hipConstraint command. 
	When executing it, first select the hip to which you are constraining, then 
	add the object to be constrained to your selection."""
	# create the main interface
	if cmds.window(kConstraintOptionsWindow, q=True, ex=True):
		cmds.deleteUI(kConstraintOptionsWindow)
	mainWindow = cmds.window(kConstraintOptionsWindow, title='%s Options' % kToolName, menuBar=True, wh=(545,350))
	
	# build the menu bar
	cmds.menu(label='Help')
	amui.helpMenuItem(kToolName, __file__)
	amui.aboutMenuItem(kToolName, kVersionNumber, kVersionDate)
	
	mainForm = cmds.formLayout(nd=100)
	
	# build the section to get information for the hip constraint
	mainFrame = cmds.formLayout(nd=100)
	
	# attempt to guess what the pelvis is if there is a selection when the GUI is created
	pelvisText = 'CenterRoot'
	sel = cmds.ls(sl=True, l=True, type='transform')
	if sel and len(sel) > 0: # BUG: in Maya 8.5, a selection of length 0 returns None rather than an empty list
		try:
			pelvis = cmds.listRelatives(sel[0], p=True, f=True) # the hip should be the first object in the selection list
			pelvisText = pelvis[0]
		except: pass
	
	if_pelvis = cmds.textFieldGrp(label='Pelvis Object:', tx=pelvisText)
	if_hipAimAxis = cmds.floatFieldGrp(v1=1, v2=0, v3=0, nf=3, pre=4, label='Hip Aim Axis:')
	if_hipFrontAxis = cmds.floatFieldGrp(v1=0, v2=0, v3=1, nf=3, pre=4, label='Hip Front Axis:')
	if_pelvisAimAxis = cmds.floatFieldGrp(v1=0, v2=1, v3=0, nf=3, pre=4, label='Pelvis Aim Axis:')
	if_pelvisFrontAxis = cmds.floatFieldGrp(v1=0, v2=0, v3=1, nf=3, pre=4, label='Pelvis Front Axis:')
	
	# position the input fields for the hip constraint
	cmds.formLayout(mainFrame, edit=True, attachForm=[(if_pelvis, 'left', 30), (if_pelvis, 'top', 5)], attachNone=[(if_pelvis, 'right'), (if_pelvis, 'bottom')])
	cmds.formLayout(mainFrame, edit=True, attachForm=[(if_hipAimAxis, 'left', 30)], attachNone=[(if_hipAimAxis, 'right'), (if_hipAimAxis, 'bottom')], attachControl=[(if_hipAimAxis, 'top', 5, if_pelvis)])
	cmds.formLayout(mainFrame, edit=True, attachForm=[(if_hipFrontAxis, 'left', 30)], attachNone=[(if_hipFrontAxis, 'right'), (if_hipFrontAxis, 'bottom')], attachControl=[(if_hipFrontAxis, 'top', 5, if_hipAimAxis)])
	cmds.formLayout(mainFrame, edit=True, attachForm=[(if_pelvisAimAxis, 'left', 30)], attachNone=[(if_pelvisAimAxis, 'right'), (if_pelvisAimAxis, 'bottom')], attachControl=[(if_pelvisAimAxis, 'top', 5, if_hipFrontAxis)])
	cmds.formLayout(mainFrame, edit=True, attachForm=[(if_pelvisFrontAxis, 'left', 30)], attachNone=[(if_pelvisFrontAxis, 'right'), (if_pelvisFrontAxis, 'bottom')], attachControl=[(if_pelvisFrontAxis, 'top', 5, if_pelvisAimAxis)])
	
	cmds.setParent('..') # go up to mainFrame
	
	# create the buttons to execute the hcript
	cmd_create='amTools.rigging.hipConstraint.doOptions (\"%s\", \"%s\", \"%s\", \"%s\", \"%s\")' % (
		if_pelvis, 
		if_hipAimAxis, 
		if_hipFrontAxis, 
		if_pelvisAimAxis, 
		if_pelvisFrontAxis)
	utils.ui.threeButtonLayout(mainForm, mainWindow, cmd_create)
	
	cmds.showWindow(mainWindow)

def doOptions(input_pelvis, input_hipAimAxis, input_hipFrontAxis, input_pelvisAimAxis, input_pelvisFrontAxis):
	"""Specifies the function called when the apply or create button is clicked"""
	try:
		# validate selection
		selection = utils.dg.validateSelection(type='transform', msg='Please select your hip object and then the twist object to constrain.', exact=2)
		
		# validate pelvis
		pelvis = cmds.textFieldGrp(input_pelvis, q=True, tx=True)
		utils.dg.verifyNode(pelvis)
		
		# create the hip constraint
		cmds.am_hipConstraint(
			selection[1],
			pelvisObject = pelvis,
			hipObject = selection[0],
			ha=cmds.floatFieldGrp(input_hipAimAxis, q=True, v=True), 
			hf=cmds.floatFieldGrp(input_hipFrontAxis, q=True, v=True), 
			pa=cmds.floatFieldGrp(input_pelvisAimAxis, q=True, v=True), 
			pf=cmds.floatFieldGrp(input_pelvisFrontAxis, q=True, v=True))
	except: raise

def unitTest():
	"""A simple unit test for the am_hipConstraint command"""
	# make joints
	jr = 0.1
	pelvis = cmds.joint(n='pelvis', p=[0,2,0], rad=jr)
	cmds.select(cl=True)
	hip = cmds.joint(n='hip', p=[0.4,2,0], rad=jr)
	knee = cmds.joint(n='knee', p=[0.4,1.05,0.1], rad=jr)
	cmds.joint(hip, e=True, oj='xzy', sao='zup')
	foot = cmds.joint(n='foot', p=[0.4,0.1,0], rad=jr)
	cmds.joint(knee, e=True, oj='xzy', sao='zup')
	cmds.joint(foot, e=True, o=[0,0,0])
	cmds.parent(hip, pelvis)
	cmds.select(hip)
	twist = cmds.joint(n='twist', rad=jr*2)
	
	# test create mode
	print '---TESTING CREATE---'
	def verifyObjects(outNum, hcNode, expPelvis, expHip, expTwist):
		"""Print test results"""
		print '%s (test %i):'%(hcNode, outNum)
		print'\tpelvis: %s'%(expPelvis == cmds.am_hipConstraint(hcNode, q=True, p=True))
		print'\thip:    %s'%(expHip == cmds.am_hipConstraint(hcNode, q=True, h=True))
		print'\ttwist:  %s'%(expTwist == cmds.listConnections('%s.rotate'%hcNode, scn=True)[0])
	hc = cmds.am_hipConstraint([pelvis,hip,twist])
	verifyObjects(0, hc, pelvis, hip, twist)
	cmds.delete(hc)
	hc = cmds.am_hipConstraint([hip,twist], pelvisObject=pelvis)
	verifyObjects(1, hc, pelvis, hip, twist)
	cmds.delete(hc)
	hc = cmds.am_hipConstraint([pelvis,twist], hipObject=hip)
	verifyObjects(2, hc, pelvis, hip, twist)
		
	# test edit mode
	def compareVectors(listVec, tupleVec):
		"""Return test result comparing vectors"""
		return listVec[0]==tupleVec[0] and listVec[1]==tupleVec[1] and listVec[2]==tupleVec[2]
	def verifyValues(outNum, hcNode, expHa, expHf, expPa, expPf):
		"""Print test results"""
		print '%s (test %i):'%(hcNode, outNum)
		print'\tha: %s'%(expHa == cmds.am_hipConstraint(hcNode, q=True, ha=True))
		print'\thf: %s'%(expHf == cmds.am_hipConstraint(hcNode, q=True, hf=True))
		print'\tpa: %s'%(expPa == cmds.am_hipConstraint(hcNode, q=True, pa=True))
		print'\tpf: %s'%(expPf == cmds.am_hipConstraint(hcNode, q=True, pf=True))
	print '---TESTING EDIT---'
	cmds.am_hipConstraint(hc, e=True, p=foot)
	verifyObjects(0, hc, foot, hip, twist)
	cmds.am_hipConstraint(hc, e=True, h=pelvis)
	verifyObjects(1, hc, foot, pelvis, twist)
	cmds.am_hipConstraint(hc, e=True, h=hip, p=pelvis)
	verifyObjects(2, hc, pelvis, hip, twist)
	ha = [2,0,0]
	hf = [0,0,2]
	pa = [1.5,0,0]
	pf = [1.2,0,0]
	cmds.am_hipConstraint(hc, e=True, ha=ha, hf=hf, pa=pa, pf=pf)
	verifyValues(0, hc, ha, hf, pa, pf)
	
	# test query mode
	print '---TESTING QUERY---'
	print 'hip:  %s'%(cmds.am_hipConstraint(hc, q=True, h=True) == cmds.listConnections('%s.hip'%hc)[0])
	print 'pelv: %s'%(cmds.am_hipConstraint(hc, q=True, p=True) == cmds.listConnections('%s.pelvis'%hc)[0])
	print 'hAim: %s'%compareVectors(cmds.am_hipConstraint(hc, q=True, ha=True), cmds.getAttr('%s.hipAim'%hc)[0])
	print 'hFor: %s'%compareVectors(cmds.am_hipConstraint(hc, q=True, hf=True), cmds.getAttr('%s.hipFront'%hc)[0])
	print 'pAim: %s'%compareVectors(cmds.am_hipConstraint(hc, q=True, pa=True), cmds.getAttr('%s.pelvisAim'%hc)[0])
	print 'pFor: %s'%compareVectors(cmds.am_hipConstraint(hc, q=True, pf=True), cmds.getAttr('%s.pelvisFront'%hc)[0])
	
	cmds.select(pelvis)