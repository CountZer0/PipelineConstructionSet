"""
A package of modules to add custom attributes to objects to describe different
parts of animation rigs. These user properties are stored in a way that they
are to be parsed by Unity's AssetPostprocessor in order to transport a rig into
Unity for evaluation at run-time.

\b Requirements: Unity Pro with ImportMayaRigs.cs editor script and all its
dependencies.

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

\namespace amTools.unity.rigs
"""

import constraints
import customNodes
import expressions

def reloadAll():
	"""Reload all modules in this package."""
	reload(constraints)
	reload(customNodes)
	reload(expressions)

def exportRigs():
	"""Add user properties to objects."""
	customNodes.exportNodes()
	constraints.exportConstraints()
	expressions.exportExpressions()