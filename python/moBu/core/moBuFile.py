'''
Author: Jason.Parks
Created: April 25, 2012
Module: core.moBuFile
Purpose: File convenience class
'''
from pyfbsdk import *
from common.core import globalVariables as gv
from common.diagnostic.pcsLogger import moBuLogger
from common.fileIO.parser_schema import ParseSchema
from common.fileIO.pcsPath import Path
from moBu.core.moBuCore import MoBuCore #@UnresolvedImport
#import P4
import getpass
import os
import re
import shutil

schemaObj = ParseSchema(mobu=1)

# eclipseSyntax
if False: from pyfbsdk_gen_doc import * #@UndefinedVariable @UnusedWildImport


class MoBuFile(MoBuCore):
	
	def __init__(self):
		""" MoBuFile.__init__():  set initial parameters """
		super(MoBuFile, self).__init__()
	
	def cleanDirs(self, folderPath='', dirExtension='.fbm'):
		''' Cleans viral .bck/.fbm folders from given folderPath
			Params:
				folderPath: director to clean
				dirExtension: extension to look for on end of dir
			Returns: True if cleaned any
			'''
		deleted = False
		if not folderPath:
			moBuLogger.error("No folderPath arg passed.")
			return False
		
		for root, dirs, unused in os.walk(folderPath):
			for _dir in dirs:
				dirPath = os.path.join(root, _dir)
				if Path(dirPath).isdir:
					if re.search(dirExtension, dirPath):
						try:
							shutil.rmtree(dirPath)
							deleted = True
						except WindowsError:
							moBuLogger.info("Failed to remove '%s'" % dirPath)
		return deleted
		
	def customFBFbxOptions(self, pLoad=False, saveAllTakes=True, allElements=True, selection=False, **kwargs):
		''' create save/load options
		Params:
			pLoad: True if loading, False if saving
			saveAllTakes: Set to False if save current take only
			allElements: Set to False and pass kwargs to save/load/merge specific elements
			selection: True to save selected only
		Returns: FBFbxOptions object
		'''
		if self.mobuVer == 2010:
			moBuLogger.warning("FBFbxOptions are not valid for 2010")
			return None
		
		elif self.mobuVer == 2012 or self.mobuVer == 2013:
			# create object
			pFbxOptions = FBFbxOptions(pLoad)
			
			if not allElements:
				# set all ElementActions and Base properties to false
				pFbxOptions.SetAll(FBElementAction.kFBElementActionDiscard, False)
				baseProperties = ['BaseCameras',
								'CameraSwitcher', 'CameraSwitcherSettings',
								'CurrentCamera', 'CurrentCameraSettings',
								'GlobalLighting', 'GlobalLightingSettings',
								'Transport', 'TransportSettings',
								'EmbedMedia', 'SaveSelectedModelsOnly', ]
				for bProperty in baseProperties:
					exec('pFbxOptions.%s=False' % bProperty)	
	
				# process kwargs
				for key in kwargs:
					# check for non-strings passed in
					if not isinstance(kwargs[key], str):
						moBuLogger.error("A non-string type arg was passed in: '%s'" % kwargs[key])
					if 'kFBElementAction' in kwargs[key]:
						# FBPropertyElementAction
						exec('pFbxOptions.%s = FBElementAction.%s' % (key, kwargs[key]))
					else:
						# FBPropertyBase
						exec('pFbxOptions.%s=%s' % (key, kwargs[key]))	
	
			# save selected for saves
			if not pLoad and selection:
				pFbxOptions.SaveSelectedModelsOnly = True
			
			# skip takes
			if not saveAllTakes:
				currentTake = self.system.CurrentTake
				
				pTakeIndex = 0
				for take in self.scene.Takes:
					# save current take only
					if not pLoad:
						if not take.Name == currentTake.Name:
							pFbxOptions.SetTakeSelect(pTakeIndex, False)
					# merge no takes
					else:
						pFbxOptions.SetTakeSelect(pTakeIndex, False)
					pTakeIndex += 1
			
			# save ASCII
			pFbxOptions.UseASCIIFormat = True
		
			return pFbxOptions
		else:
			moBuLogger.error("Wrong version of MotionBuilder '%s'" % self.mobuVer)
	
	def fixThis(self, message=''):
		''' sends scene and email to T.A.
			Params:
				message: passed message for email
			Returns: True/False
		'''
		successes = 0
		
		#1. Note currentScene name for reload
		currentScene = self.sceneName
		
		#2. Enter notes
		if not message:
			result = FBMessageBoxGetUserValue("Send Message", "Can you tell me what you were doing?", "Nothing to say", FBPopupInputType.kFBPopupString, "Send scene", "Cancel")
			if result[0] == 1:
				message = result[1]
			elif result[0] == 2:
				moBuLogger.info("Cancelled mbCore.fixThis()")
				return False
		
		#3. Save to network location
		savePath = Path('%s/data/%s/fixThis' % (gv.schemaLocation, getpass.getuser()))
		saveFilePath = '%s/%s' % (savePath, Path(currentScene).basename())
		
		# make dir
		if not os.path.exists(savePath):
			os.makedirs(savePath)
			
		if self.savePCSoptions(pathFile=saveFilePath, quiet=True, pOptions=None, p4=False):
			moBuLogger.info("Saved scene to: '%s'" % saveFilePath)
			successes += 1
		else:
			moBuLogger.info("Failed to save scene to: '%s'" % saveFilePath)
			return False
			
		
		#4. Email TechArtist
		#TODO: email message
		_file = open(saveFilePath.replace('.fbx', '.txt'), "w")
		_file.write(message)
		_file.close()
		
		#5. Reload original scene
		if self.loadPCSoptions(pathFile=currentScene, quiet=False, pOptions=None):
			successes += 1
		else:
			moBuLogger.info("Failed to reload original scene: '%s'" % currentScene)
			
		if successes == 2:
			return True
		else:
			return False
	
	def loadPCSoptions(self, pathFile=None, quiet=False, pOptions=None):
		''' saves with customFBFbxOptions
		Params:
			pathFile: complete file path to save
			quiet: suppress messages
			pOptions: pre-made options
		Returns: True/False
		'''
		
		# pick file if not passed
		if not pathFile:
			pathFile = self.openFileDialog(openSave='open')
			
