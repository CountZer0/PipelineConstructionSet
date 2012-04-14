'''
Author: jason
Created: Apr 09, 2012
Module: 
Purpose: Adds paths to MoBu env
'''

import getpass
import platform
import re
import sys
import xml.etree.ElementTree as ET
import inspect
import os

PCSglobal = "/Users/jason/remotePCS/PCSglobal"	#Must match networkLoc path in gVarInit

# get user's main main Project tool path
userXML = ET.parse("%s/data/%s/PCSuser.xml" % (PCSglobal, getpass.getuser()))
userXMLcore = userXML.getiterator('Core')[0]
userToolRoot = userXMLcore.get('PCSprojectToolPath')
userTeam = userXMLcore.get('PCSactiveTeam')

# get extra relative paths to add for MotionBuilder
globalXML = ET.parse("%s/installData/PCSstudio.xml" % PCSglobal)
globalXMLcore = globalXML.getiterator('Core')[0]
mobuRelPaths = eval(globalXMLcore.get('MoBuPaths'))

# get team tool path
try:
	teamTBXML = ET.parse("%s/installData/%sTB.xml" % (PCSglobal, userTeam))
	teamTBXMLcore = teamTBXML.getiterator('Core')[0]
	teamTBroot = teamTBXMLcore.get('teamTBRoot')

	# add Team ToolBox path
	sys.path.append('%s/python' % teamTBroot)
except: print 'No team menu setup yet'

# get bitVersion
bit = 'win32'
if platform.architecture()[0] == '64bit': bit = 'win64'


# add to sys.path
for mobuRelPath in mobuRelPaths:
	
	# add correct bit sub-folder
	if re.search('perforce', mobuRelPath):
		mobuRelPath = '%s/%s' % (mobuRelPath, bit)

	# add correct bit sub-folder
	if re.search('PIL', mobuRelPath):
		mobuRelPath = '%s/%s' % (mobuRelPath, bit)
	
	# add paths
	sys.path.append('%s/%s' % (userToolRoot, mobuRelPath))




# start debugging
import diagnostic.wingdbstub #@UnusedImport

from diagnostics.pcsLogger import moBuLogger

# start PCS Global menu
from moBu.sysGlobalMenu import MobuMenu
try:
	MobuMenu().createTool()
except:
	moBuLogger.error("Failed to create PCSglobal menu")

#moBuLogger.info('Ran pcsGlobalSetup.py')

#--------------------------------------------
# report run from location
def tempFunc():
	pass
fileLocation = os.path.dirname(inspect.getsourcefile(tempFunc))
moBuLogger.info("Ran pcsGlobalSetup.py from '%s'" % fileLocation)