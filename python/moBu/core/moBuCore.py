'''
Author: Jason.Parks
Created: Apr 22, 2012
Module: moBu.core.moBuCore
Purpose: main utility functions for MotionBuilder
'''

from common.core import globalVariables as gv
from common.diagnostic.decorators import deprecated
from common.diagnostic.pcsLogger import moBuLogger
from common.fileIO.parser_schema import ParseSchema
from common.fileIO.pcsPath import Path
from os import listdir, remove, rmdir
from os.path import exists, isfile
from pyfbsdk import *
from pymobu import * #@UnusedWildImport
from unbind import UnboundWrapperError #@UnresolvedImport
import os
import re #@Reimport
import time

schemaObj = ParseSchema(mobu=1)

# eclipseSyntax
if False: from pyfbsdk_gen_doc import * #@UnusedWildImport

regex = re.compile(r'^(-?\d+)(\d{3})')

class MoBu(object):
	"""
	Super class and foundational MotionBuilder utility library
	"""
	
	def __init__(self):
		""" MoBu.__init__():  set initial parameters """
		super(MoBu, self).__init__()

		#MoBu info
		self.mobuVer = self.moBuVersion()		# has to be first, 'cause it is read in other methods
		
		# make app attr
		# Create global objects needed for our work...
		self.app = FBApplication()
		self.system = FBSystem()
		self.scene = FBSystem().Scene
		self.player = FBPlayerControl()
		
#		if self.pcsParseObj.isp4Active:
#			self.p4 = pcsP4.P4Lib()
#			self.p4 = pcsP4.P4Lib(maya=False) #TODO: Causes crash on this line 'from perforce.p426.win64.P4 import P4'
	
	
	@property
	def teamA(self):
		''' Property, do not use ()'''
		return gv.teamA
	
	@property
	def teamB(self):
		''' Property, do not use ()'''
		return gv.teamB
		
	@property
	def sceneName(self):
		''' Property, do not use ()'''
		name = Path(self.app.FBXFileName).makePretty()
		if name == '': name = 'Untitled'
		return name
	
	def evaluate(self):
		self.scene.Evaluate()
		
	def getObject(self, name, pyMB=False, exact=False, quiet=False):
		''' gets FBObject or PMBObject
			Params:
				name: string name of object
				pyMB: return PMBObject type
				exact: if true search namespace as well
				quiet: if true does not warn when object doesn't exist
			Returns: FBObject/PMBObject
		'''
		if not isinstance(name, str):
			moBuLogger.debug("MoBu.getObject() was passed '%s'" % name)
			# probably already an object
			if pyMB:
				if not isinstance(name, PMBModel):
					pModel = name.ConvertToPyMoBu()
					return pModel
			return name
			
		pModel = FBFindModelByName(name)
		exactWord = ''
		if exact:
			# Need to find EXACT name
			pModel = FBFindModelByLabelName(name)
			exactWord = 'exact '

		# convert to PMBModel?
		if pModel:
			if pyMB:
				if not isinstance(pModel, PMBModel):
					pModel = pModel.ConvertToPyMoBu()
			return pModel
		
		if not quiet:
			moBuLogger.warning("Could not find object with %sname '%s'" % (exactWord, name))
		return None
	
	def getObjectFromWildcardName(self, pattern, byName=True, returnLongNames=False, byType=False):
		''' Searches through scene via pattern and returns single object/name
			Params:
				pattern: search pattern
				byName: if False, search by Namespace
				returnLongNames: return names instead of objects
				byType: pass in type to filter by FBObject type
			Returns: object or name
		'''
		listOfObjects = self.getObjectsFromWildcardName(pattern, byName, returnLongNames)
		if listOfObjects:
			# cull by type
			if byType:
				modifiedReturnList = []
				for node in listOfObjects:
					if isinstance(node, byType):
						modifiedReturnList.append(node)
				listOfObjects = modifiedReturnList
			if len(listOfObjects) > 0:
				return listOfObjects[0]
			else:
				return []
		else:
			return []
		
	def getObjectsFromWildcardName(self, pattern, byName=True, returnLongNames=False, byType=False):
		''' Searches through scene via pattern
			Params:
				pattern: search pattern
				byName: if False, search by Namespace
				returnLongNames: return names instead of objects
				byType: pass in type to filter by FBObject type
			Returns: [list] of objects or names
		'''
		SEARCH_INCLUDE_NAMESPACE = True
		SEARCH_ALL_OBJECTS = False		 
		cl = FBComponentList()
		returnList = []	
		if byName:
			FBFindObjectsByName(pattern, cl, SEARCH_INCLUDE_NAMESPACE, SEARCH_ALL_OBJECTS)
		else:
			FBFindObjectsByNamespace(pattern, cl)		
		if len(cl) > 0:
			for _object in cl:
				if returnLongNames:
					returnList.append(_object.LongName)
				else:
					returnList.append(_object)
		# check type
		if byType:
			modifiedReturnList = []
			for node in returnList:
				if isinstance(node, byType):
					modifiedReturnList.append(node)
			returnList = modifiedReturnList
		return returnList
			
	def moBuVersion(self, stringFloat='float'):
		appPath = FBSystem().ApplicationPath
		if len(appPath) > 2:
			appName = appPath.split('\\')[3]
			if len(appName) > 0:
				appNum = float(appName.split(' ')[1])
				if stringFloat == 'string': appNum = str(appNum)
		else:
			return 0
		
		return appNum

	def moBuBitVersion(self):
		appPath = FBSystem().ApplicationPath
		if len(appPath) > 4:
			bit = appPath.split('\\')[5]
		else:
			return 'unknown'
		
		return bit
	
	def validate(self, pModel, _type, pyMB=None):
		''' checks for object type and returns True/false
			Params:
				pModel: model object to check
				_type: object type to check against
				pyMB: is 'OK' if pyMoBu object type
			Returns: True/False
		'''
		# check for string accidentally passed as pModel
		if isinstance(pModel, str):
			# string was passed, get object
			pModel = self.getObject(pModel)
			
		# not string type	
		if isinstance(pModel, _type):
			return True
		elif pyMB and isinstance(pModel, PMBModel) and isinstance(pModel.component, _type):
			return True
		else:
			moBuLogger.warning("Object '%s' not of type '%s'" % (pModel, _type))
			return False
		
