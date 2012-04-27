'''
Author: Jason.Parks
Created: April 25, 2012
Module: menu.Fix this!
Purpose: call FixThis method
'''

from moBu.core import moBuFile

# eclipseSyntax
if False: from pyfbsdk_gen_doc import * #@UnusedWildImport

def run():
	reload(moBuFile)
	moBuFile.MoBuFile().fixThis()

if not __name__ == '__main__':
	print "mobuMenu.Fix this! imported"