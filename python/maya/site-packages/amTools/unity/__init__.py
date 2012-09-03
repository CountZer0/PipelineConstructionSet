"""
A collection of modules for making modifications to the Maya scene during FBX
export to Unity.

\b Usage:
Comment or uncomment the functions in modifyExport() as desired. Call
modifyExport() from FBXMayaExport.mel or in your scene before manually
exporting to FBX. To call from FBXMayaExport.mel, change the following line:
\verbatim file -force -o $filename; \endverbatim
to this: 
\verbatim
file -force -o $filename;

// begin customization
python("try: import amTools.unity as unity\nexcept: pass");
python("try:\n\treload(unity)\n\tunity.reloadAll()\nexcept: pass");
python("try: unity.modifyExport()\nexcept: pass");
// end customization \endverbatim

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

\namespace amTools.unity
"""

import maya.cmds as cmds
import maya.mel as mel
import blendShapes
import models
import rigs

def reloadAll():
	"""Reload all modules in this package."""
	reload(blendShapes)
	reload(models)
	reload(rigs)
	rigs.reloadAll()
	return
	
def modifyExport():
	"""Entry point for all desired functions. It is advised you use the AMTools
	menu in Maya to enable and disable features."""
	rigs.exportRigs() # Export Rigs
	blendShapes.exportBlendShapes() # Export BlendShapes
	#models.deleteNonDeformerHistory() # Delete Non-Deformer History
	#models.triangulateAll() # Triangulate All
	return