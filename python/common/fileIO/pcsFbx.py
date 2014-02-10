"""
FBX SDK wrappers.

Must download appropriate FBX Python SDK version and add to PATH
i.e.-
sys.path.append(r'C:\Program Files\Autodesk\FBX\FBX Python SDK\2014.2\lib\Python27_x64')

*Examples:* ::

    >>> import common.fileIO.pcsFbx
    >>> filepath = r"d:[path_to_art_asset]\test_anim.fbx"
    >>> fbx_file = common.fileIO.pcsFbx.FBX( filepath )

*Todo:*
    * more methods, I'm sure
    * unitTests

*Author:*
    * Jason.Parks, jason@continuityai.com, 1/8/14 4:22 PM
"""

# Python std lib
#import os

# Python published lib
# noinspection PyUnresolvedReferences
import fbx
import FbxCommon

# common tools API
import common.diagnostic.pcsLogger


class FBX(object):
    """
        Python FBX SDK wrapper class

        *Author:*
            * Jason.Parks, jason@continuityai.com, 1/8/14 4:22 PM
        """

    def __init__(self, filepath):
        """
        Python FBX SDK wrapper class

        *Arguments:*
            * ``filepath`` file to work on

        *Keyword Arguments:*
            * ``none``

        *Examples:* ::

            >>> import common.fileIO.pcsFbx
            >>> import common.core
            >>> filepath = r"d:[path_to_art_asset]\test_anim.fbx"
            >>> fbx_file = common.fileIO.pcsFbx.FBX( filepath )
            >>> fbx_master = fbx_file.find_node( 'root' )
            # Result: <fbx.FbxNode object at 0x0000000033FAD8C8> #

        *Author:*
            * Jason.Parks, jason@continuityai.com, 1/8/14 4:22 PM
        """

        self.logger = common.diagnostic.pcsLogger.pcs_logger()
        self.filepath = filepath

        # get scene object
        self.scene = None
        self.sdk_manager = None
        self.sdk_manager, self.scene = FbxCommon.InitializeSdkObjects()
        FbxCommon.LoadScene(self.sdk_manager, self.scene, filepath)

        # get master
        self.root_node = self.scene.GetRootNode()

        self.all_nodes = []

    # noinspection PyUnresolvedReferences
    @staticmethod
    def cast_to_property_type(fbx_property):
        """
        Have to cast to a specific property type to get value

        :param fbx_property:
        *Arguments:*
            * ``fbx_property`` fbx.FbxProperty object

        *Keyword Arguments:*
            * ``none``

        *Returns:*
            * ``casted_property`` specific fbx property type

        *Examples:* ::

            >>> casted_property = self.cast_to_property_type( fbx_property )

        *Author:*
            * Jason.Parks, jason@continuityai.com, 1/8/14 4:22 PM
        """

        prop_type = fbx_property.GetPropertyDataType().GetType()
        if prop_type == pcsFbx.eFbxBool:
            casted_property = pcsFbx.FbxPropertyBool1(fbx_property)
        elif prop_type == pcsFbx.eFbxDouble:
            casted_property = pcsFbx.FbxPropertyDouble1(fbx_property)
        elif prop_type == pcsFbx.eFbxDouble2:
            casted_property = pcsFbx.FbxPropertyDouble2(fbx_property)
        elif prop_type == pcsFbx.eFbxDouble3:
            casted_property = pcsFbx.FbxPropertyDouble3(fbx_property)
        elif prop_type == pcsFbx.eFbxDouble4:
            casted_property = pcsFbx.FbxPropertyDouble4(fbx_property)
        elif prop_type == pcsFbx.eFbxInt:
            casted_property = pcsFbx.FbxPropertyInteger1(fbx_property)
        elif prop_type == pcsFbx.eFbxFloat:
            casted_property = pcsFbx.FbxPropertyFloat1(fbx_property)
        elif prop_type == pcsFbx.eFbxString:
            casted_property = pcsFbx.FbxPropertyString(fbx_property)
        elif (
            prop_type == pcsFbx.eFbxUndefined or
            prop_type == pcsFbx.eFbxChar or
            prop_type == pcsFbx.eFbxUChar or
            prop_type == pcsFbx.eFbxShort or
            prop_type == pcsFbx.eFbxUShort or
            prop_type == pcsFbx.eFbxUInt or
            prop_type == pcsFbx.eFbxLongLong or
            prop_type == pcsFbx.eFbxHalfFloat or
            prop_type == pcsFbx.eFbxDouble4x4 or
            prop_type == pcsFbx.eFbxEnum or
            prop_type == pcsFbx.eFbxTime or
            prop_type == pcsFbx.eFbxReference or
            prop_type == pcsFbx.eFbxBlob or
            prop_type == pcsFbx.eFbxDistance or
            prop_type == pcsFbx.eFbxDateTime or
            prop_type == pcsFbx.eFbxTypeCount
        ):
            raise ValueError(
                'Unsupported property type: %s %d' % (fbx_property.GetPropertyDataType().GetName(), prop_type))
        else:
            raise ValueError(
                'Unknown property type: %s %d' % (fbx_property.GetPropertyDataType().GetName(), prop_type))
        return casted_property if casted_property is not None else None

    def clean_up(self):
        """
        Destroy sdk_manager

        *Arguments:*
            * ``none``

        *Keyword Arguments:*
            * ``none``

        *Returns:*
            * ``none``

        *Author:*
            * Jason.Parks, jason@continuityai.com, 1/8/14 4:22 PM
        """

        # Destroy all objects created by the FBX SDK.
        self.sdk_manager.Destroy()

    def find_node(self, name):
        """
        Finds a node in fbx scene

        *Arguments:*
            * ``name`` of node

        *Keyword Arguments:*
            * ``none``

        *Returns:*
            * ``node`` fbx.FbxNode object

        *Examples:* ::

            >>> import common.fileIO.pcsFbx
            >>> filepath = r"d:[path_to_art_asset]\test_anim.fbx"
            >>> pcsFbx = common.fileIO.pcsFbx.FBX( filepath )
            >>> fbx_master = pcsFbx.find_node( 'root' )

        *Todo:*
            * find with wildcard

        *Author:*
            * Jason.Parks, jason@continuityai.com, 1/8/14 4:22 PM
        """

        # populate all nodes
        self.get_all_nodes()
        for node in self.all_nodes:
            if name in node.GetName():
                return node

        self.logger.warning("Could not find node with name '{0}' in scene: {1}".format(name, self.filepath))
        return None

    def get_all_nodes(self):
        """
        Get all nodes in a .fbx file

        *Arguments:*
            * ``none``

        *Keyword Arguments:*
            * ``none``

        *Returns:*
            * ``none`` just populates instance variable self.all_nodes

        *Examples:* ::

            >>> import common.fileIO.pcsFbx
            >>> filepath = r"d:[path_to_art_asset]\test_anim.fbx"
            >>> fbx_file = common.fileIO.pcsFbx.FBX( filepath )
            >>> fbx_file.get_all_nodes()
            >>> all_nodes = fbx_file.all_nodes

        *Author:*
            * Jason.Parks, jason@continuityai.com, 1/8/14 4:22 PM
        """

        self.all_nodes = []

        for i in range(self.root_node.GetChildCount()):
            self.scrape_node_hierarchy(self.root_node.GetChild(i))

    def get_property_value(self, node, property_name):
        """
        Gets the value of a property on a pcsFbx node

        *Arguments:*
            * ``node`` fbx.FbxNode
            * ``property_name`` name of property to find and get value of

        *Keyword Arguments:*
            * ``none``

        *Returns:*
            * ``value`` property value

        *Examples:* ::

            >>> import common.fileIO.pcsFbx
            >>> filepath = r"d:[path_to_art_asset]\test_anim.fbx"
            >>> fbx_file = common.fileIO.pcsFbx.FBX( filepath )
            >>> fbx_master = fbx_file.find_node( 'root' )
            >>> file_rig_type = fbx_file.get_property_value(fbx_master, 'p_asset_namespace')

        *Author:*
            * Jason.Parks, jason@continuityai.com, 1/8/14 4:22 PM
        """

        fbx_property = node.FindProperty(property_name)
        # cast to correct property type so you can get
        casted_property = self.cast_to_property_type(fbx_property)

        return casted_property.Get()

    def make_marker(self, name):
        #TODO:
        lMarker = fbx.FbxMarker.Create(self.sdk_manager, name)
        lNode = fbx.FbxNode.Create(self.sdk_manager, name)
        lNode.SetNodeAttribute(lMarker)

        # position
        lNode.LclTranslation.Set(fbx.FbxDouble3(1.0, 2.0, 3.0))
        lNode.LclRotation.Set(fbx.FbxDouble3(0.0, 0.0, 0.0))
        lNode.LclScaling.Set(fbx.FbxDouble3(1.0, 1.0, 1.0))

        # add to scene
        # fbx_file.root_node.AddChild(lNode)
        self.root_node.AddChild(lNode)

    def remove_namespace(self):
        """
        Removes all namespaces from nodes in-line in the scene

        *Arguments:*
            * ``none``

        *Keyword Arguments:*
            * ``none``

        *Returns:*
            * ``True/False``

        *Examples:* ::

            >>> import common.fileIO.pcsFbx
            >>> filepath = r"d:[path_to_art_asset]\test_anim.fbx"
            >>> fbx_file = common.fileIO.pcsFbx.FBX( filepath )
            >>> fbx_file.remove_namespace()

        *Todo:*
            * Remove specific, passed namespace

        *Author:*
            * Jason.Parks, jason@continuityai.com, 1/8/14 4:22 PM
        """

        self.get_all_nodes()

        # rename
        removed = False
        for node in self.all_nodes:
            orig_name = node.GetName()
            split_by_colon = orig_name.split(':')
            if len(split_by_colon) > 1:
                new_name = split_by_colon[-1:][0]
                node.SetName(new_name)
                removed = True

        if removed:
            # save
            FbxCommon.SaveScene(self.sdk_manager, self.scene, self.filepath)
            self.logger.info("Successfully removed namespaces from: '{0}'".format(self.filepath))
            return True

        return False

    def save_scene(self):
        #TODO:
        FbxCommon.SaveScene(self.sdk_manager, self.scene, self.filepath)

    def scrape_node_hierarchy(self, top_node):
        """
        Fills FBX instance attr .all_nodes with every top_node from the scene

        :param top_node:
        *Arguments:*
            * ``top_node`` top top_node of hierarchy to search

        *Keyword Arguments:*
            * ``none``

        *Returns:*
            * ``none``

        *Examples:* ::

            >>> FBX().scrape_node_hierarchy('root')

        *Author:*
            * Jason.Parks, jason@continuityai.com, 1/8/14 4:22 PM
        """

        self.all_nodes.append(top_node)

        for i in range(top_node.GetChildCount()):
            self.scrape_node_hierarchy(top_node.GetChild(i))


#fbx_file = FBX() # Do not instantiate helper. Need individual instances for each filepath
