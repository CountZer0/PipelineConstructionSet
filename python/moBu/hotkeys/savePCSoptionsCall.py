'''
Author: jason
Created: Apr 09, 2012
Module: moBu.hotkeys.savePCSoptionsCall
Purpose: call custom save process
'''

import moBu.core.moBuFile
from pyfbsdk import *

# eclipseSyntax
if False: from pyfbsdk_gen_doc import * #@UnusedWildImport

def savePCSoptionsCall():
	reload(moBu.core.moBuFile)
	app=FBApplication()
	moBu.core.moBuFile.savePCSoptions(app.FBXFileName)

	
	
if __name__ == '__main__':
	print "moBu.hotkeys.savePCSoptionsCall imported" 
else:
	savePCSoptionsCall()