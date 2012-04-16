'''
Author: jason
Created: Apr 15, 2012
Module: moBu.hotkeys.loadPCSoptionsCall
Purpose: call to custom load process
'''

import moBu.core.mobuFile

# eclipseSyntax
if False: from pyfbsdk_gen_doc import *


def loadPCSoptionsCall():
	reload(moBu.core.mobuFile)
	moBu.core.mobuFile.loadPCSoptions()
	pass
	
	
if __name__ == '__main__':
	print "moBu.hotkeys.loadPCSoptionsCall imported" 
else:
	loadPCSoptionsCall()