'''
Author: Jason.Parks
Created: Jan 17, 2012
Module: common.perforce.pcsP4
Purpose: perforce methods
'''

from common.core import globalVariables as gv
from common.diagnostic.pcsLogger import logger
from common.fileIO import pcsPath
from getpass import getuser
from os import path #@UnusedImport
import getpass #@UnusedImport
import platform
import re
import sys
import xml.etree.ElementTree as ET #@UnusedImport

class P4Lib(object):
	"""
	SYNOPSIS: Perforce library class
	"""

	def __init__(self, maya=1, pyTargetVersion='26', fileName=None):
		"""
		SYNOPSIS: 	Perforce Library class init
		INPUTS: 	maya* - instantiate for use in Maya
					pyTargetVersion* - where to import P4 from
					fileName* - Which system file name to act upon (self.fileName)
		Example: 	mP4 = pcsP4.P4Lib()
		"""	

		# Parse User XML
		userXML = ET.parse("%s/data/%s/PCSuser.xml" % (gv.toolsLocation, getpass.getuser()))
		self.userXMLcore = userXML.getiterator('Core')[0]
		p4Mode = self.userXMLcore.get('P4_Mode')
		
		# Parse Team XML
		globalXML = ET.parse("%s/installData/PCSstudio.xml" % gv.toolsLocation)
		self.globalXMLcore = globalXML.getiterator(self.userXMLcore.get('PCSactiveTeam'))[0]
			
		self.maya = maya
		self.pyTargetVersion = pyTargetVersion
		
		if fileName: 
			self.fileName = fileName
		else:
			self._fileName = fileName
			self.depotPath = None
		
		if p4Mode:			
			if self.maya:
				try:
					# Path is hardcoded per team in PCSstudio.xml
					from P4 import P4 #@UnusedImport @UnresolvedImport
				except:
					logger.error('Failed to import P4 from Maya - check that the path is in pcsGlobalSetup')
			else:
				if self.pyTargetVersion == '26':
					try:
						if platform.architecture()[0] == '64bit':
							# cannot import via '.' path, bug, must add this path to sys.path
#							from perforce.p426.win64.P4 import P4 #@Reimport @UnresolvedImport @UnusedImport
							from P4 import P4 #@Reimport @UnresolvedImport @UnusedImport
						else:
#							from perforce.p426.win32.P4 import P4 #@UnresolvedImport @Reimport @UnusedImport
							from P4 import P4 #@UnresolvedImport @Reimport @UnusedImport
					except:
						logger.error('Failed to import P4 for pyTargetVersion - %s' % self.pyTargetVersion)
				elif self.pyTargetVersion == '25':
					try:
#						from perforce.p425.P4 import P4 #@Reimport @UnresolvedImport @UnusedImport
						from P4 import P4 #@Reimport @UnresolvedImport @UnusedImport
					except:
						logger.error('Failed to import P4 for pyTargetVersion - %s' % self.pyTargetVersion)
						
			if self.canP4connect:
				self.createP4Instance()
				self.p4Connect()
		else:
			logger.warning('Perforce is turned off, if you want to use it, turn it on in your Maya menu')
		
				
	@property	
	def fileName(self):
		return self._fileName
	
	@fileName.setter
	def fileName(self, passedName):
		self._fileName = passedName
		self.depotPath = pcsPath.Path(self._fileName).toP4Path()
		
	@fileName.deleter
	def fileName(self):
		del self._fileName					

##################################################################################################################################
##	Foundation																													##
##################################################################################################################################

	def createP4Instance(self):
		"""
		SYNOPSIS: Creates basic instance, connects and returns instance
		INPUTS NONE
		RETURNS: True/None - sets the self.p4i instance 
		"""
		if self.maya:
			# path should be hardcoded in pcsGlobalSetup.mel
			from P4 import P4 #@UnusedImport @UnresolvedImport
		else:
			if self.pyTargetVersion == '26':
				if platform.architecture()[0] == '64bit':
					# cannot import via '.' path, bug, must add this path to sys.path
#					from perforce.p426.win64.P4 import P4 #@Reimport @UnresolvedImport @UnusedImport
					from P4 import P4 #@Reimport @UnresolvedImport @UnusedImport
				else:
