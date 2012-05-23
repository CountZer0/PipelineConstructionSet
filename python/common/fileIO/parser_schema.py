'''
Author: Jason.Parks
Created: Apr 22, 2012
Module: Scommon.fileIO.parser_schema
Purpose: main parser of schema xml files
'''

from common.core import globalVariables as gv
from common.diagnostic.pcsLogger import pcs_logger
from common.fileIO.pcsPath import Path
import os
import re #@UnresolvedImport
import xml.etree.ElementTree as ET

logger = pcs_logger(name='schema')

class ParseSchema(object):
	""" Super class that parses all necessary content that can be parsed on a global level """
	def __init__(self, filePath='', team='', mobu=0, **kwargs):
		super(ParseSchema, self).__init__()
		self.filePath = filePath

		if not filePath:
			if mobu:
				# get sceneName
				from pyfbsdk import FBApplication #@UnresolvedImport
				self.filePath = Path(FBApplication().FBXFileName.replace('\\', '/'))
				if not self.filePath: self.filePath = None
				elif self.filePath.basename() == '': self.filePath = None
			else:
				try:
					from pymel.core import sceneName
				except ImportError:
					logger.errorDialog("ParseSchema thinks it is in Maya mode, forgot to pass 'mobu=1' arg?")
				self.filePath = Path(sceneName())
				if not self.filePath: self.filePath = None
				elif self.filePath.basename() == 'untitled.ma': self.filePath = None

		# if no team passed, use first team listed in globalVariables.py
		if not team:
			team = gv.teamA
			
		#Parse the schema file
		relPath = (os.path.dirname(__file__)
			.replace('\\', '/')
			.replace('python/common/fileIO', 'schemas/'))
		self.xmlContent = ET.parse(relPath + team + '.xml')

		#Gather all global headers
		self.coreList = self.xmlContent.getiterator('Core')[0]
		self.characterList = self.xmlContent.getiterator('Character')[0]
		self.environmentList = self.xmlContent.getiterator('Environment')[0]
		self.exportList = self.xmlContent.getiterator('Export')[0]
		self.areaList = self.xmlContent.getiterator('Areas')[0]
		self.mayaList = self.xmlContent.getiterator('Maya')[0]
		self.mobuList = self.xmlContent.getiterator('MoBu')[0]
		self.team = team

				
		# Read in the asset hub xml section
		if self.team == gv.teamA:
			# Added headers
			self.riggingList = self.xmlContent.getiterator('Rigging')[0]
			self.assetHubList = self.xmlContent.getiterator('AssetHubUi')[0]
			
			# Self attributes
			self.fbxModels = eval(self.mobuList.get("FBXmodels"))
			self.retargetProcessing = eval(self.mobuList.get("retargetProcessing"))
			self.targetChar = eval(self.mobuList.get("targetCharacter"))
			self.sourceRetargetChar = eval(self.mobuList.get("sourceRetargetCharacters"))
			self.targetCharNode = self.mobuList.get("targetCharacterNode")
			
		if self.team == gv.teamB:
			# Added headers
			self.riggingList = self.xmlContent.getiterator('Rigging')[0]
			
			# Self attributes
			self.fbxModels = eval(self.mobuList.get("FBXmodels"))
			self.retargetProcessing = eval(self.mobuList.get("retargetProcessing"))
			self.targetChar = eval(self.mobuList.get("targetCharacter"))
			self.sourceRetargetChar = eval(self.mobuList.get("sourceRetargetCharacters"))
			self.targetCharNode = self.mobuList.get("targetCharacterNode")

		if self.team == gv.teamC:
			# Added headers
			self.riggingList = self.xmlContent.getiterator('Rigging')[0]
			
			# Self attributes
			self.fbxModels = eval(self.mobuList.get("FBXmodels"))
			self.retargetProcessing = eval(self.mobuList.get("retargetProcessing"))
			self.targetChar = eval(self.mobuList.get("targetCharacter"))
			self.sourceRetargetChar = eval(self.mobuList.get("sourceRetargetCharacters"))
			self.targetCharNode = self.mobuList.get("targetCharacterNode")
			
	def getMayaDir(self, attr):
		return eval(self.mayaList.get(attr))
	
	def getMoBuDir(self, attr):
		return eval(self.mobuList.get(attr))
	
	@property
	def artRoot(self):
		return self.getMayaDir('artRoot')
	
	@property
	def animationsRoot(self):
		return self.getMoBuDir('animationsRoot')
	
	@property
	def environmentRoot(self):
		return self.getMayaDir('environmentRoot')
	
	@property
	def characterRoot(self):
		return self.getMayaDir('characterRoot')
	
	def getUnitTestSource(self):
		return '%s/python/tests/source/' % gv.toolsLocation
	
	def getWellFormed(self, varName='', listName='Rigging'):
		
		if not listName.__class__ == str and listName.__module__ == 'xml.etree.ElementTree': self.list = listName
		else:
			self.list = self.xmlContent.getiterator(listName)
			if not self.list:
				logger.error('Failed to find list named "%s" in xml file: %s, wrong team? "%s"' % (listName, self.xmlContent, self.team))
				return
			#assert(len(self.list) > 0), logger.error('Failed to find list named "%s" in xml file: %s, wrong team? "%s"' % (listName, self.xmlContent, self.team))
			self.list = self.list[0]
			
		for under in self.list.getiterator():
			if under.get('name') == varName:
				result = under.get('value')
				if re.search('\.', result):
					result = float(result)
				return result
									
	def setFilePath(self, filePath):
		self.filePath = Path(filePath)

	def setTeam(self, team):
		self.team = team

	def findAnimationFolder(self, team):
		self.replace (self.characterList.get("AnimationFolderKey"), '')
		
