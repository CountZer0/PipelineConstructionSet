"""
start: voxelize meshes v.2
this script turns the selected meshes into cubes
over the current timeline range.

From Maya-Python mailing list
http://zoomy.net/2010/02/25/voxelize-meshes-script-v2
http://groups.google.com/group/python_inside_maya/browse_thread/thread/3f973f5bddf35e15#

TODO: Implement Dean's critique of this module
the overall algorithm being used to voxelize the mesh is flawed.
It shoots rays along the *edges* of the voxels then places the *centers* of the
cubes it creates at the intersection points, That guarantees a halo of 
half-empty voxels around the mesh.
Also, the shooting of rays is pretty hit-or-miss. There could be lots of 
geometry within a given voxel but none of it happens to lie along the ray, 
leading to that voxel being incorrectly discarded. A better algorithm would 
be to iterate over the mesh's triangles and clip them against the voxel boundaries,
which is trivial given that the voxels are axis-aligned.
"""

import pymel.core.context as context
import pymel.core.rendering as rendering
import maya.cmds as cmds
import pymel.util as util
import pymel.core.runtime as runtime
import pymel.api as api
import pymel.core.system as system
import pymel.core.uitypes as ui
import pymel.core.uitypes as uitypes
import pymel.core.nodetypes as nodetypes
import pymel.core.nodetypes as nt
import pymel.core.animation as animation
import pymel.core.datatypes as dt
import pymel.core.language as language
import maya.OpenMaya as om
import pymel.core.windows as windows
import pymel.core.modeling as modeling
import pymel.core.effects as effects

from pymel.core.general import *
from pymel.core.windows import *
from pymel.core.system import *
from pymel.core.animation import *
from pymel.core.context import *
from pymel.core.modeling import *
from pymel.core.other import *
from pymel.core.rendering import *
from pymel.core.effects import *

from pymel.core.language import Env
from pymel.core.language import callbacks
from pymel.core.language import MelConversionError
from pymel.core.language import MelError
from pymel.core.language import Mel
from pymel.core.language import evalNoSelectNotify
from pymel.core.language import Catch
from pymel.core.language import getProcArguments
from pymel.core.language import pythonToMel
from pymel.core.language import stackTrace
from pymel.core.language import resourceManager
from pymel.core.language import isValidMelType
from pymel.core.language import getMelType
from pymel.core.language import conditionExists
from pymel.core.language import OptionVarList
from pymel.core.language import MelUnknownProcedureError
from pymel.core.language import getLastError
from pymel.core.language import MelArgumentError
from pymel.core.language import evalEcho
from pymel.core.language import getMelGlobal
from pymel.core.language import OptionVarDict
from pymel.core.language import MelGlobals
from pymel.core.language import scriptJob
from pymel.core.language import python
from pymel.core.language import pythonToMelCmd
from pymel.core.language import MelSyntaxError
from pymel.core.language import setMelGlobal
from pymel.core.language import waitCursor

def voxelize(cubeSize=None):
    """
    voxelize the currently selected mesh
    \param cubeSize float size of voxels
    """

    pass


def promptNumber():
    pass


def roundToFraction(input, fraction):
    """
    # round to nearest fraction in decimal form: 1, .5, .25
    """

    pass


def rayIntersect(fnMesh, point, direction=(0.0, 0.0, -1.0)):
    """
    # shoot a ray from point in direction and return all hits within the mesh
    """

    pass


def makeProgBar(length):
    pass



MELTYPES = []

optionVar = {}

catch = None

env = None

_MeshIsectAccelParams = None