#					from perforce.p426.win32.P4 import P4 #@UnresolvedImport @Reimport
					from P4 import P4 #@Reimport @UnresolvedImport @UnusedImport
		self.p4i = P4()
		return True
		
	def p4Connect(self):
		"""
		SYNOPSIS: Attempts to connect to perforce
		INPUTS NONE
		RETURNS: True/None 
		Example: mP4.p4Connect()
		"""
		if not self.p4i: self.createP4Instance()
		if self.p4i:		
			logger.debug('-- Entered p4Connect --')
			if not self.isP4Connected: 
				if self.activeTeam:
					logger.debug('P4 UserName is - %s' % self.userXMLcore.get('PCSP4userName'))			
					logger.debug('P4 Workspace is - %s' % self.userXMLcore.get('PCSP4workspace'))				
					logger.debug('P4 Server is - %s' % self.globalXMLcore.get('P4_Server'))				
					self.p4i.user = self.userXMLcore.get('PCSP4userName')
					self.p4i.client = self.userXMLcore.get('PCSP4workspace')
					self.p4i.port = self.globalXMLcore.get('P4_Server')
					self.p4i.connect()
					self.p4Version
				else:
					logger.error('No active team set/Team P4 data is missing')
		
			logger.debug('-- Exiting p4Connect --')
			return True
		else:
			logger.error('Could not create P4 instance')
			
	@property	
	def p4Version(self):
		"""
		**Property, do not use ()**
		SYNOPSIS: Query perforce version
		INPUTS NONE
		RETURNS: Perforce version 
		Example: mP4.p4Version
		"""
		if (2, 4) < sys.version_info and sys.version_info < (2, 5): return 2.4
		if (2, 5) < sys.version_info and sys.version_info < (2, 6): return 2.5
		if (2, 5) < sys.version_info: return 2.6
		else:
			logger.warning('Could not determine P4 lib version.')
			return False

##################################################################################################################################
##	Connection Verifications																									##
##################################################################################################################################
			
	@property
	def canP4connect(self):
		"""
		**Property, do not use ()**
		SYNOPSIS: Check if we can connect to P4
					Creates instance and connects
		INPUTS NONE
		RETURNS: True/False
		Example: mP4.canP4connect
		"""
		try:
			self.createP4Instance()
			if not self.isP4Connected:
				#self.p4i.connect()
				self.p4Connect()
			return True
		except:
			return False
	
	@property	
	def isP4Connected(self):
		"""
		**Property, do not use ()**
		SYNOPSIS: Check if P4 is connected
		INPUTS NONE
		RETURNS: True/False
		Example: mP4.isP4Connected
		"""
		if not re.search('disconnected', str(self.p4i)): return 1
		else: return 0
			