class RigParse(ParseSchema):
	""" Class to solve for the rigging tools """
	def __init__(self, filePath='', team=''):
		super(RigParse, self).__init__()
		
		self.fileName = None
		
		#assert(self.filePath), "No file path found"
		if not self.filePath: return
		#if not self.filePath: logger.error("No filepath found, suggest renaming scene using cmds.file(rn='sceneName')")
			
		# remove double forward slashes
		self.filePath = self.filePath.replace('//', '/')
		self.filePath = self.filePath.replace('\\', '/')
		if self.team != gv.teamA: self.filePath = self.filePath.replace('_combined', '').replace('_wSkel', '')


		# Path manipulation
		if re.search('\.', self.filePath): self.fileName = self.filePath[self.filePath.rfind('/') + 1:self.filePath.rfind('.')]
		else: self.fileName = self.filePath[self.filePath.rfind('/') + 1:]
		self.fileNameParts = self.fileName.split('_')
		self.relativeFilePath = self.filePath.replace(self.characterRoot, '').rsplit('/', 1)[0] + '/'
		self.pathNameParts = self.filePath.split('/')
		self.pathNameParts = [notQuote for notQuote in self.pathNameParts if not notQuote == '']


	def getBaseDir(self):
		""" Method to get old baseDir attr for metarigging.importAllGripShapes """
		rigShort = self.getRig().replace(self.artRoot, '')
		return rigShort[:rigShort.rfind('/') + 1]

	def getBuildScript(self, charName):
		if not self.filePath: logger.error("No filepath found, suggest renaming scene using file(rn='sceneName')")
		if self.team == gv.teamA:
			return self.filePath.replace(self.filePath[self.filePath.rfind('/'):], '/%s.py' % charName)

		elif self.team == gv.teamD:
			return self.filePath.replace(self.filePath[self.filePath.rfind('/'):], '/%s.py' % charName)

		elif self.team == gv.teamD:
			return '%s%s.py' % (self.getMayaDir('buildScriptLoc'), charName)

	def getExpression(self):
		""" Method to pass back expression file """

		target = 'Expression'

		self.folderKey = self.characterList.get('%sFolderKey' % target)
		self.nameKey = self.characterList.get('%sNameKey' % target)

		self.result = ''.join(self._trailConstruct())
		if os.path.exists(self.result): return self.result
		else:
			self.pokeDir = self._trailConstruct()[0]
			if self.team == gv.teamD:
				self.pokeResult = self._pokeFiles()
			if self.pokeResult: return self.pokeResult

	def getLocator(self):
		""" Method to pass back locator file """

		target = 'Locators'

		self.folderKey = self.characterList.get('%sFolderKey' % target)
		self.nameKey = self.characterList.get('%sNameKey' % target)

		self.result = ''.join(self._trailConstruct())
		if os.path.exists(self.result): return self.result
		else:
			self.pokeDir = self._trailConstruct()[0]
			if self.team == gv.teamD:
				self.pokeResult = self._pokeFiles()
			if self.pokeResult: return self.pokeResult

	def getMesh(self, charType='', charRace='', charVariant='', charGender='', combined='', **kwargs):
		# NOTE: Must pass all these args or none. If you want to set individuals, use .set[Var] method
		""" Method to pass back mesh file path """
		if charType:
			self.charType = charType
			self.charRace = charRace
			self.charVariant = charVariant
			self.charGender = charGender
			self.fileName = charVariant		#self.fileName doesn't exist if these args are passed
											#so search charVariant arg instead of fileName

		target = 'Mesh'

		# check charVariant for explicitly set fileName
		explicit = 0
		if re.search('_', self.charVariant): explicit = 1
		if not explicit:
			if self.team == gv.teamA:
					if re.search('body', self.fileName): target = 'Body' + target
					if re.search('head', self.fileName): target = 'Head' + target

			elif self.team == gv.teamD:
				if re.search('Body', self.fileName): target = 'Body' + target
				if re.search('Head', self.fileName): target = 'Head' + target

		# parse .xml
		self.folderKey = self.characterList.get('%sFolderKey' % target)
		self.nameKey = self.characterList.get('%sNameKey' % target)

		resultPath, resultFile = self._trailConstruct()
		if explicit: resultFile = '%s.ma' % self.charVariant

		self.result = '%s%s' % (resultPath, resultFile)

		if combined:
			if not combined == 1: self.result = self.result.replace('.ma', '_%s.ma' % combined)
			else: self.result = self.result.replace('.ma', '_combined.ma')
			if self.team == gv.teamA:
				# remove charVariant from combined file
				self.result = self.result.replace('_%s' % self.charVariant, '')
		if os.path.exists(self.result): return self.result
		else:
			self.pokeDir = self._trailConstruct()[0]
			if self.team == gv.teamA:
				self.pokeResult = self._pokeFiles(type='mesh')
			elif self.team == gv.teamD:
				self.pokeResult = self._pokeFiles(type='mesh')
			elif self.team == gv.teamD:
				self.pokeResult = self._pokeFiles()
			if 'pokeResult' in dir(self):
				if not self.pokeResult == None: return self.pokeResult
			#else:
