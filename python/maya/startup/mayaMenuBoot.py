"""
boots Maya menu

*Author:*
    * Jason.Parks, jason@continuityai.com, 1/8/14 4:55 PM
"""

############ DEPRECATED, NOT NEEDED WITH EXPANDED userSetup.mel

# Python std lib
import imp
import os
import sys

# common lib
import common.core

menuModulePath = '%s/python/maya/core/sysGlobalMenu.py' % common.core.globalVariables.toolsLocation
if os.path.exists(menuModulePath):
    sys.path.append(os.path.split(menuModulePath)[0])
else:
    raise Exception("network down")

# debugger
#import common.diagnostic.wingdbstub #@UnusedImport

# import sysGlobalMenu
fp, pathname, description = imp.find_module(os.path.basename(menuModulePath).strip('.py'))
startModule = imp.load_module(os.path.basename(menuModulePath).strip('.py'), fp, pathname, description)


# Set Off the creation & Set up
#try:
startModule.MayaMenu().startUp()
#except:
#    print "Failed to fully start MayaMenu."


print "maya.startup.mayaMenuBoot imported"
