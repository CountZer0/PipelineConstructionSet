"""
A GUI to automatically create the twist structure for an upper leg.

\b Requirements:
AM_HipConstraint.py

To use this tool, select one or more knee joints and enter the desired data
into the option fields before pressing either the Create or Apply button.

To skin the model, the leg mesh should be skinned in segments for each twist
joint, plus one additional for the hip joint, where the segment at the base of
the hip is skinned to the first twist joint and the final segment is skinned to
the hip joint.

\par Setup Hip Options:
- \b Suffix \b of \b New \b Twist \b Joints:
Specifies the base naming suffix to apply to the newly created joints. Their
prefix will match the shoulder on which they are twisting and they will also be
numbered from 1 to n.
- \b Number \b of \b Twist \b Joints:
Specifies the number of twist joints to create for each hip. You must create at
least one and the first will always have the hip constraint applied to it.
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

\namespace amTools.rigging.hipSetup
"""

import sys
import maya.cmds as cmds
import amTools.utilities as utils
import amTools.utilities.ui as amui

# verify requirements
utils.plugins.verifyPlugin('AM_HipConstraint', __file__)

## options window name
kSetupOptionsWindow = 'am_setupHipOptionsWindow'
## name of the tool
kToolName = 'Setup Hip'
## current version of the tool
kVersionNumber = '1.05'
## date of current version
kVersionDate = '2011.03.27'

def menuItem(*args):
	"""This function calls optionsWindow() from a menu item"""
	optionsWindow()