##################################################################################################################################
##	File Verifications																											##
##################################################################################################################################
	
	@property
	def isInP4(self):
		"""
		**Property, do not use ()**
		SYNOPSIS: Check if file is in depot
		INPUTS NONE
		RETURNS: True/False
		Example: mP4.isInP4
		"""
		if not self.p4i: self.createP4Instance()
		if self.p4i:
			logger.debug('-- Entered isInP4 --')
			try:
				result = self.p4i.run("files", self.depotPath)
				if result: result = 1
			except: result = 0
			
			logger.debug('- isInP4 Result is -- %s' % result)
			logger.debug('- Exiting isInP4 --')
			
			return result
		else:
			logger.error('Could not create P4 instance')
		
	@property	
	def isLatest(self):
		"""
		**Property, do not use ()**
		SYNOPSIS: Check if file is latest
		INPUTS NONE
		RETURNS: True/False
		Example: mP4.isLatest
		"""
		if not self.p4i: self.createP4Instance()
		if self.p4i:
			logger.debug('-- Entered isLatest --')
			if self.isInP4:
				try:
					if not pcsPath.Path(self._fileName).isdir():
						fileStatDict = self.p4i.run("fstat", self.depotPath)
						if fileStatDict:
							if fileStatDict[0]['headRev'] == fileStatDict[0]['haveRev']:
								logger.debug('Head revision - %s - same as Have Revision - %s - on file file - %s' % (str(fileStatDict[0]['headRev']), str(fileStatDict[0]['haveRev']), self.depotPath))
								return 1
							else:
								logger.debug('Head revision - %s - not the same as Have Revision - %s - on file file - %s' % (str(fileStatDict[0]['headRev']), str(fileStatDict[0]['haveRev']), self.depotPath))
								return 0
						else:
							logger.debug('Empty fstat list returned on file - %s' % self.depotPath)
							return 0
					else:
						logger.debug('Passed file is a directory - %s' % self.depotPath)
						return 0
				except:
					logger.debug('Failed on file - %s' % self.depotPath)
					return 0
			else:
				logger.debug('File not in perforce - %s' % self.depotPath)
				return 0
		else:
			logger.error('Could not create P4 instance')
		logger.debug('- Exiting isLatest --')
	
	@property	
	def isCheckedOutByAnyoneElse(self):
		"""
		**Property, do not use ()**
		SYNOPSIS: Check if file is checked out by anyone but me
		INPUTS NONE
		RETURNS: (True/False, [whom])
		Example: mP4.isCheckedOutByAnyoneElse
		"""	
		if not self.p4i: self.createP4Instance()
		if self.p4i:		
			logger.debug('-- Entered isCheckedOutByAnyoneElse --')
			if self.isInP4:
				logger.debug('%s is in depot' % self.depotPath)
				stats = self.p4i.run("opened", "-a", self._fileName)
				otherUsers = []
				if stats:
					for d in stats:
						for dKey, dVal in d.iteritems():
							if dKey == 'user':
								if not dVal == getuser():
									otherUsers.append(dVal)
				if otherUsers:
					return (1, otherUsers)
				else:
					return(0, 0)
			else:
				return (0, 0)
				
	@property	
	def isCheckedOut(self):
		"""
		**Property, do not use ()**
		SYNOPSIS: Check if file is checked out
		INPUTS NONE
		RETURNS: True/False
		Example: mP4.isCheckedOut
		"""
		if not self.p4i: self.createP4Instance()
		if self.p4i:		
			logger.debug('-- Entered isCheckedOut --')
			checkedOut = 0
			if self.isInP4:
				logger.debug('%s is in depot' % self.depotPath)
				stats = self.p4i.run("opened", "-a", self._fileName)
				if stats:
					if self.p4Version == 2.4:
						logger.debug('p4(Python2.4) stats are:%s' % stats)
						if not stats[0].find(' by ') == -1:
							checkedOut = stats[0][stats[0].rfind(' ') + 1:]
					elif self.p4Version == 2.5 or 2.6:
						logger.debug('P4(Python2.5) stats are:\n%s' % '\n'.join('%s,%s' % (stat, stats[0][stat]) for stat in stats[0].keys()))

						if stats[0].has_key('user'):
							logger.debug('Already checked out by: %s' % stats[0]['user'])
							checkedOut = stats[0]['user']
				logger.debug('Not checked out.')
		
			logger.debug('-- Exiting isCheckedOut --')
			return checkedOut
		else:
			logger.error('Could not create P4 instance')
			return 0

##################################################################################################################################
##	Actions																														##
##################################################################################################################################

	
	def p4DeleteChangelist(self, changelist, enforceEmpty=1):
		
		if not self.p4i: self.createP4Instance()
		if self.p4i:
			logger.debug('-- Entered p4DeleteChangelist --')
			try:
				self.p4i.run('change', "-d", int(changelist))
				logger.info("***Deleting changelist: '%s'***" % changelist)
				return 1
			except:
				return 0
			logger.debug('-- Exiting p4DeleteChangelist --')
		else:
			logger.error('Could not create P4 instance')
			return 0
			
	def p4RevertFile(self):
		
		if not self.p4i: self.createP4Instance()
		if self.p4i:
			logger.debug('-- Entered p4Revert --')
			try:
