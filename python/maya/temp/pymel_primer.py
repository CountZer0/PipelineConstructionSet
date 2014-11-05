"""
Samples of pymel form importing

*Author:*
    * Jason.Parks, jason@continuityai.com, 2/25/14 8:08 AM
"""

import pymel.core


pymel.core.__file__

#No, no. Stomps maya.cmds
#from pymel.core import *

# Not explicit
#import pymel.core as pm

sphereT, sphereP = pymel.core.polySphere()
sphereP.setRadius(3)
#sphereP.


# maya.cmds
import maya.cmds
# strings :-(
ps = maya.cmds.polySphere()


# test object's name vs. string
if sphereT.name() == 'pSphere1':
    print 'yep, they match'

# test object vs. string
if sphereT == 'pSphere1':
    print 'yep, they match'

# use constants instead of strings
import temp.constants

reload(temp.constants)
# noinspection PyStatementEffect
temp.constants.SPHERE

sphereT, sphereP = pymel.core.polySphere(n=temp.constants.SPHERE)

# test object vs. string
if sphereT == temp.constants.SPHERE:
    print 'yep, they match'

# check type
my_list = []
if type(my_list) == list:
    print "yep, it's a list"

if type(sphereP) == pymel.core.nodetypes.PolySphere:
    print "yep, it's a PolySphere"

if type(sphereP) == pymel.core.nodetypes.DependNode:
    print "yep, it's a DependNode"

# check instance type
if isinstance(sphereT, pymel.core.nodetypes.Transform):
    print "yep, it's a Transform"

if isinstance(sphereT, pymel.core.nodetypes.DagNode):
    print "yep, it inherits from DagNode"

if isinstance(sphereT, pymel.core.nodetypes.DependNode):
    print "yep, it inherits from DependNode"


# command wrapper
sphere_nodes = pymel.core.polySphere()
g = pymel.core.group()

# class instance
polySphere_node = pymel.core.nodetypes.PolySphere(n=temp.constants.SPHERE)
trans = polySphere_node.outputs()[0]

trans = pymel.core.nodetypes.Transform()



# Path
filepath = pymel.core.sceneName()
filepath.basename()
filepath.name
filepath.parent
filepath.parent.parent
filepath.exists()





# logging
from pymel.internal.plogging import pymelLogger

pymelLogger.info('test')

from pymel.tools import loggingControl

loggingControl.initMenu()

