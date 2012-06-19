'''
Author: Jason.Parks
Created: Jan 17, 2012
Module: moBu.moBuSets
Purpose: FBSet convenience class
'''
from pyfbsdk import *
from common.diagnostic.pcsLogger import moBuLogger
from moBu.core.moBuCore import MoBuCore, mbCore


# eclipseSyntax
if False: from pyfbsdk_gen_doc import * #@UndefinedVariable @UnusedWildImport

# Load additions dependent on MoBu version
if mbCore.mobuVer == 2010:
	from pyfbsdk_additions import CreateUniqueTool as FBCreateUniqueTool #@UnresolvedImport @UnusedImport
	from pyfbsdk_additions import GridLayout as FBGridLayout #@UnusedImport @UnresolvedImport
	from pyfbsdk_additions import VBoxLayout as FBVBoxLayout #@UnusedImport @UnresolvedImport
elif mbCore.mobuVer == 2012 or mbCore.mobuVer == 2013:
	from pyfbsdk_additions import FBCreateUniqueTool, FBGridLayout, FBVBoxLayout #@Reimport @UnresolvedImport @UnusedImport
else:
	moBuLogger.error("Failed to find proper MoBu version: '%s'" % mbCore.mobuVer)

class MoBuSets(MoBuCore):
	
	def __init__(self):
		""" MoBuSets.__init__():  set initial parameters """
		super(MoBuSets, self).__init__()
		
		self.listSelection = ''
		self.lst = FBList()
	
	def goButtonCallback(self, control, event):
		moBuLogger.info("Button '%s' pressed" % control.Name)
		# create set
		newSet = FBSet(self.listSelection)
		moBuLogger.debug("Result of set creation is '%s'" % newSet)
		self.addAllToSet(name=newSet.Name, quiet=False)

	def newButtonCallback(self, control, event):
		moBuLogger.info("Button '%s' pressed" % control.Name)
		btn, value = FBMessageBoxGetUserValue("New Set", "Type name of new set", "mySet", FBPopupInputType.kFBPopupString, "OK", "Cancel", None, 1, True)
		if btn == 2:
			return
		self.lst.Items.append(value)

	def listCallback(self, control, event):
		self.listSelection = control.Items[control.ItemIndex] 
		moBuLogger.debug("%s has been selected!" % self.listSelection)
	
	def PopulateLayoutCreateSet(self, mainLyt):
	
		x = FBAddRegionParam(0, FBAttachType.kFBAttachLeft, "")
		y = FBAddRegionParam(0, FBAttachType.kFBAttachTop, "")
		w = FBAddRegionParam(0, FBAttachType.kFBAttachRight, "")
		h = FBAddRegionParam(0, FBAttachType.kFBAttachBottom, "")
		mainLyt.AddRegion("main", "main", x, y, w, h)
		
		# add grid to mainLayout
		grid = FBGridLayout()
		mainLyt.SetControl("main", grid)
		
		vBox = FBVBoxLayout()
		grid.Add(vBox, 0, 0, attachX=FBAttachType.kFBAttachLeft, width=200, height=100)
		
		self.lst.OnChange.Add(self.listCallback)
		self.lst.Style = FBListStyle.kFBVerticalList
		vBox.Add(self.lst, 75)
		
		# add selected to list
		selected = mbCore.getSelected(_type=FBModel, found=False)
		if selected:
			self.lst.Items.append(selected[0].Name)
		
		# add name of character Node to list
		char = mbCore.getCharacter(hipsJoint='')
		if char:
			# remove Version suffix
			if "_V" in char.Name:
				setName = char.Name[:-4]
			else:
				setName = char.Name
			self.lst.Items.append(setName)
		
		# create buttons
		newBut = FBButton()
		newBut.Caption = "New Set"
		newBut.Look = FBButtonLook.kFBLookNormal
		newBut.OnClick.Add(self.newButtonCallback)
		grid.Add(newBut, 1, 0, attachX=FBAttachType.kFBAttachLeft, width=60, height=30)
			
		# create buttons
		goBut = FBButton()
		goBut.Caption = "Go"
		goBut.Look = FBButtonLook.kFBLookNormal
		goBut.OnClick.Add(self.goButtonCallback)
		grid.Add(goBut, 2, 0, attachX=FBAttachType.kFBAttachLeft, width=60, height=30)

	def addAllToSetUI(self):
		''' finds the set with name
			Params:
				name: name of set
				quiet: suppress dialogs
			Returns: FBSet/False
		'''
		t = FBCreateUniqueTool("Create Set")
		self.PopulateLayoutCreateSet(t)
		t.StartSizeX = 230
		t.StartSizeY = 220
		ShowTool(t) #@UndefinedVariable
		
		return
						
	def addAllToSet(self, name='', quiet=False):
		''' finds the set with name
			Params:
				name: name of set
				quiet: suppress dialogs
			Returns: FBSet/False
		'''
		ourSet = None
		
		# type or select set name if not passed
		if not name:
			# check for selected set
			selected = self.getSelected(_type=FBSet, found=True)
			if selected:
				# test type
				if isinstance(selected, FBSet):
					ourSet = selected
			else:
				# spawn dialogue listing choices
				self.addAllToSetUI()
				return False
		else:
			# check for set existence
			if self.findSet(name=name, quiet=quiet):
				ourSet = self.findSet(name=name, quiet=quiet)
			else:
				# create set
				ourSet = FBSet(name)
			
