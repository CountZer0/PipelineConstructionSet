'''
Author: jason
Created: April 25, 2012
Module: menu.RemoveNameSpace
Purpose: removes namespace from all components
'''

from moBu.core import moBuNamespace

# eclipseSyntax
if False: from pyfbsdk_gen_doc import * #@UnusedWildImport

def run():
    moBuNamespace.MoBuNamespace().removeAllNamespacesFromScene()

print "menu.RemoveNameSpace imported" 