#			if combined: mCore.errorDisplay("Failed to find meshFile '%s'. If no combined file, use combined=0" % self.result)
			if combined: logger.error("Failed to find meshFile '%s'. If no combined file, use combined=0" % self.result)
			else: logger.error("Failed to find meshFile. Wrong project? '%s'" % self.team)

	def getRig(self):
		""" Method to pass back rig file """

		assert(self.fileName), "%s object does not have fileName attr. suggest renaming scene using cmds.file(rn='sceneName')" % self
		
		target = 'Rig'

		if self.team == gv.teamA:
			if re.search('body', self.fileName): target = 'Body' + target
			if re.search('head', self.fileName): target = 'Head' + target

		elif self.team == gv.teamD:
			#if re.search('Body', self.fileName): target = 'Body' + target
			if re.search('Body', self.fileNameParts[1]): target = 'Body' + target
			if re.search('Head', self.fileNameParts[1]): target = 'Head' + target
			if re.search('Environments', self.charType): target = 'Environment' + target
		
		elif self.team == gv.teamD:
			if re.search('mounts', self.charType): target = 'WVariant' + target
			
		self.folderKey = self.characterList.get('%sFolderKey' % target)
		self.nameKey = self.characterList.get('%sNameKey' % target)

		self.result = ''.join(self._trailConstruct())

		return self.result

	def getSkeleton(self):
		""" Method to pass back skeleton file """

		target = 'Skeleton'

		if self.team == gv.teamA:
			if re.search('body', self.fileName): target = 'Body' + target
			if re.search('head', self.fileName): target = 'Head' + target

		elif self.team == gv.teamD:
			if re.search('Body', self.fileName): target = 'Body' + target
			if re.search('Head', self.fileName): target = 'Head' + target

		self.folderKey = self.characterList.get('%sFolderKey' % target)
		self.nameKey = self.characterList.get('%sNameKey' % target)

		self.result = ''.join(self._trailConstruct())
		if os.path.exists(self.result): return self.result
		else:
			self.pokeDir = self._trailConstruct()[0]
			if self.team == gv.teamD:
				self.pokeResult = self._pokeFiles()
			if self.pokeResult: return self.pokeResult

	def getWeight(self):
		""" Method to pass back weight directory """

		target = 'Weights'

		if self.team == gv.teamA:
			if re.search('body', self.fileName): target = 'Body' + target
			if re.search('head', self.fileName): target = 'Head' + target

		elif self.team == gv.teamD:
			if re.search('Body', self.fileName): target = 'Body' + target
			if re.search('Head', self.fileName): target = 'Head' + target

		self.folderKey = self.characterList.get('%sFolderKey' % target)
		self.nameKey = self.characterList.get('%sNameKey' % target)

		self.result = self._trailConstruct()[0]
		if os.path.exists(self.result): return self.result
		
	def setCharVariant(self, charVariant=''):
		self.charVariant = charVariant

	def _pokeFiles(self, _type=''):
		""" Method to poke for files the main methods can't find """

		if self.team == gv.teamD:
			if _type == 'mesh':
				if os.path.exists(self.result.replace('LOD0', 'lod0')): return self.result.replace('LOD0', 'lod0')
				elif os.path.exists(self.result.replace('Models', 'Model')): return self.result.replace('Models', 'Model')

		elif self.team == gv.teamD:
			searchTerm = self.nameKey[self.nameKey.rfind('~') + 1:]
			matchFile = ''
			for unused, unused, files in os.walk(self.pokeDir):
				for name in files:
					if name.strip().endswith(searchTerm): matchFile = self.pokeDir + name
			if matchFile: return matchFile

		elif self.team == gv.teamA: pass

	def _trailConstruct(self):
		""" Method to build the file name and path for all main methods """

		if not self.charVariant: charVariant = '_charVariant'
		else: charVariant = 'charVariant'

		resultFile = (self.nameKey.replace(':', '_')
				.replace('charRace', self.charRace)
				.replace('charGender', self.charGender)
				.replace(charVariant, self.charVariant)
				.replace('charType', self.charType)
				.replace('~', ''))

		resultPath = (self.characterRoot + (self.folderKey.replace(':', '/')
				.replace('charRace', self.charRace)
				.replace('charGender', self.charGender)
				.replace('charVariant', self.charVariant)
				.replace('charType', self.charType)
				.replace('~', '')))

		# remove extra underscores and forward-slashes
		resultFile = resultFile.replace('__', '_')
		resultPath = resultPath.replace('//', '/')

		return resultPath, resultFile