#		count = 0
#		allItems = []
#		
#		modelSkeletons = self.getAllByType(_type='FBModelSkeleton')
#		allItems.extend(modelSkeletons)
#		
#		models = self.getAllByType(_type='FBModel')
#		allItems.extend(models)
#		
#		modelNulls = self.getAllByType(_type='FBModelNull')
#		allItems.extend(modelNulls)
#		materials = self.getAllByType(_type='FBMaterial')
#		allItems.extend(materials)
#		textures = self.getAllByType(_type='FBTexture')
#		allItems.extend(textures)
#		
#		deformers = self.getAllByType(_type='FBDeformer')
#		allItems.extend(deformers)
#		constraintRelation = self.getAllByType(_type='FBConstraintRelation')
#		allItems.extend(constraintRelation)
#		groups = self.getAllByType(_type='FBGroup')
#		allItems.extend(groups)
#		poses = self.getAllByType(_type='FBPose')
#		allItems.extend(poses)
#		vidClips = self.getAllByType(_type='FBVideoClipImage')
#		allItems.extend(vidClips)
#		characters = self.getAllByType(_type='FBCharacter')
#		allItems.extend(characters)
#		
#		for item in allItems:
#			ourSet.Items.append(item)
#			count+=1
		
		count = 0
		allItems = self.getAllByType(_type='all')
		for item in allItems:
								
			# skip Sets
			if isinstance(item, FBSet):
				continue
				
			# safe to add
			ourSet.Items.append(item)
			count += 1
			
		if not quiet:
			moBuLogger.infoDialog("%d items added to Set '%s'" % (count, ourSet.Name), "Set Created")
		else:
			moBuLogger.info("%d items added to Set '%s'" % (count, ourSet.Name))
		
		return ourSet
	
	def findSet(self, name='', quiet=False):
		''' finds the set with name
			Params:
				name: name of set
				quiet: suppress dialogs
			Returns: FBSet/False
		'''
		if not name:
			if not quiet:
				moBuLogger.errorDialog("No name arg passed.")
			return False
			
		# get all sets
		allSets = self.scene.Sets
		if not allSets:
			if not quiet:
				moBuLogger.infoDialog("No sets found in scene.")
			return False

		# check sets for name
		for _set in allSets:
			if name == _set.Name:
				return _set
				
		# not found
		if not quiet:
			moBuLogger.infoDialog("No set found with name '%s'" % name)
		return False
		
	def findSetFromObject(self, pObject='', quiet=False):
		''' finds the set that an object is in
			Params:
				pObject: object to look for
				quiet: suppress dialogs
			Returns: FBSet/False
		'''
		# get all sets
		allSets = self.scene.Sets
		
		# check for string
		if isinstance(pObject, str):
			pObject = self.getObject(name=pObject, pyMB=False, exact=False, quiet=quiet)
			if not pObject:
				if not quiet:
					moBuLogger.infoDialog("No valid object passed.")
				return False
		
		if not allSets:
			if not quiet:
				moBuLogger.infoDialog("No sets found in scene.")
			return False

		# check sets
		for _set in allSets:
			if self.isInSet(pObject=pObject, pSet=_set):
				moBuLogger.info("Found '%s' in set '%s'" % (pObject.Name, _set.Name))
				return _set
		
		# not found
		if not quiet:
			moBuLogger.infoDialog("'%s' not found in any sets" % pObject.Name)
		return False
	
	def deleteAllInSet(self, setName='', quiet=False):
		''' deletes all items in passed set name
			Params:
				setName: name of set
				quiet: suppress dialogs
			Returns: True/False
		'''
		mySet = self.findSet(name=setName, quiet=quiet)
		if not mySet:
			moBuLogger.warning("Could not find Set %s" % setName)
			return False
		if len(mySet.Items) == 0:
			moBuLogger.warning("No items in Set %s" % setName)
			return False
		success = self.deleteAll(mySet.Items)
		
		# delete set itself
		mySet.FBDelete()
		
		return success
	
	def isInSet(self, pObject='', pSet=''):
		''' see if object is in set
			Params:
				pObject: object to look for
				pSet: set to look in
			Returns: True/False
		'''			
		if not isinstance(pSet, FBSet):
			moBuLogger.error("'%s' is not of type(set)" % pSet)
			return False
		if not pObject:
			moBuLogger.error("No pObject passed.")
		
		# check if pObject is str
		if isinstance(pObject, str):
			#check directly
			for item in pSet.Items:
				if item.Name == pObject:
					moBuLogger.info("Found '%s' in '%s'" % (item.Name, pSet.Name))
					return True
		else:
			#check directly
			for item in pSet.Items:
				if item == pObject:
					moBuLogger.info("Found '%s' in '%s'" % (item.Name, pSet.Name))
					return True 
		
		# not found
		if isinstance(pObject, str):
			pObjectName = pObject
		else:
			pObjectName = pObject.LongName
		moBuLogger.info("Did not find '%s' in '%s'" % (pObjectName, pSet.Name))
		return False
	
	
mbSets = MoBuSets()
	
print "moBu.moBuSets imported" 