class MoBuSceneCore(MoBu):
	
	def __init__(self):
		""" MoBuSceneCore.__init__():  set initial parameters """
		super(MoBuSceneCore, self).__init__()
	
	def deleteAll(self, pObjects=[]):
		''' deletes all objects passed in the list
			Params:
				pObjects: list of FBObjects
			Returns: True/False
		'''
		success = True
		
		# try selected if nothing passed
		if len(pObjects) == 0:
			pObjects = self.getSelected(_type='all', found=False)
			if len(pObjects) == 0:
				moBuLogger.warning("Must pass list or have something selected.")
				return False
		
		# covert to python list from FBPropertyListComponent
		pObjectsList = []
		if isinstance(pObjects, FBPropertyListComponent):
			for obj in pObjects:
				pObjectsList.append(obj)
		else:
			pObjectsList = pObjects
		
		# cull FBModelSkeleton type out to delete last
		deleteList = []
		modelSkels = []
		for _object in pObjectsList:
			if not isinstance(_object, FBModelSkeleton):
				deleteList.append(_object)
			else:
				modelSkels.append(_object)
		
		
		# delete everything but FBModelSkeletons
		count = 0
		for obj in deleteList:
			
			try:
				# stupid list and unbound, have to test
				try:
					name = obj.Name	# have to store before deleting
					obj.FBDelete()
					moBuLogger.debug("Deleted: %s" % name)
					count += 1
				except UnboundWrapperError:
					moBuLogger.debug("%s already deleted, skipping." % name)
			except:
				moBuLogger.debug("Failed to delete: %s" % name)
				success = False
		
		##WARNING!! Must delete other objects BEFORE
		##deleting FBModelSkeletons via children first

		# destroy FBModelSkeleton from hier up
		for modelSkel in modelSkels:
			try:
				# stupid list and unbound, have to test
				try:
					name = modelSkel.Name	# have to store before deleting
					modelSkel.FBDelete()
					moBuLogger.debug("Deleted: %s" % name)
					count += 1
				except UnboundWrapperError:
					moBuLogger.debug("%s already deleted, skipping." % name)
			except:
				moBuLogger.debug("Failed to delete: %s" % name)
				success = False
		
		moBuLogger.info("Deleted '%d' objects" % count)
		
		# clean
		del(pObjectsList, pObjects)
			
		return success
	
	def findAnimationNode(self, pParent, pName):
		''' search child Nodes for pName
		Params:
			pParent: animation node to search through children
			pName: name of child node to look for
		Returns: child animation node
		'''
		lResult = None
		for lNode in pParent.Nodes:
			if lNode.Name == pName:
				lResult = lNode
				break
		return lResult

	def getAllByType(self, _type='all'):
		''' return list[] of everything in scene of specific type
		Params:
			#_type: passed FBobject type
			_type: passed FBObject type as a str
			found: [list] of objects of type
		'''
		# check for str(_type)
		if not isinstance(_type, str):
			moBuLogger.error("_type arg must be type(str) now.")
			
		allComps = FBSystem().Scene.Components
		pObjects = []
		for comp in allComps:
			if _type == 'all':
				
				# skip __SYSTEM objects
				if '__SYSTEM' in comp.LongName:
					continue
				
				# skip animationLayers
				if comp.ClassName() == 'FBBox':
					if "Anim" in comp.Name:
						continue
				
				# skip if type(FBBox), BaseAnimation
				if isinstance(comp, FBBox) and ('BaseAnimation' in comp.Name or 'AnimLayer1' in comp.LongName):
					continue
				
				# skip if type(FBModel), 'ActorBodyBone' and 'ActorBodyMesh'
				if isinstance(comp, FBModel) and ('ActorBodyBone' in comp.LongName or 'ActorBodyMesh' in comp.LongName):
					continue
				
				# skip if type(FBModel), 'Motion Blend Result'
				if isinstance(comp, FBModel) and 'Motion Blend Result' in comp.Name:
					continue
				
				pObjects.append(comp)
				
				
			elif _type == comp.ClassName():
				pObjects.append(comp)
			moBuLogger.debug("Adding %s  <---type	 %s  <--LongName" % (comp.ClassName(), comp.LongName))
			
		return pObjects
	
	def getAllRefNodes(self):
		''' find all reference nodes in the scene
		Params: n/a
		Returns: [list] of ref nodes
		'''
		refNodes = []
