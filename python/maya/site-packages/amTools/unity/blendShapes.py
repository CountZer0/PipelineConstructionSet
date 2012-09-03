"""
Export sparse blendShape data from the Maya scene when Unity exports it to FBX.
Note that this tool only supports models with fewer than 65536 vertices, which
is all that Unity's importer supports. It does not yet have support for
in-between targets, and it assumes that 1.0 is the max value for any particular
shape.

\b Requirements: Unity Pro with ImportBlendShapes.cs editor script and all its
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

\namespace amTools.unity.blendShapes
"""

import re
import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMaya as om

## a premultiplied division to expedite computation
__oneOverTwoFiftyFive = (1.0/255.0)

def exportBlendShapes():
	"""Exports sparse blendShape data from the scene for each mesh with a
	blendShape deformer in its history. This is accomplished by duplicating
	the mesh and tagging vertices in the duplicate using vertex colors. The
	duplicate then stores all of the data as user properties."""
	
	# find all of the potential models in the scene
	models = om.MSelectionList()
	for model in cmds.ls(transforms=True): models.add(model)
	
	# store a dictionary mapping models whose shapes have a blendShape upstream to all of their blendShape nodes
	modelsWithBlendShapeDeformers = {}
	dagPath = om.MDagPath()
	iter = om.MItSelectionList(models)
	while not iter.isDone():
		iter.getDagPath(dagPath)
		model = om.MDagPath(dagPath)
		try:
			# ensure the current transform has a shape node
			dagPath.extendToShape()
			# search upstream from shape for all blendShape nodes
			dg = om.MItDependencyGraph(dagPath.node(), om.MFn.kBlendShape, om.MItDependencyGraph.kUpstream)
			while not dg.isDone():
				# add the blendShape nodes to a list in the dictionary
				if not modelsWithBlendShapeDeformers.has_key(model):
					modelsWithBlendShapeDeformers[model] = []
				modelsWithBlendShapeDeformers[model].append(dg.currentItem())
				dg.next()
		except: pass
		iter.next()
	
	# create tagged duplicates for each model with blendShapes and its targets
	for model in modelsWithBlendShapeDeformers.keys():
		
		# delete non-deformer history on the model in order to collapse intermediate nodes
		# model will come into Unity wrong, but at least not with ugly error
		cmds.select(model.partialPathName())
		mel.eval('doBakeNonDefHistory( 1, {"prePost" });')
		cmds.select(cl=True)
		
		# zero all blendShape target weights on the model
		for blendNode in modelsWithBlendShapeDeformers[model]:
			fn = om.MFnDependencyNode(blendNode)
			aliases = cmds.aliasAttr(fn.name(), q=True)
			for alias in aliases:
				# skip non-weight attributes
				if not re.match('weight\[[0-9]+\]', alias): continue
				dest = '%s.%s'%(fn.name(), alias)
				source = cmds.listConnections(dest, p=True)
				if source: cmds.disconnectAttr(source[0], dest)
				cmds.setAttr(dest, 0.0)
		
		# duplicate the base mesh and indicate that it is the base index map
		taggedBaseMesh = cmds.duplicate(model.partialPathName())[0]
		taggedBaseMesh = cmds.rename(taggedBaseMesh, model.partialPathName()+'__blendShapeIndexMap')
		customAttrs = cmds.listAttr(taggedBaseMesh, ud=True)
		if (customAttrs):	
			for attr in customAttrs:
				try: cmds.deleteAttr(taggedBaseMesh, at=attr)
				except: pass
		cmds.addAttr(taggedBaseMesh, ln='isBlendShapeMapFor', dt='string')
		cmds.setAttr('%s.isBlendShapeMapFor'%taggedBaseMesh, model.partialPathName(), type='string')
		
		# tag each vertex in the base shape duplicate
		dagPath = om.MDagPath()
		sel = om.MSelectionList()
		sel.add(taggedBaseMesh)
		sel.getDagPath(0, dagPath)
		dagPath.extendToShape()
		tagMesh(dagPath)
		
		# duplicate the tagged base mesh to create the seamless base mesh
		seamlessBaseMesh = cmds.duplicate(taggedBaseMesh)[0]
		seamlessBaseMesh = cmds.rename(seamlessBaseMesh, model.partialPathName()+'__seamlessBaseMesh')
		for attr in cmds.listAttr(seamlessBaseMesh, ud=True):
			try: cmds.deleteAttr(seamlessBaseMesh, at=attr)
			except: pass
		makeSeamless(seamlessBaseMesh)
		# link seamless mesh to tagged base shape
		cmds.addAttr(seamlessBaseMesh, ln='isSeamlessBaseMeshFor', dt='string')
		cmds.setAttr('%s.isSeamlessBaseMeshFor'%seamlessBaseMesh, taggedBaseMesh, type='string')
		# make the seamless base mesh a child of the tagged base mesh, in order to avoid creating additional roots
		cmds.parent(seamlessBaseMesh, taggedBaseMesh)
		
		# create a color-tagged copy of each target, linked back to the tagged base shape via user properties
		for blendNode in modelsWithBlendShapeDeformers[model]:
			fn = om.MFnDependencyNode(blendNode)
			aliases = cmds.aliasAttr(fn.name(), q=True)
			for alias in aliases:
				# skip weight attributes
				if re.match('weight\[[0-9]+\]', alias): continue
				# create a duplicate of the composite shape and convert it into a seamless mesh
				cmds.setAttr('%s.%s'%(fn.name(), alias), 1.0)
				taggedTarget = cmds.duplicate(model.partialPathName())[0]
				attrs = cmds.listAttr(taggedTarget, ud=True)
				if (attrs):
					for attr in attrs:
						try: cmds.deleteAttr(taggedTarget, at=attr)
						except: pass
				taggedTarget = cmds.rename(taggedTarget, '%s__blendShapeTarget__%s'%(model.partialPathName(), alias))
				makeSeamless(taggedTarget)
				cmds.setAttr('%s.%s'%(fn.name(), alias), 0.0)
				# tag the duplicated target
				dagPath = om.MDagPath()
				sel = om.MSelectionList()
				sel.add(taggedTarget)
				sel.getDagPath(0, dagPath)
				dagPath.extendToShape()
				tagMesh(dagPath)
				# link target to tagged base shape
				cmds.addAttr(taggedTarget, ln='isBlendShapeTargetFor', dt='string')
				cmds.setAttr('%s.isBlendShapeTargetFor'%taggedTarget, taggedBaseMesh, type='string')
				# make the tagged mesh a child of the tagged base mesh, in order to avoid creating additional roots
				cmds.parent(taggedTarget, taggedBaseMesh)
	
		# make the tagged mesh a child of the original, in order to avoid creating additional roots
		cmds.parent(taggedBaseMesh, model.partialPathName())

