'''
Author: Jason.Parks
Created: April 25, 2012
Module: menu.ConnectToWing
Purpose: call diagnostic.debug.connectToWing
'''

from common.diagnostic import debug

# eclipseSyntax
if False: from pyfbsdk_gen_doc import * #@UnusedWildImport

def run():
	reload(debug)
	debug.Debug().connectToWing()

if not __name__ == '__main__':
	print "menu.ConnectToWing imported"