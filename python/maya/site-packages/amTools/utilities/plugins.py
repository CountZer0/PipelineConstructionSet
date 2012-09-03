"""
Utility functions for working with plug-ins.

\b Creation \b Info:

\b Donations: http://adammechtley.com/donations/

\b License: The MIT License

Copyright (c) 2011 Adam Mechtley (http://adammechtley.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the 'Software'), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

\namespace amTools.utilities.plugins
"""

import sys, os.path
import maya.cmds as cmds
import amTools.python as ampy

## a list of all plug-ins currently loaded
__allPlugins__ = cmds.pluginInfo(q=True, listPlugins=True)

def verifyPlugin(pluginName, requiredBy):
	"""
	Verify that a particular plug-in is loaded and attempt to load it if it
	cannot be found.
	@param pluginName Name of the plugin without extension
	@param requiredBy __file__ member of the caller
	"""
	try: ampy.indexOf(pluginName, __allPlugins__)
	except:
		try:
			cmds.loadPlugin('%s.py'%pluginName)
			cmds.pluginInfo('%s.py'%pluginName, e=True, autoload=True)
		except:
			sys.stderr.write('Error: Could not locate the %s plug-in. It is required for the %s module.\nPlease ensure that %s.py is located somewhere in your plug-in path.\n' 
				%(pluginName, os.path.basename(requiredBy), pluginName))