#		allJoints = self.getAllByType(_type='FBModelSkeleton')
		allNulls = self.getAllByType(_type='FBModelNull')
		for joint in allNulls:
			if re.search(schemaObj.getWellFormed('moBuRoot'), joint.Name):
				# double check for no parent
				if not joint.Parent:
					refNodes.append(joint)
			
		return refNodes
	
	def getCharacter(self, hipsJoint='', nSpace=''):
		''' gets FBCharacter object by searching through
			hips joints
		Params:
			hipsJoint: name of hips joint from character
			nSpace: nameSpace of character to look for
		Returns: FBCharacter/False
		'''
		allCharacters = FBSystem().Scene.Characters
		for pChar in allCharacters:
			hips = pChar.GetModel(FBBodyNodeId.kFBHipsNodeId)
			if hips:
				if hipsJoint:
					if not self.validate(hipsJoint, FBModelSkeleton, pyMB='OK'):
						hipsJoint = self.getObject(hipsJoint)
					hipsLongName = None
					if isinstance(hipsJoint, PMBModel) or isinstance(hipsJoint, str):
						hipsLongName = str(hipsJoint)
					else:
						hipsLongName = hipsJoint.LongName
					if hips.LongName == hipsLongName:
						return pChar
				else:
					# first check namespaces
					if nSpace:
						if nSpace in hips.LongName:
							return pChar
					else:
						# if no joint passed, just return first character
						return pChar
		return False
	
	def getHierarchy (self, pModel, pList=[], strings=False, pyMB=False):
		''' returns list of FBObjects
		Params:
			pModel: hierarchy under this object
			pList: alternate list to append to
			string: return model.Name
			pyMB: return PyMB objects, overrides 'strings' arg
		Returns: [list]
		'''
		if len(pList) == 0:
			# reset
			pList = []
		if pModel:
			# ensure FBObject type
			if isinstance(pModel, str):
				pModel = self.getObject(pModel)
			
			#add to list
			if pyMB:
				if not isinstance(pModel, PMBModel):
					pList.append(pModel.ConvertToPyMoBu())
				else:
					pList.append(pModel)
			elif strings:
				pList.append(pModel.Name)
			else: pList.append(pModel)
			
			# traverse down the hierarchy
			for lChild in pModel.Children:
				self.getHierarchy(lChild, pList, strings, pyMB)
			else:
				return pList
	
	def getReference(self, namespace='', pyMB=False):
		''' Returns reference node in form of PMBModel
		Params:
			namespace: namespace to search reference node for
			pyMB: return PMBModel type
		Returns: FBModel or PMBModel
		'''
		refNode = schemaObj.getWellFormed('moBuRoot')
		if namespace:
			refNode = '%s:%s' % (namespace, refNode)
		pymbModel = self.getObject(name=refNode, pyMB=pyMB, exact=True, quiet=False)
		return pymbModel
	
	def getSelected(self, _type='all', found=False):
		''' return list[] of everything selected in scene
		Params:
			_type: passed FBobject type
			found: returns first object type if found
		Returns: [list], single object if found=True, False
		'''
		results = []
		
		for comp in self.scene.Components:
			if _type == 'all':
				if True == comp.Selected:
					# skip AnimLayers
					# use ClassName to get exact class, no sub-classes
					if comp.ClassName() == 'FBBox':
						if "Anim" in comp.Name:
							continue
					results.append(comp)
					if found:
						return comp 
			else:
				if isinstance(comp, _type):
					if True == comp.Selected:
						# skip AnimLayers
						# use ClassName to get exact class, no sub-classes
						if comp.ClassName() == 'FBBox':
							if "Anim" in comp.Name:
								continue
						results.append(comp)
						if found:
							return comp
		
		if len(results) == 0:
			results = False
			
		return results
		
	def getSelectedModels(self, _type='all', found=False):
		''' return list[] of every FBMOdel selected in scene
		Params:
			_type: passed FBobject type
			found: returns first object type if found
		Returns: [list], single object if found=True, False
		'''
		results = []
		selectedModels = FBModelList()
		FBGetSelectedModels (selectedModels, None, True)
		for pModel in selectedModels:
			if _type == 'all':
				results.append(pModel)
				if found:
					return pModel 
			else:
				if isinstance(pModel, _type):
					results.append(pModel)
					if found:
						return pModel
		
		if len(results) == 0:
			results = False
		
		return results

	def getSelectedCharacters(self):
		''' returns list of selected FBCharacter objects
		Params:
			None
		Returns: [list]
		'''
		pList = []
		lScene = FBSystem().Scene
		charactersList = lScene.Characters
		for character in charactersList:
			if character.Selected:
				moBuLogger.debug("%s is selected" % character.Name)
				pList.append (character)
		return pList
			
	def localRotationAxisToggle(self, pModel='', size=25):
		modelList = []
		#work on everything selected
		selected = self.getSelected()
		if selected:
			modelList = selected 
		else:
			modelList = [pModel]
		if len(modelList) == 1 and modelList[0] == '':
			moBuLogger.info("Nothing selected or passed to function localRotationAxisToggle()")
			return
		
		for pModel in modelList:
#			pModel = self.validate(pModel, FBModelSkeleton)
			if not self.validate(pModel, FBModelSkeleton):
				moBuLogger.error("'%s' is not type FBModelSkeleton" % pModel)
			pModel = self.getObject(pModel, pyMB=True)
			if pModel:
				vis = True
				if pModel.GetPropertyValue('Show Rotation Axis'):
					vis = False
				
				pModel.SetPropertyValue('Show Rotation Axis', vis)
				pModel.SetPropertyValue('Pivot Visibility', 2)
				pModel.SetPropertyValue('Pivot Size', size)
		
		# for unitTests
		return True
	#			if MoBuUtilCore().getProperty(pModel, 'Show Rotation Axis'):
	#				vis = False
	#			
	#			if pModel:
	#				MoBuUtilCore().setProperty(pModel, 'Show Rotation Axis', vis)
	#				MoBuUtilCore().setProperty(pModel, 'Pivot Visibility', 2)
	#				MoBuUtilCore().setProperty(pModel, 'Pivot Size', 25)

	def returnNameList (self, pList):
		nameList = []
		for item in pList:
			nameList.append (item.Name)
		return nameList
	
	def returnUnselected (self, _type=''):
		''' find all un-selected models
		Params:
			_type: return only unselected of this type
		Returns: [list] of unselected models (of type)
		'''
		lResults = []
		lModels = FBModelList()
		#FBGetSelectedModels (,,False) means all unselected models
		FBGetSelectedModels (lModels, None, False)
		for pModel in lModels:
			if _type:
				if isinstance(pModel, _type):
					lResults.append(pModel)
			else:
				lResults.append(pModel)
		return lResults

#	@deprecated("Please use mbCore.returnUnselected(_type=pType)")
#	def GetUnSelectedType (self, pType):
#		lResults = []
#		lModels = FBModelList()
#		#FBGetSelectedModels (,,False) means all unselected models
#		FBGetSelectedModels (lModels, None, False)
#		for lModel in lModels:
#			if lModel.ClassName() == pType:
#				lResults.append(lModel)
#		return lResults
	