#				self.p4i.run('revert', "%s" % self.fileName)
				self.p4i.run('revert', "%s" % self.depotPath)
				logger.info("***Reverting: '%s'***" % self.fileName)
				return 1
			except:
				return 0
			logger.debug('-- Exiting p4Revert --')
		else:
			logger.error('Could not create P4 instance')
			return 0
		
	def p4RevertChangelist(self, changelist):
			
		if not self.p4i: self.createP4Instance()
		if self.p4i:
			logger.debug('-- Entered p4RevertChangelist --')
			try:
				self.p4i.run('revert', "-c%s" % changelist, '//...')
				logger.info("***Reverting: '%s'***" % self.fileName)
				return 1
			except:
				return 0
			logger.debug('-- Exiting p4RevertChangelist --')
		else:
			logger.error('Could not create P4 instance')
			return 0
	
	def p4CheckOut (self, desc="Updated via python script", force=0, stomp=0, sync=1, returnTuple=0):
		"""
		SYNOPSIS: Check out or add to P4
		INPUTS:	desc* 	- Changelist description
				force* 	- Force check out
				stomp*	- Overwrite
		RETURNS: Tuple (Success/Failure, changelist, userCheckedOutBy)
		Example: mP4.p4CheckOut("My Changelist Name")
		"""
		if not self.p4i: self.createP4Instance()
		if self.p4i:
			logger.debug('-- Entered p4CheckOut --')
			if self.isInP4:
				# get latest
				if sync:
					self.p4Sync(force)
				checkedOut = self.isCheckedOut
				if checkedOut:
					if not checkedOut == getuser():
						logger.warning("Checked out by %s" % checkedOut)
						if not stomp: return (0, checkedOut, 0)
				newChangeList = self.p4MakeChangeList(desc)
				self.p4i.run('edit', "-c%s" % newChangeList, self.depotPath)	# moves file to newChangeList
				logger.info("***Checking out: '%s'***" % self.depotPath)
				logger.debug('-- Exiting p4CheckOut --')
				if checkedOut and stomp:
					if not checkedOut == getuser():
						return (1, newChangeList, checkedOut)
					else: return (1, newChangeList, 0)
				else:
					return (1, newChangeList, 0)
		
			else:
				changeListNum = self.p4MakeChangeList(desc.replace('Updated', 'Added'))
				try:
					self.p4i.run("add", "-c%s" % changeListNum, self.depotPath)
					return (1, changeListNum, 0)
				except: pass
					#print p4i.warnings()[0]
				logger.debug('Added to "%s" changelist' % changeListNum)
			logger.debug('-- Exiting p4CheckOut --')
		else:
			logger.error('Could not create P4 instance')
	
	def p4MoveRename(self, newName, desc="Py Rename/Move file(s)", stomp=0):
		"""
		SYNOPSIS: Move and rename files in P4
		INPUTS:	newName	- New path name (system or P4 path)
				desc* 	- [New change, old change]
				stomp*	- Overwrite
		RETURNS: Changelist
		Example: mP4.p4MoveRename(["My New File Changelist Name", "My Old File Changelist Name"])
		"""
		if not self.p4i: self.createP4Instance()
		if self.p4i:		
			logger.debug('-- Entered p4CheckOut --')
			if not re.search('//depot/', str(newName)):
				newDepotPath = pcsPath.Path(newName).toP4Path()
			else: newDepotPath = newName
			changeListNum = (0, "doesn't exist")
			if self.isInP4:
				# get latest
				self.p4Sync(1)
		
				checkedOut = self.isCheckedOut
				if checkedOut:
					if not checkedOut == getuser():
						logger.warning('WARNING!: Checked out by %s' % checkedOut)
						if not stomp: return (0, checkedOut)
				# copy
				changeListNum = self.p4MakeChangeList(desc)
				self.p4i.run('integrate', '-c%s' % changeListNum, self.depotPath, newDepotPath)
				logger.debug("Copied '%s' to '%s'" % (self._fileName, newName))
		
				# delete
				changeListNum = self.p4MakeChangeList(desc)
				self.p4i.run('delete', '-c%s' % changeListNum, self.depotPath)
				logger.debug('Marked "%s" for delete' % self._fileName)
			return changeListNum
		else:
			logger.error('Could not create P4 instance')
			return 0
			
	def p4Delete(self, desc="Deprecated via python script", stomp=0):
		"""
		SYNOPSIS: Delete files in P4
		INPUTS:	desc* 	- Changelist name
				stomp*	- Overwrite
		RETURNS: Changelist
		Example: mP4.p4Delete("My Del File Changelist Name")
		"""
		if not self.p4i: self.createP4Instance()
		if self.p4i:
			logger.debug('-- Entered p4Delete --')
			changeListNum = (0, "Doesn't Exist")
			if self.isInP4:
				# get latest
				self.p4Sync(1)
				if self.isCheckedOut:
					if not self.isCheckedOut == getuser():
						logger.warning('WARNING!: Checked out by %s' % self.isCheckedOut)
						if not stomp: return '-1%s' % self.isCheckedOut
		
				changeListNum = self.p4MakeChangeList(desc)
				self.p4i.run('delete', '-c%s' % changeListNum, self.depotPath)
				logger.debug('Marked "%s" for delete' % self.depotPath)
			return changeListNum
		else:
			logger.error('Could not create P4 instance')
			return 0
	
	def p4DescribeChangeList(self, changeListNum):
		"""
		NAME: p4DescribeChangList
		
		SYNOPSIS
		 Queries changeList and returns files and description
		
		INPUTS	* = optional
		 (int)			changListNum:	changeList to lookup	
	
		##RETURNS: (list),(string)	files, desc 
		RETURNS: (string)	description
		"""
		if not self.p4i: self.createP4Instance()
		if self.p4i:	
			logger.debug('-- Entered p4DescribeChangList --')
			description = ''
			try:
				if self.p4Version == 2.4:
					results = self.p4i.run('describe', '-dc', str(changeListNum))
					if not results:
						logger.info("Changelist %s probably doesn't exist" % changeListNum)
						return
					doneWithDesc, doneWithFiles = [0, 0]
					desc, files = [[], []]
					for line in results:
						if 'Affected files ' in line: doneWithDesc = 1
						if 'Differences ' in line: doneWithFiles = 1
						if not doneWithDesc: desc.append(line)
						elif not doneWithFiles: files.append(line)
		
					text = '\nDescription of change:\n\n'
					for des in desc:
						if des[:1] == '\t': des = des[1:]	# remove tab
						text = '%s%s\n' % (text, des)
					for _file in files:
						if _file[:2] == '//': _file = _file[:-5]	# remove '#edit'
						text = '%s%s\n' % (text, _file)
					description = text
				elif self.p4Version == 2.5 or 2.6:
					results = self.p4i.run('describe', '-dc', changeListNum)[0]
					files = results['depotFile']
					desc = results['desc']
					#description = [desc, files]
					filesText = ''
					for _file in files:
						filesText = '%s%s\n' % (filesText, _file)
					description = '\nDescription of change:\n\n%s\n\nAffected files ...\n\n%s\n' % (desc, filesText)
			except:
				logger.info("Changelist %s probably doesn't exist" % changeListNum)
				return
		
			return description
		else:
			logger.error('Could not create P4 instance')
	
	def p4MakeChangeList (self, desc="Updated via python script"):
		"""
		SYNOPSIS: Make a new changelist
		INPUTS:	desc* 	- Changelist name
		RETURNS: New Changelist
		Example: mP4.p4MakeChangeList("My New Changelist Name")
		"""		
		if not self.p4i: self.createP4Instance()
		if self.p4i:
			logger.debug('-- Entered p4MakeChangeList --')
		
			# check for desc length
			if len(desc) > 31: logger.warning("WARNING!: '%s' is longer than 31 characters, descriptions will NOT match." % desc)
		
			# create new list with:
			newChangeList = 0
		
			if not self.isP4Connected:
				logger.error('Could not connect')
				return False
			# check if already exists
			changeLists = self.p4i.run("changes", "-c%s" % self.p4i.client, "-spending")
			logger.debug("changeLists is '%s'" % changeLists)
		
			if changeLists:
				for cl in changeLists:
		
					if self.p4Version == 2.4:
						logger.debug("Checking p4 (Python 2.4) changelist: '%s'" % cl)
						if re.search(desc, cl):
							# list = P4 for Python 2.4
							newChangeList = cl[cl.find(' ') + 1:cl.find('on') - 1]
							logger.debug("Found desc: '%s' for changeList %s" % (desc, newChangeList))
					elif self.p4Version == 2.5 or 2.6:
						# dictionary = P4 for Python 2.5,2.6
						logger.debug("Checking P4 (Python 2.5) changelist: '%s'" % cl)
						if re.search(desc, cl["desc"]): newChangeList = cl['change']
		
			if not newChangeList:
				change = ''
				if self.p4Version == 2.4:
					change = 'Description:%s\nChange: new' % desc
				elif self.p4Version == 2.5 or 2.6:
					change = {}
					change["Description"] = desc
					change['Change'] = 'new'
				self.p4i.input = change
				result = self.p4i.run('change', '-i')[0]
				newChangeList = result[result.find(' ') + 1:result.rfind(' ')]
			logger.debug("newChangeList is: '%s'" % newChangeList)
			logger.debug('-- Exiting p4MakeChangeList --')
			return newChangeList
		else:
			logger.error('Could not create P4 instance')
	
	def p4Submit (self, changeList):
		"""
		SYNOPSIS: Submit a specified changelist to P4
		INPUTS:	changeList 	- Changelist name
		RETURNS: True/False
		Example: mP4.p4Submit(changeList)
		"""	
		if not self.p4i: self.createP4Instance()
		if self.p4i:
			logger.debug('-- Entered p4Submit --')
			if self.isInP4:
				if self.isCheckedOut:
					logger.debug("\n***Submitting In: '%s'***\n" % self.depotPath)
					try:
						change = self.p4i.fetch_change(changeList)
						result = self.p4i.save_submit(change)
					except:
						logger.error('p4 Submit failed')
		
					logger.debug('-- Exiting p4Submit --')
					return result
		
			logger.debug('-- Exiting p4Submit --')
		else:
			logger.error('Could not create P4 instance')
			return 0
			
	def p4Sync(self, force=0):
		"""
		SYNOPSIS: Sync file
		INPUTS:	force* - Force sync (0/1)
		RETURNS: True/False/-1
		Example: mP4.p4Sync()
		"""	
		if not self.p4i: self.createP4Instance()
		if self.p4i:
			if not self.isP4Connected:
				if self.canP4connect:
					self.p4Connect()
			logger.debug('-- Entered p4Sync --')
		#	depotPath = depotPath.replace('\\', '/')
			# test to see whether its a file or a dir
