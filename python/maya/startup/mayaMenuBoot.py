'''
Author: jason
Created: Jun 20, 2012
Module: maya.startup.mayaMenuBoot
Purpose: boots MayaMenu
'''

############ DEPRECATED, NOT NEEDED WITH EXPANDED userSetup.mel
 
from common.core import globalVariables as gv
import imp
import os
import sys

menuModulePath = '%s/python/maya/core/sysGlobalMenu.py' % gv.toolsLocation
if os.path.exists(menuModulePath):
    sys.path.append(os.path.split(menuModulePath)[0])
else:
    raise Exception("network down")

# debugger
import common.diagnostic.wingdbstub #@UnusedImport

# import sysGlobalMenu
fp, pathname, description = imp.find_module(os.path.basename(menuModulePath).strip('.py'))
startModule = imp.load_module(os.path.basename(menuModulePath).strip('.py'), fp, pathname, description)


# Set Off the creation & Set up
#try:
startModule.MayaMenu().startUp()
#except:
#    print "Failed to fully start MayaMenu."



print "maya.startup.mayaMenuBoot imported"
