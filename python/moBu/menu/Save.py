'''
Author: Jason.Parks
Created: April 25, 2012
Module: menu.Save
Purpose: call MobuFile().loadPCSoptions()
'''

from moBu.core import moBuFile
from moBu.core import moBuCore

# eclipseSyntax
if False: from pyfbsdk_gen_doc import * #@UnusedWildImport

def run():
	# determine sceneName
	scenePathFile = moBuCore.MoBuCore().sceneName
	reload(moBuFile)
	moBuFile.MoBuFile().loadPCSoptions(scenePathFile)

if not __name__ == '__main__':
	print "menu.Save imported"