#			if self.depotPath[-1:] == '/': self.depotPath = self.depotPath[:-1]
			if pcsPath.Path(self._fileName).isdir():
				self.depotPath = self.depotPath + '...'
				logger.debug('Depot Path is: %s' % self.depotPath) 
			
			if self.isInP4:
				if not self.isLatest:
					result = 0
					try:
						if force:
							result = self.p4i.run("sync", "-f", self.depotPath)
							logger.debug("***Syncing (force): '%s'***" % self.depotPath)
						else:
							result = self.p4i.run("sync", self.depotPath)
							logger.debug("***Syncing: '%s'***" % self.depotPath)
						#if result: result = 1
					except:
						logger.debug("Failed to sync. Already in sync?...")
						result = 0
					logger.debug('-- Exiting p4Sync --')
					return result
				else: return True
		else:
			logger.error('Could not create P4 instance')
			
	def p4SetFileType(self, fileType='binary'):
		"""
		SYNOPSIS: Set file type
		INPUTS:	fileType - 
		RETURNS: Nothing
		Example: mP4.p4SetFileType()
		"""
		if not self.p4i: self.createP4Instance()
		if self.p4i:
			logger.debug('-- Entered p4SetFileType --')
			if self.isInP4:
				self.p4i.run("reopen", "-t%s" % fileType, self.depotPath)
