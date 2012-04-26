'''
Author: Jason.Parks
Created: Apr 19, 2012
Module: common.build.buildPipeline
Purpose: builds and pushes Toolchain to network
'''

from common.core import globalVariables as gv
import sys

# test gVarInit has been changed back
if not gv.toolsLocation[:6] == '/Users':
	print "Forgot to set gVarInit back"
	sys.exit()
	
from common.diagnostic.pcsLogger import logger
from common.fileIO.pcsPath import Path
from common.perforce import pcsP4
import compileall
import os
import shutil
import xml.etree.ElementTree as ET

# switch to leave .py files on network
_KEEP_NETWORK_PY = False

class PipelineBuild(object):
	"""
	Class to handle building of pipeline
	"""
	
	def __init__(self, remoteBuild=True):
		""" PipelineBuild.__init__():  set initial parameters """
		''' create class
		Params:
			remoteBuild: build for remote location delivery
		Returns: PipelineBuild object
		'''
		super(PipelineBuild, self).__init__()
		self.p4 = pcsP4.P4Lib(maya=0)
		self.networkLoc = gv.toolsLocation
		
		# create in location on network
		self.remoteBuild = remoteBuild
		self.buildDest = Path(gv.toolsLocation).parent + '/AMremoteBuild/ArtMonkey'
		
		
	def buildPCSPipeline(self, compileInstaller=False, pyc=True, removePY=True, removePYC=True):
		''' main pipeline build and push process
			Params: 
				compileInstaller: try to compile APEinstaller.exe
				pyc: create .pyc files in source first
				removePY: remove .py files on network build location
				removePYC: remove local .pyc files in source
			Returns: True/False
		'''
		completeSuccess = True
		
		#TODO: run unitTself.pipeBuildself.pipeBuildself.pipeBuildests

#		# hack gVarInit
#		self.swapGVarInit(direction='REMOTE')
#		
#		#TODO: Compile APE
#		self.compileAPE()
#		
#		# swap back
#		self.p4.p4RevertFile()
##		self.swapGVarInit(direction='PCS')
				
		# create pyc
		if pyc:
			if not self.createPYCfiles(self.pipelineSourceLocation):
				completeSuccess = False

		# copy to network
		if self.remoteBuild:
			# build for remote delivery
			if not self.pushToNetwork(self.buildDest, remote=True):
				completeSuccess = False
			if removePY:
				if not _KEEP_NETWORK_PY:
					if not self.removePYfiles(pathToScrape=self.buildDest):
						completeSuccess = False
			
			# make Mobu/Maya startup files writable
			for pyFile in Path(self.buildDest).walkfiles('*py'):
				if "pcsGlobalSetup.py" in pyFile or "gVarInit.py" in pyFile or "sysGlobalMenu.py" in pyFile:
					# make non-readOnly
					pyFile.makeWritable()
			
			# make PCSstudio.xml writable too
			pcsStudioXML = Path('%s/installData/PCSstudio.xml' % self.buildDest)
			if pcsStudioXML.exists():
				pcsStudioXML.makeWritable(_dir=False)
			
			# clean
			self.clean(self.buildDest)
			
			
		else:
			# push to local network
			if not self.pushToNetwork(self.networkLoc, remote=False):
				completeSuccess = False
		
			if removePY:
				if not _KEEP_NETWORK_PY:
					if not self.removePYfiles(pathToScrape=self.networkLoc):
						completeSuccess = False
		
		if removePYC:
			if not self.removePYfiles(pathToScrape=self.pipelineSourceLocation, optionalExt='.pyc'):
				completeSuccess = False


		
		# provide reminder
		print "Remember to remove unneeded:\n./schemas/.\n\nand change:\n./installData/PCSstudio.xml\n./python/maya/maya/sysGlobalMenu.py\n./python/moBu/startup/pcsGlobalSetup.py\n./python/common/core/gVarInit.py"
		
		#TODO: email T.A.
		
		print "********************************************"
		print "*** Build complete."
		print "********************************************"
		logger.info("********************************************")
		logger.info("*** Build complete.")
		logger.info("********************************************")
		
		return completeSuccess
	
	def clean(self, pNetworkLoc=''):
		_pNetworkLoc = pNetworkLoc
		
		# clean pymel
		pymel102 = Path('%s/python/maya/pymel-1.0.2' % _pNetworkLoc)
		if pymel102.exists():
			print "Cleaning old: %s/." % _pNetworkLoc
			for _dir in pymel102.dirs():
				# make writable
				for _file in _dir.walk():
					_file.makeWritable()
					
				if _dir.exists():
					try:
						_dir.rmtree()
						print "Removing dir: %s" % _dir
					except WindowsError:
						print "Unable to delete dir: '%s'" % _dir
						raise
			# remote top dir too
			pymel102.rmtree()
			
		pymel103 = Path('%s/python/maya/pymel-1.0.3' % _pNetworkLoc)
		
		for _dir in pymel103.dirs():
			if "pymel" not in _dir.basename() and "maya" not in _dir.basename():	#keep 'pymel' & 'maya'!
				print "Cleaning unneeded: %s/." % _dir
				# make writable
				for _file in _dir.walk():
					_file.makeWritable()
					
				if _dir.exists():
					try:
						_dir.rmtree()
						print "Removing dir: %s" % _dir
					except WindowsError:
						print "Unable to delete dir: '%s'" % _dir
						raise
		
		# make writable
		for _file in pymel103.files():
			_file.makeWritable()
			_file.remove()		
		