def optionsWindow():
	"""This function creates an options window for creating the hip twist
	structure. When executing it, select the knees in the legs you are setting
	up, then press Create or Apply."""
	# create the main interface
	if cmds.window(kSetupOptionsWindow, q=True, ex=True):
		cmds.deleteUI(kSetupOptionsWindow)
	mainWindow = cmds.window(kSetupOptionsWindow, title='%s Options'%kToolName, menuBar=True, wh=(545,350))
	
	# build the menu bar
	cmds.menu(label='Help')
	amui.helpMenuItem(kToolName, __file__)
	amui.aboutMenuItem(kToolName, kVersionNumber, kVersionDate)
	
	mainForm = cmds.formLayout(nd=100)
	
	# build the section to get information about the new twist joints
	if_suffixName = cmds.textFieldGrp(text='_Twist', label='Suffix of New Twist Joints:')
	if_numberTwistJoints = cmds.intSliderGrp(v=3, min=1, max=10, fmn=1, fmx=100, label='Number of Twist Joints:', field=True)
	
	# position the input fields for the twist joints
	cmds.formLayout(mainForm, edit=True, attachForm=[(if_suffixName, 'left', 30), (if_suffixName, 'top', 5)], attachNone=[(if_suffixName, 'right'), (if_suffixName, 'bottom')])
	cmds.formLayout(mainForm, edit=True, attachForm=[(if_numberTwistJoints, 'left', 30)], attachNone=[(if_numberTwistJoints, 'right'), (if_numberTwistJoints, 'bottom')], attachControl=[(if_numberTwistJoints, 'top', 5, if_suffixName)])
	
	# build the section to get information for the hip constraint
	constraintFrame = eval('cmds.frameLayout(collapsable=True, label="Hip Constraint Options:" %s)'%amui.__frameAlignCenter__)
	constraintForm = cmds.formLayout(nd=100)
	
	# attempt to guess what the pelvis is if there is a selection when the GUI is created
	pelvisText = 'CenterRoot'
	sel = cmds.ls(sl=True, l=True, type='transform')
	if sel and len(sel) > 0: # BUG: in Maya 8.5, a selection of length 0 returns None rather than an empty list
		try:
			hip = cmds.listRelatives(sel[0], p=True, f=True) # just use the first knee in the selection
			pelvis = cmds.listRelatives(hip[0], p=True, f=True)
			pelvisText = pelvis[0]
		except: pass
		
	if_pelvis = cmds.textFieldGrp(label='Pelvis Object:', tx=pelvisText)
	if_hipAimAxis = cmds.floatFieldGrp(v1=1, v2=0, v3=0, nf=3, pre=4, label='Hip Aim Axis:')
	if_hipFrontAxis = cmds.floatFieldGrp(v1=0, v2=0, v3=1, nf=3, pre=4, label='Hip Front Axis:')
	if_pelvisAimAxis = cmds.floatFieldGrp(v1=0, v2=1, v3=0, nf=3, pre=4, label='Pelvis Aim Axis:')
	if_pelvisFrontAxis = cmds.floatFieldGrp(v1=0, v2=0, v3=1, nf=3, pre=4, label='Pelvis Front Axis:')
	
	# position the input fields for the hip constraint
	cmds.formLayout(constraintForm, edit=True, attachForm=[(if_pelvis, 'left', 30), (if_pelvis, 'top', 5)], attachNone=[(if_pelvis, 'right'), (if_pelvis, 'bottom')])
	cmds.formLayout(constraintForm, edit=True, attachForm=[(if_hipAimAxis, 'left', 30)], attachNone=[(if_hipAimAxis, 'right'), (if_hipAimAxis, 'bottom')], attachControl=[(if_hipAimAxis, 'top', 5, if_pelvis)])
	cmds.formLayout(constraintForm, edit=True, attachForm=[(if_hipFrontAxis, 'left', 30)], attachNone=[(if_hipFrontAxis, 'right'), (if_hipFrontAxis, 'bottom')], attachControl=[(if_hipFrontAxis, 'top', 5, if_hipAimAxis)])
	cmds.formLayout(constraintForm, edit=True, attachForm=[(if_pelvisAimAxis, 'left', 30)], attachNone=[(if_pelvisAimAxis, 'right'), (if_pelvisAimAxis, 'bottom')], attachControl=[(if_pelvisAimAxis, 'top', 5, if_hipFrontAxis)])
	cmds.formLayout(constraintForm, edit=True, attachForm=[(if_pelvisFrontAxis, 'left', 30)], attachNone=[(if_pelvisFrontAxis, 'right'), (if_pelvisFrontAxis, 'bottom')], attachControl=[(if_pelvisFrontAxis, 'top', 5, if_pelvisAimAxis)])
	
	cmds.setParent('..') # go up to constraintForm
	cmds.setParent('..') # go up to mainForm
	
	# position the frame for the hip constraint
	cmds.formLayout(mainForm, edit=True, attachPosition=[(constraintFrame, 'left', -1, 0), (constraintFrame, 'right', -1, 100)], attachControl=[(constraintFrame, 'top', 5, if_numberTwistJoints)], attachNone=[(constraintFrame, 'bottom')])
	
	# create the buttons to execute the script
	cmd_create='amTools.rigging.hipSetup.doOptions ("%s", "%s", "%s", "%s", "%s", "%s", "%s")'%(
		if_suffixName, 
		if_numberTwistJoints, 
		if_pelvis, 
		if_hipAimAxis, 
		if_hipFrontAxis, 
		if_pelvisAimAxis, 
		if_pelvisFrontAxis)
	utils.ui.threeButtonLayout(mainForm, mainWindow, cmd_create)
	
	cmds.showWindow(mainWindow)

def doOptions(input_suffix, input_numberTwistJoints, input_pelvis, input_hipAimAxis, input_hipFrontAxis, input_pelvisAimAxis, input_pelvisFrontAxis):
	"""Specifies the function called when the apply or create button is clicked"""
	try:
		# validate selection
		selection = utils.dg.validateSelection(type='transform', name='knee joint objects', min=1)
		
		# validate suffix
		suffix = cmds.textFieldGrp(input_suffix, q=True, tx=True)
		utils.dg.validateAffix(suffix)
		
		# validate pelvis
		pelvis = cmds.textFieldGrp(input_pelvis, q=True, tx=True)
		utils.dg.verifyNode(pelvis)
		
		# set up the hip
		numberTwistJoints = cmds.intSliderGrp(input_numberTwistJoints, q=True, v=True)
		newSelection = []
		# perform setup for each knee in the selection
		for knee in selection:
			hip = cmds.listRelatives(knee, p=True, f=True)
			hipShort = cmds.listRelatives(knee, p=True)
			newJoints = doSetup(
				hipShort[0] + suffix, 
				numberTwistJoints, 
				knee, 
				hip[0], 
				pelvis, 
				cmds.floatFieldGrp(input_hipAimAxis, q=True, v=True), 
				cmds.floatFieldGrp(input_hipFrontAxis, q=True, v=True), 
				cmds.floatFieldGrp(input_pelvisAimAxis, q=True, v=True), 
				cmds.floatFieldGrp(input_pelvisFrontAxis, q=True, v=True))
			newSelection += newJoints
		# select the newly created joints for easy editing
		cmds.select(newSelection)
	except: raise

