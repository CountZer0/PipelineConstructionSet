'''
Author: Jason.Parks
Created: April 25, 2012
Module: menu.SaveAs
Purpose: call MobuFile().savePCSoptions()
'''

from moBu.core import moBuFile

# eclipseSyntax
if False: from pyfbsdk_gen_doc import * #@UnusedWildImport

def run():
	reload(moBuFile)
	moBuFile.MoBuFile().savePCSoptions(pathFile=None, quiet=False, pOptions=None, p4=False)

if not __name__ == '__main__':
	print "menu.SaveAs imported"