#	@deprecated("Please use mbCore.getAllByType(_type=pType)")
#	def ReturnAllModelsByType (self, pType):
#		lResults = []
#		lModels = FBModelList()
#		#FBGetSelectedModels (,,False) means all unselected models
#		FBGetSelectedModels (lModels, None, False)
#		for lModel in lModels:
#			if lModel.ClassName() == pType:
#				lResults.append(lModel)
#		return lResults
	
	def ReturnAllNamesByType (self, pType):
		lResults = []
		lModels = FBModelList()
		#FBGetSelectedModels (,,False) means all unselected models
		FBGetSelectedModels (lModels, None, False)
		for lModel in lModels:
			if lModel.ClassName() == pType:
				lResults.append(lModel.Name)
		return lResults
	
	@property
	def selected(self):
		''' property, don't use ()
			if want to pass args, use getSelected() '''
		self.getSelected(_type='all', found=False)
		
	def GetType (self, pModel):
		return pModel.ClassName()
	
	def GetTopNodeOfHierarchy (self, pModel):
		if not pModel:
			return None
		if pModel.Parent:
			return self.GetTopNodeOfHierarchy (pModel.Parent)
		else:
			return pModel
	
	def GetTopJointOfHierarchy (self, pModel):
		if pModel.Parent:
			if pModel.Parent.ClassName() == "FBModelSkeleton":
				return self.GetTopJointOfHierarchy (pModel.Parent)
			else:
				return pModel
		else:
			return pModel

#TODO: Move to moBuAnimation	
class MoBuAnimationCore(MoBu):

	def __init__(self):
		""" MoBuAnimationCore.__init__():  set initial parameters """
		super(MoBuAnimationCore, self).__init__()

	def checkForValues(self, pModel):
		#Check the values on the Reference node
		nonZero = 0
		pymbModel = self.getObject(pModel, pyMB=True, quiet=True)
		if pymbModel:
			trans = pymbModel.GetTranslation()
			rot = pymbModel.GetRotation()
			moBuLogger.debug("'%s' trans='%s', rot='%s'" % (pymbModel, trans, rot))
			if  trans[0] != 0 or trans[1] != 0 or trans[2] != 0 or rot[0] != 0 or rot[1] != 0 or rot[2] != 0:
				nonZero = 1
		return nonZero
	
	def clearAnimCurve(self, pAnimNode):
		''' Clears curves from passed FBAnimationNode
		Params:
			pAnimNode: FBAnimationNode to clear curves with
		Returns: True/False
		'''
		if not isinstance(pAnimNode, FBAnimationNode):
			moBuLogger.error("Was not passed FBAnimationNode object: '%s'" % pAnimNode)
		if not len(pAnimNode.Nodes) == 3:
			moBuLogger.warning("No subAnimNodes found on: '%s'" % pAnimNode)
		else:
			pAnimNode.Nodes[0].FCurve.EditClear()
			pAnimNode.Nodes[1].FCurve.EditClear()
			pAnimNode.Nodes[2].FCurve.EditClear()
			return True
		
		return False

	def cleanTakes(self, takeNames=['Take 001'], pTakeToKeep=''):
		''' will remove standard non-needed takes 'Take 001', 'Characterization'
		Params:
			takeNames: [list] of takes to remove
			pTakeToKeep: take object/name to keep, delete others
		Returns: [list] take names deleted
		'''
		deletedTakeNames = []
		pTakes = []
		takesToDelete = []
		
		# check takeNames are for list
		if not isinstance(takeNames, list):
			moBuLogger.error("mbCore.cleanTakes() expects 'list' type arg for 'takeNames'")

		if pTakeToKeep:
			takeNames[0] = 'all'
			# check for str
			if isinstance(pTakeToKeep, str):
				pTakeToKeep = self.getTakeFromName(pTakeToKeep)
		
		# get all takes
		if takeNames[0] == 'all':
			pTakes = FBSystem().Scene.Takes
		else:
			for takeName in takeNames:
				if isinstance(takeName, str):
					# convert to FBPropertyListTake
					pTakes.append(self.getTakeFromName(takeName))
				else:
					# just in case FBTake objects were passed
					pTakes.append(takeName)
		# clean takeNames
		del(takeNames)
			
		# delete takes added to list
		if pTakes:
			for pTake in pTakes:
				if not pTake == pTakeToKeep:
					takesToDelete.append(pTake)
			# perform deletion
			for takeToDelete in takesToDelete:
				deletedTakeName = self.deleteTake(takeToDelete)
				if deletedTakeName:
					deletedTakeNames.append(deletedTakeName)
				
		return deletedTakeNames
		
	def deleteTake(self, pTake):
		''' delete take and validate
		Params:
			pTake: FBTake object or name
		Returns: name of Take deleted
		'''
		# check for str
		if isinstance(pTake, str):
			pTake = self.getTakeFromName(pTake)
		if pTake:
			takeName = pTake.Name
			pTake.FBDelete()
			return takeName
		else:
			return None
	
	def getFrame(self):
		return self.system.LocalTime.GetFrame(True)
			
	@deprecated("Un-reliable take order")
	def getLastTake(self):
		''' does not work because listTakes does not return Takes in correct order in scene '''
		# have to use self.listTakeNames because cannot do len() on FBPropertyListTake
		allTakes = self.listTakeNames()
		if not allTakes:
			return None
		numTakes = len(allTakes)
		lastTake = allTakes[numTakes - 1]
		for pTake in FBSystem().Scene.Takes:
			if pTake.Name == lastTake:
				moBuLogger.debug(pTake.Name)
				return pTake
	
	def getTakeFromName(self, takeName):
		for pTake in FBSystem().Scene.Takes:
			if pTake.Name == takeName:
				return pTake
	
	def getTimeInt(self, time):
		''' gets frame of time in integer format
		Params:
			time: FBTime object
		Returns: frame (int)
		'''
		
		strTime = time.GetTimeString()
		
		if '*' in strTime:
			strTime = strTime[:-1]
			moBuLogger.warning("Sub frame (%s*) found in FBTime object: %s" % (strTime, time))
		
		# convert to int
		intTime = int(strTime)
		
		return intTime
	
	@deprecated("Please use PMBModel().GetTranslate()")
	def getVectorTranslate(self, pModel):
		pModel = self.validate(pModel)
