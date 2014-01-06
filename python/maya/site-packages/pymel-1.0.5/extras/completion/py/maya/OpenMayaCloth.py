from . import OpenMaya
import _OpenMayaCloth
import weakref

from __builtin__ import object as _object
from __builtin__ import property as _swig_property

class MClothForce(_object):
    def __init__(self, *args, **kwargs):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def getParticle(*args, **kwargs):
        pass
    
    
    def setOffset(*args, **kwargs):
        pass
    
    
    def setStrength(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MClothConstraint(_object):
    def __init__(self, *args, **kwargs):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def execute(*args, **kwargs):
        pass
    
    
    def getParticle(*args, **kwargs):
        pass
    
    
    def userDefined(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MClothConstraintBridge(_object):
    def __init__(self, *args, **kwargs):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def execute(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MClothEdge(_object):
    def __init__(self, *args, **kwargs):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def equals(*args, **kwargs):
        pass
    
    
    def getCreaseAngle(*args, **kwargs):
        pass
    
    
    def getParticle(*args, **kwargs):
        pass
    
    
    def getTriangle(*args, **kwargs):
        pass
    
    
    def setCreaseAngle(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MClothPolyhedron(_object):
    def __init__(self, *args, **kwargs):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def create(*args, **kwargs):
        pass
    
    
    def disableCollisions(*args, **kwargs):
        pass
    
    
    def getPosition(*args, **kwargs):
        pass
    
    
    def getUserdata(*args, **kwargs):
        pass
    
    
    def numTriangles(*args, **kwargs):
        pass
    
    
    def numVertices(*args, **kwargs):
        pass
    
    
    def resetDisabledCollisions(*args, **kwargs):
        pass
    
    
    def setCollisionEnable(*args, **kwargs):
        pass
    
    
    def setPosition(*args, **kwargs):
        pass
    
    
    def setUserdata(*args, **kwargs):
        pass
    
    
    def updateCollisionDepth(*args, **kwargs):
        pass
    
    
    def updateCollisionOffset(*args, **kwargs):
        pass
    
    
    def updateDynFrictionMultiplier(*args, **kwargs):
        pass
    
    
    def updateFromMesh(*args, **kwargs):
        pass
    
    
    def updateNormals(*args, **kwargs):
        pass
    
    
    def updateStaticFrictionMultiplier(*args, **kwargs):
        pass
    
    
    def updateVelocityMultiplier(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class new_instancemethod(_object):
    """
    instancemethod(function, instance, class)
    
    Create an instance method object.
    """
    
    
    
    def __call__(*args, **kwargs):
        """
        x.__call__(...) <==> x(...)
        """
    
        pass
    
    
    def __cmp__(*args, **kwargs):
        """
        x.__cmp__(y) <==> cmp(x,y)
        """
    
        pass
    
    
    def __delattr__(*args, **kwargs):
        """
        x.__delattr__('name') <==> del x.name
        """
    
        pass
    
    
    def __get__(*args, **kwargs):
        """
        descr.__get__(obj[, type]) -> value
        """
    
        pass
    
    
    def __getattribute__(*args, **kwargs):
        """
        x.__getattribute__('name') <==> x.name
        """
    
        pass
    
    
    def __hash__(*args, **kwargs):
        """
        x.__hash__() <==> hash(x)
        """
    
        pass
    
    
    def __repr__(*args, **kwargs):
        """
        x.__repr__() <==> repr(x)
        """
    
        pass
    
    
    def __setattr__(*args, **kwargs):
        """
        x.__setattr__('name', value) <==> x.name = value
        """
    
        pass
    
    
    __func__ = None
    
    __self__ = None
    
    im_class = None
    
    im_func = None
    
    im_self = None
    
    __new__ = None


class MSeamInfo(_object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    particleIndex = None
    
    thisown = None
    
    triangleIndex = None
    
    u = None
    
    v = None
    
    __swig_destroy__ = None


class MClothTriangle(_object):
    def __init__(self, *args, **kwargs):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def contains(*args, **kwargs):
        pass
    
    
    def equals(*args, **kwargs):
        pass
    
    
    def getEdge(*args, **kwargs):
        pass
    
    
    def getMaterial(*args, **kwargs):
        pass
    
    
    def getParticle(*args, **kwargs):
        pass
    
    
    def getUV(*args, **kwargs):
        pass
    
    
    def getUVs(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MClothSystem(_object):
    def __init__(self, *args, **kwargs):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def addCloth(*args, **kwargs):
        pass
    
    
    def addCommand(*args, **kwargs):
        pass
    
    
    def addRigidbody(*args, **kwargs):
        pass
    
    
    def addSpring(*args, **kwargs):
        pass
    
    
    def createRigidbody(*args, **kwargs):
        pass
    
    
    def currentTime(*args, **kwargs):
        pass
    
    
    def findClosestPolyhedron(*args, **kwargs):
        pass
    
    
    def findClothTriangle(*args, **kwargs):
        pass
    
    
    def findNeighborTriangles(*args, **kwargs):
        pass
    
    
    def findTriangle(*args, **kwargs):
        pass
    
    
    def frameSize(*args, **kwargs):
        pass
    
    
    def getBendingForce(*args, **kwargs):
        pass
    
    
    def getClothContacts(*args, **kwargs):
        pass
    
    
    def getClothForces(*args, **kwargs):
        pass
    
    
    def getClothNeighbours(*args, **kwargs):
        pass
    
    
    def getNewMaterialInstance(*args, **kwargs):
        pass
    
    
    def getParticle(*args, **kwargs):
        pass
    
    
    def getPosition(*args, **kwargs):
        pass
    
    
    def getRecoilDuration(*args, **kwargs):
        pass
    
    
    def getRecoilWidth(*args, **kwargs):
        pass
    
    
    def getStress(*args, **kwargs):
        pass
    
    
    def getStress_scaled(*args, **kwargs):
        pass
    
    
    def getTriangle(*args, **kwargs):
        pass
    
    
    def getUserdata(*args, **kwargs):
        pass
    
    
    def getVelocity(*args, **kwargs):
        pass
    
    
    def initRecoilState(*args, **kwargs):
        pass
    
    
    def interpolate(*args, **kwargs):
        pass
    
    
    def lastTime(*args, **kwargs):
        pass
    
    
    def lockParticle(*args, **kwargs):
        pass
    
    
    def numParticles(*args, **kwargs):
        pass
    
    
    def numTriangles(*args, **kwargs):
        pass
    
    
    def postSolve(*args, **kwargs):
        pass
    
    
    def preSolve(*args, **kwargs):
        pass
    
    
    def recoilScale(*args, **kwargs):
        pass
    
    
    def removeCloth(*args, **kwargs):
        pass
    
    
    def removeCommand(*args, **kwargs):
        pass
    
    
    def removeRigidbody(*args, **kwargs):
        pass
    
    
    def removeSpring(*args, **kwargs):
        pass
    
    
    def restart(*args, **kwargs):
        pass
    
    
    def setBendResistance(*args, **kwargs):
        pass
    
    
    def setBendingForce(*args, **kwargs):
        pass
    
    
    def setCurrentTime(*args, **kwargs):
        pass
    
    
    def setFrameSize(*args, **kwargs):
        pass
    
    
    def setIgnoreCollisions(*args, **kwargs):
        pass
    
    
    def setMaterial(*args, **kwargs):
        pass
    
    
    def setPinchMethod(*args, **kwargs):
        pass
    
    
    def setPosition(*args, **kwargs):
        pass
    
    
    def setRecoilDuration(*args, **kwargs):
        pass
    
    
    def setRecoilParams(*args, **kwargs):
        pass
    
    
    def setRecoilWidth(*args, **kwargs):
        pass
    
    
    def setUserdata(*args, **kwargs):
        pass
    
    
    def setVelocity(*args, **kwargs):
        pass
    
    
    def setVelocity_CutOff(*args, **kwargs):
        pass
    
    
    def solverNode(*args, **kwargs):
        pass
    
    
    def stepSize(*args, **kwargs):
        pass
    
    
    def step_forward(*args, **kwargs):
        pass
    
    
    def tagRecoilParticle(*args, **kwargs):
        pass
    
    
    def unlockParticle(*args, **kwargs):
        pass
    
    
    def updateMaterial(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MClothParticle(_object):
    def __init__(self, *args, **kwargs):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def collideWithPolyhedron(*args, **kwargs):
        pass
    
    
    def equals(*args, **kwargs):
        pass
    
    
    def getAccelaration(*args, **kwargs):
        pass
    
    
    def getEdge(*args, **kwargs):
        pass
    
    
    def getIndex(*args, **kwargs):
        pass
    
    
    def getMass(*args, **kwargs):
        pass
    
    
    def getMaterial(*args, **kwargs):
        pass
    
    
    def getOriginalMass(*args, **kwargs):
        pass
    
    
    def getPosition(*args, **kwargs):
        pass
    
    
    def getVelocity(*args, **kwargs):
        pass
    
    
    def ignoreClothCollision(*args, **kwargs):
        pass
    
    
    def ignoreSolid(*args, **kwargs):
        pass
    
    
    def numEdges(*args, **kwargs):
        pass
    
    
    def setAccelaration(*args, **kwargs):
        pass
    
    
    def setForceMultiplier(*args, **kwargs):
        pass
    
    
    def setMass(*args, **kwargs):
        pass
    
    
    def setPosition(*args, **kwargs):
        pass
    
    
    def setVelocity(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MClothMaterial(_object):
    def __iadd__(*args, **kwargs):
        pass
    
    
    def __imul__(*args, **kwargs):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def equal(*args, **kwargs):
        pass
    
    
    def setupRelaxProperty(*args, **kwargs):
        pass
    
    
    def update(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    airDamping = None
    
    clothDamping = None
    
    clothFriction = None
    
    density = None
    
    dynamicFriction = None
    
    gravity = None
    
    mat_thickness = None
    
    shear = None
    
    staticFriction = None
    
    thickness = None
    
    thicknessForce = None
    
    thisown = None
    
    uBend = None
    
    uBendRate = None
    
    uScale = None
    
    uStretchResistance = None
    
    vBend = None
    
    vBendRate = None
    
    vScale = None
    
    vStretchResistance = None
    
    __swig_destroy__ = None


class MClothSolverRegister(_object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def registerClothSolver(*args, **kwargs):
        pass
    
    
    def unregisterClothSolver(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MClothControl(_object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def collisionCB(*args, **kwargs):
        pass
    
    
    def currentSolver(*args, **kwargs):
        pass
    
    
    def dgTimeGivenClothFrame(*args, **kwargs):
        pass
    
    
    def externalForces(*args, **kwargs):
        pass
    
    
    def getClothFromSolver(*args, **kwargs):
        pass
    
    
    def getClothSystem(*args, **kwargs):
        pass
    
    
    def getPrecedingFrame(*args, **kwargs):
        pass
    
    
    def getSucceedingFrame(*args, **kwargs):
        pass
    
    
    def getUVs(*args, **kwargs):
        pass
    
    
    def interruptCheckCB(*args, **kwargs):
        pass
    
    
    def isClothMesh(*args, **kwargs):
        pass
    
    
    def isSolverCloth(*args, **kwargs):
        pass
    
    
    def loadFrame(*args, **kwargs):
        pass
    
    
    def panelFaces(*args, **kwargs):
        pass
    
    
    def panelId(*args, **kwargs):
        pass
    
    
    def pinch(*args, **kwargs):
        pass
    
    
    def solveCB(*args, **kwargs):
        pass
    
    
    def solverNode(*args, **kwargs):
        pass
    
    
    def stepCB(*args, **kwargs):
        pass
    
    
    def stitcherNode(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MClothConstraintCmd(MClothConstraint):
    def __init__(self, *args, **kwargs):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def desired_position(*args, **kwargs):
        pass
    
    
    def getCustomConstraintBehavior(*args, **kwargs):
        pass
    
    
    def getDamp(*args, **kwargs):
        pass
    
    
    def getShear(*args, **kwargs):
        pass
    
    
    def isSoft(*args, **kwargs):
        pass
    
    
    def setCustomConstraintBehavior(*args, **kwargs):
        pass
    
    
    def setSoft(*args, **kwargs):
        pass
    
    
    def setStrength(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None



def MClothControl_stitcherNode(*args, **kwargs):
    pass


def MClothControl_pinch(*args, **kwargs):
    pass


def _swig_setattr(self, class_type, name, value):
    pass


def MClothControl_externalForces(*args, **kwargs):
    pass


def MClothEdge_swigregister(*args, **kwargs):
    pass


def MClothSystem_swigregister(*args, **kwargs):
    pass


def MClothControl_solveCB(*args, **kwargs):
    pass


def MClothControl_panelId(*args, **kwargs):
    pass


def MClothControl_stepCB(*args, **kwargs):
    pass


def MClothControl_collisionCB(*args, **kwargs):
    pass


def _swig_getattr(self, class_type, name):
    pass


def MClothParticle_swigregister(*args, **kwargs):
    pass


def MClothControl_getPrecedingFrame(*args, **kwargs):
    pass


def MClothControl_currentSolver(*args, **kwargs):
    pass


def MClothConstraint_swigregister(*args, **kwargs):
    pass


def MClothPolyhedron_swigregister(*args, **kwargs):
    pass


def _swig_repr(self):
    pass


def MClothControl_loadFrame(*args, **kwargs):
    pass


def MClothMaterial_swigregister(*args, **kwargs):
    pass


def MClothControl_getClothSystem(*args, **kwargs):
    pass


def MSeamInfo_swigregister(*args, **kwargs):
    pass


def MClothConstraintBridge_swigregister(*args, **kwargs):
    pass


def MClothControl_isClothMesh(*args, **kwargs):
    pass


def MClothControl_getUVs(*args, **kwargs):
    pass


def MClothControl_dgTimeGivenClothFrame(*args, **kwargs):
    pass


def weakref_proxy(*args, **kwargs):
    """
    proxy(object[, callback]) -- create a proxy object that weakly
    references 'object'.  'callback', if given, is called with a
    reference to the proxy when 'object' is about to be finalized.
    """

    pass


def MClothControl_isSolverCloth(*args, **kwargs):
    pass


def MClothControl_panelFaces(*args, **kwargs):
    pass


def MClothControl_getClothFromSolver(*args, **kwargs):
    pass


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    pass


def MClothControl_solverNode(*args, **kwargs):
    pass


def MClothSolverRegister_swigregister(*args, **kwargs):
    pass


def MClothControl_getSucceedingFrame(*args, **kwargs):
    pass


def _swig_setattr_nondynamic_method(set):
    pass


def MClothSolverRegister_registerClothSolver(*args, **kwargs):
    pass


def MClothControl_interruptCheckCB(*args, **kwargs):
    pass


def MClothTriangle_swigregister(*args, **kwargs):
    pass


def MClothConstraintCmd_swigregister(*args, **kwargs):
    pass


def MClothControl_swigregister(*args, **kwargs):
    pass


def MClothSolverRegister_unregisterClothSolver(*args, **kwargs):
    pass


def MClothForce_swigregister(*args, **kwargs):
    pass



_newclass = 1


