'''
Author: Jason.Parks
Created: May 06, 2012
Module: menu.SystemPaths
Purpose: print sys.paths
'''

import sys

# eclipseSyntax
if False: from pyfbsdk_gen_doc import * #@UnusedWildImport

def run():
	for p in sys.path:
		print p

if not __name__ == '__main__':
	print "menu.SystemPaths imported"