#		if isinstance(pObject, str):
#			pObject = mbCore.returnObject(pObject) 
		vPosition = FBVector3d()
		pModel.GetVector (vPosition, FBModelTransformationMatrix.kModelTranslation)
		return vPosition
	
	def gotoFrame(self, frame=0):
		FBPlayerControl().Goto(FBTime (0, 0, 0, frame))
		FBPlayerControl().LoopStart = (FBTime (0, 0, 0, frame))
		FBSystem().Scene.Evaluate()
		
	def hasAnimCurves(self, pModel, axis='x', transform='T'):
		''' made to work on FBModelSkeleton, only 1 axis checking at a time
			Params:
				pModel: FBModel object to check
				axis: Axis to examine
				transform: transformation type to examine
			Returns: True/False
		'''
		pModel = self.getObject(pModel)
		
		# convert axis to index
		index = 0
		if axis.lower() == 'y':
			index = 1
		elif axis.lower() == 'z':
			index = 2
		
		animNode = None
		if transform == 'T':
			if isinstance(pModel, PMBModel):
				animNode = pModel.GetAnimationNode()
			else:
				animNode = pModel.Translation.GetAnimationNode()
			if animNode and animNode.Nodes[index].IsKey():
				return True
		elif transform == 'R':
			if isinstance(pModel, PMBModel):
				animNode = pModel.GetAnimationNode('Rotation')
			else:
				animNode = pModel.Rotation.GetAnimationNode()
			if animNode and animNode.Nodes[index].IsKey():
				return True
		elif transform == 'S':
			if isinstance(pModel, PMBModel):
				animNode = pModel.GetAnimationNode('Scale')
			else:
				animNode = pModel.Scale.GetAnimationNode()
			if animNode and animNode.Nodes[index].IsKey():
				return True
		return False
			
	def listTakes(self):
		''' Must be a FBPropertyListTake type object '''
		return FBSystem().Scene.Takes
	
	def listTakeNames(self):
		''' prints and returns list of all Takes in scene
		Params: n/a
		Returns: [list] of take names
		'''
		takeNames = []
		allTakes = self.listTakes()
		for pTake in allTakes:
			if not pTake.Name == "None":
				takeNames.append(pTake.Name)
				moBuLogger.debug(pTake.Name)
		return takeNames

	def listTakeNamesFromFile(self, targetFilePath):
		''' prints and returns list of all Takes from a file
		Params:
			targetFilePath: file to get take names from 
		Returns: [list] of take names
		'''
		takeNames = []
		if not os.path.exists(targetFilePath):
			moBuLogger.error("'%s' does not exist")
		pFbxOptionsLoad = FBFbxOptions(1, targetFilePath)
		for idx in range(0, pFbxOptionsLoad.GetTakeCount()):
			moBuLogger.info(pFbxOptionsLoad.GetTakeName(idx))
			takeNames.append(pFbxOptionsLoad.GetTakeName(idx))
		return takeNames

	def moveAnimCurve(self, pModel, trans=True, rot=None, scale=None, x=None, y=None, z=None, _all=False):
		''' made to work on FBModelSkeleton, FBModelRoot
			default will move curves so first frame of curve is 0
			TODO: if int passed to an axis, will move curve so first frame
			of curve is passed int
		Params:
			
		Returns: True if moved a Key
		'''
		
		indexes = []
		if _all:
			x, y, z, = True, True, True
		
		moved = False
		
		pModel = self.getObject(pModel)
		
		# Translation
		if x:
			# validate has a curve
			if self.hasAnimCurves(pModel, 'x'):
				indexes.append(0)
				moBuLogger.info("Moved animCurve '%s.Translation.X' to 0 at frame 0" % pModel.Name)
		if y:
			if self.hasAnimCurves(pModel, 'y'):
				indexes.append(1)
				moBuLogger.info("Moved animCurve '%s.Translation.Y' to 0 at frame 0" % pModel.Name)
		if z:
			if self.hasAnimCurves(pModel, 'z'):
				indexes.append(2)
				moBuLogger.info("Moved animCurve '%s.Translation.Z' to 0 at frame 0" % pModel.Name)
		
		for axis in indexes:
			transAnimNode = None
			if isinstance(pModel, PMBModel):
				transAnimNode = pModel.GetAnimationNode()
			else:
				transAnimNode = pModel.Translation.GetAnimationNode()
			if transAnimNode.Nodes[axis].FCurve:
				if transAnimNode.Nodes[axis].FCurve.Keys:
					fFirstValAxis = transAnimNode.Nodes[axis].FCurve.Keys[0].Value
					for key in transAnimNode.Nodes[axis].FCurve.Keys:
						fKeyVal = key.Value 
						key.Value = (fKeyVal - fFirstValAxis)
						moved = True
		
		#TODO: rot and scale	
		# Rotation
		indexes = None
		if x:
			# validate has a curve
			if self.hasAnimCurves(pModel, 'x', 'R'):
				indexes = 0
				
		# Scale
		
		# for unitTests
		return moved
	
	def plotCharacter(self, character=None, nSpace='', quiet=False):
		''' plots character
				Params:
					character: passed FBCharacter object
					nSpace: namespace to search for character
					quiet: suppress message
				Returns: True/False
			'''
		if not character:
			if nSpace:
				character = MoBuSceneCore().getCharacter(hipsJoint='', nSpace=nSpace)
		
		lOptions = self.SetPlotOptions()
		lOptions.PlotTranslationOnRootOnly = True
