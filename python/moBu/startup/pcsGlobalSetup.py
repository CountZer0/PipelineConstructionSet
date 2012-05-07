'''
Author: jason
Created: Apr 15, 2012
Module: startup.pcsGlobalSetup
Purpose: Adds paths to Mobu env
'''
#import getpass #@UnresolvedImport
import os
import platform #@UnresolvedImport
import re #@UnresolvedImport
import sys
import xml.etree.ElementTree as ET #@UnresolvedImport
import inspect #@UnresolvedImport
from pyfbsdk import FBMessageBox, FBSystem #@UnresolvedImport

# assumes system/user PYTHONPATH contains path to ./PipelineConstructionSet/python
try:
	import common.core.globalVariables as gv
except:
	FBMessageBox("PYTHONPATH setup", "Please add system variable PYTHONPATH to\nlocation of ./PipelineConstructionSet/python", "OK", None, None, 1)

_MAINTENANCE = False

# find app version
version = None
appPath = FBSystem().ApplicationPath
if len(appPath) > 2:
	appName = appPath.split('\\')[3]
	if len(appName) > 0:
		version = int(appName.split(' ')[1])
if not version:
	FBMessageBox("Version failure", "Failed to find MoBu version.\n\nSkipping ArtMonkey boot.", "OK", None, None, 1, False)
else:	
	if _MAINTENANCE:
		FBMessageBox("Performing Maintenance", "Sorry, ArtMonkey is temporarily down for maintenance.\n\nShould be back up within the hour.", "OK", "Darn", "That Sucks", 1, False)
	else:
		#--------------------------------------------
		# get extra relative paths to add for MotionBuilder
		pcsXML = ET.parse('%s/pcsSchema.xml' % gv.schemaLocation)
		pcsXMLcore = pcsXML.getiterator('Core')[0]
		mobuRelPaths = eval(pcsXMLcore.get('moBuPaths'))
		
		#--------------------------------------------
		# get bitVersion
		bit = 'win32'
		if platform.architecture()[0] == '64bit': bit = 'win64'
		
		# now MoBu-specific
		for mobuRelPath in mobuRelPaths:
			
			# add correct bit sub-folder
			if re.search('perforce', mobuRelPath) or re.search('PIL', mobuRelPath):
				mobuRelPath = '%s/%s' % (mobuRelPath, bit)
		
			# add paths from userXML toolpath
			sys.path.append('%s/python/moBu/%s' % (gv.toolsLocation, mobuRelPath))
		
		#--------------------------------------------
		# add PyMoBu path
		pyMoBuVer = eval(pcsXMLcore.get('pyMoBuVer'))['%s' % version]
		sys.path.append('%s/python/moBu/site-packages/%s' % (gv.toolsLocation, pyMoBuVer))
				
		#--------------------------------------------
		# start debugging
		import common.diagnostic.wingdbstub #@UnusedImport
		
		#--------------------------------------------
		from common.diagnostic.pcsLogger import moBuLogger
		# do main import loop
		try:
			from moBu.core.sysGlobalMenu import MoBuToolsMenu
		except:
			moBuLogger.info(sys.exc_info())
			moBuLogger.errorDialog("Failed to import moBu and start ArtMonkey")
			print "Failed to import moBu. Error: "
			print sys.exc_info()
		
		#--------------------------------------------
		# start ArtMonkey Global menu
		try:
			MoBuToolsMenu().createTool()
		except:
			moBuLogger.error("Failed to create Art Monkey menu")
		
		#--------------------------------------------
		# report run from location
		def tempFunc():
			pass
		fileLocation = os.path.dirname(inspect.getsourcefile(tempFunc))
		moBuLogger.info("Ran pcsGlobalSetup.py from '%s'" % fileLocation)