#		# Check for binary
#		lFbp = FBProgress()
#		lFbp.ProgressBegin()
#		lFbp.Caption = "Checking binary on %s" % pathFile.basename
#		lFbp.Percent = 50 
#		if Path(pathFile).isbin:
#			moBuLogger.warning("Skipping file '%s' because detected binary" % pathFile)
#			lFbp.ProgressDone()
#			return False
#		moBuLogger.debug("Checked '%s' for binary, passed." % pathFile)
#
#		lFbp.ProgressDone()
		
		# check for cancel
		if not pathFile:
			moBuLogger.info("Cancelled open via loadPCSoptions()")
			return False
		
		if not pOptions:
			pOptions = self.customFBFbxOptions(pLoad=True)
				
		# by default, load all takes
		success = self.app.FileOpen(str(pathFile), 1 - quiet, self.customFBFbxOptions(pLoad=1, saveAllTakes=1, allElements=1))
		if success:
			moBuLogger.info("Success opening '%s'" % pathFile)
		else:
			moBuLogger.error("Failed to open '%s'" % pathFile)
		
		# check for hips
		ref = self.getObject("Reference")
		if ref:
			if len(ref.Children) > 0:
				if not ref.Children[0].Name == 'Hips':
					moBuLogger.infoDialog("WARNING: No Hips found in scene. Check your joint names.", "Joints Missing")
		
		return success

	def mergePCSoptions(self, pathFile='', quiet=True, pOptions=None):
		''' merges with customFBFbxOptions
		Params:
			pathFile: complete file path to merge
			quiet: suppress messages
			pOptions: pre-made options
		Returns: True/False
		'''
		if not pathFile:
			pathFile = self.openFileDialog()
		
		if not pOptions:
			pOptions = self.customFBFbxOptions(pLoad=True, saveAllTakes=True, allElements=True)
				
		# by default, do NOT merge takes
		if self.app.FileMerge(str(pathFile), 1 - quiet, pOptions):
			# report
			if not quiet:
				moBuLogger.info("Merged %s with PCSoptions" % pathFile)
			return True
		else:
			moBuLogger.error("Failed to merge '%s'" % pathFile)
			return False
				
	def openFileDialog(self, openSave='open', startPath=''):
		''' opens dialog box to select a file
		Params:
			openSave: open or save file type
			startPath: start in path
		Returns: path and fileName/False
		'''
		lFp = FBFilePopup()
		lFp.Caption = "Select a file"
		if openSave == 'open':
			lFp.Style = FBFilePopupStyle.kFBFilePopupOpen
		elif openSave == 'save':
			lFp.Style = FBFilePopupStyle.kFBFilePopupSave
		else:
			moBuLogger.error("Illegal arg passed. openSave=%s" % openSave)
			
		
		# BUG: If we do not set the filter, we will have an exception.
		lFp.Filter = "*"

		if not startPath:
			if not self.sceneName == 'Untitled':
				lFp.Path = str(self.sceneName.parent)
			else:
				lFp.Path = str(schemaObj.artRoot.replace('/', "\\"))
		else:
			lFp.Path = str(Path(startPath).makePretty(lastSlash=False, backward=True))
			
		# open window
		lRes = lFp.Execute()
		
		if lRes:
			return lFp.FullFilename
		else:
			return False

	def openFolderDialog(self):
		''' opens dialog box to select a folder
		Params: none
		Returns: path to folder/False
		'''
		
		lFp = FBFolderPopup()
		lFp.Caption = "Select a folder"
		
		self.app = FBApplication()
		if not self.sceneName == 'Untitled':
			lFp.Path = str(self.sceneName.parent)
		else:
			lFp.Path = str(schemaObj.artRoot)
		lRes = lFp.Execute()
		
		if lRes:
			return lFp.Path
		else:
			return False

	def savePCSoptions(self, pathFile=None, quiet=True, pOptions=None, p4=True):
		''' saves with customFBFbxOptions
		Params:
			pathFile: complete file path to save
			quiet: suppress messages
			pOptions: pre-made options
			p4: markForAdd/checkout or not
		Returns: True/False
		'''
		
		text = 'Saved with PCSoptions'
		
		# pick file if not passed
		if not pathFile:
			if not quiet:
				pathFile = self.openFileDialog(openSave='save')
			else:
				moBuLogger.error("No pathFile passed and quiet=True")
				return False
		if not pathFile:
			moBuLogger.info("Cancelled")
			return False
		
		# add extension if they didn't type it
		if not Path(pathFile).ext:
			pathFile = '%s.fbx' % pathFile
			
