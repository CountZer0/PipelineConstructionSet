'''
Author: Jason.Parks
Created: April 25, 2012
Module: menu.Load
Purpose: call MobuFile().loadPCSoptions()
'''

from moBu.core import moBuFile

# eclipseSyntax
if False: from pyfbsdk_gen_doc import * #@UnusedWildImport

def run():
	reload(moBuFile)
	moBuFile.MoBuFile().loadPCSoptions()

if not __name__ == '__main__':
	print "menu.Load imported"