def makeSeamless(meshName):
	"""Makes a supplied mesh "seamless" in Unity by deleting its UV coordinates, smoothing normals, triangulating, and clearing material assignments"""
	# clear uvs so there are no seams or tangents
	uvs = cmds.polyUVSet(meshName, q=True, auv=True)
	for uv in uvs:
		try: cmds.polyUVSet(meshName, e=True, uvSet=uv, delete=True)
		except: pass
	uvSet = cmds.polyUVSet(meshName, q=True, auv=True)[0]
	sel = om.MSelectionList()
	sel.add(meshName)
	dagPath = om.MDagPath()
	sel.getDagPath(0, dagPath)
	fn = om.MFnMesh(dagPath)
	fn.clearUVs(uvSet)
	# smooth normals so there are no normal separations
	cmds.polySoftEdge(meshName, a=180, ch=True)
	# triangulate geometry
	cmds.polyTriangulate(meshName)
	# apply a single material so there are no submesh separations
	cmds.sets(meshName, e=True, forceElement='initialShadingGroup')
	# delete all history
	cmds.delete(meshName, ch=True)
	cmds.select(clear=True)

def tagMesh(meshDagPath):
	"""Tag the points on the supplied mesh with vertex colors to store Maya's point order"""
	# clear any extant vertex colors
	try: cmds.polyColorSet(meshDagPath.partialPathName(), e=True, delete=True, acs=True)
	except: pass
	
	# encode each point index in the red and green channels of each point's color value
	meshFn = om.MFnMesh(meshDagPath)
	vertexCount = om.MIntArray()
	vertexList = om.MIntArray()
	meshFn.getVertices(vertexCount, vertexList)
	vertexColors = om.MColorArray(meshFn.numVertices(), om.MColor(0.0,0.0,1.0,1.0))	
	
	for i in xrange(meshFn.numVertices()):
		col = om.MColor(tagIndexToColor(i))
		vertexColors[i].r = col.r
		vertexColors[i].g = col.g
	meshFn.createColorSetWithName('blendShapeIndexMap')
	meshFn.setColors(vertexColors, 'blendShapeIndexMap')
	meshFn.assignColors(vertexList)

def tagIndexToColor(i):
	"""Encode an integer as an MColor value."""
	# get 4 complete hex digits to represent i
	asHex = hex(i)
	digits = asHex[asHex.find('x')+1::][::-1]
	while len(digits) < 4: digits += '0'
	digits = digits[::-1]
	# pack hex digits into the red and green color values
	return om.MColor(
		int('0x%s'%digits[2:4], 16)*__oneOverTwoFiftyFive,
		int('0x%s'%digits[0:2], 16)*__oneOverTwoFiftyFive,
		1.0,
		1.0)

def colorToTagIndex(col):
	"""Convert an MColor value to a tag index."""
	r = hex(int(round(col.r*255.0)))[::-1]
	while len(r) < 4: r += '0'
	r = r[::-1]
	g = hex(int(round(col.g*255.0)))[::-1]
	while len(g) < 4: g += '0'
	g = g[::-1]
	return int('0x%s%s'%(g[g.find('x')+1::], r[r.find('x')+1::]), 16)