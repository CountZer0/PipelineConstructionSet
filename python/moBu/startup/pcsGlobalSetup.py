'''
Author: jason
Created: Apr 15, 2012
Module: startup.pcsGlobalSetup
Purpose: Adds paths to Mobu env
'''


import getpass #@UnresolvedImport
import os
import platform #@UnresolvedImport
import re #@UnresolvedImport
import sys
import xml.etree.ElementTree as ET #@UnresolvedImport
import inspect #@UnresolvedImport


PCSglobal = "/Users/jason/remotePCS/ArtMonkey"	#Must match networkLoc path in gVarInit

#--------------------------------------------
# get user's main main Project tool path
userXML = ET.parse("%s/data/%s/PCSuser.xml" % (PCSglobal, getpass.getuser()))
userXMLcore = userXML.getiterator('Core')[0]
userToolRoot = userXMLcore.get('PCSprojectToolPath')

#--------------------------------------------
# get extra relative paths to add for MotionBuilder
globalXML = ET.parse("%s/installData/PCSstudio.xml" % PCSglobal)
globalXMLcore = globalXML.getiterator('Core')[0]
mobuRelPaths = eval(globalXMLcore.get('MoBuPaths'))

#--------------------------------------------
# get bitVersion
bit = 'win32'
if platform.architecture()[0] == '64bit': bit = 'win64'

#--------------------------------------------
# add to sys.path
for mobuRelPath in mobuRelPaths:
	
	# add correct bit sub-folder
	if re.search('perforce', mobuRelPath):
		mobuRelPath = '%s/%s' % (mobuRelPath, bit)

	# add correct bit sub-folder
	if re.search('PIL', mobuRelPath):
		mobuRelPath = '%s/%s' % (mobuRelPath, bit)
	
	# add paths from userXML toolpath
	sys.path.append('%s/%s' % (userToolRoot, mobuRelPath))

#--------------------------------------------
# start debugging
import diagnostic.wingdbstub #@UnusedImport

from diagnostic.pcsLogger import moBuLogger

#--------------------------------------------
# do main import loop
try:
	from moBu.sysGlobalMenu import MobuArtMonkeyMenu
except:
	moBuLogger.info(sys.exc_info())
	moBuLogger.errorDialog("Failed to import moBu and start ArtMonkey")
	print "Failed to import moBu. Error: "
	print sys.exc_info()

#--------------------------------------------
# start ArtMonkey Global menu
try:
	MobuArtMonkeyMenu().createTool()
except:
	moBuLogger.error("Failed to create Art Monkey menu")

#--------------------------------------------
# report run from location
def tempFunc():
	pass
fileLocation = os.path.dirname(inspect.getsourcefile(tempFunc))
moBuLogger.info("Ran pcsGlobalSetup.py from '%s'" % fileLocation)