#		lOptions.PreciseTimeDiscontinuities = True	#?
		
		if character.ActiveInput:
			if quiet:
				# default to choice 1, plot & continue
				character.PlotAnimation(FBCharacterPlotWhere.kFBCharacterPlotOnSkeleton, lOptions)
				character.ActiveInput = False
			else:
				res = FBMessageBox("Control Set Active", "Warning: Control set on %s is Active.\n\nWhat do you want to do?" % character.LongName, "Plot & Continue", "De-activate & Continue", "Cancel", 1, 1)
				if res == 1:
					character.PlotAnimation(FBCharacterPlotWhere.kFBCharacterPlotOnSkeleton, lOptions)
					character.ActiveInput = False
				if res == 2:
					character.ActiveInput = False
				elif res == 3:
					return False
		moBuLogger.info("Plotted to skeleton for character: '%s'" % character.LongName)
		
		return True
					
	def SetPlotOptions (self):
		#set plot options, must create blank character and set options during blank character's plot
		dummyCharacter = FBCharacter("dummyChar") 
		lOptions = FBPlotOptions ()
		lOptions.PlotOnFrame = True
		lOptions.PlotAllTakes = False
		lOptions.PlotPeriod = FBTime (0, 0, 0, 1)
		lOptions.RotationFilterToApply = FBRotationFilter.kFBRotationFilterNone
		lOptions.UseConstantKeyReducer = False
		lOptions.ConstantKeyReducerKeepOneKey = False
		lOptions.PlotTranslationOnRootOnly = False
		lOptions.PreciseTimeDiscontinuities = False
		dummyCharacter.PlotAnimation (FBCharacterPlotWhere.kFBCharacterPlotOnSkeleton, lOptions)
		dummyCharacter.FBDelete()
		
		return lOptions
	
	def zeroTimeline(self, character=None):
		''' moves timeline to zero with character animation
			Params:
				character: FBcharacterNode
			Returns: True/False
		'''
		
		# find start of current take
		currentTake = FBSystem().CurrentTake
		currentTimeSpan = currentTake.LocalTimeSpan
		currentTakeStartTimeInt = int(currentTimeSpan.GetStart().GetTimeString())
		
		# check timeline
		if currentTakeStartTimeInt == 0:
			# abort
			moBuLogger.warning("No need to run zeroTimeline, first frame is already 0.")
			return False
		
		# find stop and offset
		currentTakeStopTimeInt = int(currentTimeSpan.GetStop().GetTimeString())
		offset = FBTime(0, 0, 0, -1 * currentTakeStartTimeInt)
		
		# create track
		lTrackContainer = FBStoryTrack(FBStoryTrackType.kFBStoryTrackCharacter)
#		lTrackContainer = FBStoryTrack(FBStoryTrackType.kFBStoryTrackAnimation)

		# find character		
		if not character:
			character = MoBuSceneCore().getCharacter(hipsJoint='')
		if not character:
			moBuLogger.error("Failed to find character.")
		
		# plot to control rig		
		if not character.GetCurrentControlSet():
			character.CreateControlRig(True) 
		character.PlotAnimation(FBCharacterPlotWhere.kFBCharacterPlotOnControlRig, self.SetPlotOptions())
		
		# assign character to track
		lTrackContainer.Character = character
		
		# create clip, and offset it
		lTrackContainer.CopyTakeIntoTrack(currentTimeSpan, currentTake, offset)
		
		# move timeline
		newTimeSpan = FBTimeSpan()
		newTimeSpan.Set(FBTime(0, 0, 0, 0), FBTime(0, 0, 0, currentTakeStopTimeInt - currentTakeStartTimeInt))
		currentTake.LocalTimeSpan = newTimeSpan
		
		# plot back down
		self.plotCharacter(character=character, nSpace='', quiet=True)
		
		# nuke story track
		lTrackContainer.FBDelete()
		
		moBuLogger.info("Zeroed-out timeline.")
		
		return True
	