class RigParseFromArgs(RigParse):
	# ***! As opposed to RigParsing from currently loaded scene !***
	def __init__(self, filePath='', team=''):
		super(RigParseFromArgs, self).__init__()

class ExportParse(ParseSchema):
	""" Class to solve for the export tools """
	def __init__(self, filePath='', team=''):
		super(ExportParse, self).__init__()
		
		# Solve needed attributes from the xml
		self.runTimeArtRoot = eval(self.exportList.get("runTimeArtRoot"))
		self.exportKey = self.exportList.get("exportKey")

		# Set needed variables
		if self.filePath:
			if os.path.isdir(self.filePath): self.exportSourceFolder = self.filePath + '/'
			else: self.exportSourceFolder = os.path.dirname(self.filePath) + '/'
		else:
			logger.warning('No scene selected')
			#self.exportSourceFolder = '/'

	def getExport(self, wFile=0):
		""" Method that returns folder for exporting meshes, animations (Character & Environment) """
		#assert(self.exportSourceFolder), ""
		if not self.filePath or not self.exportSourceFolder: return
		
		if self.team == gv.teamA:
			self.exportKey = int(self.exportKey)
			if wFile:
				self.exportPath = ('%s%s' % (self.exportSourceFolder.rsplit('/', (self.exportKey + 1))[0] + '/', self.filePath[self.filePath.rfind('/') + 1:])).replace(".ma", ".gr2").replace(".mb", "gr2")
			else:
				self.exportPath = self.exportSourceFolder.rsplit('/', (self.exportKey + 1))[0] + '/'
				#print 'printStatement: ' + self.exportSourceFolder
				logger.debug('Export folder: %s' % self.exportSourceFolder)

			return self.exportPath

		elif self.team == gv.teamB:
			if re.search('Animations', self.filePath):
				self.exportFileName = self.filePath.basename().replace(".ma", ".xmd").replace(".mb", ".xmd").replace(".fbx", ".xmd")
				rigPath = self.filePath[:self.filePath.rfind('MoBu')]
				weapon = self.exportFileName.split('_')[1]
				self.exportPath = Path('%s/Morpheme/Animations/%s/%s' % (rigPath, weapon, self.exportFileName))
			else:
				self.exportPath = Path(self.filePath.replace(".ma", ".gr2").replace(".mb", "gr2"))
			if not wFile: self.exportPath = self.exportPath.parent
			return self.exportPath.makePretty()
		
		elif self.team == gv.teamD:
			strFrom = self.exportKey[self.exportKey.find(':', 2) + 1:self.exportKey.rfind(':', 1)]
			#print strFrom
			strTo = self.exportKey[self.exportKey.rfind(':', 1) + 1:]
			#print strTo
			self.exportPath = self.exportSourceFolder.replace(strFrom, strTo)
			if wFile: self.exportPath = '%s%s' % (self.exportPath, self.filePath[self.filePath.rfind('/') + 1:])
			return self.exportPath

		elif self.team == gv.teamD:
			# If the asset is an environment asset
			if re.match(self.environmentRoot, self.exportSourceFolder):
				envMeshKey = self.exportList.get('environmentMeshExportKey')
				envMeshKeySource = envMeshKey[envMeshKey.find(':', 2) + 1:envMeshKey.rfind(':', 1)]
				envMeshKeyTarget = envMeshKey[envMeshKey.rfind(':', 1) + 1:]
				envAnimKey = self.exportList.get('environmentAnimExportKey')
				envAnimKeySource = envAnimKey[envAnimKey.find(':', 2) + 1:envAnimKey.rfind(':', 1) - 3]
				envAnimKeyTarget = envAnimKey[envAnimKey.rfind(':', 1) + 1:]

				# If the environment asset is an animation
				if re.search(envAnimKeySource, self.exportSourceFolder):
					self.exportPath = self.exportSourceFolder.split(envAnimKeySource)[0] + envAnimKeyTarget
					if wFile: self.exportPath = '%s%s' % (self.exportPath, self.filePath[self.filePath.rfind('/') + 1:])
					if self.exportPath: return self.exportPath

				# If the asset is not an animation
				else:
					self.exportPath = self.exportSourceFolder.replace(envMeshKeySource, envMeshKeyTarget)
					if wFile: self.exportPath = '%s%s' % (self.exportPath, self.filePath[self.filePath.rfind('/') + 1:])
					if self.exportPath: return self.exportPath

			# If the asset is a character asset
			if re.match(self.characterRoot, self.exportSourceFolder) :
				charMeshKey = self.exportList.get('characterMeshExportKey')
				charMeshKeySource = charMeshKey[charMeshKey.find(':', 2) + 1:charMeshKey.rfind(':', 1)]
				charMeshKeyTarget = charMeshKey[charMeshKey.rfind(':', 1) + 1:]
				charAnimKey = self.exportList.get('characterAnimExportKey')
				charAnimKeySource = charAnimKey[charAnimKey.find(':', 2) + 1:charAnimKey.rfind(':', 1) - 3]
				charAnimKeyTarget = charAnimKey[charAnimKey.rfind(':', 1) + 1:]

				# If the character asset is an animation
				if re.search(charAnimKeySource, self.exportSourceFolder):
					self.exportPath = self.exportSourceFolder.split(charAnimKeySource)[0] + charAnimKeyTarget
					if wFile: self.exportPath = '%s%s' % (self.exportPath, self.filePath[self.filePath.rfind('/') + 1:])
					if self.exportPath: return self.exportPath
				# If the asset is not an animation
				else:
					self.exportPath = self.exportSourceFolder.replace(charMeshKeySource, charMeshKeyTarget)
					if wFile: self.exportPath = '%s%s' % (self.exportPath, self.filePath[self.filePath.rfind('/') + 1:])
					if self.exportPath: return self.exportPath

	def getRunTimeArt(self, wFile=0):
		""" method to return the folder (or w/ file) for the run time copy """
		fileLoc = self.getExport(wFile)
		runTimeFilePath = fileLoc.replace(self.characterRoot, self.runTimeArtRoot)
		return runTimeFilePath

	def getRunTime(self):
		return self.runTimeArtRoot[:self.runTimeArtRoot.rfind('Runtime') + 8]



if __name__ == '__main__':
	print 'run from command line'
else:
	print "common.fileIO.parser_schema imported"
	
	