#				result = self.p4i.run("fstat", self.depotPath)
				logger.debug('-- Exiting p4SetFileType --')
				return 1
#				return result[0]['headType']
			else: return 0
		else:
			logger.error('Could not create P4 instance')
								
	@property	
	def p4clientDiag(self):
		"""
		SYNOPSIS: Diagnose specs about P4 client
		INPUTS:	NONE
		RETURNS: clientName
		Example: mP4.p4clientDiag
		"""	
		if not self.p4i: self.createP4Instance()
		if self.p4i:			
			logger.debug('-- Entered p4clientDiag --')
			infoL = self.p4i.run("info")
			#print "infoL is: '%s'" %infoL
			info = infoL[0]
		
			j = 0
			clientName = 0
			# perforce diagnostics
			if self.p4Version == 2.4:
				# list = P4 for Python 2.4
				logger.debug("Client 'info' specs are:\n%s" % '\n'.join(i for i in infoL))
				for i in infoL:
					if not i.find("Client unknown") == -1: clientName = '*unknown*'
					elif not i.find("Client name") == -1: clientName = i[i.rfind(' ') + 1:]
			elif self.p4Version == 2.5 or 2.6:
				logger.debug("Client 'info' specs are:\n%s" % '\n'.join('%s is: %s' % (stat, val) for stat, val in info.iteritems()))
				keys = info.keys() #@UnusedVariable
				for i in info:
					j = j + 1
					clientName = info['clientName']
		
			logger.debug('returning %s' % clientName)
			logger.debug('-- Exiting p4clientDiag --')
			return clientName
		else:
			logger.error('Could not create P4 instance')
			return 0
	
	def p4GetFileType(self):
		"""
		SYNOPSIS: fstat info about the file
		INPUTS:	NONE
		RETURNS: True/False
		Example: mP4.p4GetFileType()
		"""	
		if not self.p4i: self.createP4Instance()
		if self.p4i:
			logger.debug('-- Entered p4GetFileType --')
			if self.isInP4:
				result = self.p4i.run("fstat", self.depotPath)
				logger.debug('-- Exiting p4GetFileType --')
				return result[0]['headType']
			else: return 0
		else:
			logger.error('Could not create P4 instance')


		
if __name__ == '__main__':
	print 'run from Maya session'
else:
	print "common.perforce.pcsP4 imported"