class MoBuUtilCore(MoBu):
	
	def __init__(self):
		""" MoBuUtilCore.__init__():  set initial parameters """
		super(MoBuUtilCore, self).__init__()
	
	def allNodesByClassName(self):
		allComps = FBSystem().Scene.Components
		for node in allComps:
			moBuLogger.info("%s  <---type	 %s  <--LongName" % (node.ClassName(), node.LongName))
		
		return allComps
	
	def createNote(self, name='', content='', attach=''):
		''' BUG: HAVE to assign result to variable!
			create FBNote
			Params:
				name: name of note
				content: content of note
			Returns: FBNote/False
		'''
		# see if note already exists
		ourNote = self.getObjectFromWildcardName(pattern=name, byName=True, returnLongNames=False, byType=FBNote)
		if ourNote:
			moBuLogger.info("Found existing FBNote: '%s'" % name)
			ourNote.StaticComment = content
			moBuLogger.info("Updating content to: '%s'" % content)
		else:
			ourNote = FBNote(name)
			moBuLogger.info("Creating new FBNote: '%s'" % name)
			ourNote.StaticComment = content
			moBuLogger.info("Setting content to: '%s'" % content)
		
		# add to scene
		if attach:
			result = ourNote.Attach(attach)
		else:
			result = ourNote.Attach()
		if not result:
			return False
		
		return ourNote
			
	def deleteCharacter(self, character):
		pass
	
	def deleteNote(self, nameOrFBNote=''):
		''' delete FBNote
		Params:
			nameOrFBNote: name of note OR FBNote object
		Returns: True/False
		'''
		if isinstance(nameOrFBNote, FBNote):
			ourNote = nameOrFBNote
		else:
			ourNote = self.getObjectFromWildcardName(pattern=nameOrFBNote, byName=True, returnLongNames=False, byType=FBNote)
			if not ourNote:
				moBuLogger.error("Could not find FBNote: '%s'" % nameOrFBNote)
				return False
		
		try:
			# detach?
			#ourNode.Detach()
			ourNote.FBDelete()
			return True
		except:
			moBuLogger.error("Failed to delete FBNote: '%s'" % nameOrFBNote)
			return False

	
	def getDirectoryList(self, defaultFolder, captionTitle='FolderSelect', returnList=1):
		"""
		SYNOPSIS
		  Return list of files from selected directory or just directory path
		
		INPUTS
		 (string) defaultFolder:	default directory path
		 (string) captionTitle:		Window title
		 (bool) returnList:			1 = returnList of files in folder, 0 = return folderName
	
		RETURNS: (string) path
					or
				(list) [path, files]
		"""
		
		#Get folder from current scene
		fullFileName = FBApplication().FBXFileName.replace('\\', '/')
		
		text = "Current Scene w/ path is: %s" % fullFileName
		moBuLogger.info(text)
		
		pathParts = fullFileName.split('/')
		fileNameOnly = pathParts[len(pathParts) - 1]
		currentFolder = fullFileName.replace(fileNameOnly, "")
		if not currentFolder: currentFolder = str(ParseSchema(fullFileName).characterRoot)
	
		text = "currentFolder is: %s" % currentFolder
		moBuLogger.info(text)
		
		#Build GUI
		folderWindow = FBFolderPopup()
		folderWindow.Caption = "%s: Select a folder for BatchProcessing" % captionTitle
		
		
		if not defaultFolder: defaultFolder = currentFolder
		folderWindow.Path = str(defaultFolder)
		
		#if window executes
		fileList = []
		if folderWindow.Execute():
			
			#iterate through each file
			fileList = listdir(folderWindow.Path)
		
		#assert(len(fileList)), logger.info('No directory selected')
		if not len(fileList): moBuLogger.info('No directory selected')
		
		if not returnList: return folderWindow.Path.replace('\\', '/')
		return [folderWindow.Path.replace('\\', '/'), fileList]
	
	def getProperty(self, pModel, _property):
		pModel = self.validate(pModel, FBModelSkeleton)
		if pModel:
			pProp = pModel.PropertyList.Find(_property)
			return pProp.Data
		return False
				
	def IntersectionStr (self, listA, listB):
		'''will return common Names from the two lists'''
		'''Note: BOTH must be lists, even if there is only 1 item in the list'''
		result = []
		for x in listA:
			for y in listB:
				if x == y:
					result.append(x)
		return result			
	
	def IntersectionObj (self, listA, listB):
		'''will return common Names from the two lists'''
		'''Note: BOTH must be lists, even if there is only 1 item in the list'''
		result = []
		for x in listA:
			for y in listB:
				if x.Name == y.Name:
					result.append(x)
		return result			
	
	def ExclusionStr (self, listA, listB):
		'''will return uncommon *names* from the two lists'''
		result = []
		intersect = self.IntersectionStr(listA, listB)
		#check listA against common
		for x in listA:
			both = 0
			for y in intersect:
				if  x == y:
					both = 1
			if not both:
				result.append(x)
		#check listB against common
		for x in listB:
			both = 0
			for y in intersect:
				if x == y:
					both = 1
			if not both:
				result.append(x)
		#have
		return result
	
	def ExclusionObj (self, listA, listB):
		'''will return uncommon *names* from the two lists'''
		result = []
		intersect = self.IntersectionObj(listA, listB)
		#check listA against common
		for x in listA:
			both = 0
			for y in intersect:
				if x.Name == y.Name:
					both = 1
			if not both:
				result.append(x)
		#check listB against common
		for x in listB:
			both = 0
			for y in intersect:
				if x.Name == y.Name:
					both = 1
			if not both:
				result.append(x)
		#have
		return result
	
	def deselectAll (self):
		self.UnSelectAll()
				
	def UnSelectAll (self):
		selectedModels = FBModelList()
		FBGetSelectedModels (selectedModels, None, True)
		for select in selectedModels:
			select.Selected = False;												#print "unselected: %s" % select.Name
		del (selectedModels)

	def newSuffix (self, sceneName, localPath):
		'''figure out what new suffix should be'''
		nameParts = sceneName.split('_')
		suffix = nameParts[-1];													#print "suffix is:	 " + suffix
		splitSuffix = suffix.split('.')
		realSuffix = splitSuffix[0];												#print "realSuffix is: " + realSuffix
		if realSuffix[0] == "v":
			number = (int(realSuffix[1:]) + 1)
			if number > 9:
				zeros = "0"
			elif number > 99:
				zeros = ""
			else:
				zeros = "00"
			extension = "v" + zeros + str(number)
			newExtension = extension + '.fbx'
			iterSceneName = sceneName.replace(suffix, newExtension)
		else:
			extension = "_v001"	
			newExtension = extension + '.fbx'
			iterSceneName = sceneName.replace('.fbx', newExtension)
	
		#print "iterScenename is: " + iterSceneName
		#check to see if file exists
		localFiles = listdir(localPath)
		for _file in localFiles:
			if iterSceneName == _file:
				iterSceneName = self.newSuffix(iterSceneName, localPath)
		return iterSceneName
	
	def jpGetUser (self):
		count = 0
		userDirs = listdir ("C:\Documents and Settings")
		for userDir in userDirs:
			if not userDir == "registered":
				firstLetter = userDir[:1]
				if firstLetter.islower():
					print "Probably found userDir '%s'" % userDir
					result = userDir
					count += 1
		if count > 1:
			#found more than 1 user, error out
			pass
		return result
	
	def jpClear (self):
		print "cleared."
	
	def cl (self):
		print "cleared"
	
	def DestroyModel(self, pModel):
		# Always destroy from the last children to the first
		while len(pModel.Children) > 0:
			self.DestroyModel(pModel.Children[-1])
		#print "Destroying model: '%s'" % pModel.Name
		pModel.FBDelete()
	
	def jpExportPropertyList (self, _object):
		logFile = '#This is the propertyList for object ' + _object.Name + '\n\n['
	
		propList = _object.PropertyList
		#list properties
		for _property in propList:
			#print character.Name
			#print _property.GetProperty
			if _property.GetName():
				logFile = logFile + _property.GetName()
			if _property.GetPropertyTypeName():
				logFile = logFile + ',' + _property.GetPropertyTypeName() + ']\n['
		
		moBuLogger.info(logFile)
		