#		# checkout from perforce
#		if p4:
#			if self.pcsParseObj.isp4Active:
#				self.p4.fileName = pathFile
#				if self.p4.isP4Connected:
#					try:
#						self.p4.p4CheckOut(desc=text)
##					except P4.P4Exception:
#					except:
#						moBuLogger.warning("Failed to checkout: '%s'" % pathFile)
#			else:
#				if not quiet:
#					moBuLogger.warning('P4Active setting FALSE, not checking out.')
#		else:
#			if not quiet:
#				moBuLogger.warning("p4 arg passed as False, not checking out for file: '%s'." % pathFile)

		if not pOptions:
			pOptions = self.customFBFbxOptions(pLoad=False, saveAllTakes=True)
	
		# 2010 save process
		currentTakeObject = FBSystem().CurrentTake
		if self.mobuVer == 2010:	
			lMgr = FBFbxManager() #@UndefinedVariable
			lMgr.SaveBegin(str(pathFile))
			lMgr.Selected = True
			for strEach in lMgr.Takes:
				if strEach.Name != currentTakeObject.Name:
					strEach.Import = False
			lMgr.EmbedMedia = False
			lMgr.BaseCameras = False
			lMgr.CameraSwitcherSettings = False
			lMgr.CurrentCameraSettings = False
			lMgr.GlobalLightingSettings = False
			lMgr.TransportSettings = False
			if not lMgr.Save():
				moBuLogger.errorDialog('There is a problem saving the file', 'Cannot Save')
			if not lMgr.SaveEnd():
				moBuLogger.errorDialog('There is a problem saving the file', 'Cannot Save')
			
		# 2012 save process
		elif self.mobuVer == 2012 or self.mobuVer == 2013:
			alreadyExists = False
			if Path(pathFile).exists():
				alreadyExists = True
			if not self.app.FileSave(str(pathFile), pOptions):
				# cancelled?
				moBuLogger.warning("Cancelled")
				return False	
			if not alreadyExists:
				# check to see if new file is there
				res = os.path.exists(str(pathFile))
				if res:
					if not quiet:
						moBuLogger.info("%s, '%s'" % (text, str(pathFile)))
					return True
				else:
					moBuLogger.errorDialog("Failed to save '%s'" % str(pathFile))
					return False	
			else:
				#TODO: check to see if different?
				if not quiet:
					moBuLogger.info("%s, '%s'" % (text, str(pathFile)))
				return True
			
mbFile = MoBuFile()
	
print "core.moBuFile imported" 
