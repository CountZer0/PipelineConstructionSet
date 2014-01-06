from . import versions
import platform
import os
from . import internal as _internal
import sys
import re

from pymel.util.path import path as _path

def getMayaAppDir(versioned=False):
    """
    Determine the Maya application directory, first by checking MAYA_APP_DIR, then by
    trying OS-specific defaults.
    
    if versioned is True, the current Maya version including '-x64' suffix, if applicable, will be appended.
    """

    pass


def source(file, searchPath=None, recurse=False):
    """
    Looks for a python script in the specified path (uses system path if no path is specified)
    and executes it if it's found
    """

    pass


def getMayaLocation(version=None):
    """
    Get the location of Maya (defined as the directory above /bin)
    
    Uses the $MAYA_LOCATION environment variable and sys.executable path.
    
    If version is passed, will attempt to find a matching Maya location.  If the
    version found by the methods above does not match the requested version, 
    this function uses a simple find/replace heuristic to modify the path and test
    if the desired version exists.  If no matching version is found, returns None
    
    Remember to pass the FULL version (with extension if any) to this function!
    """

    pass


def executeDeferred(func, *args, **kwargs):
    """
    This is a wrap for maya.utils.executeDeferred.  Maya's version does not execute at all when in batch mode, so this
    function does a simple check to see if we're in batch or interactive mode.  In interactive it runs maya.utils.executeDeferred,
    and if we're in batch mode, it just executes the function.
    
    Use this function in your userSetup.py file if:
        1. you are importing pymel there
        2. you want to execute some code that relies on maya.cmds
        3. you want your userSetup.py to work in both interactive and standalone mode
    
    Example userSetup.py file::
    
        from pymel.all import *
        def delayedStartup():
           print "executing a command"
           pymel.about(apiVersion=1)
        mayautils.executeDeferred( delayedStartup )
    
    Takes a single parameter which should be a callable function.
    """

    pass


def getUserScriptsDir():
    pass


def getUserPrefsDir():
    pass


def recurseMayaScriptPath(roots=[], verbose=False, excludeRegex=None, errors='warn', prepend=False):
    """
    Given a path or list of paths, recurses through directories appending to
    the MAYA_SCRIPT_PATH environment variable any found directories containing
    mel scripts
    
    The root directories, if given, are always added to the MAYA_SCRIPT_PATH,
    even if they don't contain any mel scripts.
    
    :Parameters:
        roots
            a single path or list of paths to recurse. if left to its default, will use the current
            MAYA_SCRIPT_PATH values
    
        verobse : bool
            verbose on or off
    
        excludeRegex : str
            string to be compiled to a regular expression of paths to skip.  This regex only needs to match
            the folder name
    """

    pass



_logger = None

sep = ':'