#		# clean
#		try:
#			Path('%s/.settings' % self.networkLoc).removedirs() # Fails. Read-Only?
#		except WindowsError:
#			print "Failed to remove %s/.settings'" % self.networkLoc



		print "**********************************"
		print "cleaning of '%s' complete." % _pNetworkLoc
		print "**********************************"
		logger.info("**********************************")
		logger.info("cleaning of '%s' complete." % _pNetworkLoc)
		logger.info("**********************************")

	def compileAPE(self):
		
		# add Lib/site-packages
		sys.path.append(r'C:/Python26/Lib/site-packages')

		# confirm paths
		for p in sys.path:
			logger.debug("Path: %s" % p)
		
		# Checkout APEinstaller.exe
		self.p4.fileName = '%s/python/apps/APE/installer/APEinstaller.exe' % self.pipelineSourceLocation
		self.p4.p4CheckOut(desc="buildPipeline")
		
		os.system(r'C:\Python26\python.exe "C:\Python26\PySetup_PCS.py"')

		print "**********************************"
		print "compileAPE complete."
		print "**********************************"
		logger.info("**********************************")
		logger.info("compileAPE complete.")
		logger.info("**********************************")
	
	def createPYCfiles(self, pathToScrape=''):
		''' compiles all .py files to .pyc
			Params:
				pathToScrape: directory to process
			Returns: True/False?
		'''
		if not pathToScrape:
			pathToScrape = self.pipelineSourceLocation
			
		result = compileall.compile_dir(pathToScrape, force=1)
		logger.debug("Result of createPYCfiles() is: %s" % result)
		
		print "**********************************"
		print "Compiling Complete"
		print "**********************************"
		logger.info("**********************************")
		logger.info("Compiling Complete")
		logger.info("**********************************")
		
		return True
	
	@property
	def pipelineSourceLocation(self):
		''' Property, do not use ()
			determine location of pipeline root as specified by .xml schema
			Params: none
			Returns: Path(fileLocation)
		'''

		# Parse Global XML
		globalPCSXMLPath = Path('%s/installData/PCSstudio.xml' % self.networkLoc)
		globalPCSXML = ET.parse(globalPCSXMLPath)
		globalXMLCore = globalPCSXML.getiterator('teamA')[0]
		sourceLoc = globalXMLCore.get('P4_Mode')
		
		return Path(sourceLoc)
	
	def pushToNetwork(self, networkLoc=gv.toolsLocation, remote=True):
		''' copies all files from depot to desired
			network test location
			Params:
				networkLoc: destination location
			Returns: True/False?
		'''

		_pNetworkLoc = Path(networkLoc)		
		result = True
		
		# copy to remote build location, straight-up delete and copy all
		if remote:
			
			# try whole loop 5 times?
			for unused in range(4):
				if _pNetworkLoc.exists():
					# nuke current folders
					print "Cleaning old: %s/." % _pNetworkLoc
					for _dir in _pNetworkLoc.dirs():
						# make writable
						for _file in _dir.walk():
							_file.makeWritable()
						
						# try /python twice
						if 'python' in _dir:
							try:
								_dir.rmtree()
								print "Removing dir: %s" % _dir
							except WindowsError:
								print "Failed once on '%s', trying again . . ." % _dir
							
						if _dir.exists():
							try:
								_dir.rmtree()
								print "Removing dir: %s" % _dir
							except WindowsError:
								print "Unable to delete dir: '%s'" % _dir
								raise
					# remote top dir too
					_pNetworkLoc.rmtree()
		
			# copy to network
			print "Copying '%s' dir to '%s'" % (self.pipelineSourceLocation, _pNetworkLoc)
			try:
				Path(self.pipelineSourceLocation).copytree(_pNetworkLoc)
			except WindowsError:
				print "Process locked trying to copy to: '%s'. Please just run again." % _pNetworkLoc
				raise
			except shutil.Error as e:
				print "Permission denied for file/folder: '%s'" % e[0]
			
			# success?
			if not _pNetworkLoc.exists():
				logger.error("Failed to copy to remote location build: '%s'" % _pNetworkLoc)
				
			# copy/move dataResources sub-folder
			for _dir in Path('%s/dataResources' % _pNetworkLoc).dirs():
				if _dir.namebase == 'installData':
					Path(_dir).move(_pNetworkLoc)

		
		# have to dance around data and installData dirs
		else:
			if _pNetworkLoc.exists():
				# nuke current folders
				print "Cleaning old: %s/." % _pNetworkLoc
				for _dir in _pNetworkLoc.dirs():
					if "data" not in _dir:	#keep 'data' & 'installData'!
						# make writable
						for _file in _dir.walk():
							_file.makeWritable()
						
						# try /python twice
						if 'python' in _dir:
							try:
								_dir.rmtree()
							except WindowsError:
								print "Failed once on '%s', trying again . . ." % _dir
							
						if _dir.exists():
							try:
								_dir.rmtree()
								print "Removing dir: %s" % _dir
							except WindowsError:
								print "Unable to delete dir: '%s'" % _dir
								raise
		
					# clean dataResources
					elif _dir == 'dataResources':
						# make writable
						for _file in _dir.walk():
							_file.makeWritable()
						print "Removing dir: %s" % _dir
						_dir.rmtree()
			
			# copy to network
			tempNetworkLoc = Path('%s/temp' % _pNetworkLoc)
			
			# copy
			print "Copying '%s' dir to '%s'" % (self.pipelineSourceLocation, tempNetworkLoc)
			try:
				Path(self.pipelineSourceLocation).copytree(tempNetworkLoc)
			except WindowsError:
				print "Process locked trying to copy to: '%s'. Please just run again." % tempNetworkLoc
			except shutil.Error as e:
				print "Permission denied for file/folder: '%s'" % e[0]
				
			# move first-layer sub-dirs from '/temp' up to parent
			for _dir in tempNetworkLoc.dirs():
				try:
					if "data" not in _dir:	#skip 'data' & 'installData'!
						Path(_dir).move(_pNetworkLoc)
				except WindowsError:
					print "failed on: " + _dir
				except shutil.Error:
					print "failed to copy from dir: '%s', already exists?" % _dir
					raise
		
			# nuke tempNetworkLoc
			if tempNetworkLoc.exists():
				print "Cleaning old: %s" % tempNetworkLoc
				# make writable
				for _file in tempNetworkLoc.walk():
					_file.makeWritable()
				print "Removing tree: %s" % tempNetworkLoc
				tempNetworkLoc.rmtree()			
		
		############# start cleaning ##############
		
		# clean un-needed root folders
		unNeededRoot = ['dataResources', 'docs', 'logs']
		for unNeeded in unNeededRoot:
			print "Cleaning un-needed: %s/%s" % (_pNetworkLoc, unNeeded)
			for _dir in Path(_pNetworkLoc).dirs():
				if _dir.namebase == unNeeded:
					# make writable
					for _file in _dir.walk():
						_file.makeWritable()
					print "Removing dir: %s" % _dir
					_dir.rmtree()

		# clean unitTests
		print "Cleaning un-needed: %s/python/unitTests" % _pNetworkLoc
		for _dir in Path('%s/python' % _pNetworkLoc).dirs():
			if _dir.namebase == 'unitTests':
				# make writable
				for _file in _dir.walk():
					_file.makeWritable()
				print "Removing dir: %s" % _dir
				_dir.rmtree()

		# clean non-maya/pymel dirs from pymels
		print "Cleaning un-needed: %s/python/maya/pymel" % _pNetworkLoc
		pyMelDirs = ['pymel-1.0.2', 'pymel-1.0.3']
		for pyMelDir in pyMelDirs:
			if not Path('%s/python/maya/%s' % (_pNetworkLoc, pyMelDir)).exists():
				logger.error("No pymel dir found, probably failed copy earlier.")
				if not _dir.namebase == 'maya' and not _dir.namebase == 'pymel':
					# make writable
					for _file in _dir.walk():
						_file.makeWritable()
					print "Removing dir: %s" % _dir
					_dir.rmtree()
				for _file in Path('%s/python/maya/%s' % (_pNetworkLoc, pyMelDir)).files():
					_file.makeWritable()
					print "Removing file: %s" % _file
					_file.remove()
		
		# clean apps
		print "Cleaning un-needed: %s/python/apps" % _pNetworkLoc
		for _dir in Path('%s/python/apps' % _pNetworkLoc).dirs():
			if not _dir.namebase == 'APE':
				# make writable
				for _file in _dir.walk():
					_file.makeWritable()
				print "Removing dir: %s" % _dir
				_dir.rmtree()

		# clean misc
		print "Cleaning un-needed project files in : %s" % _pNetworkLoc
		unNeededRoot = ['.project', '.pydevproject', 'artMonkey.wpr', 'artMonkey.wpu']
		for unNeeded in unNeededRoot:
			for _file in _pNetworkLoc.files():
				if _file.basename() == unNeeded:
					# make writable
					_file.makeWritable()
					print "Removing file: %s" % _file
					_file.remove()
		
		print "**********************************"
		print "Push To Network complete."
		print "**********************************"
		logger.info("**********************************")
		logger.info("Push To Network complete.")
		logger.info("**********************************")

		return result
	
	def removePYfiles(self, pathToScrape='', optionalExt='.py'):
		''' removes all .py files from directory
		NOTE: may need to make non-Read only
			Params:
				pathToScrape: directory to process
				optionalExt: can remove .pyc if needed
			Returns: True/False?
		'''
		completeSuccess = True
		logger.info("Removing %s files from : '%s'" % (optionalExt, pathToScrape))				
		
		if not pathToScrape:
			pathToScrape = self.networkLoc
		
		count = 0
		for pyFile in Path(pathToScrape).walkfiles('*%s' % optionalExt):
			# skip Mobu/Maya startup files
			if "pcsGlobalSetup.py" in pyFile or "gVarInit.py" in pyFile or "sysGlobalMenu.py" in pyFile:
				# make non-readOnly
				pyFile.makeWritable()
				continue
			# template files need to stay
			if not "mayaMenuBoot.py" in pyFile:
				if not "teamMenu.py" in pyFile and not "teamMenuBoot.py" in pyFile:
						try:
							if Path(pyFile).isReadOnly:
								Path(pyFile).makeWritable()
							os.remove(pyFile)
							logger.debug("Removing: '%s'" % pyFile)
							count += 1
						except:
							logger.info("Failed to remove: '%s'" % pyFile)
							completeSuccess = False
						
		print "Removed %d %s files from : '%s'" % (count, optionalExt, pathToScrape)
		logger.info("Removed %d %s files from : '%s'" % (count, optionalExt, pathToScrape))
		
		print "**********************************"
		print "Remove %s complete." % optionalExt
		print "**********************************"
		logger.info("**********************************")
		logger.info("Remove %s complete." % optionalExt)
		logger.info("**********************************")
						
		return completeSuccess

	def swapGVarInit(self, direction='PCS'):
		# swap 'em
		gVarFile = '%s/python/common/core/gVarInit.py' % self.pipelineSourceLocation
		
		# Checkout APEinstaller.exe
		self.p4.fileName = gVarFile
		self.p4.p4CheckOut(desc="buildPipeline_Temp")
		
		try:
			f = open(gVarFile, "r")
			gVarContent = f.readlines()
			f.close()
			newLines = []
			for line in gVarContent:
				if "remoteLoc" in line:
					if '#@%s' % direction in line:
						newLines.append(line.replace('#r', 'r'))
					else:
						newLines.append('#%s' % line)
				else:
					newLines.append(line)
			
			f = open(gVarFile, "w")
			f.writelines(newLines)
			f.close()
		except:
			logger.info("Failed to mod '%s'" % gVarFile)
			print "Failed to mod '%s'" % gVarFile
			
			# revert
			self.p4.p4RevertFile()
		
		print "**********************************"
		print "swapGVarInit complete."
		print "**********************************"
		logger.info("**********************************")
		logger.info("swapGVarInit complete.")
		logger.info("**********************************")
	
def run():	
	# default
	PipelineBuild(remoteBuild=True).buildPCSPipeline(compileInstaller=False, pyc=True, removePY=True, removePYC=True)
	
	# no pyc removal
#	PipelineBuild(remoteBuild=True).buildPCSPipeline(compileInstaller=False, pyc=True, removePY=True, removePYC=False)

	# no py removal
#	PipelineBuild(remoteBuild=True).buildPCSPipeline(compileInstaller=False, pyc=False, removePY=False, removePYC=False)
	
	# no pyc
#	PipelineBuild(remoteBuild=True).buildPCSPipeline(compileInstaller=False, pyc=False, removePY=True, removePYC=False)

	# local network
#	PipelineBuild(remoteBuild=False).buildPCSPipeline(compileInstaller=False, pyc=False, removePY=False, removePYC=True)

run()

if not __name__ == "__main__":
	print "common.build.buildPipeline imported"