#		#save to text file
#		logFilePath = 'C:/temp/' + _object.Name + '_propertyList.txt';									#print "logFilePath is " + logFilePath
#		os.myfile = open(logFilePath, 'w')
##		os.myfile.writelines(logFile)
#		os.myfile.write (logFile)
#		os.myfile.close()
	
	def jpMakePropertyList (self):
		#Intended to work on a selected character
		pList = []	
		self.FBGetSelectedCharacters (pList)
		for character in pList:
			print 'working on character ' + character.Name
			self.jpExportPropertyList (character)
	
	def jpCreateNote (self, variableName, variableValue):
		name = "||Note||" + variableName + "|" + variableValue
		#check for variableName already exists
		allNulls = MoBuSceneCore().getAllByType(_type='FBModelNull')
		for null in allNulls:
			nullName = null.Name
			tokenized = nullName.split('||Note||')
			if len(tokenized) > 1:
				#tokenize again
				results = tokenized[1].split('|')
				if len(results) > 1:
					variableNameExists = results[0]
					if variableNameExists == variableName:
						#already a Note null in scene with variableName, prompt for warning
						newVariable = FBMessageBoxGetUserValue("Custom ||Note|| Null error", ("A ||Note|| null with variable name '%s' already exists\nin this scene. Please enter a new variable name." % variableName), str, FBPopupInputType.kFBPopupString, "Continue")
						name = "||Note||" + newVariable[1] + "|" + variableValue
	
		nullNode = FBModelNull (name)
		nullNode.Visible = False
		return nullNode
	
	def jpReadNote (self, variableName):
		variableValue = "none found"
		#name = "||Note||" + variableName + "|*"
		#must get all the nulls and parse for ||Note||
		allNulls = MoBuSceneCore().getAllByType(_type='FBModelNull')
		for null in allNulls:
			nullName = null.Name
			tokenized = nullName.split('||Note||')
			if len(tokenized) > 1:
				#tokenize again
				results = tokenized[1].split('|')
				if len(results) > 1:
					variableValue = results[1]
	
		return variableValue
	
	def jpGetNote (self, variableName):
		#name = "||Note||" + variableName + "|*"
		#must get all the nulls and parse for ||Note||
		allNulls = MoBuSceneCore().getAllByType(_type='FBModelNull')
		for null in allNulls:
			nullName = null.Name
			tokenized = nullName.split('||Note||')
			if len(tokenized) > 1:
				#tokenize again
				results = tokenized[1].split('|')
				if len(results) > 1:
					thisVariableName = results[0]
					if thisVariableName == variableName:
						#found it
						noteNode = null
		return noteNode
	
	def jpDeleteNote (self, variableName):
		#name = "||Note||" + variableName + "|*"
		#must get all the nulls and parse for ||Note||
		allNulls = MoBuSceneCore().getAllByType(_type='FBModelNull')
		for null in allNulls:
			nullName = null.Name
			tokenized = nullName.split('||Note||')
			#print tokenized
			if len(tokenized) > 1:
				#tokenize again
				results = tokenized[1].split('|')
				if len(results) > 1:
					thisVariableName = results[0]
					if thisVariableName == variableName:
						#found it
						null.FBDelete()
		return 1
	
	def jpRemoveDirsAndFiles (self, path):
		if exists(path):
			#first remove files inside
			files = listdir(path)
			if len(files) > 0:
				for _file in files:
					if isfile(path + "/" + _file):
						remove (path + "/" + _file)
					else:
						try:
							rmdir (path + "/" + _file)
						except:
							self.jpRemoveDirsAndFiles(path + "/" + _file)
			#then remove dir
			rmdir(path)
	
	def jpCommify(self, num, separator=','):
		"""commify(num, separator) -> string
	
		Return a string representing the number num with separator inserted
		for every power of 1000.   Separator defaults to a comma.
		E.g., commify(1234567) -> '1,234,567'
		"""
		num = str(num)  # just in case we were passed a numeric value
		more_to_do = 1
		while more_to_do:
			(num, more_to_do) = regex.subn(r'\1%s\2' % separator, num)
		return num
	
	def readNote(self, nameOrFBNote=''):
		''' read from FBNote
		Params:
			nameOrFBNote: name of note OR FBNote object
		Returns: content/False
		'''
		if isinstance(nameOrFBNote, FBNote):
			ourNote = nameOrFBNote
		else:
			ourNote = self.getObjectFromWildcardName(pattern=nameOrFBNote, byName=True, returnLongNames=False, byType=FBNote)
			if not ourNote:
				moBuLogger.warning("Could not find FBNote: '%s'" % nameOrFBNote)
				return False
		
		content = ourNote.StaticComment
		
		return content
	
	def setProperty(self, pModel, _property, value):
		pModel = self.validate(pModel, FBModelSkeleton)
		pProp = pModel.PropertyList.Find(_property)
		pProp.Data = value
	
	def timetostring(self, timeinseconds):
		"""Return w3 datetime compliant listing of timeinseconds"""
		return time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(timeinseconds))
		
class MoBuExportCore(MoBu):

	def __init__(self):
		""" MoBuExportCore.__init__():  set initial parameters """
		super(MoBuExportCore, self).__init__()

	def checkMappedDrive(self):
		schemaDriveLetter = str(schemaObj.artRoot[0])
		if not self.sceneName[0] == schemaDriveLetter.upper() and not self.sceneName[0] == schemaDriveLetter.lower():
			moBuLogger.warning("Current scene '%s' was not loaded from '%s:' drive" % (self.sceneName, schemaDriveLetter))
			return 0
		else:
			return 1

class MoBuUICore(MoBu):
	
	def __init__(self):
		""" MoBuUICore.__init__():  set initial parameters """
		super(MoBuUICore, self).__init__()
	
	@property
	def Black(self):
		''' Property, do not use ()'''
		return FBColor(0, 0, 0)

	@property
	def Blackish(self):
		''' Property, do not use ()'''
		return FBColor(.1, .1, .1)

	@property
	def Blue(self):
		''' Property, do not use ()'''
		return FBColor(0, 0, 1)
		
	@property
	def DarkGrey(self):
		''' Property, do not use ()'''
		return FBColor(.2, .2, .2)						
		
	@property
	def Grey(self):
		''' Property, do not use ()'''
		return FBColor(.3, .3, .3)						

	@property
	def Green(self):
		''' Property, do not use ()'''
		return FBColor(.3, .8, .3)						

	@property
	def LightBlue(self):
		''' Property, do not use ()'''
		return FBColor(.3, .3, .8)

	@property
	def LightGrey(self):
		''' Property, do not use ()'''
		return FBColor(.5, .5, .5)
	
	@property
	def Red(self):
		''' Property, do not use ()'''
		return FBColor(.8, .3, .3)						
		
			
class MoBuCore(MoBuSceneCore, MoBuAnimationCore, MoBuUtilCore, MoBuExportCore, MoBuUICore):
		
	"""
	Super/sub class and foundational MotionBuilder utility library
	"""
	
	def __init__(self):
		""" MayaCore.__init__():  set initial parameters """
		super(MoBuCore, self).__init__()
												
mbCore = MoBuCore()		

print "moBu.moBuCore imported"
