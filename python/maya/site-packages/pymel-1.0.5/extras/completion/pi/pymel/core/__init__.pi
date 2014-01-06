import pymel.api.plugins as _plugins
import pymel.internal.startup as _startup
import pymel as _pymel
import maya.cmds as cmds
import pymel.internal as _internal
import pymel.util as util
import pymel.internal.cmdcache as _cmdcache
import pymel.internal.pmcmds as _pmcmds
from . import runtime
import pymel.api as _api
import pymel.api as api
from . import uitypes as ui
from . import uitypes
from . import nodetypes
from . import nodetypes as nt
from . import datatypes as dt
import pymel.versions as _versions
import pymel.internal.factories as _factories

from pymel.core.general import *
from pymel.core.system import *
from pymel.core.windows import *
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

def _addPluginNode(pluginName, mayaType):
    pass


def _removePluginNode(pluginName, node):
    pass


def _addPluginCommand(pluginName, funcName):
    pass


def _installCallbacks():
    """
    install the callbacks that trigger new nodes and commands to be added to pymel when a
    plugin loads.  This is called from pymel.__init__
    """

    pass


def _removePluginCommand(pluginName, command):
    pass


def _pluginLoaded(*args):
    pass


def _pluginUnloaded(*args):
    pass



MELTYPES = []

_logger = None

optionVar = {}

catch = None

env = None

_pluginLoadedCB = True

_pluginData = {}