def doSetup(baseName, numberTwistJoints, knee, hip, pelvis, hipAimAxis, hipFrontAxis, pelvisAimAxis, pelvisFrontAxis):
	"""This function creates the new twist joints and returns a list of their names."""
	try:
		# validate baseName
		utils.dg.validateNodeName(baseName)
		
		# validate incoming object names
		utils.dg.verifyNode(knee)
		utils.dg.verifyNode(hip)
		utils.dg.verifyNode(pelvis)
		
		# get the translation value for the knee
		kneeTranslate = cmds.getAttr('%s.translate'%knee)[0]
		
		# see if there is a side label
		bodySide = cmds.getAttr('%s.side'%hip)
		
		# find out what rotate order the hip is using
		rotateOrder = cmds.getAttr('%s.rotateOrder'%hip)
		
		# create the twist joints
		twistJoints = []
		
		for i in range(numberTwistJoints):
			cmds.select(cl=True)
			newJoint = cmds.joint(name='%s%s'%(baseName, i + 1))
			
			# set up the first joint
			if i == 0:
				newJoint = cmds.parent(newJoint, hip)[0]
				jointRadius = 1.0
				jointOrient = []
				if cmds.objectType(hip, isType='joint'):
					jointRadius = cmds.getAttr('%s.radius'%hip) * 0.5
	
				cmds.setAttr('%s.radius'%newJoint, jointRadius)
				cmds.setAttr('%s.jointOrient'%newJoint, 0,0,0)
				cmds.setAttr('%s.translate'%newJoint, 0,0,0)
				
				# create the hip constraint
				cmds.am_hipConstraint(
					newJoint,
					pelvisObject = pelvis,
					hipObject = hip,
					ha=hipAimAxis, 
					hf=hipFrontAxis, 
					pa=pelvisAimAxis, 
					pf=pelvisFrontAxis)
			# set up the rest of the joints
			else:
				newJoint = cmds.parent(newJoint, hip)[0]
				cmds.setAttr('%s.radius'%newJoint, jointRadius)
				cmds.setAttr('%s.jointOrient'%newJoint, 0,0,0)
				pct = float(i)/float(numberTwistJoints)
				cmds.setAttr('%s.translate'%newJoint, kneeTranslate[0]*pct, kneeTranslate[1]*pct, kneeTranslate[2]*pct)
				
				# create the orient constraint
				orientConstraint = cmds.orientConstraint([twistJoints[0], hip, newJoint])
				targetWeights = cmds.orientConstraint(q=True, weightAliasList=True)
				cmds.setAttr('%s.%s'%(orientConstraint[0], targetWeights[0]), numberTwistJoints - i)
				cmds.setAttr('%s.%s'%(orientConstraint[0], targetWeights[1]), i)
				cmds.setAttr('%s.interpType'%orientConstraint[0], 1)
				
			# set label and rotate order
			cmds.setAttr('%s.side'%newJoint, bodySide)
			cmds.setAttr('%s.type'%newJoint, 18)
			cmds.setAttr('%s.otherType'%newJoint, 'Hip Twist %s'%(i + 1), type='string')
			cmds.setAttr('%s.rotateOrder'%newJoint, rotateOrder)
			
			# add the new joint to the list to return
			twistJoints.append(newJoint)
		
		return twistJoints
	except: raise