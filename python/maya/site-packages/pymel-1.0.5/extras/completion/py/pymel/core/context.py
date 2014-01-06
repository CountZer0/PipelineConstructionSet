import pymel.internal.factories as _factories

def keyframeRegionDollyCtx(*args, **kwargs):
    """
    This command can be used to create a dolly context for the dope sheet editor.
    
    Flags:
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.Flag can appear in Create mode of commandFlag can have multiple
          arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.keyframeRegionDollyCtx`
    """

    pass


def art3dPaintCtx(*args, **kwargs):
    """
    This is a tool context command for 3d Paint tool. In query mode, return type is based on queried flag.
    
    Modifications:
      - converts a whitespace-separated string of names to a list of PyNode objects for flags: (query and (shapenames or shadernames))
    
    Flags:
      - accopacity : aco               (bool)          [create,query,edit]
          Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When
          queried, it returns a boolean.
    
      - afterStrokeCmd : asc           (unicode)       []
    
      - alphablendmode : abm           (unicode)       [create,query,edit]
          Specifies the blend mode used while painting RGB channel. Currently, we support the following blend modes: "Default"
          "Lighten" "Darken" "Difference" "Exclusion" "Hard Light" "Soft Light" "Multiply" "Screen" "Overlay" Default is
          "Default".
    
      - assigntxt : ast                (bool)          [edit]
          Sends a request to the tool to allocate and assign file textures to the specified attibute on the selected shaders.
    
      - attrnames : atn                (unicode)       []
    
      - beforeStrokeCmd : bsc          (unicode)       []
    
      - brushalignment : bra           (bool)          [create,query,edit]
          Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector.
          C: Default is true. Q: When queried, it returns a boolean.
    
      - brushdepth : bd                (float)         []
    
      - brushfeedback : brf            (bool)          [create,query,edit]
          Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
    
      - brushtype : brt                (unicode)       []
    
      - clear : clr                    (bool)          [create,edit]
          Floods all cvs/vertices to the current value.
    
      - commonattr : cat               (unicode)       [query]
          Returns a string with the names of all common to all the shaders paintable attributes and supported by the Paint Texture
          Tool.
    
      - dragSlider : dsl               (unicode)       [create,edit]
          Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The
          string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C:
          Default is "none".
    
      - dynclonemode : dcm             (bool)          []
    
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - expandfilename : eef           (bool)          [create,edit]
          If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the
          name as it is. C: Default is true.
    
      - exportaspectratio : ear        (float)         []
    
      - exportfilemode : efm           (unicode)       [create,query,edit]
          Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is
          "luminance/rgb". Q: When queried, it returns a string.
    
      - exportfilesave : esf           (unicode)       [edit]
          Exports the attribute map and saves to a specified file.
    
      - exportfilesizex : fsx          (int)           [create,query,edit]
          Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
    
      - exportfilesizey : fsy          (int)           [create,query,edit]
          Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
    
      - exportfiletype : eft           (unicode)       [create,query,edit]
          Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit"
          "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
    
      - extendFillColor : efc          (bool)          [create,query,edit]
          States if the painted textures will be automatically postprocessed on each stroke to fill in the background color.
          Default is true.
    
      - fileformat : eff               (unicode)       []
    
      - filetxtaspectratio : far       (float)         [create,query,edit]
          Specifies the aspect ration of the texture width and height. Default is 1.
    
      - filetxtsizex : ftx             (int)           [create,query,edit]
          Specifies the width of the texture. Default is 256.
    
      - filetxtsizey : fty             (int)           [create,query,edit]
          Specifies the height of the texture. Default is 256.
    
      - floodOpacity : fop             (float)         []
    
      - floodall : fal                 (bool)          []
    
      - floodselect : fsl              (bool)          []
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - importfileload : ifl           (unicode)       [edit]
          Load the attribute map a specified file.
    
      - importfilemode : ifm           (unicode)       [create,query,edit]
          Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C:
          Default is "alpha". Q: When queried, it returns a string.
    
      - importreassign : irm           (bool)          [create,query,edit]
          Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within
          Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a boolean.
    
      - keepaspectratio : kar          (bool)          [create,query,edit]
          States if the aspect ratio of the file texture sizes should remain constant. Default is true. boolean.
    
      - lastRecorderCmd : lrc          (unicode)       []
    
      - lastStampName : lsn            (unicode)       []
    
      - lowerradius : lr               (float)         [create,query,edit]
          Sets the lower size of the brush (only apply on tablet).
    
      - makeStroke : mst               (int)           []
    
      - mappressure : mp               (unicode)       [create,query,edit]
          Sets the tablet pressure mapping when the table is used. There are four options: "none" - the pressure has no effect,
          "opacity" - the pressure is mapped to the opacity, "radius" - the is mapped to modify the radius of the brush, "both" -
          the pressure modifies both the opacity and the radius. C: Default is "none". Q: When queried, it returns a string.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.
    
      - opacity : op                   (float)         [create,query,edit]
          Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
    
      - outline : o                    (bool)          [create,query,edit]
          Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
    
      - outwhilepaint : owp            (bool)          [create,query,edit]
          Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a
          boolean.
    
      - paintmode : pm                 (unicode)       [create,query,edit]
          Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried,
          it returns a string.
    
      - paintoperationtype : pot       (unicode)       [create,query,edit]
          Specifies the operation type used by the Paint Tool. Currently, we support the following paint modes: "Paint", "Smear",
          "Blur", "Erase" and "Clone". Default is "Paint".
    
      - painttxtattr : pta             (unicode)       [create,query,edit]
          Specifies the attribute on the shader which the user wants to paint. Currently, we support the following attributes:
          "Color", "Transparency", "Ambient", "Incandescence", "BumpMap", "Diffuse", "Translucence" "Eccentricity"
          "SpecularColor", "Reflectivity", "ReflectedColor", and user-defined float, float3, double, and double3 attributes.
          Default is "Color".
    
      - painttxtattrname : ptn         (unicode)       [query,edit]
          Returns a string with the names of all paintable attributes supported by the Paint Texture Tool.
    
      - pfxScale : psc                 (float)         [query,edit]
          Specifies the scale for Paint Effect brushes.
    
      - pfxWidth : pwd                 (float)         [query,edit]
          Specifies the width for Paint Effect brushes.
    
      - pickColor : pcm                (bool)          []
    
      - pickValue : pv                 (bool)          []
    
      - playbackCursor : plc           (float, float)  []
    
      - playbackPressure : plp         (float)         []
    
      - preserveclonesource : pcs      (bool)          []
    
      - pressureMapping1 : pm1         (int)           []
    
      - pressureMapping2 : pm2         (int)           []
    
      - pressureMapping3 : pm3         (int)           []
    
      - pressureMax1 : px1             (float)         []
    
      - pressureMax2 : px2             (float)         []
    
      - pressureMax3 : px3             (float)         []
    
      - pressureMin1 : ps1             (float)         []
    
      - pressureMin2 : ps2             (float)         []
    
      - pressureMin3 : ps3             (float)         []
    
      - profileShapeFile : psf         (unicode)       [query,edit]
          Passes a name of the image file for the stamp shape profile.
    
      - projective : prm               (bool)          [create,query,edit]
          Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
    
      - radius : r                     (float)         [create,query,edit]
          Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
    
      - record : rec                   (bool)          []
    
      - reflection : rn                (bool)          [create,query,edit]
          Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
    
      - reflectionaboutorigin : rno    (bool)          []
    
      - reflectionaxis : ra            (unicode)       [create,query,edit]
          Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it
          returns a string.
    
      - reloadtexfile : rtf            (bool)          [edit]
          Sends a request to the tool to reload the texture from the disc.
    
      - resizeratio : rr               (float)         [query,edit]
          Specifies the scale by which to resize the current textures.
    
      - resizetxt : rft                (bool)          [edit]
          Sends a request to the tool to resize all the currently in use textures.
    
      - rgbcolor : rgb                 (float, float, float) []
    
      - rgbflood : fc                  (float, float, float) []
    
      - saveTextureOnStroke : sts      (bool)          [create,query,edit]
          States if the original texture will be automatically saved on each stroke. Default is false.
    
      - saveonstroke : sos             (bool)          [create,query,edit]
          States if the temporary texture will be automatically saved on each stroke. Default is false.
    
      - savetexture : stx              (bool)          [edit]
          Sends a request to the tool to save the texture to the disc.
    
      - screenRadius : scR             (float)         []
    
      - selectclonesource : scs        (bool)          []
    
      - shadernames : hnm              (unicode)       [query]
          Returns a string with the names of all shaders assigned to selected surfaces.
    
      - shapenames : shn               (unicode)       [query]
          Returns a string with the names of all surfaces which are being painted on.
    
      - showactive : sa                (bool)          [create,query,edit]
          Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
    
      - stampDepth : stD               (float)         []
    
      - stampProfile : stP             (unicode)       [create,query,edit]
          Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "soft",
          "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
    
      - stampSpacing : stS             (float)         [create,query,edit]
          Specifies the stamp spacing. Default is 1.0.
    
      - strokesmooth : ssm             (unicode)       []
    
      - surfaceConformedBrushVertices : scv (bool)          [create,query,edit]
          Enables/disables the the display of the effective brush area as affected vertices.
    
      - tablet : tab                   (bool)          [query]
          Returns true if the tablet device is present, false if it is absent
    
      - tangentOutline : to            (bool)          [create,query,edit]
          Enables/disables the display of the brush circle tangent to the surface.
    
      - textureFilenames : tfn         (bool)          [query]
          Returns a string array with the names of all the painted file textures.Flag can appear in Create mode of commandFlag can
          have multiple arguments, passed either as a tuple or a list.
    
      - updateEraseTex : uet           (bool)          []
    
      - usepressure : up               (bool)          [create,query,edit]
          Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
    
      - worldRadius : wlR              (float)         []
    
    
    Derived from mel command `maya.cmds.art3dPaintCtx`
    """

    pass


def polyMergeEdgeCtx(*args, **kwargs):
    """
    Create a new context to merge edges on polygonal objects In query mode, return type is based on queried flag.
    
    Flags:
      - activeNodes : anq              (bool)          [query]
          Return the active nodes in the tool
    
      - caching : cch                  (bool)          []
    
      - constructionHistory : ch       (bool)          []
    
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - firstEdge : fe                 (int)           []
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - immediate : im                 (bool)          [edit]
          Acts on the object not the tool defaults
    
      - mergeMode : mm                 (int)           [create,query,edit]
          The merge mode. (at first edge : 0, in between : 1, at last edge : 2)Default is in between.Flag can appear in Create
          mode of commandFlag can have multiple arguments, passed either as a tuple or a list.
    
      - mergeTexture : mt              (bool)          []
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.
    
      - nodeState : nds                (int)           []
    
      - previous : pv                  (bool)          [edit]
          Reset to previously stored values
    
      - reset : rs                     (bool)          [edit]
          Reset to default values
    
      - secondEdge : se                (int)           []
    
      - toolNode : tnq                 (bool)          [query]
          Return the node used for tool defaults
    
    
    Derived from mel command `maya.cmds.polyMergeEdgeCtx`
    """

    pass


def createNurbsTorusCtx(*args, **kwargs):
    """
    Flags:
      - attachToHeightRatio : ahr      (bool)          []
    
      - attachToSections : attachToSections (bool)          []
    
      - attachToSpans : asp            (bool)          []
    
      - axis : ax                      (float, float, float) []
    
      - axisType : axt                 (int)           []
    
      - doDragEdit : dde               (bool)          []
    
      - endSweep : esw                 (float)         []
    
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - minorRadius : mr               (float)         []
    
      - minorSweep : msw               (float)         []
    
      - name : n                       (unicode)       []
    
      - radius : r                     (float)         []
    
      - sections : sc                  (int)           []
    
      - spans : sp                     (int)           []
    
      - startSweep : ssw               (float)         []
    
      - surfaceDegree : sd             (int)           []
    
      - tolerance : tol                (float)         []
    
      - toleranceType : tlt            (int)           []
    
      - useTolerance : ut              (bool)          []
    
    
    Derived from mel command `maya.cmds.createNurbsTorusCtx`
    """

    pass


def createPolyPlatonicSolidCtx(*args, **kwargs):
    """
    Flags:
      - axis : ax                      (int)           []
    
      - createUVs : cuv                (int)           []
    
      - doDragEdit : dde               (bool)          []
    
      - doSubdivisionsCapsEdit : dsc   (bool)          []
    
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
      - radius : r                     (float)         []
    
      - sideLength : sl                (float)         []
    
      - solidType : st                 (int)           []
    
    
    Derived from mel command `maya.cmds.createPolyPlatonicSolidCtx`
    """

    pass


def texManipContext(*args, **kwargs):
    """
    Command used to register the texManipCtx tool.
    
    Flags:
      - exists : ex                    (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
    
    Derived from mel command `maya.cmds.texManipContext`
    """

    pass


def trimCtx(*args, **kwargs):
    """
    Flags:
      - activeNodes : anq              (bool)          []
    
      - autoCreate : ac                (bool)          []
    
      - caching : cch                  (bool)          []
    
      - constructionHistory : ch       (bool)          []
    
      - exists : ex                    (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - immediate : im                 (bool)          []
    
      - locatorU : lu                  (float)         []
    
      - locatorV : lv                  (float)         []
    
      - name : n                       (unicode)       []
    
      - nodeState : nds                (int)           []
    
      - object : o                     (bool)          []
    
      - replaceOriginal : rpo          (bool)          []
    
      - reset : rs                     (bool)          []
    
      - selected : sl                  (int)           []
    
      - shrink : sh                    (bool)          []
    
      - tolerance : tol                (float)         []
    
      - toolNode : tnq                 (bool)          []
    
    
    Derived from mel command `maya.cmds.trimCtx`
    """

    pass


def dynWireCtx(*args, **kwargs):
    """
    Flags:
      - brushDrag : bd                 (float)         []
    
      - brushMass : bm                 (float)         []
    
      - displayQuality : dq            (float)         []
    
      - doProject : dp                 (int)           []
    
      - dragBrushSize : dbs            (unicode)       []
    
      - drawAsMesh : dam               (bool)          []
    
      - exists : ex                    (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - inputSamples : inputSamples    (int)           []
    
      - paintAtDepth : pd              (bool)          []
    
      - pixelMode : pxm                (int)           []
    
      - pressureMapping1 : pm1         (int)           []
    
      - pressureMapping2 : pm2         (int)           []
    
      - pressureMapping3 : pm3         (int)           []
    
      - pressureMax1 : px1             (float)         []
    
      - pressureMax2 : px2             (float)         []
    
      - pressureMax3 : px3             (float)         []
    
      - pressureMin1 : ps1             (float)         []
    
      - pressureMin2 : ps2             (float)         []
    
      - pressureMin3 : ps3             (float)         []
    
      - sampleSeparation : sp          (float)         []
    
      - setSelection : ss              (bool)          []
    
      - surfaceOffset : sof            (float)         []
    
      - usePressure : usp              (bool)          []
    
    
    Derived from mel command `maya.cmds.dynWireCtx`
    """

    pass


def regionSelectKeyCtx(*args, **kwargs):
    """
    This command creates a context which may be used to scale keyframes within the graph editor using the region select
    tool.
    
    Flags:
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.Flag can appear in Create mode of commandFlag can have multiple
          arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.regionSelectKeyCtx`
    """

    pass


def createPolyTorusCtx(*args, **kwargs):
    """
    Flags:
      - attachToSectionRadius : asr    (bool)          []
    
      - attachToSubdivisionsAxis : asa (bool)          []
    
      - attachToSubdivisionsHeight : ash (bool)          []
    
      - axis : ax                      (int)           []
    
      - createUVs : cuv                (int)           []
    
      - doDragEdit : dde               (bool)          []
    
      - doSubdivisionsCapsEdit : dsc   (bool)          []
    
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
      - radius : r                     (float)         []
    
      - sectionRadius : sr             (float)         []
    
      - subdivisionsHeight : sh        (int)           []
    
      - subdivisionsWidth : sw         (int)           []
    
      - twist : tw                     (float)         []
    
    
    Derived from mel command `maya.cmds.createPolyTorusCtx`
    """

    pass


def snapshotBeadCtx(*args, **kwargs):
    """
    Creates a context for manipulating in and/or out tangent beads on the motion trail
    
    Flags:
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - inTangent : i                  (bool)          [query,edit]
          Indicates that we will be showing beads for the in tangent when entering the context
    
      - name : n                       (unicode)       []
    
      - outTangent : o                 (bool)          [query,edit]
          Indicates that we will be showing beads for the out tangent when entering the contextFlag can appear in Create mode of
          commandFlag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.snapshotBeadCtx`
    """

    pass


def boxDollyCtx(*args, **kwargs):
    """
    This command can be used to create, edit, or query a dolly context.
    
    Flags:
      - alternateContext : ac          (bool)          [create,query,edit]
          Set the ALT+CRL+LMB to refer to this context.Flag can appear in Create mode of commandFlag can have multiple arguments,
          passed either as a tuple or a list.
    
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
      - toolName : tn                  (unicode)       []
    
    
    Derived from mel command `maya.cmds.boxDollyCtx`
    """

    pass


def polyVertexNormalCtx(*args, **kwargs):
    """
    Flags:
      - deformmode : dm                (bool)          []
    
      - exists : ex                    (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - lockmode : lm                  (int)           []
    
      - relativemode : rm              (int)           []
    
      - rotatemode : rot               (int)           []
    
    
    Derived from mel command `maya.cmds.polyVertexNormalCtx`
    """

    pass


def texSelectShortestPathCtx(*args, **kwargs):
    """
    Creates a new context to select shortest edge path between two vertices or UVs in the texture editor window. In query
    mode, return type is based on queried flag.
    
    Flags:
      - exists : ex                    (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
    
    Derived from mel command `maya.cmds.texSelectShortestPathCtx`
    """

    pass


def createNurbsCylinderCtx(*args, **kwargs):
    """
    Flags:
      - attachToHeightRatio : ahr      (bool)          []
    
      - attachToSections : attachToSections (bool)          []
    
      - attachToSpans : asp            (bool)          []
    
      - axis : ax                      (float, float, float) []
    
      - axisType : axt                 (int)           []
    
      - caps : cp                      (int)           []
    
      - doDragEdit : dde               (bool)          []
    
      - endSweep : esw                 (float)         []
    
      - exists : ex                    (bool)          []
    
      - extraTransformOnCaps : xtc     (bool)          []
    
      - height : h                     (float)         []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
      - radius : r                     (float)         []
    
      - sections : sc                  (int)           []
    
      - spans : sp                     (int)           []
    
      - startSweep : ssw               (float)         []
    
      - surfaceDegree : sd             (int)           []
    
      - tolerance : tol                (float)         []
    
      - toleranceType : tlt            (int)           []
    
      - useTolerance : ut              (bool)          []
    
    
    Derived from mel command `maya.cmds.createNurbsCylinderCtx`
    """

    pass


def ctxData(*args, **kwargs):
    """
    Derived from mel command `maya.cmds.ctxData`
    """

    pass


def curveEditorCtx(*args, **kwargs):
    """
    The curveEditorCtx command creates a new NURBS editor context, which is used to edit a NURBS curve or surface.
    
    Flags:
      - direction : dir                (int)           [query]
          Query the current direction of the tangent control. Always zero for the curve case. In the surface case, its 0 for the
          normal direction, 1 for U direction and 2 for V direction.
    
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
      - relativeTangentSize : rts      (float)         [create,query,edit]
          Relative size of the tangent manipulator handle. Helps to adjust as the surface parameterization controls the size of
          the tangent, even if the shape of the surface remains the same. The default is 4.Flag can appear in Create mode of
          commandFlag can have multiple arguments, passed either as a tuple or a list.
    
      - title : t                      (unicode)       [query,edit]
          The title for the tool.
    
    
    Derived from mel command `maya.cmds.curveEditorCtx`
    """

    pass


def shadingGeometryRelCtx(*args, **kwargs):
    """
    This command creates a context that can be used for associating geometry to shading groups. You can put the context into
    shading-centric mode by using the -shadingCentric flag and specifying true. This means that the shading group is
    selected first then geometry associated with the shading group are highlighted. Subsequent selections result in
    assignments. Specifying -shadingCentric false means that the geometry is to be selected first. The shading group
    associated with the geometry will then be selected and subsequent selections will result in assignments being made.
    
    Flags:
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
      - offCommand : ofc               (unicode)       [create,query,edit]
          command to be issued when context is turned onFlag can appear in Create mode of commandFlag can have multiple arguments,
          passed either as a tuple or a list.
    
      - onCommand : onc                (unicode)       [create,query,edit]
          command to be issued when context is turned on
    
      - shadingCentric : s             (bool)          [create,query,edit]
          shading-centric mode.
    
    
    Derived from mel command `maya.cmds.shadingGeometryRelCtx`
    """

    pass


def polySuperCtx(*args, **kwargs):
    """
    Flags:
      - attach : a                     (unicode)       []
    
      - exists : ex                    (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
    
    Derived from mel command `maya.cmds.polySuperCtx`
    """

    pass


def polySelectEditCtx(*args, **kwargs):
    """
    Create a new context to select and edit polygonal objects
    
    Flags:
      - absoluteOffset : abo           (bool)          []
    
      - adjustEdgeFlow : aef           (float)         []
    
      - autoComplete : ac              (bool)          []
    
      - deleteEdge : de                (bool)          []
    
      - divisions : div                (int)           []
    
      - endVertexOffset : evo          (float)         []
    
      - exists : ex                    (bool)          []
    
      - fixQuads : fq                  (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - insertWithEdgeFlow : ief       (bool)          []
    
      - mode : m                       (int)           [create,query,edit]
          which mode to work on. Available modes are 1-loop and 2-ringFlag can appear in Create mode of commandFlag can have
          multiple arguments, passed either as a tuple or a list.
    
      - smoothingAngle : sma           (float)         []
    
      - splitType : spt                (int)           []
    
      - startVertexOffset : svo        (float)         []
    
      - useEqualMultiplier : uem       (bool)          []
    
    
    Derived from mel command `maya.cmds.polySelectEditCtx`
    """

    pass


def artPuttyCtx(*args, **kwargs):
    """
    This is a context command to set the flags on the artAttrContext, which is the base context for attribute painting
    operations. All commands require the name of the context as the last argument as this provides the name of the context
    to create, edit or query. This command is used to modify NURBS surfaces using a brush based interface (Maya Artisan).
    This is accomplished by moving the control vertices (cvs) under the brush in the specified direction. In query mode,
    return type is based on queried flag.
    
    Flags:
      - accopacity : aco               (bool)          [create,query,edit]
          Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When
          queried, it returns a boolean.
    
      - activeListChangedProc : alp    (unicode)       [create,query,edit]
          Accpts a string which contains a MEL command that is invoked whenever the active list changes. There may be some
          situations where the UI, for example, needs to be updated, when objects are selected/deselected in the scene. In query
          mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
    
      - afterStrokeCmd : asc           (unicode)       [create,query,edit]
          The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When
          queried, it returns the current command
    
      - alphaclamp : alc               (unicode)       [create,query,edit]
          Specifies if the weight value should be alpha clamped to the lower and upper bounds. There are four options here: "none"
          - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both"
          - clamps to the lower and upper bounds. C: Default is "none". Q: When queried, it returns a string.
    
      - alphaclamplower : acl          (float)         [create,query,edit]
          Specifies the lower bound for the alpha values. C: Default is 0.0. Q: When queried, it returns a float.
    
      - alphaclampupper : acu          (float)         [create,query,edit]
          Specifies the upper bound for the alpha values. C: Default is 1.0. Q: When queried, it returns a float.
    
      - attrSelected : asl             (unicode)       [query]
          Returns a name of the currently selected attribute. Q: When queried, it returns a string.
    
      - autosmooth : asm               (bool)          [create,query,edit]
          Sets up the auto smoothing option. When the brush is in the smooth mode, adjusting the strength will adjust how fast the
          surfaces is smoothed out. C: Default is FALSE. Q: When queried, it returns a boolean.
    
      - beforeStrokeCmd : bsc          (unicode)       [create,query,edit]
          The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q:
          When queried, it returns the current command
    
      - brushStrength : bs             (float)         [create,query,edit]
          Sets the strength of the brush. Brush strength is supported by the pinch and slide brushes. In pinch mode, adjusting the
          strength will adjust how quickly the surface converges on the brush center. In slide mode, the strength scales the
          motion of the brush. C: Default is 1.0. Q: When queried, it returns an float.
    
      - brushalignment : bra           (bool)          [create,query,edit]
          Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector.
          C: Default is true. Q: When queried, it returns a boolean.
    
      - brushfeedback : brf            (bool)          [create,query,edit]
          Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
    
      - clamp : cl                     (unicode)       [create,query,edit]
          Specifies if the weight value should be clamped to the lower and upper bounds. There are four options here: "none" - no
          clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both" -
          clamps to the lower and upper bounds. C: Default is "none". Q: When queried, it returns a string.
    
      - clamplower : cll               (float)         [create,query,edit]
          Specifies the lower bound for the values. C: Default is 0.0. Q: When queried, it returns a float.
    
      - clampupper : clu               (float)         [create,query,edit]
          Specifies the upper bound for the values. C: Default is 1.0. Q: When queried, it returns a float.
    
      - clear : clr                    (bool)          [create,edit]
          Floods all cvs/vertices to the current value.
    
      - collapsecvtol : clc            (float)         [create,query,edit]
          Specifies the tolerance for the collapse cv detection. C: Default is 0.005 cm. Q: When queried, it returns a float.
    
      - colorAlphaValue : cl1          (float)         []
    
      - colorRGBAValue : cl4           (float, float, float, float) []
    
      - colorRGBValue : cl3            (float, float, float) []
    
      - colorRamp : cr                 (unicode)       [create,query,edit]
          Allows a user defined color ramp to be used to map values to colors.
    
      - colorfeedback : cf             (bool)          [create,query,edit]
          Sets on/off the color feedback display. C: Default is FALSE. Q: When queried, it returns a boolean.
    
      - colorfeedbackOverride : cfo    (bool)          []
    
      - colorrangelower : crl          (float)         [create,query,edit]
          Specifies the value which maps to black when color feedback mode is on C: Default is 0.0. Q: When queried, it returns a
          float.
    
      - colorrangeupper : cru          (float)         [create,query,edit]
          Specifies the value which maps to the maximum color when color feedback mode is on C: Default is 1.0. Q: When queried,
          it returns a float.
    
      - dataTypeIndex : dti            (int)           [query,edit]
          When the selected paintable attribute is a vectorArray, it specifies which field to paint on.
    
      - disablelighting : dl           (bool)          [create,query,edit]
          If color feedback is on, this flag determines whether lighting is disabled or not for the surfaces that are affected C:
          Default is FALSE. Q: When queried, it returns a boolean.
    
      - dispdecr : dde                 (bool)          [create,edit]
          Decreases a maximum displacement by 10%.Flag can appear in Create mode of commandFlag can have multiple arguments,
          passed either as a tuple or a list.
    
      - dispincr : din                 (bool)          [create,edit]
          Increases a maximum displacement by 10%.
    
      - dragSlider : dsl               (unicode)       [create,edit]
          Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The
          string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C:
          Default is "none".
    
      - duringStrokeCmd : dsk          (unicode)       [create,query,edit]
          The passed string is executed as a MEL command during the stroke, each time the mouse is dragged. C: Default is no
          command. Q: When queried, it returns the current command
    
      - dynclonemode : dcm             (bool)          []
    
      - erasesrfupd : eut              (bool)          []
    
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - expandfilename : eef           (bool)          [create,edit]
          If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the
          name as it is. C: Default is true.
    
      - exportaspectratio : ear        (float)         []
    
      - exportfilemode : efm           (unicode)       [create,query,edit]
          Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is
          "luminance/rgb". Q: When queried, it returns a string.
    
      - exportfilesave : esf           (unicode)       [edit]
          Exports the attribute map and saves to a specified file.
    
      - exportfilesizex : fsx          (int)           [create,query,edit]
          Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
    
      - exportfilesizey : fsy          (int)           [create,query,edit]
          Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
    
      - exportfiletype : eft           (unicode)       [create,query,edit]
          Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit"
          "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
    
      - filterNodes : fon              (bool)          [edit]
          Sets the node filter.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - importfileload : ifl           (unicode)       [edit]
          Load the attribute map a specified file.
    
      - importfilemode : ifm           (unicode)       [create,query,edit]
          Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C:
          Default is "alpha". Q: When queried, it returns a string.
    
      - importreassign : irm           (bool)          [create,query,edit]
          Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within
          Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a boolean.
    
      - interactiveUpdate : iu         (bool)          [create,query,edit]
          Specifies how often to transfer the painted values into the attribute. TRUE: transfer them "continuously" (many times
          per stroke) FALSE: transfer them only at the end of a stroke (on mouse button release) C: Default is TRUE. Q: When
          queried, it returns a boolean.
    
      - invertrefvector : irv          (bool)          [create,query,edit]
          Sets the invert of the reference vector option when the reflection is ON. If it is true, the reference vector for the
          reflected stroke is negated with respect to the original one. C: Default is FALSE. Q: When queried, it returns a
          boolean.
    
      - lastRecorderCmd : lrc          (unicode)       []
    
      - lastStampName : lsn            (unicode)       []
    
      - lowerradius : lr               (float)         [create,query,edit]
          Sets the lower size of the brush (only apply on tablet).
    
      - makeStroke : mst               (int)           []
    
      - mappressure : mp               (unicode)       [create,query,edit]
          Sets the tablet pressure mapping when the table is used. There are four options: "none" - the pressure has no effect,
          "opacity" - the pressure is mapped to the opacity, "radius" - the is mapped to modify the radius of the brush, "both" -
          the pressure modifies both the opacity and the radius. C: Default is "none". Q: When queried, it returns a string.
    
      - maxdisp : md                   (float)         [create,query,edit]
          Defines a maximum displacement ( maxDisp in [0.0..5.0] ). C: Default is 1.0. Q: When queried, it returns a float.
    
      - maxvalue : mxv                 (float)         [create,query,edit]
          Specifies the maximum value for each attribute. C: Default is 1.0. Q: When queried, it returns a float.
    
      - minvalue : miv                 (float)         [create,query,edit]
          Specifies the minimum value for each attribute. C: Default is 0.0. Q: When queried, it returns a float.
    
      - mouldtypehead : mth            (unicode)       []
    
      - mouldtypemouse : mtm           (unicode)       [create,query,edit]
          Specifies the putty operations/mode ("push" - pushes cvs along the given direction (see refvector flag), "pull" - pulls
          cvs along the specified direction, "smooth" - smooths the sculpt, "erase" - erases the paint). C: Default is "push". Q:
          When queried, it returns a string.
    
      - mouldtypetail : mtt            (unicode)       []
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.
    
      - objattrArray : oaa             (unicode)       [query]
          An array of all paintable attributes. Each element of the array is a string with the following information:
          NodeType.NodeName.AttributeName.MenuType \*MenuType: type(level) of the item in the Menu (UI). Q: When queried, it
          returns a string.
    
      - opacity : op                   (float)         [create,query,edit]
          Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
    
      - outline : o                    (bool)          [create,query,edit]
          Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
    
      - outwhilepaint : owp            (bool)          [create,query,edit]
          Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a
          boolean.
    
      - paintNodeArray : pna           (unicode)       [query]
          An array of paintable nodes. Q: When queried, it returns a string.
    
      - paintattrselected : pas        (unicode)       [edit]
          An array of selected paintable attributes. Each element of the array is a string with the following information:
          NodeType.NodeName.AttributeName.
    
      - paintmode : pm                 (unicode)       [create,query,edit]
          Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried,
          it returns a string.
    
      - paintoperationtype : pot       (unicode)       []
    
      - pickColor : pcm                (bool)          []
    
      - pickValue : pv                 (bool)          []
    
      - playbackCursor : plc           (float, float)  []
    
      - playbackPressure : plp         (float)         []
    
      - polecv : pcv                   (bool)          [create,query,edit]
          Pull all the pole cvs to the same position
    
      - preserveclonesource : pcs      (bool)          []
    
      - profileShapeFile : psf         (unicode)       [query,edit]
          Passes a name of the image file for the stamp shape profile.
    
      - projective : prm               (bool)          [create,query,edit]
          Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
    
      - radius : r                     (float)         [create,query,edit]
          Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
    
      - rampMaxColor : rxc             (float, float, float) [create,query,edit]
          Defines a special color to be used when the value is greater than or equal to the maximum value.
    
      - rampMinColor : rmc             (float, float, float) [create,query,edit]
          Defines a special color to be used when the value is less than or equal to the minimum value.
    
      - record : rec                   (bool)          []
    
      - reflection : rn                (bool)          [create,query,edit]
          Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
    
      - reflectionaboutorigin : rno    (bool)          []
    
      - reflectionaxis : ra            (unicode)       [create,query,edit]
          Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it
          returns a string.
    
      - refsurface : rs                (bool)          [create,query,edit]
          Sets on/off the update of the reference surface. If it is true the reference surface is automatically updated on the per
          stroke bases. If it is false, the user has to update the reference surface explicitly by pressing the update button (see
          updaterefsrf). C: Default is TRUE. Q: When queried, it returns a boolean.
    
      - refvector : rv                 (unicode)       [create,query,edit]
          Specifies the direction of the push/pull operation ("normal" - sculpt along normals, "firstnormal" - sculpt along the
          first normal of the stroke, "view" - sculpt along the view direction, "xaxis", "yaxis", "zaxis" - sculpt along a given
          axis directions, "uisoparm", "visoparm" - sculpt along U or V isoparametric lines), "uvvector" - sculpt along an
          arbitrary vector in UV space. C: Default is "normal". Q: When queried, it returns a string.
    
      - refvectoru : rvu               (float)         [create,query,edit]
          Specifies the U component of the UV vector to be used when -refVector is set to "uvvector".
    
      - refvectorv : rvv               (float)         [create,query,edit]
          Specifies the V component of the UV vector to be used when -refVector is set to "uvvector".
    
      - screenRadius : scR             (float)         []
    
      - selectclonesource : scs        (bool)          []
    
      - selectedattroper : sao         (unicode)       [create,query,edit]
          Sets the edit weight operation. Four edit weights operations are provided : "absolute" - the value of the weight is
          replaced by the current one, "additive" - the value of the weight is added to the current one, "scale" - the value of
          the weight is multiplied by the current one, "smooth" - the value of the weight is divided by the current one. C:
          Default is "absolute". Q: When queried, it returns a string.
    
      - showactive : sa                (bool)          [create,query,edit]
          Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
    
      - smoothiters : si               (int)           [create,query,edit]
          Sets the quality of the smoothing operation (number of iterations). C: Default is 3. Q: When queried, it returns an int.
    
      - stampDepth : stD               (float)         []
    
      - stampProfile : stP             (unicode)       [create,query,edit]
          Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "soft",
          "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
    
      - stampSpacing : stS             (float)         []
    
      - stitchcorner : stc             (bool)          [create,query,edit]
          Sets on/off the stitching corner mode C: Default is "off". Q: When queried, it returns a boolean.
    
      - stitchedgeflood : sef          (bool)          [edit]
          Triggers postprocessing stitching edge procedure.
    
      - stitchtype : stt               (unicode)       [create,query,edit]
          Sets on/off the stitching mode ( "off" - stitching is turned off, "position" - position stitching is done without taking
          care about the tangent continuity C0, "tan" - C1 continuity is preserved). C: Default is "position". Q: When queried, it
          returns a string.
    
      - strokesmooth : ssm             (unicode)       []
    
      - surfaceConformedBrushVertices : scv (bool)          [create,query,edit]
          Enables/disables the the display of the effective brush area as affected vertices.
    
      - tablet : tab                   (bool)          [query]
          Returns true if the tablet device is present, false if it is absent
    
      - tangentOutline : to            (bool)          [create,query,edit]
          Enables/disables the display of the brush circle tangent to the surface.
    
      - toolOffProc : tfp              (unicode)       [create,query,edit]
          Accepts a strings describing the name of a MEL procedure which is invoked whenever the tool is turned off. For example,
          cloth invokes "clothPaintToolOff" when the cloth paint tool is turned on. Define this callback if your tool requires
          special functionality when your tool is deactivated. It is typical that if you implement a toolOffProc you will want to
          implement a toolOnProc as well (see the -toolOnProc flag. In query mode, the name of the currently registered MEL
          command is returned and this will be an empty string if none is defined.
    
      - toolOnProc : top               (unicode)       [create,query,edit]
          Accepts a strings describing the name of a MEL procedure which is invoked whenever the tool is turned on. For example,
          cloth invokes "clothPaintToolOn" when the cloth paint tool is turned on. Define this callback if your tool requires
          special functionality when your tool is activated. It is typical that if you implement a toolOnProc you will want to
          implement a toolOffProc as well (see the -toolOffProc flag. In query mode, the name of the currently registered MEL
          command is returned and this will be an empty string if none is defined.
    
      - updateerasesrf : ues           (bool)          [create,edit]
          Updates the erase surface.
    
      - updaterefsrf : urs             (bool)          [create,edit]
          Updates the reference surface.
    
      - useColorRamp : ucr             (bool)          [create,query,edit]
          Specifies whether the user defined color ramp should be used to map values from to colors. If this is turned off, the
          default greyscale feedback will be used.
    
      - useMaxMinColor : umc           (bool)          [create,query,edit]
          Specifies whether the out of range colors should be used. See rampMinColor and rampMaxColor flags for further details.
    
      - usepressure : up               (bool)          [create,query,edit]
          Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
    
      - value : val                    (float)         [create,query,edit]
          Specifies the value for each attribute. C: Default is 0.0. Q: When queried, it returns a float.
    
      - whichTool : wst                (unicode)       [create,query,edit]
          The string defines the name of the tool to be used for the Artisan context. An example is "artClothPaint". In query
          mode, the tool name for the given context is returned. Note: due to the way MEL works, always specify the -query flag
          last when specifying a flag which takes arguments.
    
      - worldRadius : wlR              (float)         []
    
    
    Derived from mel command `maya.cmds.artPuttyCtx`
    """

    pass


def wireContext(*args, **kwargs):
    """
    This command creates a tool that can be used to create a wire deformer.
    
    Flags:
      - crossingEffect : ce            (float)         [create,query,edit]
          Set the amount of convolution filter effect. Varies from fully convolved at 0 to a simple additive effect at 1. Default
          is 0.
    
      - deformationOrder : do          (unicode)       [create,query,edit]
          Set the appropriate flag that determines the position in in the deformation hierarchy.
    
      - dropoffDistance : dds          (float)         [create,query,edit]
          Set the dropoff Distance for the wires.
    
      - envelope : en                  (float)         [create,query,edit]
          Set the envelope value for the deformer. Default is 1.0
    
      - exclusive : exc                (bool)          [create,query,edit]
          Set exclusive mode on or off
    
      - exclusivePartition : ep        (unicode)       [create,query,edit]
          Set the name of an exclusive partition.Flag can appear in Create mode of commandFlag can have multiple arguments, passed
          either as a tuple or a list.
    
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - groupWithBase : gw             (bool)          [create,query,edit]
          Groups the wire with the base wire so that they can easily be moved together to create a ripple effect. Default is
          false.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - holder : ho                    (bool)          [create,edit]
          Controls whether the user can specify holders for the wires from the wire context. A holder is a curve that you can use
          to limit the wire's deformation region. Default is false.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - localInfluence : li            (float)         [create,query,edit]
          Set the amount of local influence a wire has with respect to other wires. Default is 0.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.
    
    
    Derived from mel command `maya.cmds.wireContext`
    """

    pass


def createPolyPyramidCtx(*args, **kwargs):
    """
    Flags:
      - attachToSubdivisionsCap : asc  (bool)          []
    
      - attachToSubdivisionsHeight : ash (bool)          []
    
      - axis : ax                      (int)           []
    
      - createUVs : cuv                (int)           []
    
      - doDragEdit : dde               (bool)          []
    
      - doSubdivisionsCapsEdit : dsc   (bool)          []
    
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
      - numberOfSides : ns             (int)           []
    
      - sideLength : sl                (float)         []
    
      - subdivisionsDepth : sd         (int)           []
    
      - subdivisionsHeight : sh        (int)           []
    
    
    Derived from mel command `maya.cmds.createPolyPyramidCtx`
    """

    pass


def polySelectCtx(*args, **kwargs):
    """
    Create a new context to select polygon components In query mode, return type is based on queried flag.
    
    Flags:
      - exists : ex                    (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - mode : m                       (int)           [create,query,edit]
          Edge loop or Edge ring or Border edge modeFlag can appear in Create mode of commandFlag can have multiple arguments,
          passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polySelectCtx`
    """

    pass


def panZoomCtx(*args, **kwargs):
    """
    This command can be used to create camera 2D pan/zoom context.
    
    Flags:
      - alternateContext : ac          (bool)          []
    
      - buttonDown : btd               (bool)          []
    
      - buttonUp : btu                 (bool)          []
    
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
      - panMode : pm                   (bool)          [create]
          Specify to create a camera 2D pan context, which is the default.
    
      - toolName : tn                  (unicode)       []
    
      - zoomMode : zm                  (bool)          [create]
          Specify to create a camera 2D zoom context.Flag can appear in Create mode of commandFlag can have multiple arguments,
          passed either as a tuple or a list.
    
      - zoomScale : zs                 (float)         [create,query,edit]
          Scale the zoom. The smaller the scale the slower the drag.
    
    
    Derived from mel command `maya.cmds.panZoomCtx`
    """

    pass


def graphSelectContext(*args, **kwargs):
    """
    This command can be used to create a selection context for the hypergraph editor.
    
    Flags:
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.Flag can appear in Create mode of
          commandFlag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.graphSelectContext`
    """

    pass


def curveEPCtx(*args, **kwargs):
    """
    The curveEPCtx command creates a new context for creating curves by placing edit points.
    
    Flags:
      - bezier : bez                   (bool)          []
    
      - degree : d                     (int)           [create,query,edit]
          Curve degree. Valid values are 1, 2, 3, 5 or 7. Default is degree 3.
    
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
      - preserveShape : ps             (bool)          []
    
      - preserveShapeFraction : pf     (float)         []
    
      - refit : rf                     (bool)          []
    
      - uniform : un                   (bool)          [create,query,edit]
          Default is true, which means uniform parameterization will be used. False means chord length parameterization.Flag can
          appear in Create mode of commandFlag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.curveEPCtx`
    """

    pass


def setEditCtx(*args, **kwargs):
    """
    This command creates a tool that can be used to modify set membership.
    
    Flags:
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.Flag can appear in Create mode of commandFlag can have multiple
          arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.setEditCtx`
    """

    pass


def artSetPaintCtx(*args, **kwargs):
    """
    This tool allows the user to modify the set membership (add, transfer, remove cvs) on nurbs surfaces using Maya
    Artisan's interface. In query mode, return type is based on queried flag.
    
    Flags:
      - accopacity : aco               (bool)          [create,query,edit]
          Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When
          queried, it returns a boolean.
    
      - afterStrokeCmd : asc           (unicode)       []
    
      - beforeStrokeCmd : bsc          (unicode)       []
    
      - brushalignment : bra           (bool)          [create,query,edit]
          Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector.
          C: Default is true. Q: When queried, it returns a boolean.
    
      - brushfeedback : brf            (bool)          [create,query,edit]
          Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
    
      - clear : clr                    (bool)          [create,edit]
          Floods all cvs/vertices to the current value.
    
      - dragSlider : dsl               (unicode)       [create,edit]
          Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The
          string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C:
          Default is "none".
    
      - dynclonemode : dcm             (bool)          []
    
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - expandfilename : eef           (bool)          [create,edit]
          If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the
          name as it is. C: Default is true.
    
      - exportaspectratio : ear        (float)         []
    
      - exportfilemode : efm           (unicode)       [create,query,edit]
          Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is
          "luminance/rgb". Q: When queried, it returns a string.
    
      - exportfilesave : esf           (unicode)       [edit]
          Exports the attribute map and saves to a specified file.
    
      - exportfilesizex : fsx          (int)           [create,query,edit]
          Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
    
      - exportfilesizey : fsy          (int)           [create,query,edit]
          Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
    
      - exportfiletype : eft           (unicode)       [create,query,edit]
          Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit"
          "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - importfileload : ifl           (unicode)       [edit]
          Load the attribute map a specified file.
    
      - importfilemode : ifm           (unicode)       [create,query,edit]
          Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C:
          Default is "alpha". Q: When queried, it returns a string.
    
      - importreassign : irm           (bool)          [create,query,edit]
          Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within
          Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a boolean.
    
      - lastRecorderCmd : lrc          (unicode)       []
    
      - lastStampName : lsn            (unicode)       []
    
      - lowerradius : lr               (float)         [create,query,edit]
          Sets the lower size of the brush (only apply on tablet).
    
      - makeStroke : mst               (int)           []
    
      - mappressure : mp               (unicode)       [create,query,edit]
          Sets the tablet pressure mapping when the table is used. There are four options: "none" - the pressure has no effect,
          "opacity" - the pressure is mapped to the opacity, "radius" - the is mapped to modify the radius of the brush, "both" -
          the pressure modifies both the opacity and the radius. C: Default is "none". Q: When queried, it returns a string.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.
    
      - objectsetnames : osn           (unicode)       []
    
      - opacity : op                   (float)         [create,query,edit]
          Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
    
      - outline : o                    (bool)          [create,query,edit]
          Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
    
      - outwhilepaint : owp            (bool)          [create,query,edit]
          Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a
          boolean.
    
      - paintmode : pm                 (unicode)       [create,query,edit]
          Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried,
          it returns a string.
    
      - paintoperationtype : pot       (unicode)       []
    
      - pickColor : pcm                (bool)          []
    
      - pickValue : pv                 (bool)          []
    
      - playbackCursor : plc           (float, float)  []
    
      - playbackPressure : plp         (float)         []
    
      - preserveclonesource : pcs      (bool)          []
    
      - profileShapeFile : psf         (unicode)       [query,edit]
          Passes a name of the image file for the stamp shape profile.
    
      - projective : prm               (bool)          [create,query,edit]
          Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
    
      - radius : r                     (float)         [create,query,edit]
          Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
    
      - record : rec                   (bool)          []
    
      - reflection : rn                (bool)          [create,query,edit]
          Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
    
      - reflectionaboutorigin : rno    (bool)          []
    
      - reflectionaxis : ra            (unicode)       [create,query,edit]
          Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it
          returns a string.
    
      - screenRadius : scR             (float)         []
    
      - selectclonesource : scs        (bool)          []
    
      - setcolorfeedback : scf         (bool)          [create,query,edit]
          Specifies if the color feedback is on or off. C: Default is ON. Q: When queried, it returns a boolean.
    
      - setdisplaycvs : dcv            (bool)          [create,query,edit]
          Specifies if the active cvs are displayed. C: Default is ON. Q: When queried, it returns a boolean.Flag can appear in
          Create mode of commandFlag can have multiple arguments, passed either as a tuple or a list.
    
      - setopertype : sot              (unicode)       [create,query,edit]
          Specifies the setEdit operation ("add", "transfer", "remove"). C: Default is "add". Q: When queried, it returns a
          string.
    
      - settomodify : stm              (unicode)       [create,query,edit]
          Specifies the name of the set to modify. Q: When queried, it returns a string.
    
      - showactive : sa                (bool)          [create,query,edit]
          Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
    
      - stampDepth : stD               (float)         []
    
      - stampProfile : stP             (unicode)       [create,query,edit]
          Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "soft",
          "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
    
      - stampSpacing : stS             (float)         []
    
      - strokesmooth : ssm             (unicode)       []
    
      - surfaceConformedBrushVertices : scv (bool)          [create,query,edit]
          Enables/disables the the display of the effective brush area as affected vertices.
    
      - tablet : tab                   (bool)          [query]
          Returns true if the tablet device is present, false if it is absent
    
      - tangentOutline : to            (bool)          [create,query,edit]
          Enables/disables the display of the brush circle tangent to the surface.
    
      - usepressure : up               (bool)          [create,query,edit]
          Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
    
      - worldRadius : wlR              (float)         []
    
    
    Derived from mel command `maya.cmds.artSetPaintCtx`
    """

    pass


def createPolySphereCtx(*args, **kwargs):
    """
    Flags:
      - attachToSubdivisionsAll : asa  (bool)          []
    
      - attachToSubdivisionsAxis : asx (bool)          []
    
      - attachToSubdivisionsHeight : ash (bool)          []
    
      - axis : ax                      (int)           []
    
      - createUVs : cuv                (int)           []
    
      - doDragEdit : dde               (bool)          []
    
      - doSubdivisionsCapsEdit : dsc   (bool)          []
    
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
      - radius : r                     (float)         []
    
      - subdivisionsHeight : sh        (int)           []
    
      - subdivisionsWidth : sw         (int)           []
    
    
    Derived from mel command `maya.cmds.createPolySphereCtx`
    """

    pass


def currentTimeCtx(*args, **kwargs):
    """
    This command creates a context which may be used to change current time within the graph editor
    
    Flags:
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.Flag can appear in Create mode of commandFlag can have multiple
          arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.currentTimeCtx`
    """

    pass


def keyframeRegionCurrentTimeCtx(*args, **kwargs):
    """
    This command creates a context which may be used to change current time within the keyframe region of the dope sheet
    editor.
    
    Flags:
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.Flag can appear in Create mode of commandFlag can have multiple
          arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.keyframeRegionCurrentTimeCtx`
    """

    pass


def createPolyCylinderCtx(*args, **kwargs):
    """
    Flags:
      - attachToSubdivisionsAxis : asa (bool)          []
    
      - attachToSubdivisionsCap : asc  (bool)          []
    
      - attachToSubdivisionsHeight : ash (bool)          []
    
      - axis : ax                      (int)           []
    
      - createUVs : cuv                (int)           []
    
      - doDragEdit : dde               (bool)          []
    
      - doSubdivisionsCapsEdit : dsc   (bool)          []
    
      - exists : ex                    (bool)          []
    
      - height : h                     (float)         []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
      - radius : r                     (float)         []
    
      - roundCap : rc                  (bool)          []
    
      - subdivisionsAxis : sa          (int)           []
    
      - subdivisionsCap : sc           (int)           []
    
      - subdivisionsHeight : sh        (int)           []
    
    
    Derived from mel command `maya.cmds.createPolyCylinderCtx`
    """

    pass


def keyframeRegionScaleKeyCtx(*args, **kwargs):
    """
    This command creates a context which may be used to scale keyframes within the keyframe region of the dope sheet editor
    
    Flags:
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.
    
      - scaleSpecifiedKeys : ssk       (bool)          [query,edit]
          Determines if only the specified keys should be scaled. If false, the non-selected keys will be adjusted during the
          scale. The default is true.Flag can appear in Create mode of commandFlag can have multiple arguments, passed either as a
          tuple or a list.
    
      - type : typ                     (unicode)       [edit]
          rect | manip Specifies the type of scale manipulator to use
    
    
    Derived from mel command `maya.cmds.keyframeRegionScaleKeyCtx`
    """

    pass


def texturePlacementContext(*args, **kwargs):
    """
    Create a command for creating new texture placement contexts. By default label mapping is on when the context is
    created.
    
    Flags:
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - labelMapping : lm              (bool)          [create,query,edit]
          Set the context to label mapping.Flag can appear in Create mode of commandFlag can have multiple arguments, passed
          either as a tuple or a list.
    
      - name : n                       (unicode)       []
    
    
    Derived from mel command `maya.cmds.texturePlacementContext`
    """

    pass


def textureLassoContext(*args, **kwargs):
    """
    Flags:
      - drawClosed : dc                (bool)          []
    
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
    
    Derived from mel command `maya.cmds.textureLassoContext`
    """

    pass


def createPolyPipeCtx(*args, **kwargs):
    """
    Flags:
      - attachToSubdivisionsAxis : asa (bool)          []
    
      - attachToSubdivisionsCap : asc  (bool)          []
    
      - attachToSubdivisionsHeight : ash (bool)          []
    
      - attachToThickness : att        (bool)          []
    
      - axis : ax                      (int)           []
    
      - createUVs : cuv                (int)           []
    
      - doDragEdit : dde               (bool)          []
    
      - doSubdivisionsCapsEdit : dsc   (bool)          []
    
      - exists : ex                    (bool)          []
    
      - height : h                     (float)         []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
      - radius : r                     (float)         []
    
      - roundCap : rc                  (bool)          []
    
      - subdivisionsAxis : sa          (int)           []
    
      - subdivisionsCap : sc           (int)           []
    
      - subdivisionsHeight : sh        (int)           []
    
      - thickness : th                 (float)         []
    
    
    Derived from mel command `maya.cmds.createPolyPipeCtx`
    """

    pass


def graphTrackCtx(*args, **kwargs):
    """
    This command can be used to create a track context for the graph editor.
    
    Flags:
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.Flag can appear in Create mode of commandFlag can have multiple
          arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.graphTrackCtx`
    """

    pass


def srtContext(*args, **kwargs):
    """
    This command can be used to create a combined transform (translate/scale/rotate) context.
    
    Flags:
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
    
    Derived from mel command `maya.cmds.srtContext`
    """

    pass


def twoPointArcCtx(*args, **kwargs):
    """
    The twoPointArcCtx command creates a new context for creating two point circular arcs
    
    Flags:
      - degree : d                     (int)           [create,query,edit]
          Valid values are 1 or 3. Default degree 3.
    
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
      - spans : s                      (int)           [create,query,edit]
          Default is 4.Flag can appear in Create mode of commandFlag can have multiple arguments, passed either as a tuple or a
          list.
    
    
    Derived from mel command `maya.cmds.twoPointArcCtx`
    """

    pass


def artBaseCtx(*args, **kwargs):
    """
    Flags:
      - accopacity : aco               (bool)          []
    
      - afterStrokeCmd : asc           (unicode)       []
    
      - beforeStrokeCmd : bsc          (unicode)       []
    
      - brushalignment : bra           (bool)          []
    
      - brushfeedback : brf            (bool)          []
    
      - clear : clr                    (bool)          []
    
      - dragSlider : dsl               (unicode)       []
    
      - dynclonemode : dcm             (bool)          []
    
      - exists : ex                    (bool)          []
    
      - expandfilename : eef           (bool)          []
    
      - exportaspectratio : ear        (float)         []
    
      - exportfilemode : efm           (unicode)       []
    
      - exportfilesave : esf           (unicode)       []
    
      - exportfilesizex : fsx          (int)           []
    
      - exportfilesizey : fsy          (int)           []
    
      - exportfiletype : eft           (unicode)       []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - importfileload : ifl           (unicode)       []
    
      - importfilemode : ifm           (unicode)       []
    
      - importreassign : irm           (bool)          []
    
      - lastRecorderCmd : lrc          (unicode)       []
    
      - lastStampName : lsn            (unicode)       []
    
      - lowerradius : lr               (float)         []
    
      - makeStroke : mst               (int)           []
    
      - mappressure : mp               (unicode)       []
    
      - name : n                       (unicode)       []
    
      - opacity : op                   (float)         []
    
      - outline : o                    (bool)          []
    
      - outwhilepaint : owp            (bool)          []
    
      - paintmode : pm                 (unicode)       []
    
      - paintoperationtype : pot       (unicode)       []
    
      - pickColor : pcm                (bool)          []
    
      - pickValue : pv                 (bool)          []
    
      - playbackCursor : plc           (float, float)  []
    
      - playbackPressure : plp         (float)         []
    
      - preserveclonesource : pcs      (bool)          []
    
      - profileShapeFile : psf         (unicode)       []
    
      - projective : prm               (bool)          []
    
      - radius : r                     (float)         []
    
      - record : rec                   (bool)          []
    
      - reflection : rn                (bool)          []
    
      - reflectionaboutorigin : rno    (bool)          []
    
      - reflectionaxis : ra            (unicode)       []
    
      - screenRadius : scR             (float)         []
    
      - selectclonesource : scs        (bool)          []
    
      - showactive : sa                (bool)          []
    
      - stampDepth : stD               (float)         []
    
      - stampProfile : stP             (unicode)       []
    
      - stampSpacing : stS             (float)         []
    
      - strokesmooth : ssm             (unicode)       []
    
      - surfaceConformedBrushVertices : scv (bool)          []
    
      - tablet : tab                   (bool)          []
    
      - tangentOutline : to            (bool)          []
    
      - usepressure : up               (bool)          []
    
      - worldRadius : wlR              (float)         []
    
    
    Derived from mel command `maya.cmds.artBaseCtx`
    """

    pass


def ikHandleCtx(*args, **kwargs):
    """
    The ikHandle context command (ikHandleCtx) updates parameters of ikHandle tool. The options for the tool will be set to
    the flags that the user specifies.
    
    Flags:
      - autoPriorityH : apH            (bool)          [create,query,edit]
          Specifies that this handle's priority is assigned automatically.C: The default is off.Q: When queried, this flag returns
          an int.
    
      - createCurve : ccv              (bool)          [create,query,edit]
          Specifies if a curve should be automatically created for the ikSplineHandle. The flag is ignored in the ikHandleCtx.C:
          The default is on.Q: When queried, this flag returns an int.
    
      - createRootAxis : cra           (bool)          [edit]
          Specifies if a root transform should automatically be created above the joints affected by the ikSplineHandle. This
          option is used to prevent the root flipping singularity on a motion path. This flag is ignored in the ikHandleCtx.C: The
          default is off.Q: When queried, this flag returns an int.
    
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - forceSolverH : fsH             (bool)          [create,query,edit]
          Specifies if the ikSolver is enabled for the ikHandle.C: The default is on.Q: When queried, this flag returns an int.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.
    
      - numSpans : ns                  (int)           [edit]
          Specifies the number of spans in the automatically generated curve of the ikSplineHandle. This flag is ignored in the
          ikHandleCtx.C: The default is 1.Q: When queried, this flag returns an int.
    
      - parentCurve : pcv              (bool)          [edit]
          Specifies if the curve should automatically be parented to the parent of the first joint affected by the ikSplineHandle.
          The flag is ignored in the ikHandleCtx.C: The default is on.Q: When queried, this flag returns an int.
    
      - poWeightH : pwH                (float)         [create,query,edit]
          Specifies the position/orientation weight of the ikHandle.C: The default is 1.Q: When queried, this flag returns a
          float.
    
      - priorityH : pH                 (int)           [create,query,edit]
          Specifies the priority of the ikHandle.C: The default is 1.Q: When queried, this flag returns an int.
    
      - rootOnCurve : roc              (bool)          [edit]
          Specifies if the root is locked onto the curve of the ikSplineHandle. This flag is ignored in the ikHandleCtx.C: The
          default is on.Q: When queried, this flag returns an int.
    
      - rootTwistMode : rtm            (bool)          [edit]
          Specifies whether the start joint is allowed to twist or not. If not, then the required twist is distributed over the
          remaining joints. This applies to all the twist types. This flag is ignored in the ikHandleCtx.C: The default is off.Q:
          When queried, this flag returns an int.Flag can appear in Create mode of commandFlag can have multiple arguments, passed
          either as a tuple or a list.
    
      - simplifyCurve : scv            (bool)          [edit]
          Specifies if the ikSplineHandle curve should be simplified. This flag is ignored in the ikHandleCtx.C: The default is
          on.Q: When queried, this returns an int.
    
      - snapCurve : snc                (bool)          [edit]
          Specifies if the curve should automatically snap to the first joint affected by the ikSplineHandle. This flag is ignored
          in the ikHandleCtx.C: The default is off.Q: When queried, this flag returns an int.
    
      - snapHandleH : snH              (bool)          [create,query,edit]
          Specifies if the ikHandle snapping is on.C: The default is on.Q: When queried, this flag returns an int.
    
      - solverTypeH : stH              (unicode)       [create,query,edit]
          Lists what ikSolver is being used. The ikSplineSolver may not be selected. To use an ikSplineSolver use the
          ikSplineHandleCtx command.C: The default solver is the default set by the user preferences.Q: When queried, this flag
          returns a string.
    
      - stickyH : sH                   (unicode)       [create,query,edit]
          Specifies if the ikHandle is sticky or not. Valid strings are "sticky" and "off".C: The default is "off".Q: When
          queried, this flag returns a string.
    
      - twistType : tws                (unicode)       [edit]
          Specifies the type of interpolation to be used by the ikSplineHandle. This flag is ignored in the ikHandleCtx. The
          interpolation options are "linear", "easeIn", "easeOut", and "easeInOut".C: The default is "linear".Q: When queried,
          this flag returns a string.
    
      - weightH : wH                   (float)         [create,query,edit]
          Specifies the weight of the ikHandle.C: The default is 1.Q: When queried, this flag returns a float.
    
    
    Derived from mel command `maya.cmds.ikHandleCtx`
    """

    pass


def showManipCtx(*args, **kwargs):
    """
    This command can be used to create a show manip context. The show manip context will display manips for all selected
    objects that have valid manips defined for them.
    
    Flags:
      - currentNodeName : cnn          (bool)          [query]
          Returns the name of the first node that the context is attached to.Flag can appear in Create mode of commandFlag can
          have multiple arguments, passed either as a tuple or a list.
    
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - incSnap : incSnap              (int, bool)     [create,query,edit]
          If true, the manipulator owned by the context will use incremental snapping for specified mode.
    
      - incSnapRelative : isr          (int, bool)     [create,query,edit]
          If true, the manipulator owned by the context will use relative incremental snapping for specified mode.
    
      - incSnapUI : isu                (bool)          [query]
          Returns an array of elements indicating what kind of incremental snap UI is required by the manipulator owned by the
          context. If no UI is required, the result array will contain a single element of with the value 0. The other values and
          their meanings are: 1 - UI for linear incremental translate2 - UI for incremental rotate3 - UI for inclremental scale
    
      - incSnapValue : isv             (int, float)    [create,query,edit]
          Supply the step value which the manipulator owned by the context will use for specified mode.
    
      - lockSelection : ls             (bool)          [create,query,edit]
          If true, this context will never change the current selection. By default this is set to false.
    
      - name : n                       (unicode)       []
    
      - toggleIncSnap : tis            (bool)          [create,edit]
          Toggles (enables/disables) snapping for all modes.
    
      - toolFinish : tf                (script)        [create,query,edit]
          Supply the script that will be run when the user exits the script.
    
      - toolStart : ts                 (script)        [create,query,edit]
          Supply the script that will be run when the user first enters the script
    
    
    Derived from mel command `maya.cmds.showManipCtx`
    """

    pass


def manipMoveContext(*args, **kwargs):
    """
    This command can be used to create, edit, or query a move manip context. Note that the flags -s, -sv, -sr, -scr, -slp,
    -slf control the global behaviour of all move manip context. Changing one context independently is not allowed. Changing
    a context's behaviour using the above flags, will change all existing move manip context.
    
    Flags:
      - activeHandle : ah              (int)           [query,edit]
          Sets the default active handle for the manip. That is, the handle which should be initially active when the tool is
          activated. Values can be: 0 - X axis handle is active1 - Y axis handle is active2 - Z axis handle is active3 - Center
          handle (all 3 axes) is active (default)
    
      - activeHandleNormal : ahn       (int)           [query,edit]
          0 - U axis handle is active1 - V axis handle is active2 - N axis handle is active ( default )3 - Center handle (all 3
          axes) is activeapplicable only when the manip mode is 3.
    
      - alignAlong : aa                (float, float, float) [create,edit]
          Aligns active handle along vector.
    
      - editPivotMode : epm            (bool)          [query]
          Returns true manipulator is in edit pivot modeFlag can appear in Create mode of commandFlag can have multiple arguments,
          passed either as a tuple or a list.
    
      - editPivotPosition : epp        (bool)          [query]
          Returns the current position of the edit pivot manipulator.
    
      - exists : ex                    (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - interactiveUpdate : iu         (bool)          [query,edit]
          Value can be : true or false. This flag value is valid only if the mode is 3 i.e. move vertex normal.
    
      - mode : m                       (int)           [query,edit]
          Translate mode: 0 - Object Space1 - Local Space2 - World Space (default)3 - Move Along Vertex Normal4 - Move Along
          Rotation Axis5 - Move Along Live Object Axis6 - Custom Axis Orientation
    
      - orientAxes : oa                (float, float, float) [query,edit]
          Orients manipulator rotating around axes by specified angles
    
      - orientJoint : oj               (unicode)       [query,edit]
          Specifies the type of orientation for joint orientation. Valid options are: none, xyz, xzy, yxz, yzx, zxy, zyx.
    
      - orientJointEnabled : oje       (bool)          [query,edit]
          Specifies if joints should be reoriented when moved.
    
      - orientTowards : ot             (float, float, float) [create,edit]
          Orients active handle towards world point
    
      - position : p                   (bool)          [query]
          Returns the current position of the manipulator
    
      - postCommand : psc              (script)        [create]
          Specifies a command to be executed when the tool is exited.
    
      - postDragCommand : pod          (script, <type 'unicode'>) [create,edit]
          Specifies a command and a node type. The command will be executed at the end of a drag when a node of the specified type
          is in the selection.
    
      - preCommand : prc               (script)        [create]
          Specifies a command to be executed when the tool is entered.
    
      - preDragCommand : prd           (script, <type 'unicode'>) [create,edit]
          Specifies a command and a node type. The command will be executed at the start of a drag when a node of the specified
          type is in the selection.
    
      - preserveChildPosition : pcp    (bool)          [query,edit]
          When false, the children objects move when their parent is moved. When true, the worldspace position of the children
          will be maintained as the parent is moved. Default is false.
    
      - preserveUV : puv               (bool)          [query,edit]
          When false, the uvs are not changes to match the vertex edit. When true, the uvs are edited to project to new values to
          stop texture swimming as vertices are moved.
    
      - reflection : rfl               (bool)          []
          This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.
    
      - reflectionAbout : rab          (int)           []
          This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.
    
      - reflectionAxis : rfa           (int)           []
          This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.
    
      - reflectionTolerance : rft      (float)         []
          This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.
    
      - secondaryAxisOrient : sao      (unicode)       [query,edit]
          Specifies the global axis (in world coordinates) that should be used to should be used to align the second axis of the
          orientJointType triple. Valid options are xup, yup, zup, xdown, ydown, zdown, none.
    
      - snap : s                       (bool)          [query,edit]
          Value can be : true or false. Enable/Disable the discrete move. If set to true, the move manipulator of all the move
          contexts would snap at discrete points along the active handle during mouse drag. The interval between the points can be
          controlled using the 'snapValue' flag.
    
      - snapComponentsRelative : scr   (bool)          [query,edit]
          Value can be : true or false. If true, while snapping a group of CVs/Vertices, the relative spacing between them will be
          preserved. If false, all the CVs/Vertices will be snapped to the target point (is used during grid snap(hotkey 'x'), and
          point snap(hotkey 'v')) Depress the 'x' key before click-dragging the manip handle and check to see the behaviour of
          moving a bunch of CVs, with this flag ON and OFF.
    
      - snapLiveFaceCenter : slf       (bool)          [query,edit]
          Value can be : true or false. If true, while moving on the live polygon object, the move manipulator will snap to the
          face centers of the object.
    
      - snapLivePoint : slp            (bool)          [query,edit]
          Value can be : true or false. If true, while moving on the live polygon object, the move manipulator will snap to the
          vertices of the object.
    
      - snapRelative : sr              (bool)          [query,edit]
          Value can be : true or false. Applicable only when the snap is enabled. If true, the snapValue is treated relative to
          the original position before moving. If false, the snapValue is treated relative to the world origin. NOTE: If in
          local/object Space Mode, the snapRelative should be ON. Absolute discrete move is not supported in local/object mode.
    
      - snapValue : sv                 (float)         [query,edit]
          Applicable only when the snap is enabled. The manipulator of all move contexts would move in steps of 'snapValue'
    
      - tweakMode : twk                (bool)          []
    
    
    Derived from mel command `maya.cmds.manipMoveContext`
    """

    pass


def polyCutCtx(*args, **kwargs):
    """
    Create a new context to cut facets on polygonal objects In query mode, return type is based on queried flag.
    
    Flags:
      - deleteFaces : df               (bool)          []
    
      - exists : ex                    (bool)          []
    
      - extractFaces : ef              (bool)          []
    
      - extractOffset : eo             (float, float, float) []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
    
    Derived from mel command `maya.cmds.polyCutCtx`
    """

    pass


def insertJointCtx(*args, **kwargs):
    """
    The command will create an insert joint context. The insert joint tool inserts joints into an existing chain of joints.
    
    Flags:
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.Flag can appear in Create mode of
          commandFlag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.insertJointCtx`
    """

    pass


def retimeKeyCtx(*args, **kwargs):
    """
    This command creates a context which may be used to scale keyframes within the graph editor using the retime tool.
    
    Flags:
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - moveByFrame : mbf              (int)           [edit]
          Move the selected retime bar by the specified number of framesFlag can appear in Create mode of commandFlag can have
          multiple arguments, passed either as a tuple or a list.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.
    
      - snapOnFrame : sof              (bool)          [query,edit]
          When set, the retime markers will snap on frames as they are moved.
    
    
    Derived from mel command `maya.cmds.retimeKeyCtx`
    """

    pass


def curveSketchCtx(*args, **kwargs):
    """
    The curveSketchCtx command creates a new curve sketch context, also known as the "pencil context".
    
    Flags:
      - degree : d                     (int)           [create,query,edit]
          Valid values are 1 or 3Flag can appear in Create mode of commandFlag can have multiple arguments, passed either as a
          tuple or a list.
    
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
    
    Derived from mel command `maya.cmds.curveSketchCtx`
    """

    pass


def dpBirailCtx(*args, **kwargs):
    """
    Flags:
      - activeNodes : anq              (bool)          []
    
      - autoCreate : ac                (bool)          []
    
      - bldProfileFirst : bpf          (bool)          []
    
      - bldProfileLast : bpl           (bool)          []
    
      - bldProfiles : bp               (bool)          []
    
      - bldRailOne : br1               (bool)          []
    
      - bldRailTwo : br2               (bool)          []
    
      - blendFactor : bl               (float)         []
    
      - caching : cch                  (bool)          []
    
      - constructionHistory : ch       (bool)          []
    
      - exists : ex                    (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - immediate : im                 (bool)          []
    
      - name : n                       (unicode)       []
    
      - nodeState : nds                (int)           []
    
      - object : o                     (bool)          []
    
      - polygon : po                   (int)           []
    
      - reset : rs                     (bool)          []
    
      - tangentContinuityProfile1 : tp1 (bool)          []
    
      - tangentContinuityProfile2 : tp2 (bool)          []
    
      - toolNode : tnq                 (bool)          []
    
      - transformMode : tm             (int)           []
    
    
    Derived from mel command `maya.cmds.dpBirailCtx`
    """

    pass


def artAttrCtx(*args, **kwargs):
    """
    This is a context command to set the flags on the artAttrContext, which is the base context for attribute painting
    operations. All commands require the name of the context as the last argument as this provides the name of the context
    to create, edit or query. This is a context command to set the flags on the Attribute Paint Tool context.
    
    Modifications:
      - converts a whitespace-separated string of names to a list of PyNode objects for flags: (query and paintNodeArray)
    
    Flags:
      - accopacity : aco               (bool)          [create,query,edit]
          Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When
          queried, it returns a boolean.
    
      - activeListChangedProc : alp    (unicode)       [create,query,edit]
          Accpts a string which contains a MEL command that is invoked whenever the active list changes. There may be some
          situations where the UI, for example, needs to be updated, when objects are selected/deselected in the scene. In query
          mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
    
      - afterStrokeCmd : asc           (unicode)       [create,query,edit]
          The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When
          queried, it returns the current command
    
      - alphaclamp : alc               (unicode)       [create,query,edit]
          Specifies if the weight value should be alpha clamped to the lower and upper bounds. There are four options here: "none"
          - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both"
          - clamps to the lower and upper bounds. C: Default is "none". Q: When queried, it returns a string.
    
      - alphaclamplower : acl          (float)         [create,query,edit]
          Specifies the lower bound for the alpha values. C: Default is 0.0. Q: When queried, it returns a float.
    
      - alphaclampupper : acu          (float)         [create,query,edit]
          Specifies the upper bound for the alpha values. C: Default is 1.0. Q: When queried, it returns a float.
    
      - attrSelected : asl             (unicode)       [query]
          Returns a name of the currently selected attribute. Q: When queried, it returns a string.
    
      - beforeStrokeCmd : bsc          (unicode)       [create,query,edit]
          The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q:
          When queried, it returns the current command
    
      - brushalignment : bra           (bool)          [create,query,edit]
          Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector.
          C: Default is true. Q: When queried, it returns a boolean.
    
      - brushfeedback : brf            (bool)          [create,query,edit]
          Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
    
      - clamp : cl                     (unicode)       [create,query,edit]
          Specifies if the weight value should be clamped to the lower and upper bounds. There are four options here: "none" - no
          clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both" -
          clamps to the lower and upper bounds. C: Default is "none". Q: When queried, it returns a string.
    
      - clamplower : cll               (float)         [create,query,edit]
          Specifies the lower bound for the values. C: Default is 0.0. Q: When queried, it returns a float.
    
      - clampupper : clu               (float)         [create,query,edit]
          Specifies the upper bound for the values. C: Default is 1.0. Q: When queried, it returns a float.
    
      - clear : clr                    (bool)          [create,edit]
          Floods all cvs/vertices to the current value.
    
      - colorAlphaValue : cl1          (float)         []
    
      - colorRGBAValue : cl4           (float, float, float, float) []
    
      - colorRGBValue : cl3            (float, float, float) []
    
      - colorRamp : cr                 (unicode)       [create,query,edit]
          Allows a user defined color ramp to be used to map values to colors.
    
      - colorfeedback : cf             (bool)          [create,query,edit]
          Sets on/off the color feedback display. C: Default is FALSE. Q: When queried, it returns a boolean.
    
      - colorfeedbackOverride : cfo    (bool)          []
    
      - colorrangelower : crl          (float)         [create,query,edit]
          Specifies the value which maps to black when color feedback mode is on C: Default is 0.0. Q: When queried, it returns a
          float.
    
      - colorrangeupper : cru          (float)         [create,query,edit]
          Specifies the value which maps to the maximum color when color feedback mode is on C: Default is 1.0. Q: When queried,
          it returns a float.
    
      - dataTypeIndex : dti            (int)           [query,edit]
          When the selected paintable attribute is a vectorArray, it specifies which field to paint on.
    
      - disablelighting : dl           (bool)          [create,query,edit]
          If color feedback is on, this flag determines whether lighting is disabled or not for the surfaces that are affected C:
          Default is FALSE. Q: When queried, it returns a boolean.
    
      - dragSlider : dsl               (unicode)       [create,edit]
          Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The
          string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C:
          Default is "none".
    
      - duringStrokeCmd : dsk          (unicode)       [create,query,edit]
          The passed string is executed as a MEL command during the stroke, each time the mouse is dragged. C: Default is no
          command. Q: When queried, it returns the current command
    
      - dynclonemode : dcm             (bool)          []
    
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - expandfilename : eef           (bool)          [create,edit]
          If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the
          name as it is. C: Default is true.
    
      - exportaspectratio : ear        (float)         []
    
      - exportfilemode : efm           (unicode)       [create,query,edit]
          Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is
          "luminance/rgb". Q: When queried, it returns a string.
    
      - exportfilesave : esf           (unicode)       [edit]
          Exports the attribute map and saves to a specified file.
    
      - exportfilesizex : fsx          (int)           [create,query,edit]
          Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
    
      - exportfilesizey : fsy          (int)           [create,query,edit]
          Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
    
      - exportfiletype : eft           (unicode)       [create,query,edit]
          Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit"
          "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
    
      - filterNodes : fon              (bool)          [edit]
          Sets the node filter.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - importfileload : ifl           (unicode)       [edit]
          Load the attribute map a specified file.
    
      - importfilemode : ifm           (unicode)       [create,query,edit]
          Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C:
          Default is "alpha". Q: When queried, it returns a string.
    
      - importreassign : irm           (bool)          [create,query,edit]
          Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within
          Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a boolean.
    
      - interactiveUpdate : iu         (bool)          [create,query,edit]
          Specifies how often to transfer the painted values into the attribute. TRUE: transfer them "continuously" (many times
          per stroke) FALSE: transfer them only at the end of a stroke (on mouse button release) C: Default is TRUE. Q: When
          queried, it returns a boolean.
    
      - lastRecorderCmd : lrc          (unicode)       []
    
      - lastStampName : lsn            (unicode)       []
    
      - lowerradius : lr               (float)         [create,query,edit]
          Sets the lower size of the brush (only apply on tablet).
    
      - makeStroke : mst               (int)           []
    
      - mappressure : mp               (unicode)       [create,query,edit]
          Sets the tablet pressure mapping when the table is used. There are four options: "none" - the pressure has no effect,
          "opacity" - the pressure is mapped to the opacity, "radius" - the is mapped to modify the radius of the brush, "both" -
          the pressure modifies both the opacity and the radius. C: Default is "none". Q: When queried, it returns a string.
    
      - maxvalue : mxv                 (float)         [create,query,edit]
          Specifies the maximum value for each attribute. C: Default is 1.0. Q: When queried, it returns a float.
    
      - minvalue : miv                 (float)         [create,query,edit]
          Specifies the minimum value for each attribute. C: Default is 0.0. Q: When queried, it returns a float.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.
    
      - objattrArray : oaa             (unicode)       [query]
          An array of all paintable attributes. Each element of the array is a string with the following information:
          NodeType.NodeName.AttributeName.MenuType \*MenuType: type(level) of the item in the Menu (UI). Q: When queried, it
          returns a string.
    
      - opacity : op                   (float)         [create,query,edit]
          Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
    
      - outline : o                    (bool)          [create,query,edit]
          Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
    
      - outwhilepaint : owp            (bool)          [create,query,edit]
          Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a
          boolean.
    
      - paintNodeArray : pna           (unicode)       [query]
          An array of paintable nodes. Q: When queried, it returns a string.
    
      - paintattrselected : pas        (unicode)       [edit]
          An array of selected paintable attributes. Each element of the array is a string with the following information:
          NodeType.NodeName.AttributeName.
    
      - paintmode : pm                 (unicode)       [create,query,edit]
          Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried,
          it returns a string.
    
      - paintoperationtype : pot       (unicode)       []
    
      - pickColor : pcm                (bool)          []
    
      - pickValue : pv                 (bool)          []
    
      - playbackCursor : plc           (float, float)  []
    
      - playbackPressure : plp         (float)         []
    
      - preserveclonesource : pcs      (bool)          []
    
      - profileShapeFile : psf         (unicode)       [query,edit]
          Passes a name of the image file for the stamp shape profile.
    
      - projective : prm               (bool)          [create,query,edit]
          Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
    
      - radius : r                     (float)         [create,query,edit]
          Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
    
      - rampMaxColor : rxc             (float, float, float) [create,query,edit]
          Defines a special color to be used when the value is greater than or equal to the maximum value.
    
      - rampMinColor : rmc             (float, float, float) [create,query,edit]
          Defines a special color to be used when the value is less than or equal to the minimum value.
    
      - record : rec                   (bool)          []
    
      - reflection : rn                (bool)          [create,query,edit]
          Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
    
      - reflectionaboutorigin : rno    (bool)          []
    
      - reflectionaxis : ra            (unicode)       [create,query,edit]
          Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it
          returns a string.
    
      - screenRadius : scR             (float)         []
    
      - selectclonesource : scs        (bool)          []
    
      - selectedattroper : sao         (unicode)       [create,query,edit]
          Sets the edit weight operation. Four edit weights operations are provided : "absolute" - the value of the weight is
          replaced by the current one, "additive" - the value of the weight is added to the current one, "scale" - the value of
          the weight is multiplied by the current one, "smooth" - the value of the weight is divided by the current one. C:
          Default is "absolute". Q: When queried, it returns a string.
    
      - showactive : sa                (bool)          [create,query,edit]
          Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
    
      - stampDepth : stD               (float)         []
    
      - stampProfile : stP             (unicode)       [create,query,edit]
          Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "soft",
          "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
    
      - stampSpacing : stS             (float)         []
    
      - strokesmooth : ssm             (unicode)       []
    
      - surfaceConformedBrushVertices : scv (bool)          [create,query,edit]
          Enables/disables the the display of the effective brush area as affected vertices.
    
      - tablet : tab                   (bool)          [query]
          Returns true if the tablet device is present, false if it is absent
    
      - tangentOutline : to            (bool)          [create,query,edit]
          Enables/disables the display of the brush circle tangent to the surface.
    
      - toolOffProc : tfp              (unicode)       [create,query,edit]
          Accepts a strings describing the name of a MEL procedure which is invoked whenever the tool is turned off. For example,
          cloth invokes "clothPaintToolOff" when the cloth paint tool is turned on. Define this callback if your tool requires
          special functionality when your tool is deactivated. It is typical that if you implement a toolOffProc you will want to
          implement a toolOnProc as well (see the -toolOnProc flag. In query mode, the name of the currently registered MEL
          command is returned and this will be an empty string if none is defined.Flag can appear in Create mode of commandFlag
          can have multiple arguments, passed either as a tuple or a list.
    
      - toolOnProc : top               (unicode)       [create,query,edit]
          Accepts a strings describing the name of a MEL procedure which is invoked whenever the tool is turned on. For example,
          cloth invokes "clothPaintToolOn" when the cloth paint tool is turned on. Define this callback if your tool requires
          special functionality when your tool is activated. It is typical that if you implement a toolOnProc you will want to
          implement a toolOffProc as well (see the -toolOffProc flag. In query mode, the name of the currently registered MEL
          command is returned and this will be an empty string if none is defined.
    
      - useColorRamp : ucr             (bool)          [create,query,edit]
          Specifies whether the user defined color ramp should be used to map values from to colors. If this is turned off, the
          default greyscale feedback will be used.
    
      - useMaxMinColor : umc           (bool)          [create,query,edit]
          Specifies whether the out of range colors should be used. See rampMinColor and rampMaxColor flags for further details.
    
      - usepressure : up               (bool)          [create,query,edit]
          Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
    
      - value : val                    (float)         [create,query,edit]
          Specifies the value for each attribute. C: Default is 0.0. Q: When queried, it returns a float.
    
      - whichTool : wst                (unicode)       [create,query,edit]
          The string defines the name of the tool to be used for the Artisan context. An example is "artClothPaint". In query
          mode, the tool name for the given context is returned. Note: due to the way MEL works, always specify the -query flag
          last when specifying a flag which takes arguments.
    
      - worldRadius : wlR              (float)         []
    
    
    Derived from mel command `maya.cmds.artAttrCtx`
    """

    pass


def spBirailCtx(*args, **kwargs):
    """
    Flags:
      - activeNodes : anq              (bool)          []
    
      - autoCreate : ac                (bool)          []
    
      - bldProfileFirst : bpf          (bool)          []
    
      - bldProfileLast : bpl           (bool)          []
    
      - bldProfiles : bp               (bool)          []
    
      - bldRailOne : br1               (bool)          []
    
      - bldRailTwo : br2               (bool)          []
    
      - caching : cch                  (bool)          []
    
      - constructionHistory : ch       (bool)          []
    
      - exists : ex                    (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - immediate : im                 (bool)          []
    
      - name : n                       (unicode)       []
    
      - nodeState : nds                (int)           []
    
      - object : o                     (bool)          []
    
      - polygon : po                   (int)           []
    
      - reset : rs                     (bool)          []
    
      - tangentContinuityProfile1 : tp1 (bool)          []
    
      - toolNode : tnq                 (bool)          []
    
      - transformMode : tm             (int)           []
    
    
    Derived from mel command `maya.cmds.spBirailCtx`
    """

    pass


def insertKeyCtx(*args, **kwargs):
    """
    This command creates a context which may be used to insert keys within the graph editor
    
    Flags:
      - breakdown : bd                 (bool)          [query,edit]
          Specifies whether or not to create breakdown keysFlag can appear in Create mode of commandFlag can have multiple
          arguments, passed either as a tuple or a list.
    
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.
    
    
    Derived from mel command `maya.cmds.insertKeyCtx`
    """

    pass


def threePointArcCtx(*args, **kwargs):
    """
    The threePointArcCtx command creates a new context for creating 3 point arcs
    
    Flags:
      - degree : d                     (int)           [create,query,edit]
          VAlid values are 1 or 3. Default degree 3.
    
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
      - spans : s                      (int)           [create,query,edit]
          Default is 8.Flag can appear in Create mode of commandFlag can have multiple arguments, passed either as a tuple or a
          list.
    
    
    Derived from mel command `maya.cmds.threePointArcCtx`
    """

    pass


def createNurbsPlaneCtx(*args, **kwargs):
    """
    Flags:
      - attachToPatchesU : apu         (bool)          []
    
      - attachToPatchesV : apv         (bool)          []
    
      - axis : ax                      (float, float, float) []
    
      - axisType : axt                 (int)           []
    
      - doDragEdit : dde               (bool)          []
    
      - exists : ex                    (bool)          []
    
      - height : h                     (float)         []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
      - surfaceDegree : sd             (int)           []
    
      - uPatches : up                  (int)           []
    
      - vPatches : vp                  (int)           []
    
      - width : w                      (float)         []
    
    
    Derived from mel command `maya.cmds.createNurbsPlaneCtx`
    """

    pass


def userCtx(*args, **kwargs):
    """
    Flags:
      - editCommand : ec               (callable)      []
    
      - editPrompt : ep                (unicode)       []
    
      - exists : ex                    (bool)          []
    
      - finalCommand : fc              (unicode)       []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
      - noSelectionPrompt : nsp        (int, unicode)  []
    
      - selectionCount : sc            (int, int)      []
    
      - selectionFlag : flg            (int, unicode)  []
    
      - selectionMask : sm             (int, unicode)  []
    
      - selectionPrompt : sp           (unicode)       []
    
    
    Derived from mel command `maya.cmds.userCtx`
    """

    pass


def manipRotateLimitsCtx(*args, **kwargs):
    """
    Create a context for the rotate limits manipulator.
    
    Flags:
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.Flag can appear in Create mode of commandFlag can have multiple
          arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.manipRotateLimitsCtx`
    """

    pass


def mpBirailCtx(*args, **kwargs):
    """
    Flags:
      - activeNodes : anq              (bool)          []
    
      - autoCreate : ac                (bool)          []
    
      - bldProfileFirst : bpf          (bool)          []
    
      - bldProfileLast : bpl           (bool)          []
    
      - bldProfiles : bp               (bool)          []
    
      - bldRailOne : br1               (bool)          []
    
      - bldRailTwo : br2               (bool)          []
    
      - caching : cch                  (bool)          []
    
      - constructionHistory : ch       (bool)          []
    
      - exists : ex                    (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - immediate : im                 (bool)          []
    
      - name : n                       (unicode)       []
    
      - nodeState : nds                (int)           []
    
      - object : o                     (bool)          []
    
      - polygon : po                   (int)           []
    
      - reset : rs                     (bool)          []
    
      - tangentContinuityProfile1 : tp1 (bool)          []
    
      - tangentContinuityProfile2 : tp2 (bool)          []
    
      - toolNode : tnq                 (bool)          []
    
      - transformMode : tm             (int)           []
    
    
    Derived from mel command `maya.cmds.mpBirailCtx`
    """

    pass


def stitchSurfaceCtx(*args, **kwargs):
    """
    Flags:
      - activeNodes : anq              (bool)          []
    
      - autoCreate : ac                (bool)          []
    
      - bias : b                       (float)         []
    
      - caching : cch                  (bool)          []
    
      - cascade : c                    (bool)          []
    
      - constructionHistory : ch       (bool)          []
    
      - cvIthIndex : ci                (int)           []
    
      - cvJthIndex : cj                (int)           []
    
      - exists : ex                    (bool)          []
    
      - fixBoundary : fb               (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - immediate : im                 (bool)          []
    
      - keepG0Continuity : kg0         (bool)          []
    
      - keepG1Continuity : kg1         (bool)          []
    
      - name : n                       (unicode)       []
    
      - nodeState : nds                (int)           []
    
      - numberOfSamples : ns           (int)           []
    
      - object : o                     (bool)          []
    
      - parameterU : u                 (float)         []
    
      - parameterV : v                 (float)         []
    
      - positionalContinuity : pc      (bool)          []
    
      - replaceOriginal : rpo          (bool)          []
    
      - reset : rs                     (bool)          []
    
      - stepCount : sc                 (int)           []
    
      - tangentialContinuity : tc      (bool)          []
    
      - togglePointNormals : tpn       (bool)          []
    
      - togglePointPosition : tpp      (bool)          []
    
      - toggleTolerance : tt           (bool)          []
    
      - tolerance : tol                (float)         []
    
      - toolNode : tnq                 (bool)          []
    
      - weight0 : wt0                  (float)         []
    
      - weight1 : wt1                  (float)         []
    
    
    Derived from mel command `maya.cmds.stitchSurfaceCtx`
    """

    pass


def moveKeyCtx(*args, **kwargs):
    """
    This command creates a context which may be used to move keyframes within the graph editor
    
    Flags:
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - moveFunction : mf              (unicode)       [query,edit]
          linear | power | constant. Specifies how the keys are dragged. The default move type is constant where all keys move the
          same amount as controlled by user movement. Power provides a fall-off function where the center of the drag moves the
          most and the keys around the drag move less.Flag can appear in Create mode of commandFlag can have multiple arguments,
          passed either as a tuple or a list.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.
    
      - option : o                     (unicode)       [create,query,edit]
          Valid values are "move," "insert," "over," and "segmentOver." When you "move" a key, the key will not cross over (in
          time) any keys before or after it. When you "insert" a key, all keys before or after (depending upon the -timeChange
          value) will be moved an equivalent amount. When you "over" a key, the key is allowed to move to any time (as long as a
          key is not there already). When you "segmentOver" a set of keys (this option only has a noticeable effect when more than
          one key is being moved) the first key (in time) and last key define a segment (unless you specify a time range). That
          segment is then allowed to move over other keys, and keys will be moved to make room for the segment.
    
    
    Derived from mel command `maya.cmds.moveKeyCtx`
    """

    pass


def createPolySoccerBallCtx(*args, **kwargs):
    """
    Flags:
      - axis : ax                      (int)           []
    
      - createUVs : cuv                (int)           []
    
      - doDragEdit : dde               (bool)          []
    
      - doSubdivisionsCapsEdit : dsc   (bool)          []
    
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
      - radius : r                     (float)         []
    
      - sideLength : sl                (float)         []
    
    
    Derived from mel command `maya.cmds.createPolySoccerBallCtx`
    """

    pass


def clipEditorCurrentTimeCtx(*args, **kwargs):
    """
    This command creates a context which may be used to change current time within the track area of a clip editor.
    
    Flags:
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.Flag can appear in Create mode of commandFlag can have multiple
          arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.clipEditorCurrentTimeCtx`
    """

    pass


def targetWeldCtx(*args, **kwargs):
    """
    Create a new context to weld vertices together on a poly object. In query mode, return type is based on queried flag.
    
    Flags:
      - exists : ex                    (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - mergeToCenter : mtc            (bool)          [create,query,edit]
          If mergeToCenter is set to true then the source and target vertices's will be moved to the center before doing the
          merge. If set to false the source vertex will be moved to the target vertex before doing the merge.Flag can appear in
          Create mode of commandFlag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.targetWeldCtx`
    """

    pass


def jointCtx(*args, **kwargs):
    """
    The joint context command (jointCtx) updates the parameters of the joint tool. The options for the tool will be set by
    the flags the user specifies.
    
    Flags:
      - autoJointOrient : ajo          (unicode)       [create,query,edit]
          Specifies the joint orientation. Valid string choices are permutations of the axes; "none", "xyz", "yzx", "zxy", "xzy",
          "yxz", "zyx". The first letter determines which axis is aligned with the bone.C: The default is "xyz".Q: When queried,
          this flag returns a string.
    
      - autoPriorityH : apH            (bool)          [create,query,edit]
          Specifies if the ikHandle's priority is assigned automatically.C: The default is off.Q: When queried, this flag returns
          an int.
    
      - createIKHandle : ikh           (bool)          [create,query,edit]
          Enables the joint tool to create an ikHandle when the tool is completed.C: The default is off.Q: When queried, this flag
          returns an int.
    
      - degreeOfFreedomJ : dJ          (unicode)       [create,query,edit]
          Specifies the degrees of freedom for all of the joints created by the tool. Valid string choices are the free axes; "x",
          "y", "z", "xy", "xz", "yz", "xyz", and "none".C: The default is "xyz".Q: When queried, this flag returns a string.
    
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - forceSolverH : fsH             (bool)          [create,query,edit]
          Specifies if the ikSolver for the ikHandle is enabled.C: The default is on.Q: When queried, this flag returns an int.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - jointAutoLimits : jal          (bool)          [create,query,edit]
          Automatically computes the joint limits based on the kind of joint created.C: The default is off.Q: When queried, this
          flag returns an int.
    
      - jointOrientationJ : joJ        (float, float, float) [create,query,edit]
          Sets the orientation of the joints created by the tool. If autoJointOrient in on, these values will be ignored.C: The
          default is 0 0 0.Q: When queried, this flag returns an array of three floats.
    
      - largeBoneLength : lbl          (float)         [create,query,edit]
          Specifies the length above which bones should be assigned the largeBoneRadius.
    
      - largeBoneRadius : lbr          (float)         [create,query,edit]
          Specifies the radius for bones whose length is above the largeBoneLength
    
      - poWeightH : pwH                (float)         [create,query,edit]
          Specifies the position/orientation weight of the ikHandle.C: The default is 1.Q: When queried, this flag returns a
          float.
    
      - priorityH : pH                 (int)           [create,query,edit]
          Specifies the priority of the ikHandle.C: The default is on.Q: When queried, this flag returns an int.
    
      - scaleCompensateJ : scJ         (bool)          [create,query,edit]
          Specifies if scale compensate is enabled.C: The default is on.Q: When queried, this flag returns an int.
    
      - scaleJ : sJ                    (float, float, float) [create,query,edit]
          Sets the scale for the joints created by the tool.C: The default is 1 1 1.Q: When queried, this flag returns an array of
          three floats.
    
      - scaleOrientationJ : soJ        (float, float, float) [create,query,edit]
          Sets the current value for the scale orientation. If autoJointOrient in on, these values will be ignored.C: The default
          is 0 0 0.Q: When queried, this flag returns an array of three floats.
    
      - secondaryAxisOrient : sao      (unicode)       [create,query,edit]
          Specifies the orientation of the secondary rotate axis. Valid string choices are: "xup", "xdown", "yup", "ydown", "zup",
          "zdown", "none".
    
      - smallBoneLength : sbl          (float)         [create,query,edit]
          Specifies the length below which bones should be assigned the smallBoneRadius.
    
      - smallBoneRadius : sbr          (float)         [create,query,edit]
          Specifies the radius for bones whose length is below the smallBoneLength.Flag can appear in Create mode of commandFlag
          can have multiple arguments, passed either as a tuple or a list.
    
      - snapHandleH : snH              (bool)          [create,query,edit]
          Sepcifies if snapping is enabled for the ikHandle.C: The default is on.Q: When queried, this flag returns an int.
    
      - solverTypeH : stH              (unicode)       [create,query,edit]
          Sets the name of the solver to use with the ikHandle.C: The default is the solver set to the default in the user
          preferences.Q: When queried, this flag returns a string.
    
      - stickyH : sH                   (unicode)       [create,query,edit]
          Specifies if the ikHandle is sticky or not. If "sticky" is passed then the ikHandle will be sticky. If "off" is used
          then ikHandle stickiness will be turned off.C: The default is "off".Q: When queried, this flag returns a string.
    
      - symmetry : sym                 (bool)          [create,query,edit]
          Automaticaly create a symmetry joint based if symmetry is on.C: The default is off.Q: When queried, this flag returns an
          int.
    
      - symmetryAxis : sa              (unicode)       [create,query,edit]
          Automaticaly create a symmetry joint use x, y , z axis or combination to do the symmetry.C: The default is x.Q: When
          queried, this flag returns a string.
    
      - variableBoneSize : vbs         (int)           [create,query,edit]
          Specifies whether or not variable bone length and radius settings should be used.
    
      - weightH : wH                   (float)         [create,query,edit]
          Specifies the weight of the ikHandle. The weight is relative to the other ikHandles in the scene.C: The default is 1.Q:
          When queried, this flag returns a float.
    
    
    Derived from mel command `maya.cmds.jointCtx`
    """

    pass


def manipScaleLimitsCtx(*args, **kwargs):
    """
    Create a context for the scale limits manipulator.
    
    Flags:
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.Flag can appear in Create mode of commandFlag can have multiple
          arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.manipScaleLimitsCtx`
    """

    pass


def mateCtx(*args, **kwargs):
    """
    Dynamic library stub function
    
    
    Derived from mel command `maya.cmds.mateCtx`
    """

    pass


def projectionContext(*args, **kwargs):
    """
    Set the context for projection manips
    
    Flags:
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
    
    Derived from mel command `maya.cmds.projectionContext`
    """

    pass


def keyframeRegionInsertKeyCtx(*args, **kwargs):
    """
    This command creates a context which may be used to insert keys within the keyframe region of the dope sheet editor
    
    Flags:
      - breakdown : bd                 (bool)          [query,edit]
          Specifies whether or not to create breakdown keysFlag can appear in Create mode of commandFlag can have multiple
          arguments, passed either as a tuple or a list.
    
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.
    
    
    Derived from mel command `maya.cmds.keyframeRegionInsertKeyCtx`
    """

    pass


def manipMoveLimitsCtx(*args, **kwargs):
    """
    Create a context for the translate limits manipulator.
    
    Flags:
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.Flag can appear in Create mode of commandFlag can have multiple
          arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.manipMoveLimitsCtx`
    """

    pass


def texLatticeDeformContext(*args, **kwargs):
    """
    This command creates a context which may be used to deform UV maps with lattice manipulator. This context only works in
    the texture UV editor.
    
    Flags:
      - envelope : ev                  (float)         [create,query,edit]
          Specifies the influence of the lattice.
    
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - latticeColumns : lc            (int)           [create,query,edit]
          Specifies the number column points the lattice contains. The maximum size lattice is restricted to 8 columns.
    
      - latticeRows : lr               (int)           [create,query,edit]
          Specifies the number of rows the lattice contains. The maximum size lattice is restricted to 8 rows.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.
    
      - snapPixelMode : spm            (bool)          [create,query,edit]
          Specifies the influenced uv points should be snapped to a pixel center or corner.
    
      - useBoundingRect : ubr          (bool)          [create,query,edit]
          When constructing the lattice use the bounding box of the selected UVs for the extents of the lattice. When this is
          disabled the extents of the marquee selections are used as the extents for the lattice.Flag can appear in Create mode of
          commandFlag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.texLatticeDeformContext`
    """

    pass


def polyAppendFacetCtx(*args, **kwargs):
    """
    Create a new context to append facets on polygonal objects In query mode, return type is based on queried flag.
    
    Flags:
      - append : ap                    (bool)          [create,query,edit]
          Allows to switch to polyCreateFacetCtx tool
    
      - exists : ex                    (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - isRotateAvailable : isr        (bool)          [query]
          Tells if the control associated to rotate flag is available. If several edges are already selected and they are not
          aligned (thus there is no "rotation axis") the rotation is no longer available.
    
      - maximumNumberOfPoints : mp     (int)           [create,query,edit]
          Allows the ability to set a upper bound on the number of points in interactively place before polygon is created. A
          value less than 2 will mean that there is no upper bound.Flag can appear in Create mode of commandFlag can have multiple
          arguments, passed either as a tuple or a list.
    
      - planarConstraint : pc          (bool)          [create,query,edit]
          Allows/avoid new facet to be non-planar.If on, all new points will be projected onto current facet plane. Selected edges
          will be checked as well.
    
      - rotate : r                     (float)         [create,query,edit]
          Rotate current facet around the first edge selected.
    
      - subdivision : s                (int)           [create,query,edit]
          Number of sub-edges created for each new edge. Default is 1.
    
      - texture : tx                   (int)           []
    
    
    Derived from mel command `maya.cmds.polyAppendFacetCtx`
    """

    pass


def keyframeRegionSelectKeyCtx(*args, **kwargs):
    """
    This command creates a context which may be used to select keyframes within the keyframe region of the dope sheet editor
    
    Flags:
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.Flag can appear in Create mode of commandFlag can have multiple
          arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.keyframeRegionSelectKeyCtx`
    """

    pass


def keyframeRegionTrackCtx(*args, **kwargs):
    """
    This command can be used to create a track context for the dope sheet editor.
    
    Flags:
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.Flag can appear in Create mode of commandFlag can have multiple
          arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.keyframeRegionTrackCtx`
    """

    pass


def roundCRCtx(*args, **kwargs):
    """
    Flags:
      - activeNodes : anq              (bool)          []
    
      - append : a                     (bool)          []
    
      - autoCreate : ac                (bool)          []
    
      - caching : cch                  (bool)          []
    
      - constructionHistory : ch       (bool)          []
    
      - currentEdge : ce               (bool)          []
    
      - currentEdgeRadius : cer        (bool)          []
    
      - exists : ex                    (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - immediate : im                 (bool)          []
    
      - name : n                       (unicode)       []
    
      - nodeState : nds                (int)           []
    
      - object : o                     (bool)          []
    
      - radius : r                     (float)         []
    
      - radiusToUse : rtu              (float)         []
    
      - reset : rs                     (bool)          []
    
      - tolerance : tol                (float)         []
    
      - toolNode : tnq                 (bool)          []
    
      - useGlobalTolerance : ugt       (bool)          []
    
    
    Derived from mel command `maya.cmds.roundCRCtx`
    """

    pass


def blendCtx(*args, **kwargs):
    """
    Flags:
      - activeNodes : anq              (bool)          []
    
      - autoCreate : ac                (bool)          []
    
      - autoDirection : ad             (bool)          []
    
      - caching : cch                  (bool)          []
    
      - constructionHistory : ch       (bool)          []
    
      - crvsInFirstRail : cfr          (int)           []
    
      - exists : ex                    (bool)          []
    
      - flipLeft : fl                  (bool)          []
    
      - flipRight : fr                 (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - immediate : im                 (bool)          []
    
      - leftParameter : lp             (float)         []
    
      - multipleKnots : mk             (bool)          []
    
      - name : n                       (unicode)       []
    
      - nodeState : nds                (int)           []
    
      - object : o                     (bool)          []
    
      - polygon : po                   (int)           []
    
      - positionTolerance : pt         (float)         []
    
      - reset : rs                     (bool)          []
    
      - rightParameter : rp            (float)         []
    
      - tangentTolerance : tt          (float)         []
    
      - toolNode : tnq                 (bool)          []
    
      - useGlobalTol : ugt             (bool)          []
    
    
    Derived from mel command `maya.cmds.blendCtx`
    """

    pass


def ctxEditMode(*args, **kwargs):
    """
    This command tells the current context to switch edit modes.It acts as a toggle.
    
    
    Derived from mel command `maya.cmds.ctxEditMode`
    """

    pass


def texSmudgeUVContext(*args, **kwargs):
    """
    This command creates a context for smudge UV tool. This context only works in the texture UV editor.
    
    Flags:
      - dragSlider : ds                (unicode)       [query,edit]
          radius | none Enables the drag slider mode. This is to support brush resizing while holding the 'b' or 'B' button.
    
      - effectType : et                (unicode)       [query,edit]
          fixed | smudge Specifies the effect of the tool. In fixed mode, the UVs move as if they are attached by a rubber band.
          In smudge mode the UVs are moved as the cursor is dragged over the UVs.
    
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - functionType : ft              (unicode)       [query,edit]
          exponential | linear | constant. Specifies how UVs fall off from the center of influence.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.
    
      - pressure : prs                 (float)         [query,edit]
          Pressure value when effect type is set to smudge.
    
      - radius : r                     (float)         [query,edit]
          Radius of the smudge tool. All UVs within this radius are affected by the tool
    
      - smudgeIsMiddle : sim           (bool)          [query,edit]
          By default, the left mouse button initiates the smudge. However, this conflicts with selection. When smudgeIsMiddle is
          on, smudge mode is activated by the middle mouse button instead of the left mouse button.Flag can appear in Create mode
          of commandFlag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.texSmudgeUVContext`
    """

    pass


def ikSplineHandleCtx(*args, **kwargs):
    """
    The ikSplineHandle context command (ikSplineHandleCtx) updates parameters of ikSplineHandle tool. The options for the
    tool will be set to the flags the user specifies.
    
    Flags:
      - autoPriorityH : apH            (bool)          [create,query,edit]
          Specifies that this handle's priority is assigned automatically.C: The default is off.Q: When queried, this flag returns
          an int.
    
      - createCurve : ccv              (bool)          [create,query,edit]
          Specifies if a curve should be automatically created for the ikSplineHandle.C: The default is on.Q: When queried, this
          flag returns an int.
    
      - createRootAxis : cra           (bool)          [edit]
          Specifies if a root transform should automatically be created above the joints affected by the ikSplineHandle. This
          option is used to prevent the root flipping singularity on a motion path.C: The default is off.Q: When queried, this
          flag returns an int.
    
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - forceSolverH : fsH             (bool)          [create,query,edit]
          Specifies if the ikSolver is enabled for the ikHandle.C: The default is on.Q: When queried, this flag returns an int.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.
    
      - numSpans : ns                  (int)           [edit]
          Specifies the number of spans in the automatically generated curve of the ikSplineHandle.C: The default is 1.Q: When
          queried, this flag returns an int.
    
      - parentCurve : pcv              (bool)          [edit]
          Specifies if the curve should automatically be parented to the parent of the first joint affected by the
          ikSplineHandle.C: The default is on.Q: When queried, this flag returns an int.
    
      - poWeightH : pwH                (float)         [create,query,edit]
          Specifies the position/orientation weight of the ikHandle.C: The default is 1.Q: When queried, this flag returns a
          float.
    
      - priorityH : pH                 (int)           [create,query,edit]
          Specifies the priority of the ikHandle.C: The default is 1.Q: When queried, this flag returns an int.
    
      - rootOnCurve : roc              (bool)          [edit]
          Specifies if the root is locked onto the curve of the ikSplineHandle.C: The default is on.Q: When queried, this flag
          returns an int.
    
      - rootTwistMode : rtm            (bool)          [edit]
          Specifies whether the start joint is allowed to twist or not. If not, then the required twist is distributed over the
          remaining joints. This applies to all the twist types. C: The default is off.Q: When queried, this flag returns an
          int.Flag can appear in Create mode of commandFlag can have multiple arguments, passed either as a tuple or a list.
    
      - simplifyCurve : scv            (bool)          [edit]
          Specifies if the ikSplineHandle curve should be simplified.C: The default is on.Q: When queried, this returns an int.
    
      - snapCurve : snc                (bool)          [edit]
          Specifies if the curve should automatically snap to the first joint affected by the ikSplineHandle.C: The default is
          off.Q: When queried, this flag returns an int.
    
      - snapHandleH : snH              (bool)          [create,query,edit]
          Specifies if the ikHandle snapping is on. This flag is ignored for the ikSplineSolver.C: The default is on.Q: When
          queried, this flag returns an int.
    
      - solverTypeH : stH              (unicode)       [create,query,edit]
          Lists what ikSolver is being used. For the ikSplineContext the solver can only be the ikSplineSolver and this flag is
          ignored.C: The default solver is the ikSplineSolver.Q: When queried, this flag returns a string.
    
      - stickyH : sH                   (unicode)       [create,query,edit]
          Specifies if the ikHandle is sticky or not. Valid strings are "sticky" and "off". This flag is ignored for the
          ikSplineSolver.C: The default is "off".Q: When queried, this flag returns a string.
    
      - twistType : tws                (unicode)       [edit]
          Specifies the type of interpolation to be used by the ikSplineHandle.The interpolation options are "linear", "easeIn",
          "easeOut", and "easeInOut".C: The default is "linear".Q: When queried, this flag returns a string.
    
      - weightH : wH                   (float)         [create,query,edit]
          Specifies the weight of the ikHandle. This flag is ignored in the ikSplineHandleCtx.C: The default is 1.Q: When queried,
          this flag returns a float.
    
    
    Derived from mel command `maya.cmds.ikSplineHandleCtx`
    """

    pass


def polyShortestPathCtx(*args, **kwargs):
    """
    Creates a new context to select shortest edge path between two vertices or UVs in the 3d viewport. In query mode, return
    type is based on queried flag.
    
    Flags:
      - exists : ex                    (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
    
    Derived from mel command `maya.cmds.polyShortestPathCtx`
    """

    pass


def ctxTraverse(*args, **kwargs):
    """
    This command tells the current context to do a traversal.Some contexts will ignore this command. Individual contexts
    determine what up/down left/right mean.
    
    Flags:
      - down : d                       (bool)          [create]
          Move "down" as defined by the current context.
    
      - left : l                       (bool)          [create]
          Move "left" as defined by the current context.Flag can appear in Create mode of commandFlag can have multiple arguments,
          passed either as a tuple or a list.
    
      - right : r                      (bool)          [create]
          Move "right" as defined by the current context.
    
      - up : up                        (bool)          [create]
          Move "up" as defined by the current context.
    
    
    Derived from mel command `maya.cmds.ctxTraverse`
    """

    pass


def shadingLightRelCtx(*args, **kwargs):
    """
    This command creates a context that can be used for associating lights to shading groups. You can put the context into
    shading-centric mode by using the -shadingCentric flag and specifying true. This means that the shading group is
    selected first then lights associated with the shading group are highlighted. Subsequent selections result in
    assignments. Specifying -shadingCentric false means that the light is to be selected first. The shading groups
    associated with the light will then be selected and subsequent selections will result in assignments being made.
    
    Flags:
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
      - offCommand : ofc               (unicode)       [create,query,edit]
          command to be issued when context is turned onFlag can appear in Create mode of commandFlag can have multiple arguments,
          passed either as a tuple or a list.
    
      - onCommand : onc                (unicode)       [create,query,edit]
          command to be issued when context is turned on
    
      - shadingCentric : s             (bool)          [create,query,edit]
          shading-centric mode.
    
    
    Derived from mel command `maya.cmds.shadingLightRelCtx`
    """

    pass


def createNurbsCircleCtx(*args, **kwargs):
    """
    Flags:
      - attachToSections : attachToSections (bool)          []
    
      - degree : d                     (int)           []
    
      - doDragEdit : dde               (bool)          []
    
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
      - normal : nr                    (float, float, float) []
    
      - normalType : nrt               (int)           []
    
      - radius : r                     (float)         []
    
      - sections : sc                  (int)           []
    
      - sweep : sw                     (float)         []
    
      - tolerance : tol                (float)         []
    
      - toleranceType : tlt            (int)           []
    
      - useTolerance : ut              (bool)          []
    
    
    Derived from mel command `maya.cmds.createNurbsCircleCtx`
    """

    pass


def arcLenDimContext(*args, **kwargs):
    """
    Command used to register the arcLenDimCtx tool.
    
    Flags:
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
    
    Derived from mel command `maya.cmds.arcLenDimContext`
    """

    pass


def createPolyCubeCtx(*args, **kwargs):
    """
    Flags:
      - attachToSubdivisionsAll : asa  (bool)          []
    
      - attachToSubdivisionsDepth : asd (bool)          []
    
      - attachToSubdivisionsHeight : ash (bool)          []
    
      - attachToSubdivisionsWidth : asw (bool)          []
    
      - axis : ax                      (int)           []
    
      - createUVs : cuv                (int)           []
    
      - depth : d                      (float)         []
    
      - doDragEdit : dde               (bool)          []
    
      - doSubdivisionsCapsEdit : dsc   (bool)          []
    
      - exists : ex                    (bool)          []
    
      - height : h                     (float)         []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
      - subdivisionsDepth : sd         (int)           []
    
      - subdivisionsHeight : sh        (int)           []
    
      - subdivisionsWidth : sw         (int)           []
    
      - width : w                      (float)         []
    
    
    Derived from mel command `maya.cmds.createPolyCubeCtx`
    """

    pass


def drawExtrudeFacetCtx(*args, **kwargs):
    """
    Flags:
      - degree : d                     (int)           []
    
      - divisions : div                (int)           []
    
      - exists : ex                    (bool)          []
    
      - facesTogether : ft             (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
    
    Derived from mel command `maya.cmds.drawExtrudeFacetCtx`
    """

    pass


def softModContext(*args, **kwargs):
    """
    Dynamic library stub function
    
    
    Derived from mel command `maya.cmds.softModContext`
    """

    pass


def renderWindowSelectContext(*args, **kwargs):
    """
    Set the selection context for the render view panel.
    
    Flags:
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.Flag can appear in Create mode of
          commandFlag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.renderWindowSelectContext`
    """

    pass


def keyframeRegionDirectKeyCtx(*args, **kwargs):
    """
    This command creates a context which may be used to directly manipulate keyframes within the dope sheet editor
    
    Flags:
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.
    
      - option : o                     (unicode)       [create]
          Valid values are "move," "insert," "over," and "segmentOver." When you "move" a key, the key will not cross over (in
          time) any keys before or after it. When you "insert" a key, all keys before or after (depending upon the -timeChange
          value) will be moved an equivalent amount. When you "over" a key, the key is allowed to move to any time (as long as a
          key is not there already). When you "segmentOver" a set of keys (this option only has a noticeable effect when more than
          one key is being moved) the first key (in time) and last key define a segment (unless you specify a time range). That
          segment is then allowed to move over other keys, and keys will be moved to make room for the segment.Flag can appear in
          Create mode of commandFlag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.keyframeRegionDirectKeyCtx`
    """

    pass


def polySlideEdgeCtx(*args, **kwargs):
    """
    Flags:
      - absolute : a                   (bool)          []
    
      - direction : d                  (int)           []
    
      - edgeDirection : ed             (float)         []
    
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
      - snappingPoints : sp            (int)           []
    
      - snappingTolerance : st         (float)         []
    
      - useSnapping : us               (bool)          []
    
    
    Derived from mel command `maya.cmds.polySlideEdgeCtx`
    """

    pass


def currentCtx(*args, **kwargs):
    """
    This command returns the currently selected tool context.
    
    
    Derived from mel command `maya.cmds.currentCtx`
    """

    pass


def ctxAbort(*args, **kwargs):
    """
    This command tells the current context to reset itself, losing what has been done so far. If a escape context has been
    set it then makes that context current.
    
    
    Derived from mel command `maya.cmds.ctxAbort`
    """

    pass


def propModCtx(*args, **kwargs):
    """
    Controls the proportional move context.
    
    Flags:
      - animCurve : ac                 (unicode)       [create,query,edit]
          Name of the anim curve to use as a drop-off curve. Only the 0 -side of the curve will be used and the distance will be
          mapped to "seconds". The profile of the curve will be used as the profile for propmod function.
    
      - animCurveFalloff : acf         (float, float)  [create,query,edit]
          The profile of the curve will be used as the profile for propmod function in both U and V. This will be scaled in U, V
          according to the paramters provided. The ratio of the U, V scaling parameters will dictate the footprint of the fuction
          while the curve itself provides the magnitudes.Flag can appear in Create mode of commandFlag can have multiple
          arguments, passed either as a tuple or a list.
    
      - animCurveParam : acp           (unicode)       [create,query,edit]
          Name of the anim curve to use as a drop-off curve. Only the 0 -side of the curve will be used and the distance will be
          mapped to "seconds", where 1 second maps to 0.01 units in parametric space.
    
      - direction : d                  (float, float, float) [create,query,edit]
          Direction along which to compute the distance for the distance based drop-off functions. The default is (1 1 1)
    
      - exists : ex                    (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - linear : l                     (float)         [create,query,edit]
          If using linear drop-off function, this is its slope. The default of -0.1 means the point at the locator moves with it
          and the point 10 units away doesn't move at all.
    
      - linearParam : lp               (float, float)  [create,query,edit]
          If using parametric linear drop-off function, these specify its limits along the U and V directions.
    
      - nurbsCurve : nc                (unicode)       [create,query,edit]
          Name of the nurbs curve to use as a drop-off curve. The closest point distance would be used as the drop off percentage.
    
      - powerCutoff : pc               (float)         [create,query,edit]
          If using the power drop-off function, this is its distance cutoff value. The default is 10.0.
    
      - powerCutoffParam : pcp         (float, float)  [create,query,edit]
          If using the power drop-off function, these specify one of it's limits, 0 for U, and 1 and V. The default cutoff is
          10.0.
    
      - powerDegree : pd               (float)         [create,query,edit]
          If using the power drop-off function, this is its degree. The default is 3.
    
      - powerDegreeParam : pdp         (float)         [create,query,edit]
          If using the power drop-off function, this is its degree. The default is 3.
    
      - script : s                     (unicode)       [create,query,edit]
          The name of the script to use to compute the drop-off. The script takes 6 floats as input - first 3 are the position of
          the move locator, the next 3 the position of the point to be manipulated. The script should return a drop-off
          coefficient which could be negative or zero.
    
      - scriptParam : sp               (unicode)       [create,query,edit]
          The name of the script to use to compute the drop-off. The script takes 4 floats as input - first 2 are the parametric
          position of the move locator, the next 2 the parametric position of the point to be manipulated. The script should
          return a drop-off coefficient which could be negative or zero.
    
      - type : t                       (int)           [create,query,edit]
          Choose the type for the drop-off function. Legal values are 1 for linear, 2 for power, 3 for script, 4 for anim curve.
          The default is 1.
    
      - worldspace : ws                (bool)          [create,query,edit]
          Set the space in which the tool works. True for world space, false for parametric space.
    
    
    Derived from mel command `maya.cmds.propModCtx`
    """

    pass


def curveMoveEPCtx(*args, **kwargs):
    """
    The curveMoveEPCtx command creates a new context for moving curve edit points using a manipulator. Edit points can only
    be moved one at a time.
    
    Flags:
      - exists : ex                    (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
    
    Derived from mel command `maya.cmds.curveMoveEPCtx`
    """

    pass


def greasePencilCtx(*args, **kwargs):
    """
    This is a tool context command for the grease pencil tool. In query mode, return type is based on queried flag.
    
    Flags:
      - canDraw : cd                   (int)           []
    
      - createOrEditFrame : cef        (int)           []
    
      - exists : ex                    (bool)          []
    
      - fileTextureSize : fts          (int)           []
    
      - greasePencilType : gpt         (int)           []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - removeFrame : rf               (int)           []
    
      - resetBrushes : rb              (bool)          []
    
      - rgbcolor : rgb                 (float, float, float) []
    
      - sequenceNodeName : snn         (unicode)       []
    
    
    Derived from mel command `maya.cmds.greasePencilCtx`
    """

    pass


def createNurbsCubeCtx(*args, **kwargs):
    """
    Flags:
      - attachToPatchesU : apu         (bool)          []
    
      - attachToPatchesV : apv         (bool)          []
    
      - axis : ax                      (float, float, float) []
    
      - axisType : axt                 (int)           []
    
      - depth : d                      (float)         []
    
      - doDragEdit : dde               (bool)          []
    
      - exists : ex                    (bool)          []
    
      - height : h                     (float)         []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
      - surfaceDegree : sd             (int)           []
    
      - uPatches : up                  (int)           []
    
      - vPatches : vp                  (int)           []
    
      - width : w                      (float)         []
    
    
    Derived from mel command `maya.cmds.createNurbsCubeCtx`
    """

    pass


def texMoveContext(*args, **kwargs):
    """
    This command can be used to create, edit, or query a texture editor move manip context. Note that the above flags
    control the global behaviour of all texture editor move manip contexts. Changing one context independently is not
    allowed. Changing a context's behaviour using the above flags, will change all existing texture editor move manip
    contexts.
    
    Flags:
      - exists : ex                    (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - position : p                   (bool)          [query]
          Returns the current position of the manipulator
    
      - snapComponentsRelative : scr   (bool)          [query,edit]
          Value can be : true or false. If true, while snapping a group of UVs, the relative spacing between them will be
          preserved. If false, all the UVs will be snapped to the target point
    
      - snapPixelMode : spm            (int)           [query,edit]
          set the snapping mode to be the pixel center or upper left cornerFlag can appear in Create mode of commandFlag can have
          multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.texMoveContext`
    """

    pass


def createPolyConeCtx(*args, **kwargs):
    """
    Flags:
      - attachToSubdivisionsAxis : asa (bool)          []
    
      - attachToSubdivisionsCap : asc  (bool)          []
    
      - attachToSubdivisionsHeight : ash (bool)          []
    
      - axis : ax                      (int)           []
    
      - createUVs : cuv                (int)           []
    
      - doDragEdit : dde               (bool)          []
    
      - doSubdivisionsCapsEdit : dsc   (bool)          []
    
      - exists : ex                    (bool)          []
    
      - height : h                     (float)         []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
      - radius : r                     (float)         []
    
      - roundCap : rc                  (bool)          []
    
      - subdivisionsDepth : sd         (int)           []
    
      - subdivisionsHeight : sh        (int)           []
    
      - subdivisionsWidth : sw         (int)           []
    
    
    Derived from mel command `maya.cmds.createPolyConeCtx`
    """

    pass


def dollyCtx(*args, **kwargs):
    """
    This command can be used to create, edit, or query a dolly context.
    
    Flags:
      - alternateContext : ac          (bool)          [create,query,edit]
          Set the ALT+LMB+MMB and ALT+CRL+LMB to refer to this context.
    
      - boxDollyType : bdt             (unicode)       [create,query,edit]
          Set the behavior of where the camera's center of interest is set to after the box dolly. In surfacemode, the center of
          interest will be snapped to the surface point at the center of the marquee. In bboxmode, the closest bounding box to the
          camera will be used. Bounding box mode will use the selection mask to determine which objects to include into the
          calculation.
    
      - centerOfInterestDolly : cd     (bool)          [create,query,edit]
          Set the translate the camera's center of interest. Left and right drag movements with the mouse will translate the
          center of interest towards or away respectively from the camera. The center of interest can be snapped to objects by
          using the left mouse button for selection. The default select mask will be used.
    
      - dollyTowardsCenter : dtc       (bool)          [create,query,edit]
          Dolly towards center (if true), else dolly towards point where user clicks in the view.Flag can appear in Create mode of
          commandFlag can have multiple arguments, passed either as a tuple or a list.
    
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - localDolly : ld                (bool)          [create,query,edit]
          Dolly with respect to the camera's center of interest. The camera will not pass through the center of interest. Local
          dolly only applies to perspective cameras.
    
      - name : n                       (unicode)       []
    
      - scale : s                      (float)         [create,query,edit]
          The sensitivity for dollying the camera.
    
      - toolName : tn                  (unicode)       []
    
    
    Derived from mel command `maya.cmds.dollyCtx`
    """

    pass


def texMoveUVShellContext(*args, **kwargs):
    """
    This command can be used to create, edit, or query a texture editor move manip context. Note that the above flags
    control the global behaviour of all texture editor move manip contexts. Changing one context independently is not
    allowed. Changing a context's behaviour using the above flags, will change all existing texture editor move manip
    contexts.
    
    Flags:
      - exists : ex                    (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - iterations : it                (int)           []
    
      - mask : m                       (bool)          []
    
      - position : p                   (bool)          [query]
          Returns the current position of the manipulatorFlag can appear in Create mode of commandFlag can have multiple
          arguments, passed either as a tuple or a list.
    
      - shellBorder : sb               (float)         []
    
    
    Derived from mel command `maya.cmds.texMoveUVShellContext`
    """

    pass


def texSmoothContext(*args, **kwargs):
    """
    Flags:
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
      - pinBorder : pb                 (bool)          []
    
      - space : sp                     (int)           []
    
    
    Derived from mel command `maya.cmds.texSmoothContext`
    """

    pass


def curveCVCtx(*args, **kwargs):
    """
    The curveCVCtx command creates a new context for creating curves by placing control vertices (CVs).
    
    Flags:
      - bezier : bez                   (bool)          []
    
      - degree : d                     (int)           [create,query,edit]
          valid values are 1, 2, 3, 5 or 7. Default is degree 3.
    
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - multEndKnots : me              (bool)          [create,query,edit]
          Default is true. False means that the curve will not pass through the end control vertices (CVs).
    
      - name : n                       (unicode)       []
    
      - preserveShape : ps             (bool)          []
    
      - rational : rl                  (bool)          []
    
      - refit : rf                     (bool)          []
    
      - symmetry : sm                  (bool)          []
    
      - uniform : un                   (bool)          [create,query,edit]
          Default is true, which means uniform parameterization will be used. False means chord length parameterization.Flag can
          appear in Create mode of commandFlag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.curveCVCtx`
    """

    pass


def distanceDimContext(*args, **kwargs):
    """
    Command used to register the distanceDimCtx tool.
    
    Flags:
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
    
    Derived from mel command `maya.cmds.distanceDimContext`
    """

    pass


def view2dToolCtx(*args, **kwargs):
    """
    This class creates a context for the View Tools "track", "dolly", and "box zoom" in the Hypergraph.
    
    Flags:
      - alternateContext : ac          (bool)          []
    
      - boxzoom : bz                   (bool)          [create,query]
          Perform Box ZoomFlag can appear in Create mode of commandFlag can have multiple arguments, passed either as a tuple or a
          list.
    
      - dolly : do                     (bool)          [create,query]
          Dollies the view
    
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
      - toolName : tn                  (unicode)       []
    
      - track : tr                     (bool)          [create,query]
          Tracks the view
    
    
    Derived from mel command `maya.cmds.view2dToolCtx`
    """

    pass


def artSelectCtx(*args, **kwargs):
    """
    This command is used to select/deselect/toggle components on selected surfaces using a brush interface (Maya Artisan).
    Since, it selects components of the surface, it only works in the component mode. In query mode, return type is based on
    queried flag.
    
    Flags:
      - accopacity : aco               (bool)          [create,query,edit]
          Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When
          queried, it returns a boolean.
    
      - addselection : ads             (bool)          [create,query,edit]
          If true, each new stroke adds cvs to the active list. If false, each stroke replaces the previous selection. C: Default
          is true. Q: When queried, it returns a boole
    
      - afterStrokeCmd : asc           (unicode)       [create,query,edit]
          The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When
          queried, it returns the current commandFlag can appear in Create mode of commandFlag can have multiple arguments, passed
          either as a tuple or a list.
    
      - beforeStrokeCmd : bsc          (unicode)       [create,query,edit]
          The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q:
          When queried, it returns the current command
    
      - brushalignment : bra           (bool)          [create,query,edit]
          Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector.
          C: Default is true. Q: When queried, it returns a boolean.
    
      - brushfeedback : brf            (bool)          [create,query,edit]
          Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
    
      - clear : clr                    (bool)          [create,edit]
          Floods all cvs/vertices to the current value.
    
      - dragSlider : dsl               (unicode)       [create,edit]
          Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The
          string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C:
          Default is "none".
    
      - dynclonemode : dcm             (bool)          []
    
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - expandfilename : eef           (bool)          [create,edit]
          If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the
          name as it is. C: Default is true.
    
      - exportaspectratio : ear        (float)         []
    
      - exportfilemode : efm           (unicode)       [create,query,edit]
          Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is
          "luminance/rgb". Q: When queried, it returns a string.
    
      - exportfilesave : esf           (unicode)       [edit]
          Exports the attribute map and saves to a specified file.
    
      - exportfilesizex : fsx          (int)           [create,query,edit]
          Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
    
      - exportfilesizey : fsy          (int)           [create,query,edit]
          Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
    
      - exportfiletype : eft           (unicode)       [create,query,edit]
          Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit"
          "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - importfileload : ifl           (unicode)       [edit]
          Load the attribute map a specified file.
    
      - importfilemode : ifm           (unicode)       [create,query,edit]
          Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C:
          Default is "alpha". Q: When queried, it returns a string.
    
      - importreassign : irm           (bool)          [create,query,edit]
          Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within
          Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a boolean.
    
      - importthreshold : ift          (float)         [create,query,edit]
          Specifies the threshold for the import of the attribute maps. C: Default is 0.5. Q: When queried, it returns a float.
    
      - lastRecorderCmd : lrc          (unicode)       []
    
      - lastStampName : lsn            (unicode)       []
    
      - lowerradius : lr               (float)         [create,query,edit]
          Sets the lower size of the brush (only apply on tablet).
    
      - makeStroke : mst               (int)           []
    
      - mappressure : mp               (unicode)       [create,query,edit]
          Sets the tablet pressure mapping when the table is used. There are four options: "none" - the pressure has no effect,
          "opacity" - the pressure is mapped to the opacity, "radius" - the is mapped to modify the radius of the brush, "both" -
          the pressure modifies both the opacity and the radius. C: Default is "none". Q: When queried, it returns a string.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.
    
      - opacity : op                   (float)         [create,query,edit]
          Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
    
      - outline : o                    (bool)          [create,query,edit]
          Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
    
      - outwhilepaint : owp            (bool)          [create,query,edit]
          Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a
          boolean.
    
      - paintmode : pm                 (unicode)       [create,query,edit]
          Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried,
          it returns a string.
    
      - paintoperationtype : pot       (unicode)       []
    
      - pickColor : pcm                (bool)          []
    
      - pickValue : pv                 (bool)          []
    
      - playbackCursor : plc           (float, float)  []
    
      - playbackPressure : plp         (float)         []
    
      - preserveclonesource : pcs      (bool)          []
    
      - profileShapeFile : psf         (unicode)       [query,edit]
          Passes a name of the image file for the stamp shape profile.
    
      - projective : prm               (bool)          [create,query,edit]
          Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
    
      - radius : r                     (float)         [create,query,edit]
          Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
    
      - record : rec                   (bool)          []
    
      - reflection : rn                (bool)          [create,query,edit]
          Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
    
      - reflectionaboutorigin : rno    (bool)          []
    
      - reflectionaxis : ra            (unicode)       [create,query,edit]
          Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it
          returns a string.
    
      - screenRadius : scR             (float)         []
    
      - selectall : sal                (bool)          [create,edit]
          Selects all vertices/egdes/faces/uvs.
    
      - selectclonesource : scs        (bool)          []
    
      - selectop : sop                 (unicode)       [create,query,edit]
          Specifies the selection operation ("select", "unselect", "toggle"). C: Default is "select". Q: When queried, it returns
          a string.
    
      - showactive : sa                (bool)          [create,query,edit]
          Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
    
      - stampDepth : stD               (float)         []
    
      - stampProfile : stP             (unicode)       [create,query,edit]
          Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "soft",
          "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
    
      - stampSpacing : stS             (float)         []
    
      - strokesmooth : ssm             (unicode)       []
    
      - surfaceConformedBrushVertices : scv (bool)          [create,query,edit]
          Enables/disables the the display of the effective brush area as affected vertices.
    
      - tablet : tab                   (bool)          [query]
          Returns true if the tablet device is present, false if it is absent
    
      - tangentOutline : to            (bool)          [create,query,edit]
          Enables/disables the display of the brush circle tangent to the surface.
    
      - toggleall : tal                (bool)          [create,edit]
          Toggle all vertices/egdes/faces/uvs.
    
      - unselectall : ual              (bool)          [create,edit]
          Unselects all vertices/egdes/faces/uvs.
    
      - usepressure : up               (bool)          [create,query,edit]
          Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
    
      - worldRadius : wlR              (float)         []
    
    
    Derived from mel command `maya.cmds.artSelectCtx`
    """

    pass


def polyMergeFacetCtx(*args, **kwargs):
    """
    Create a new context to merge facets on polygonal objects In query mode, return type is based on queried flag.
    
    Flags:
      - activeNodes : anq              (bool)          [query]
          Return the active nodes in the tool
    
      - caching : cch                  (bool)          []
    
      - constructionHistory : ch       (bool)          []
    
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - firstFacet : ff                (int)           []
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - immediate : im                 (bool)          [edit]
          Acts on the object not the tool defaults
    
      - mergeMode : mm                 (int)           [create,query,edit]
          The merge mode. (at first facet : 0, in between : 1, at last facet : 2)Default is in between.Flag can appear in Create
          mode of commandFlag can have multiple arguments, passed either as a tuple or a list.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.
    
      - nodeState : nds                (int)           []
    
      - previous : pv                  (bool)          [edit]
          Reset to previously stored values
    
      - reset : rs                     (bool)          [edit]
          Reset to default values
    
      - secondFacet : sf               (int)           []
    
      - toolNode : tnq                 (bool)          [query]
          Return the node used for tool defaults
    
    
    Derived from mel command `maya.cmds.polyMergeFacetCtx`
    """

    pass


def texRotateContext(*args, **kwargs):
    """
    This command can be used to create, edit, or query a rotate context for the UV Texture Editor. Note that the above flag
    controls the global behaviour of all texture editor rotate contexts. Changing one context independently is not allowed.
    Changing a context's behaviour using the above flag, will change all existing texture editor rotate contexts.
    
    Flags:
      - exists : ex                    (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - position : p                   (bool)          [query]
          Returns the current position of the manipulatorFlag can appear in Create mode of commandFlag can have multiple
          arguments, passed either as a tuple or a list.
    
      - snap : s                       (bool)          []
    
      - snapRelative : sr              (bool)          []
    
      - snapValue : sv                 (float)         []
    
    
    Derived from mel command `maya.cmds.texRotateContext`
    """

    pass


def wrinkleContext(*args, **kwargs):
    """
    This command creates a context that creates wrinkles.
    
    Flags:
      - branchCount : brc              (int)           [create,query,edit]
          Set the number of branches spawned from a crease for radial wrinkles. Default is 2.
    
      - branchDepth : bd               (int)           [create,query,edit]
          Set the depth of branching for radial wrinkles. Defaults to 0.
    
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.
    
      - randomness : rnd               (float)         [create,query,edit]
          Set the deviation of the wirnkle creases from straight lines and other elements of the wrinkle structure. Defaults to
          0.2.
    
      - style : st                     (unicode)       [create,query,edit]
          Set the wrinkle characteristic shape."lines"|"radial"|"custom. Default is "radial".
    
      - thickness : th                 (float)         [create,query,edit]
          Set the thickness of wirnkle creases by setting the dropoff distance on the underlying wires.Flag can appear in Create
          mode of commandFlag can have multiple arguments, passed either as a tuple or a list.
    
      - wrinkleCount : wc              (int)           [create,query,edit]
          Set the number of wrinkle creases. Default is 3.
    
      - wrinkleIntensity : wi          (float)         [create,query,edit]
          Set the depth intensity of the wrinkle furrows. Defaults to 0.5.
    
    
    Derived from mel command `maya.cmds.wrinkleContext`
    """

    pass


def graphDollyCtx(*args, **kwargs):
    """
    This command can be used to create a dolly context for the graph editor.
    
    Flags:
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.Flag can appear in Create mode of commandFlag can have multiple
          arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.graphDollyCtx`
    """

    pass


def lassoContext(*args, **kwargs):
    """
    Creates a context to perform selection via a "lasso". Use for irregular selection regions, where the "marquee-style"
    select of the "selectContext" is inappropriate.
    
    Flags:
      - drawClosed : dc                (bool)          []
    
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - fastComponents : fc            (bool)          []
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.Flag can appear in Create mode of commandFlag can have multiple
          arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.lassoContext`
    """

    pass


def snapshotBeadContext(*args, **kwargs):
    """
    Dynamic library stub function
    
    
    Derived from mel command `maya.cmds.snapshotBeadContext`
    """

    pass


def keyframeRegionSetKeyCtx(*args, **kwargs):
    """
    This command creates a context which may be used to set keys within the keyframe region of the dope sheet editor
    
    Flags:
      - breakdown : bd                 (bool)          [query,edit]
          Specifies whether or not to create breakdown keysFlag can appear in Create mode of commandFlag can have multiple
          arguments, passed either as a tuple or a list.
    
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.
    
    
    Derived from mel command `maya.cmds.keyframeRegionSetKeyCtx`
    """

    pass


def createNurbsSphereCtx(*args, **kwargs):
    """
    Flags:
      - attachToHeightRatio : ahr      (bool)          []
    
      - attachToSections : attachToSections (bool)          []
    
      - attachToSpans : asp            (bool)          []
    
      - axis : ax                      (float, float, float) []
    
      - axisType : axt                 (int)           []
    
      - degree : d                     (int)           []
    
      - doDragEdit : dde               (bool)          []
    
      - endSweep : esw                 (float)         []
    
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
      - radius : r                     (float)         []
    
      - sections : sc                  (int)           []
    
      - spans : sp                     (int)           []
    
      - startSweep : ssw               (float)         []
    
      - tolerance : tol                (float)         []
    
      - toleranceType : tlt            (int)           []
    
      - useTolerance : ut              (bool)          []
    
    
    Derived from mel command `maya.cmds.createNurbsSphereCtx`
    """

    pass


def alignCtx(*args, **kwargs):
    """
    The alignCtx command creates a tool for aligning and distributing objects.
    
    Flags:
      - align : a                      (bool)          [create,query,edit]
          Align objects
    
      - anchorFirstObject : afo        (bool)          [create,query,edit]
          Anchor first or last selected object. Default false. Only applicable when aligning objects.
    
      - distribute : d                 (bool)          [create,query,edit]
          Distribute objects
    
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.
    
      - showAlignTouch : sat           (bool)          [create,query,edit]
          Show or hide align touching handles. Default true. Only applicable when aligning objects.Flag can appear in Create mode
          of commandFlag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.alignCtx`
    """

    pass


def ctxCompletion(*args, **kwargs):
    """
    This command tells the current context to finish what it is doing and create any objects that is is working on.
    
    
    Derived from mel command `maya.cmds.ctxCompletion`
    """

    pass


def polyCreaseCtx(*args, **kwargs):
    """
    Create a new context to crease components on polygonal objects In query mode, return type is based on queried flag.
    
    Flags:
      - createSet : cs                 (unicode)       [edit]
          Creates a set for the selected components.Flag can appear in Create mode of commandFlag can have multiple arguments,
          passed either as a tuple or a list.
    
      - exists : ex                    (bool)          []
    
      - extendSelection : es           (bool)          [create,query,edit]
          Enable/disable extending selection to all connected creased components.
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - relative : r                   (bool)          [create,query,edit]
          Enable/disable applying value relative to existing crease value. If disabled, absolute value is applied.
    
    
    Derived from mel command `maya.cmds.polyCreaseCtx`
    """

    pass


def scriptCtx(*args, **kwargs):
    """
    This command allows a user to create their own tools based on the selection tool. A number of selection lists can be
    collected, the behaviour of the selection and the selection masks are fully customizable, etc. The command is processed
    prior to being executed. The keyword "$Selection#" where # is a number 1 or greater specifies a selection set. The
    context can specify several selection sets which are substituted in place of the $Selection# keyword in the form of a
    Mel string array. Items that are specific per set need to be specified in each set, if they are going to be specified
    for any of the sets. See examples below. In addition, in order to specify the type of selection you need to be making,
    any of the selection type flags from "selectType" command can be used here.
    
    Flags:
      - allComponents : alc            (bool)          []
    
      - allObjects : alo               (bool)          []
    
      - animBreakdown : abd            (bool)          []
    
      - animCurve : ac                 (bool)          []
    
      - animInTangent : ait            (bool)          []
    
      - animKeyframe : ak              (bool)          []
    
      - animOutTangent : aot           (bool)          []
    
      - baseClassName : bcn            (unicode)       [create,query,edit]
          This string will be used to produce MEL function names for the property sheets for the tool. For example, if
          "myScriptTool" was given, the functions "myScriptToolValues" and "myScriptToolProperties" will be used for the property
          sheets. The default is "scriptTool".
    
      - byName : bn                    (unicode, int)  []
    
      - camera : ca                    (bool)          []
    
      - cluster : cl                   (bool)          []
    
      - collisionModel : clm           (bool)          []
    
      - controlVertex : cv             (bool)          []
    
      - cumulativeLists : cls          (bool)          [create,query,edit]
          If set, the selection lists will be cumulative. For example, the second list will contain all the items from the first
          list, the third all the items from the second list etc. Make sure your script specified above takes that into account.
          Relevant if there is more than one selection set.
    
      - curve : c                      (bool)          []
    
      - curveKnot : ck                 (bool)          []
    
      - curveOnSurface : cos           (bool)          []
    
      - curveParameterPoint : cpp      (bool)          []
    
      - dimension : dim                (bool)          []
    
      - dynamicConstraint : dc         (bool)          []
    
      - edge : eg                      (bool)          []
    
      - editPoint : ep                 (bool)          []
    
      - emitter : em                   (bool)          []
    
      - enableRootSelection : ers      (bool)          [create,query,edit]
          If set, the items to be selected are at their root transform level. Default is false.
    
      - exists : ex                    (bool)          []
    
      - exitUponCompletion : euc       (bool)          [create,query,edit]
          If set, completing the last selection set will exit the tool. Default is true.
    
      - expandSelectionList : esl      (bool)          [create,query,edit]
          If set, the selection lists will expand to have a single component in each item. You probably want this as a default,
          otherwise two isoparms on the same surface will show up as 1 item. To ensure that components on the same object are
          returned in the order in which they are selected, use the selectPref -trackSelectionOrder oncommand in your
          -toolStartscript to enable ordered selection, then restore it to its original value in your -toolFinishscript.
    
      - facet : fc                     (bool)          []
    
      - field : fi                     (bool)          []
    
      - finalCommandScript : fcs       (script)        [create,query,edit]
          Supply the script that will be run when the user presses the enter key and the context is completed. Depending on the
          number of selection sets you have, the script can make use of variables string $Selection1[], $Selection2[], ...
    
      - fluid : fl                     (bool)          []
    
      - follicle : fo                  (bool)          []
    
      - forceAddSelect : fas           (bool)          [create,query,edit]
          If set to true, together with -setAutoToggleSelection (see below) on the first selection set, causes the first selection
          after the computation of the previous result to be "shift" selection, unless a modifier key is pressed. Default is
          false. Flags for each selection set. These flags are multi-use.
    
      - hairSystem : hs                (bool)          []
    
      - handle : ha                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - hull : hl                      (bool)          []
    
      - ignoreInvalidItems : iii       (bool)          [create,query,edit]
          If you have multiple selection sets, the state of the selection set is recorded at the time you "complete it". You could
          then delete some of the items in that list and end up with invalid items in one or more of your selection sets. If this
          flag is set, those items will be detected and ignored. You will never know it happened. Its as if they were never
          selected in the first place, except that your selection set now does not have as many items as it may need. If this flag
          is not set, you will get a warning and your final command callback script will likely not execute because of an error
          condition.
    
      - ikEndEffector : iee            (bool)          []
    
      - ikHandle : ikh                 (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - imagePlane : ip                (bool)          []
    
      - implicitGeometry : ig          (bool)          []
    
      - isoparm : iso                  (bool)          []
    
      - joint : j                      (bool)          []
    
      - jointPivot : jp                (bool)          []
    
      - lastAutoComplete : lac         (bool)          [create,query,edit]
          True if auto complete is set for the last selection set, false otherwise. Mostly used for query, but if present in
          conjuction with -sac/setAutoComplete flag, -sac flag takes precedence.
    
      - lattice : la                   (bool)          []
    
      - latticePoint : lp              (bool)          []
    
      - light : lt                     (bool)          []
    
      - localRotationAxis : ra         (bool)          []
    
      - locator : lc                   (bool)          []
    
      - locatorUV : luv                (bool)          []
    
      - locatorXYZ : xyz               (bool)          []
    
      - meshComponents : mc            (bool)          []
    
      - motionTrailPoint : mtp         (bool)          []
    
      - motionTrailTangent : mtt       (bool)          []
    
      - nCloth : ncl                   (bool)          []
    
      - nParticle : npr                (bool)          []
    
      - nParticleShape : nps           (bool)          []
    
      - nRigid : nr                    (bool)          []
    
      - name : n                       (unicode)       []
    
      - nonlinear : nl                 (bool)          []
    
      - nurbsCurve : nc                (bool)          []
    
      - nurbsSurface : ns              (bool)          []
    
      - objectComponent : ocm          (bool)          []
    
      - orientationLocator : ol        (bool)          []
    
      - particle : pr                  (bool)          []
    
      - particleShape : ps             (bool)          []
    
      - plane : pl                     (bool)          []
    
      - polymesh : p                   (bool)          []
    
      - polymeshEdge : pe              (bool)          []
    
      - polymeshFace : pf              (bool)          []
    
      - polymeshFreeEdge : pfe         (bool)          []
    
      - polymeshUV : puv               (bool)          []
    
      - polymeshVertex : pv            (bool)          []
    
      - polymeshVtxFace : pvf          (bool)          []
    
      - queryByName : qbn              (unicode)       []
    
      - rigidBody : rb                 (bool)          []
    
      - rigidConstraint : rc           (bool)          []
    
      - rotatePivot : rp               (bool)          []
    
      - scalePivot : sp                (bool)          []
    
      - sculpt : sc                    (bool)          []
    
      - selectHandle : sh              (bool)          []
    
      - setAllowExcessCount : sae      (bool)          [create,edit]
          If set, the number if items is to be interpreted as the minimum.
    
      - setAutoComplete : sac          (bool)          [create,edit]
          If set to true, as soon as the specified number of items is selected the tool will start the next selection set or run
          the command.
    
      - setAutoToggleSelection : sat   (bool)          [create,edit]
          If set to true, it is as if "shift" key is pressed when there are no modifiers pressed. That means that you get the
          "toggle select" behaviour by default. This only applies to the 3D view, and the selection done in the hypergraph,
          outliner or elsewhere is still a subject to the usual rules.Flag can appear in Create mode of commandFlag can have
          multiple arguments, passed either as a tuple or a list.
    
      - setDoneSelectionPrompt : dsp   (unicode)       [create,edit]
          If setAutoComplete is not set (see below) this string will be shown as soon as the tool has enough items for a
          particular selection set. If this is not set, but is needed, the same string as set with -setSelectionPrompt flag will
          be used.
    
      - setNoSelectionHeadsUp : snh    (unicode)       [create,edit]
          Supply a string that will be shown as a heads up prompt when there is nothing selected. This must be set separately for
          each selection set.
    
      - setNoSelectionPrompt : snp     (unicode)       [create,edit]
          Supply a string that will be shown as help when there is nothing selected. This must be set separately for each
          selection set.
    
      - setSelectionCount : ssc        (int)           [create,edit]
          The number of items in this selection set. 0 means as many as you need until completion.
    
      - setSelectionHeadsUp : ssh      (unicode)       [create,edit]
          Supply a string that will be shown as a heads up prompt when there is something selected. This must be set separately
          for each selection set.
    
      - setSelectionPrompt : ssp       (unicode)       [create,edit]
          Supply a string that will be shown as help when there is something selected. This must be set separately for each
          selection set.
    
      - sets : set                     (bool)          []
    
      - showManipulators : sm          (bool)          [create,query,edit]
          If set, the manipulators will be shown for any active objects. Basically, it is as if you are in the Show Manipulator
          tool.
    
      - slugObject : slo               (bool)          []
    
      - slugVertex : sv                (bool)          []
    
      - spotlightComponent : slc       (bool)          []
    
      - spring : spr                   (bool)          []
    
      - springComponent : spc          (bool)          []
    
      - stroke : str                   (bool)          []
    
      - subdiv : sd                    (bool)          []
    
      - subdivMeshEdge : sme           (bool)          []
    
      - subdivMeshFace : smf           (bool)          []
    
      - subdivMeshPoint : smp          (bool)          []
    
      - subdivMeshUV : smu             (bool)          []
    
      - subdivisionPolymesh : spl      (bool)          []
    
      - subdivisionPolymeshEdge : spe  (bool)          []
    
      - subdivisionPolymeshFace : spf  (bool)          []
    
      - subdivisionPolymeshVertex : spv (bool)          []
    
      - surfaceEdge : se               (bool)          []
    
      - surfaceFace : sf               (bool)          []
    
      - surfaceKnot : sk               (bool)          []
    
      - surfaceParameterPoint : spp    (bool)          []
    
      - surfaceRange : sr              (bool)          []
    
      - surfaceUV : suv                (bool)          []
    
      - texture : tx                   (bool)          []
    
      - title : t                      (unicode)       [create,query,edit]
          Supply a string that will be used as a precursor to all the messages; i.e., the "name" of the tool.
    
      - toolCursorType : tct           (unicode)       [create,query,edit]
          Supply the string identifier to set the tool cursor type when inside of tool. The following are the valid ids: "create",
          "dolly", "edit", "pencil", "track", "trackHorizontal", "trackVertical", "transformation", "tumble", "zoom", "zoomIn",
          "zoomOut", "flyThrough", "dot", "fleur", "leftArrow", "question", "doubleHorizArrow", "doubleVertArrow", "sizing",
          "dollyIn", "dollyOut", "brush", "camera", "noAccess", "input", "output", "leftCycle", "rightCycle", "rightExpand",
          "knife".
    
      - toolFinish : tf                (script)        [create,query,edit]
          Supply the script that will be run when the user exits the script.
    
      - toolStart : ts                 (script)        [create,query,edit]
          Supply the script that will be run when the user first enters the script
    
      - totalSelectionSets : tss       (int)           [create,query,edit]
          Total number of selection sets.
    
      - vertex : v                     (bool)          []
    
    
    Derived from mel command `maya.cmds.scriptCtx`
    """

    pass


def directKeyCtx(*args, **kwargs):
    """
    This command creates a context which may be used to directly manipulate keyframes within the graph editor
    
    Flags:
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.
    
      - option : o                     (unicode)       [create,query,edit]
          Valid values are "move," "insert," "over," and "segmentOver." When you "move" a key, the key will not cross over (in
          time) any keys before or after it. When you "insert" a key, all keys before or after (depending upon the -timeChange
          value) will be moved an equivalent amount. When you "over" a key, the key is allowed to move to any time (as long as a
          key is not there already). When you "segmentOver" a set of keys (this option only has a noticeable effect when more than
          one key is being moved) the first key (in time) and last key define a segment (unless you specify a time range). That
          segment is then allowed to move over other keys, and keys will be moved to make room for the segment.
    
      - selectedOnly : so              (bool)          [create,query,edit]
          Controls whether only selected curves/keys can be moved, or all.Flag can appear in Create mode of commandFlag can have
          multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.directKeyCtx`
    """

    pass


def selectKeyCtx(*args, **kwargs):
    """
    This command creates a context which may be used to select keyframes within the graph editor
    
    Flags:
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.Flag can appear in Create mode of commandFlag can have multiple
          arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.selectKeyCtx`
    """

    pass


def manipRotateContext(*args, **kwargs):
    """
    This command can be used to create, edit, or query a rotate manip context.
    
    Flags:
      - activeHandle : ah              (int)           [query,edit]
          Sets the default active handle for the manip. That is, the handle which should be initially active when the tool is
          activated. Values can be: 0 - X axis handle is active1 - Y axis handle is active2 - Z axis handle is active3 - View
          rotation handle (outer ring) is active (default)
    
      - centerTrackball : ctb          (bool)          []
    
      - editPivotMode : epm            (bool)          [query]
          Returns true manipulator is in edit pivot mode
    
      - editPivotPosition : epp        (bool)          [query]
          Returns the current position of the edit pivot manipulator.
    
      - exists : ex                    (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - mode : m                       (int)           [query,edit]
          Arcball mode (0 - Object Space (default), 1 - World Space)
    
      - position : p                   (bool)          [query]
          Returns the current position of the manipulator
    
      - postDragCommand : pod          (script, <type 'unicode'>) [create,edit]
          Specifies a command and a node type. The command will be executed at the end of a drag when a node of the specified type
          is in the selection.
    
      - preDragCommand : prd           (script, <type 'unicode'>) [create,edit]
          Specifies a command and a node type. The command will be executed at the start of a drag when a node of the specified
          type is in the selection.
    
      - preserveChildPosition : pcp    (bool)          [query,edit]
          When false, the children objects move when their parent is rotated. When true, the worldspace position of the children
          will be maintained as the parent is moved. Default is false.Flag can appear in Create mode of commandFlag can have
          multiple arguments, passed either as a tuple or a list.
    
      - preserveUV : puv               (bool)          []
    
      - reflection : rfl               (bool)          []
          This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.
    
      - reflectionAbout : rab          (int)           []
          This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.
    
      - reflectionAxis : rfa           (int)           []
          This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.
    
      - reflectionTolerance : rft      (float)         []
          This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.
    
      - snap : s                       (bool)          []
    
      - snapRelative : sr              (bool)          []
    
      - snapValue : sv                 (float)         []
    
      - tweakMode : twk                (bool)          []
    
      - useManipPivot : ump            (bool)          []
    
      - useObjectPivot : uop           (bool)          []
    
    
    Derived from mel command `maya.cmds.manipRotateContext`
    """

    pass


def softModCtx(*args, **kwargs):
    """
    Controls the softMod context.
    
    Flags:
      - dragSlider : ds                (unicode)       [edit]
          Specify the slider mode for hotkey radius resizing.
    
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - falseColor : fc                (bool)          [edit]
          Enable or disable false color display on the soft mod manipulator.Flag can appear in Create mode of commandFlag can have
          multiple arguments, passed either as a tuple or a list.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - reset : rst                    (bool)          [query,edit]
          Reset the tool options to their default values.
    
    
    Derived from mel command `maya.cmds.softModCtx`
    """

    pass


def createNurbsConeCtx(*args, **kwargs):
    """
    Flags:
      - attachToHeightRatio : ahr      (bool)          []
    
      - attachToSections : attachToSections (bool)          []
    
      - attachToSpans : asp            (bool)          []
    
      - axis : ax                      (float, float, float) []
    
      - axisType : axt                 (int)           []
    
      - caps : cp                      (int)           []
    
      - doDragEdit : dde               (bool)          []
    
      - endSweep : esw                 (float)         []
    
      - exists : ex                    (bool)          []
    
      - extraTransformOnCaps : xtc     (bool)          []
    
      - height : h                     (float)         []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
      - radius : r                     (float)         []
    
      - sections : sc                  (int)           []
    
      - spans : sp                     (int)           []
    
      - startSweep : ssw               (float)         []
    
      - surfaceDegree : sd             (int)           []
    
      - tolerance : tol                (float)         []
    
      - toleranceType : tlt            (int)           []
    
      - useTolerance : ut              (bool)          []
    
    
    Derived from mel command `maya.cmds.createNurbsConeCtx`
    """

    pass


def skinBindCtx(*args, **kwargs):
    """
    This command creates a tool that can be used to edit volumes from an interactive bind.
    
    Flags:
      - about : a                      (unicode)       [create,query,edit]
          The space in which the axis should be mirrored. Valid values are: "world" and "object".
    
      - axis : ax                      (unicode)       [create,query,edit]
          The mirror axis. Valid values are: "x","y", and "z".
    
      - colorRamp : cr                 (unicode)       [create,query,edit]
          Set the values on the color ramp used to display the weight values.
    
      - currentInfluence : ci          (int)           [create,query,edit]
          Set the index of the current influence or volume to be adjusted by the manipulator.
    
      - displayInactiveMode : di       (int)           [create,query,edit]
          Determines the display mode for drawing volumes that are not selected, in particular which volume cages if any are
          displayed. 0 - None 1 - Nearby volumes 2 - All volumes
    
      - displayNormalized : dn         (bool)          [create,query,edit]
          Display raw select weights (false) or finalized normalized weights (true).
    
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - falloffCurve : fc              (unicode)       [create,query,edit]
          Set the values on the falloff curve control.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.
    
      - symmetry : s                   (bool)          [create,query,edit]
          Controls whether or not the tool operates in symmetric (mirrored) mode.
    
      - tolerance : t                  (float)         [create,query,edit]
          The tolerance setting for determining whether another influence is symmetric to the the current influence.Flag can
          appear in Create mode of commandFlag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.skinBindCtx`
    """

    pass


def superCtx(*args, **kwargs):
    """
    Flags:
      - attach : a                     (unicode)       []
    
      - exists : ex                    (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
    
    Derived from mel command `maya.cmds.superCtx`
    """

    pass


def artAttrPaintVertexCtx(*args, **kwargs):
    """
    This is a context command to set the flags on the artAttrContext, which is the base context for attribute painting
    operations. All commands require the name of the context as the last argument as this provides the name of the context
    to create, edit or query. This is a context command to set the flags on the Paint color on vertex Tool context. In query
    mode, return type is based on queried flag.
    
    Flags:
      - accopacity : aco               (bool)          [create,query,edit]
          Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When
          queried, it returns a boolean.
    
      - activeListChangedProc : alp    (unicode)       [create,query,edit]
          Accpts a string which contains a MEL command that is invoked whenever the active list changes. There may be some
          situations where the UI, for example, needs to be updated, when objects are selected/deselected in the scene. In query
          mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
    
      - afterStrokeCmd : asc           (unicode)       [create,query,edit]
          The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When
          queried, it returns the current command
    
      - alphaclamp : alc               (unicode)       [create,query,edit]
          Specifies if the weight value should be alpha clamped to the lower and upper bounds. There are four options here: "none"
          - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both"
          - clamps to the lower and upper bounds. C: Default is "none". Q: When queried, it returns a string.
    
      - alphaclamplower : acl          (float)         [create,query,edit]
          Specifies the lower bound for the alpha values. C: Default is 0.0. Q: When queried, it returns a float.
    
      - alphaclampupper : acu          (float)         [create,query,edit]
          Specifies the upper bound for the alpha values. C: Default is 1.0. Q: When queried, it returns a float.
    
      - attrSelected : asl             (unicode)       [query]
          Returns a name of the currently selected attribute. Q: When queried, it returns a string.
    
      - beforeStrokeCmd : bsc          (unicode)       [create,query,edit]
          The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q:
          When queried, it returns the current command
    
      - brushalignment : bra           (bool)          [create,query,edit]
          Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector.
          C: Default is true. Q: When queried, it returns a boolean.
    
      - brushfeedback : brf            (bool)          [create,query,edit]
          Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
    
      - clamp : cl                     (unicode)       [create,query,edit]
          Specifies if the weight value should be clamped to the lower and upper bounds. There are four options here: "none" - no
          clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both" -
          clamps to the lower and upper bounds. C: Default is "none". Q: When queried, it returns a string.
    
      - clamplower : cll               (float)         [create,query,edit]
          Specifies the lower bound for the values. C: Default is 0.0. Q: When queried, it returns a float.
    
      - clampupper : clu               (float)         [create,query,edit]
          Specifies the upper bound for the values. C: Default is 1.0. Q: When queried, it returns a float.
    
      - clear : clr                    (bool)          [create,edit]
          Floods all cvs/vertices to the current value.
    
      - colorAlphaValue : cl1          (float)         []
    
      - colorRGBAValue : cl4           (float, float, float, float) []
    
      - colorRGBValue : cl3            (float, float, float) []
    
      - colorRamp : cr                 (unicode)       [create,query,edit]
          Allows a user defined color ramp to be used to map values to colors.
    
      - colorfeedback : cf             (bool)          [create,query,edit]
          Sets on/off the color feedback display. C: Default is FALSE. Q: When queried, it returns a boolean.
    
      - colorfeedbackOverride : cfo    (bool)          []
    
      - colorrangelower : crl          (float)         [create,query,edit]
          Specifies the value which maps to black when color feedback mode is on C: Default is 0.0. Q: When queried, it returns a
          float.
    
      - colorrangeupper : cru          (float)         [create,query,edit]
          Specifies the value which maps to the maximum color when color feedback mode is on C: Default is 1.0. Q: When queried,
          it returns a float.
    
      - dataTypeIndex : dti            (int)           [query,edit]
          When the selected paintable attribute is a vectorArray, it specifies which field to paint on.
    
      - disablelighting : dl           (bool)          [create,query,edit]
          If color feedback is on, this flag determines whether lighting is disabled or not for the surfaces that are affected C:
          Default is FALSE. Q: When queried, it returns a boolean.
    
      - dragSlider : dsl               (unicode)       [create,edit]
          Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The
          string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C:
          Default is "none".
    
      - duringStrokeCmd : dsk          (unicode)       [create,query,edit]
          The passed string is executed as a MEL command during the stroke, each time the mouse is dragged. C: Default is no
          command. Q: When queried, it returns the current command
    
      - dynclonemode : dcm             (bool)          []
    
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - expandfilename : eef           (bool)          [create,edit]
          If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the
          name as it is. C: Default is true.
    
      - exportaspectratio : ear        (float)         []
    
      - exportfilemode : efm           (unicode)       [create,query,edit]
          Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is
          "luminance/rgb". Q: When queried, it returns a string.
    
      - exportfilesave : esf           (unicode)       [edit]
          Exports the attribute map and saves to a specified file.
    
      - exportfilesizex : fsx          (int)           [create,query,edit]
          Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
    
      - exportfilesizey : fsy          (int)           [create,query,edit]
          Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
    
      - exportfiletype : eft           (unicode)       [create,query,edit]
          Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit"
          "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
    
      - filterNodes : fon              (bool)          [edit]
          Sets the node filter.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - importfileload : ifl           (unicode)       [edit]
          Load the attribute map a specified file.
    
      - importfilemode : ifm           (unicode)       [create,query,edit]
          Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C:
          Default is "alpha". Q: When queried, it returns a string.
    
      - importreassign : irm           (bool)          [create,query,edit]
          Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within
          Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a boolean.
    
      - interactiveUpdate : iu         (bool)          [create,query,edit]
          Specifies how often to transfer the painted values into the attribute. TRUE: transfer them "continuously" (many times
          per stroke) FALSE: transfer them only at the end of a stroke (on mouse button release) C: Default is TRUE. Q: When
          queried, it returns a boolean.
    
      - lastRecorderCmd : lrc          (unicode)       []
    
      - lastStampName : lsn            (unicode)       []
    
      - lowerradius : lr               (float)         [create,query,edit]
          Sets the lower size of the brush (only apply on tablet).
    
      - makeStroke : mst               (int)           []
    
      - mappressure : mp               (unicode)       [create,query,edit]
          Sets the tablet pressure mapping when the table is used. There are four options: "none" - the pressure has no effect,
          "opacity" - the pressure is mapped to the opacity, "radius" - the is mapped to modify the radius of the brush, "both" -
          the pressure modifies both the opacity and the radius. C: Default is "none". Q: When queried, it returns a string.
    
      - maxvalue : mxv                 (float)         [create,query,edit]
          Specifies the maximum value for each attribute. C: Default is 1.0. Q: When queried, it returns a float.
    
      - minvalue : miv                 (float)         [create,query,edit]
          Specifies the minimum value for each attribute. C: Default is 0.0. Q: When queried, it returns a float.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.
    
      - objattrArray : oaa             (unicode)       [query]
          An array of all paintable attributes. Each element of the array is a string with the following information:
          NodeType.NodeName.AttributeName.MenuType \*MenuType: type(level) of the item in the Menu (UI). Q: When queried, it
          returns a string.
    
      - opacity : op                   (float)         [create,query,edit]
          Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
    
      - outline : o                    (bool)          [create,query,edit]
          Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
    
      - outwhilepaint : owp            (bool)          [create,query,edit]
          Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a
          boolean.
    
      - paintComponent : pc            (int)           [create,query,edit]
          Specifies whether face or vertex or vertex face is being painted. 1 - Vertex 2 - VertexFace 3 - Face C: Default is
          Vertex. Q: When queried, it returns a int.
    
      - paintNodeArray : pna           (unicode)       [query]
          An array of paintable nodes. Q: When queried, it returns a string.
    
      - paintNumChannels : pnc         (int)           []
    
      - paintRGBA : pc4                (bool)          [create,query,edit]
          Specifies whether RGB or RGBA channels are being painted. TRUE: RGBA channels. FALSE: RGB channels. Alpha channel
          remains unaffected. C: Default is FALSE (Painting RGB channels). Q: When queried, it returns a int.
    
      - paintVertexFace : pvf          (bool)          [create,query,edit]
          Specifies whether vertex face is being painted. TRUE: Vertex face being painted. (Allows each face connected to the
          vertex to be painted) FALSE: Vertex being painted.(affects all connected faces) C: Default is FALSE. Q: When queried, it
          returns a int.
    
      - paintattrselected : pas        (unicode)       [edit]
          An array of selected paintable attributes. Each element of the array is a string with the following information:
          NodeType.NodeName.AttributeName.
    
      - paintmode : pm                 (unicode)       [create,query,edit]
          Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried,
          it returns a string.
    
      - paintoperationtype : pot       (unicode)       []
    
      - pickColor : pcm                (bool)          []
    
      - pickValue : pv                 (bool)          []
    
      - playbackCursor : plc           (float, float)  []
    
      - playbackPressure : plp         (float)         []
    
      - preserveclonesource : pcs      (bool)          []
    
      - profileShapeFile : psf         (unicode)       [query,edit]
          Passes a name of the image file for the stamp shape profile.
    
      - projective : prm               (bool)          [create,query,edit]
          Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
    
      - radius : r                     (float)         [create,query,edit]
          Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
    
      - rampMaxColor : rxc             (float, float, float) [create,query,edit]
          Defines a special color to be used when the value is greater than or equal to the maximum value.
    
      - rampMinColor : rmc             (float, float, float) [create,query,edit]
          Defines a special color to be used when the value is less than or equal to the minimum value.
    
      - record : rec                   (bool)          []
    
      - reflection : rn                (bool)          [create,query,edit]
          Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
    
      - reflectionaboutorigin : rno    (bool)          []
    
      - reflectionaxis : ra            (unicode)       [create,query,edit]
          Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it
          returns a string.
    
      - screenRadius : scR             (float)         []
    
      - selectclonesource : scs        (bool)          []
    
      - selectedattroper : sao         (unicode)       [create,query,edit]
          Sets the edit weight operation. Four edit weights operations are provided : "absolute" - the value of the weight is
          replaced by the current one, "additive" - the value of the weight is added to the current one, "scale" - the value of
          the weight is multiplied by the current one, "smooth" - the value of the weight is divided by the current one. C:
          Default is "absolute". Q: When queried, it returns a string.
    
      - showactive : sa                (bool)          [create,query,edit]
          Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
    
      - stampDepth : stD               (float)         []
    
      - stampProfile : stP             (unicode)       [create,query,edit]
          Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "soft",
          "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
    
      - stampSpacing : stS             (float)         []
    
      - strokesmooth : ssm             (unicode)       []
    
      - surfaceConformedBrushVertices : scv (bool)          [create,query,edit]
          Enables/disables the the display of the effective brush area as affected vertices.
    
      - tablet : tab                   (bool)          [query]
          Returns true if the tablet device is present, false if it is absent
    
      - tangentOutline : to            (bool)          [create,query,edit]
          Enables/disables the display of the brush circle tangent to the surface.
    
      - toolOffProc : tfp              (unicode)       [create,query,edit]
          Accepts a strings describing the name of a MEL procedure which is invoked whenever the tool is turned off. For example,
          cloth invokes "clothPaintToolOff" when the cloth paint tool is turned on. Define this callback if your tool requires
          special functionality when your tool is deactivated. It is typical that if you implement a toolOffProc you will want to
          implement a toolOnProc as well (see the -toolOnProc flag. In query mode, the name of the currently registered MEL
          command is returned and this will be an empty string if none is defined.
    
      - toolOnProc : top               (unicode)       [create,query,edit]
          Accepts a strings describing the name of a MEL procedure which is invoked whenever the tool is turned on. For example,
          cloth invokes "clothPaintToolOn" when the cloth paint tool is turned on. Define this callback if your tool requires
          special functionality when your tool is activated. It is typical that if you implement a toolOnProc you will want to
          implement a toolOffProc as well (see the -toolOffProc flag. In query mode, the name of the currently registered MEL
          command is returned and this will be an empty string if none is defined.
    
      - useColorRamp : ucr             (bool)          [create,query,edit]
          Specifies whether the user defined color ramp should be used to map values from to colors. If this is turned off, the
          default greyscale feedback will be used.
    
      - useMaxMinColor : umc           (bool)          [create,query,edit]
          Specifies whether the out of range colors should be used. See rampMinColor and rampMaxColor flags for further details.
    
      - usepressure : up               (bool)          [create,query,edit]
          Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
    
      - value : val                    (float)         [create,query,edit]
          Specifies the value for each attribute. C: Default is 0.0. Q: When queried, it returns a float.
    
      - vertexColorRange : vcr         (bool)          [create,query,edit]
          Specifies whether the vertex color range should be applied to the currently selected object. C: Default is false Q: When
          queried, it returns a boolean.
    
      - vertexColorRangeLower : vcl    (float)         [create,query,edit]
          Specifies the min value of the vertex color range. C: Default is 0.0. Q: When queried, it returns a float.
    
      - vertexColorRangeUpper : vcu    (float)         [create,query,edit]
          Specifies the max value of the vertex color range. C: Default is 1.0. Q: When queried, it returns a float.Flag can
          appear in Create mode of commandFlag can have multiple arguments, passed either as a tuple or a list.
    
      - whichTool : wst                (unicode)       [create,query,edit]
          The string defines the name of the tool to be used for the Artisan context. An example is "artClothPaint". In query
          mode, the tool name for the given context is returned. Note: due to the way MEL works, always specify the -query flag
          last when specifying a flag which takes arguments.
    
      - worldRadius : wlR              (float)         []
    
    
    Derived from mel command `maya.cmds.artAttrPaintVertexCtx`
    """

    pass


def trackCtx(*args, **kwargs):
    """
    This command can be used to create a track context.
    
    Flags:
      - alternateContext : ac          (bool)          [create,query,edit]
          Set the ALT+MMB and ALT+SFT+MMB to refer to this context.
    
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
      - toolName : tn                  (unicode)       []
    
      - trackGeometry : tg             (bool)          [create,query,edit]
          Toggle whether the drag should try to track geometry. The context will compute a track plane by intersecting the initial
          press with geometry or the live object.
    
      - trackScale : ts                (float)         [create,query,edit]
          Specify the distance to the track plane from the camera. The smaller the scale the slower the drag.Flag can appear in
          Create mode of commandFlag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.trackCtx`
    """

    pass


def artAttrSkinPaintCtx(*args, **kwargs):
    """
    This is a context command to set the flags on the artAttrContext, which is the base context for attribute painting
    operations. All commands require the name of the context as the last argument as this provides the name of the context
    to create, edit or query. This is a context command to set the flags on the Paint skin weights tool context. In query
    mode, return type is based on queried flag.
    
    Flags:
      - accopacity : aco               (bool)          [create,query,edit]
          Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When
          queried, it returns a boolean.
    
      - activeListChangedProc : alp    (unicode)       [create,query,edit]
          Accpts a string which contains a MEL command that is invoked whenever the active list changes. There may be some
          situations where the UI, for example, needs to be updated, when objects are selected/deselected in the scene. In query
          mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
    
      - afterStrokeCmd : asc           (unicode)       [create,query,edit]
          The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When
          queried, it returns the current command
    
      - alphaclamp : alc               (unicode)       [create,query,edit]
          Specifies if the weight value should be alpha clamped to the lower and upper bounds. There are four options here: "none"
          - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both"
          - clamps to the lower and upper bounds. C: Default is "none". Q: When queried, it returns a string.
    
      - alphaclamplower : acl          (float)         [create,query,edit]
          Specifies the lower bound for the alpha values. C: Default is 0.0. Q: When queried, it returns a float.
    
      - alphaclampupper : acu          (float)         [create,query,edit]
          Specifies the upper bound for the alpha values. C: Default is 1.0. Q: When queried, it returns a float.
    
      - attrSelected : asl             (unicode)       [query]
          Returns a name of the currently selected attribute. Q: When queried, it returns a string.
    
      - beforeStrokeCmd : bsc          (unicode)       [create,query,edit]
          The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q:
          When queried, it returns the current command
    
      - brushalignment : bra           (bool)          [create,query,edit]
          Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector.
          C: Default is true. Q: When queried, it returns a boolean.
    
      - brushfeedback : brf            (bool)          [create,query,edit]
          Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
    
      - clamp : cl                     (unicode)       [create,query,edit]
          Specifies if the weight value should be clamped to the lower and upper bounds. There are four options here: "none" - no
          clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both" -
          clamps to the lower and upper bounds. C: Default is "none". Q: When queried, it returns a string.
    
      - clamplower : cll               (float)         [create,query,edit]
          Specifies the lower bound for the values. C: Default is 0.0. Q: When queried, it returns a float.
    
      - clampupper : clu               (float)         [create,query,edit]
          Specifies the upper bound for the values. C: Default is 1.0. Q: When queried, it returns a float.
    
      - clear : clr                    (bool)          [create,edit]
          Floods all cvs/vertices to the current value.
    
      - colorAlphaValue : cl1          (float)         []
    
      - colorRGBAValue : cl4           (float, float, float, float) []
    
      - colorRGBValue : cl3            (float, float, float) []
    
      - colorRamp : cr                 (unicode)       [create,query,edit]
          Allows a user defined color ramp to be used to map values to colors.
    
      - colorfeedback : cf             (bool)          [create,query,edit]
          Sets on/off the color feedback display. C: Default is FALSE. Q: When queried, it returns a boolean.
    
      - colorfeedbackOverride : cfo    (bool)          []
    
      - colorrangelower : crl          (float)         [create,query,edit]
          Specifies the value which maps to black when color feedback mode is on C: Default is 0.0. Q: When queried, it returns a
          float.
    
      - colorrangeupper : cru          (float)         [create,query,edit]
          Specifies the value which maps to the maximum color when color feedback mode is on C: Default is 1.0. Q: When queried,
          it returns a float.
    
      - dataTypeIndex : dti            (int)           [query,edit]
          When the selected paintable attribute is a vectorArray, it specifies which field to paint on.
    
      - disablelighting : dl           (bool)          [create,query,edit]
          If color feedback is on, this flag determines whether lighting is disabled or not for the surfaces that are affected C:
          Default is FALSE. Q: When queried, it returns a boolean.
    
      - dragSlider : dsl               (unicode)       [create,edit]
          Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The
          string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C:
          Default is "none".
    
      - duringStrokeCmd : dsk          (unicode)       [create,query,edit]
          The passed string is executed as a MEL command during the stroke, each time the mouse is dragged. C: Default is no
          command. Q: When queried, it returns the current command
    
      - dynclonemode : dcm             (bool)          []
    
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - expandfilename : eef           (bool)          [create,edit]
          If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the
          name as it is. C: Default is true.
    
      - exportaspectratio : ear        (float)         []
    
      - exportfilemode : efm           (unicode)       [create,query,edit]
          Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is
          "luminance/rgb". Q: When queried, it returns a string.
    
      - exportfilesave : esf           (unicode)       [edit]
          Exports the attribute map and saves to a specified file.
    
      - exportfilesizex : fsx          (int)           [create,query,edit]
          Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
    
      - exportfilesizey : fsy          (int)           [create,query,edit]
          Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
    
      - exportfiletype : eft           (unicode)       [create,query,edit]
          Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit"
          "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
    
      - filterNodes : fon              (bool)          [edit]
          Sets the node filter.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - importfileload : ifl           (unicode)       [edit]
          Load the attribute map a specified file.
    
      - importfilemode : ifm           (unicode)       [create,query,edit]
          Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C:
          Default is "alpha". Q: When queried, it returns a string.
    
      - importreassign : irm           (bool)          [create,query,edit]
          Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within
          Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a boolean.
    
      - influence : inf                (unicode)       [query,edit]
          Specifies which joint has been selected by the user for painting. Q: When queried, it returns a string.
    
      - interactiveUpdate : iu         (bool)          [create,query,edit]
          Specifies how often to transfer the painted values into the attribute. TRUE: transfer them "continuously" (many times
          per stroke) FALSE: transfer them only at the end of a stroke (on mouse button release) C: Default is TRUE. Q: When
          queried, it returns a boolean.
    
      - lastRecorderCmd : lrc          (unicode)       []
    
      - lastStampName : lsn            (unicode)       []
    
      - lowerradius : lr               (float)         [create,query,edit]
          Sets the lower size of the brush (only apply on tablet).
    
      - makeStroke : mst               (int)           []
    
      - mappressure : mp               (unicode)       [create,query,edit]
          Sets the tablet pressure mapping when the table is used. There are four options: "none" - the pressure has no effect,
          "opacity" - the pressure is mapped to the opacity, "radius" - the is mapped to modify the radius of the brush, "both" -
          the pressure modifies both the opacity and the radius. C: Default is "none". Q: When queried, it returns a string.
    
      - maxvalue : mxv                 (float)         [create,query,edit]
          Specifies the maximum value for each attribute. C: Default is 1.0. Q: When queried, it returns a float.
    
      - minvalue : miv                 (float)         [create,query,edit]
          Specifies the minimum value for each attribute. C: Default is 0.0. Q: When queried, it returns a float.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.
    
      - objattrArray : oaa             (unicode)       [query]
          An array of all paintable attributes. Each element of the array is a string with the following information:
          NodeType.NodeName.AttributeName.MenuType \*MenuType: type(level) of the item in the Menu (UI). Q: When queried, it
          returns a string.
    
      - opacity : op                   (float)         [create,query,edit]
          Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
    
      - outline : o                    (bool)          [create,query,edit]
          Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
    
      - outwhilepaint : owp            (bool)          [create,query,edit]
          Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a
          boolean.
    
      - paintNodeArray : pna           (unicode)       [query]
          An array of paintable nodes. Q: When queried, it returns a string.
    
      - paintSelectMode : psm          (int)           [query,edit]
          Specifies whether the paint select tool: adds to selection (1) removes from selection (2), toggles selection (3) Q: When
          queried, it returns an int as defined above.Flag can appear in Create mode of commandFlag can have multiple arguments,
          passed either as a tuple or a list.
    
      - paintattrselected : pas        (unicode)       [edit]
          An array of selected paintable attributes. Each element of the array is a string with the following information:
          NodeType.NodeName.AttributeName.
    
      - paintmode : pm                 (unicode)       [create,query,edit]
          Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried,
          it returns a string.
    
      - paintoperationtype : pot       (unicode)       []
    
      - pickColor : pcm                (bool)          []
    
      - pickValue : pv                 (bool)          []
    
      - playbackCursor : plc           (float, float)  []
    
      - playbackPressure : plp         (float)         []
    
      - preserveclonesource : pcs      (bool)          []
    
      - profileShapeFile : psf         (unicode)       [query,edit]
          Passes a name of the image file for the stamp shape profile.
    
      - projective : prm               (bool)          [create,query,edit]
          Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
    
      - radius : r                     (float)         [create,query,edit]
          Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
    
      - rampMaxColor : rxc             (float, float, float) [create,query,edit]
          Defines a special color to be used when the value is greater than or equal to the maximum value.
    
      - rampMinColor : rmc             (float, float, float) [create,query,edit]
          Defines a special color to be used when the value is less than or equal to the minimum value.
    
      - record : rec                   (bool)          []
    
      - reflection : rn                (bool)          [create,query,edit]
          Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
    
      - reflectionaboutorigin : rno    (bool)          []
    
      - reflectionaxis : ra            (unicode)       [create,query,edit]
          Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it
          returns a string.
    
      - screenRadius : scR             (float)         []
    
      - selectclonesource : scs        (bool)          []
    
      - selectedattroper : sao         (unicode)       [create,query,edit]
          Sets the edit weight operation. Four edit weights operations are provided : "absolute" - the value of the weight is
          replaced by the current one, "additive" - the value of the weight is added to the current one, "scale" - the value of
          the weight is multiplied by the current one, "smooth" - the value of the weight is divided by the current one. C:
          Default is "absolute". Q: When queried, it returns a string.
    
      - showactive : sa                (bool)          [create,query,edit]
          Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
    
      - skinPaintMode : spm            (int)           [query,edit]
          Specifies whether the skin paint tool is in paint skin weights mode (1) Marquee select mode (0), or paint select mode
          (2) Q: When queried, it returns an int as defined above.
    
      - stampDepth : stD               (float)         []
    
      - stampProfile : stP             (unicode)       [create,query,edit]
          Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "soft",
          "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
    
      - stampSpacing : stS             (float)         []
    
      - strokesmooth : ssm             (unicode)       []
    
      - surfaceConformedBrushVertices : scv (bool)          [create,query,edit]
          Enables/disables the the display of the effective brush area as affected vertices.
    
      - tablet : tab                   (bool)          [query]
          Returns true if the tablet device is present, false if it is absent
    
      - tangentOutline : to            (bool)          [create,query,edit]
          Enables/disables the display of the brush circle tangent to the surface.
    
      - toolOffProc : tfp              (unicode)       [create,query,edit]
          Accepts a strings describing the name of a MEL procedure which is invoked whenever the tool is turned off. For example,
          cloth invokes "clothPaintToolOff" when the cloth paint tool is turned on. Define this callback if your tool requires
          special functionality when your tool is deactivated. It is typical that if you implement a toolOffProc you will want to
          implement a toolOnProc as well (see the -toolOnProc flag. In query mode, the name of the currently registered MEL
          command is returned and this will be an empty string if none is defined.
    
      - toolOnProc : top               (unicode)       [create,query,edit]
          Accepts a strings describing the name of a MEL procedure which is invoked whenever the tool is turned on. For example,
          cloth invokes "clothPaintToolOn" when the cloth paint tool is turned on. Define this callback if your tool requires
          special functionality when your tool is activated. It is typical that if you implement a toolOnProc you will want to
          implement a toolOffProc as well (see the -toolOffProc flag. In query mode, the name of the currently registered MEL
          command is returned and this will be an empty string if none is defined.
    
      - useColorRamp : ucr             (bool)          [create,query,edit]
          Specifies whether the user defined color ramp should be used to map values from to colors. If this is turned off, the
          default greyscale feedback will be used.
    
      - useMaxMinColor : umc           (bool)          [create,query,edit]
          Specifies whether the out of range colors should be used. See rampMinColor and rampMaxColor flags for further details.
    
      - usepressure : up               (bool)          [create,query,edit]
          Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
    
      - value : val                    (float)         [create,query,edit]
          Specifies the value for each attribute. C: Default is 0.0. Q: When queried, it returns a float.
    
      - whichTool : wst                (unicode)       [create,query,edit]
          The string defines the name of the tool to be used for the Artisan context. An example is "artClothPaint". In query
          mode, the tool name for the given context is returned. Note: due to the way MEL works, always specify the -query flag
          last when specifying a flag which takes arguments.
    
      - worldRadius : wlR              (float)         []
    
      - xrayJoints : xry               (bool)          [query,edit]
          Specifies whether joints should be displayed in xray mode while painting Q: When queried, it returns a boolean.
    
    
    Derived from mel command `maya.cmds.artAttrSkinPaintCtx`
    """

    pass


def draggerContext(*args, **kwargs):
    """
    The draggerContext allows the user to program the behavior of the mouse or an equivalent dragging device in MEL.
    
    Flags:
      - anchorPoint : ap               (float, float, float) [query]
          Anchor point (double array) where dragger was initially pressed.
    
      - button : bu                    (int)           [query]
          Returns the current mouse button (1,2,3).
    
      - currentStep : cs               (int)           [query]
          Current step (press-drag-release sequence) for dragger context. When queried before first press event happened, returns
          0.Flag can appear in Create mode of commandFlag can have multiple arguments, passed either as a tuple or a list.
    
      - cursor : cur                   (unicode)       [create,query,edit]
          Cursor displayed while context is active. Valid values are: "default", "hand", "crossHair", "dolly", "track", and
          "tumble".
    
      - dragCommand : dc               (script)        [create,query,edit]
          Command called when mouse dragger is dragged.
    
      - dragPoint : dp                 (float, float, float) [query]
          Drag point (double array) current position of dragger during drag.
    
      - drawString : ds                (unicode)       [create,edit]
          A string to be drawn at the current position of the pointer.
    
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - finalize : fnz                 (script)        [create,query,edit]
          Command called when the tool is exited.
    
      - helpString : hs                (unicode)       []
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - holdCommand : hc               (script)        [create,query,edit]
          Command called when mouse dragger is held.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - initialize : inz               (script)        [create,query,edit]
          Command called when the tool is entered.
    
      - modifier : mo                  (unicode)       [query]
          Returns the current modifier type: ctrl, alt or none.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.
    
      - plane : pl                     (float, float, float) [create,edit]
          Provide normal of projection plane (see -projection flag for details).
    
      - prePressCommand : ppc          (script)        [create,query,edit]
          Command called when mouse dragger is pressed. It is called before pressCommand, so it can be used for initialization of
          context.
    
      - pressCommand : pc              (script)        [create,query,edit]
          Command called when mouse dragger is pressed.
    
      - projection : pr                (unicode)       [create,query,edit]
          Sets current projection of drag point. Valid types are: viewPlaneproject to view planeobjectViewPlaneproject to object
          plane (parallel to view plane)objectPlaneproject to specified plane defined by object location and normal (default)
          0,1,0planeproject to specified plane defined by origin and normal (default) 0,1,0sketchPlaneproject to sketch
          planexAxisproject to closest point on X axisyAxisproject to closest point on Y axiszAxisproject to closest point on Z
          axisboundingSphereproject to closest point on object sphere boundsboundingBoxproject to closest point on object bounding
          box
    
      - releaseCommand : rc            (script)        [create,query,edit]
          Command called when mouse dragger is released.
    
      - snapping : snp                 (bool)          [create,query,edit]
          Enable/disable snapping for dragger context.
    
      - space : sp                     (unicode)       [create,query,edit]
          Sets current space that coordinates are reported in. Types are: worldworld space (global)objectobject space
          (local)screenscreen space
    
      - stepsCount : sc                (int)           [create,query,edit]
          Number of steps (press-drag-release sequences) for dragger context. When combined with undoMode flag, several steps
          might be recorded as single undo action.
    
      - undoMode : um                  (unicode)       [create,query,edit]
          Undo queue mode for the context actions. Acceptable values are: "all" default behaviour when every action that happens
          during dragger context activity is recorded as an individual undo chunk."step" - all the actions that happen between
          each press and release are combined into one undo chunk."sequence" - all the actions that happen between very first
          press and very last release are combined into single undo chunk. This works exactly the same as "step" for a single step
          dragger context.
    
    
    Derived from mel command `maya.cmds.draggerContext`
    """

    pass


def createNurbsSquareCtx(*args, **kwargs):
    """
    Flags:
      - attachToSpans : asp            (bool)          []
    
      - axis : ax                      (float, float, float) []
    
      - axisType : axt                 (int)           []
    
      - doDragEdit : dde               (bool)          []
    
      - exists : ex                    (bool)          []
    
      - height : h                     (float)         []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
      - spans : sp                     (int)           []
    
      - surfaceDegree : sd             (int)           []
    
      - width : w                      (float)         []
    
    
    Derived from mel command `maya.cmds.createNurbsSquareCtx`
    """

    pass


def polySplitCtx(*args, **kwargs):
    """
    Create a new context to split facets on polygonal objects In query mode, return type is based on queried flag.
    
    Flags:
      - enablesnap : es                (bool)          [create,query,edit]
          Enable/disable custom magnet snapping to start/middle/end of edge
    
      - exists : ex                    (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - magnetsnap : ms                (int)           [create,query,edit]
          number of extra magnets to snap onto, regularly spaced along the edge
    
      - precsnap : ps                  (float)         [create,query,edit]
          precision for custom magnet snapping. Range[0,100]. Value 100 means any click on an edge will snap to either extremities
          or magnets.
    
      - smoothingangle : sma           (float)         [create,query,edit]
          the threshold that controls whether newly created edges are hard or softFlag can appear in Create mode of commandFlag
          can have multiple arguments, passed either as a tuple or a list.
    
      - snaptoedge : ste               (bool)          [create,query,edit]
          Enable/disable snapping to edge. If enabled any click in the current face will snap to the closest valid edge. If there
          is no valid edge, the click will be ignored. NOTE: This is different from magnet snapping, which causes the click to
          snap to certain points along the edge.
    
      - subdivision : s                (int)           [create,query,edit]
          number of sub-edges to add between 2 consecutive edge points. Default is 1.
    
    
    Derived from mel command `maya.cmds.polySplitCtx`
    """

    pass


def texScaleContext(*args, **kwargs):
    """
    This command can be used to create, edit, or query a scale context for the UV Texture Editor. Note that the above flag
    controls the global behaviour of all texture editor scale contexts. Changing one context independently is not allowed.
    Changing a context's behaviour using the above flag, will change all existing texture editor scale contexts.
    
    Flags:
      - exists : ex                    (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - position : p                   (bool)          [query]
          Returns the current position of the manipulatorFlag can appear in Create mode of commandFlag can have multiple
          arguments, passed either as a tuple or a list.
    
      - snap : s                       (bool)          []
    
      - snapRelative : sr              (bool)          []
    
      - snapValue : sv                 (float)         []
    
    
    Derived from mel command `maya.cmds.texScaleContext`
    """

    pass


def createPolyHelixCtx(*args, **kwargs):
    """
    Flags:
      - attachToNumberCoils : anc      (bool)          []
    
      - attachToRadius : atr           (bool)          []
    
      - attachToSubdivisionsAxis : asa (bool)          []
    
      - attachToSubdivisionsCap : asc  (bool)          []
    
      - attachToSubdivisionsCoil : aso (bool)          []
    
      - axis : ax                      (int)           []
    
      - coils : c                      (float)         []
    
      - createUVs : cuv                (int)           []
    
      - direction : dir                (bool)          []
    
      - doDragEdit : dde               (bool)          []
    
      - doSubdivisionsCapsEdit : dsc   (bool)          []
    
      - exists : ex                    (bool)          []
    
      - height : h                     (float)         []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
      - radius : r                     (float)         []
    
      - roundCap : rc                  (bool)          []
    
      - subdivisionsAxis : sa          (int)           []
    
      - subdivisionsCap : sc           (int)           []
    
      - subdivisionsCoil : sl          (int)           []
    
      - width : w                      (float)         []
    
    
    Derived from mel command `maya.cmds.createPolyHelixCtx`
    """

    pass


def tumbleCtx(*args, **kwargs):
    """
    This command can be used to create, edit, or query a tumble context.
    
    Flags:
      - alternateContext : ac          (bool)          [create,query,edit]
          Set the ALT+LMB and ALT+SFT+LMB to refer to this context.
    
      - autoOrthoConstrain : aoc       (bool)          [create,query,edit]
          Automatically constrain horizontal and vertical rotations when the camera is orthographic. The shift key can be used to
          unconstrain the rotation.
    
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - localTumble : lt               (int)           [create,query,edit]
          Describes what point the camera will tumble around: 0 for the camera's tumble pivot1 for the camera's center of
          interest2 for the camera's local axis, offset by its tumble pivot
    
      - name : n                       (unicode)       []
    
      - objectTumble : ot              (bool)          []
    
      - orthoLock : ol                 (bool)          [create,query,edit]
          Orthographic cameras cannot be tumbled while orthoLock is on.Flag can appear in Create mode of commandFlag can have
          multiple arguments, passed either as a tuple or a list.
    
      - orthoStep : os                 (float)         [create,query,edit]
          Specify the angular step in degrees for orthographic rotation. If camera is orthographic and autoOrthoConstrain is
          toggled on the rotation will be stepped by this amount.
    
      - toolName : tn                  (unicode)       []
    
      - tumbleScale : ts               (float)         [create,query,edit]
          Set the rotation speed. A tumble scale of 1.0 will result in in 40 degrees of rotation per 100 pixels of cursor drag.
    
    
    Derived from mel command `maya.cmds.tumbleCtx`
    """

    pass


def softSelectOptionsCtx(*args, **kwargs):
    """
    Flags:
      - buttonDown : btd               (bool)          []
    
      - buttonUp : btu                 (bool)          []
    
      - colorCurve : cc                (unicode)       []
    
      - condition : cdn                (bool)          []
    
      - enableFalseColor : efc         (int)           []
    
      - enabled : en                   (bool)          []
    
      - exists : ex                    (bool)          []
    
      - falloffCurve : fc              (unicode)       []
    
      - falloffMode : fm               (int)           []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - size : sz                      (float)         []
    
      - uvSize : uvs                   (float)         []
    
    
    Derived from mel command `maya.cmds.softSelectOptionsCtx`
    """

    pass


def latticeDeformKeyCtx(*args, **kwargs):
    """
    This command creates a context which may be used to deform key frames with lattice manipulator. This context only works
    in the graph editor.
    
    Flags:
      - envelope : ev                  (float)         [query,edit]
          Specifies the influence of the lattice.
    
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - latticeColumns : lc            (int)           [query,edit]
          Specifies the number column points the lattice contains.
    
      - latticeRows : lr               (int)           [query,edit]
          Specifies the number of rows the lattice contains.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.
    
      - scaleLatticePts : slp          (bool)          [query,edit]
          Specifies if the selected lattice points should scale around the pick point. If this value is false the the default
          operation is 'move'Flag can appear in Create mode of commandFlag can have multiple arguments, passed either as a tuple
          or a list.
    
    
    Derived from mel command `maya.cmds.latticeDeformKeyCtx`
    """

    pass


def setKeyCtx(*args, **kwargs):
    """
    This command creates a context which may be used to set keys within the graph editor
    
    Flags:
      - breakdown : bd                 (bool)          [query,edit]
          Specifies whether or not to create breakdown keysFlag can appear in Create mode of commandFlag can have multiple
          arguments, passed either as a tuple or a list.
    
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.
    
    
    Derived from mel command `maya.cmds.setKeyCtx`
    """

    pass


def texWinToolCtx(*args, **kwargs):
    """
    This class creates a context for the View Tools "track", "dolly", and "box zoom" in the texture window.
    
    Flags:
      - alternateContext : ac          (bool)          []
    
      - boxzoom : bz                   (bool)          [create,query,edit]
          Perform Box ZoomFlag can appear in Create mode of commandFlag can have multiple arguments, passed either as a tuple or a
          list.
    
      - dolly : do                     (bool)          [create,query,edit]
          Dollies the view
    
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
      - toolName : tn                  (unicode)       []
    
      - track : tr                     (bool)          [create,query,edit]
          Tracks the view
    
    
    Derived from mel command `maya.cmds.texWinToolCtx`
    """

    pass


def dynPaintCtx(*args, **kwargs):
    """
    Flags:
      - brushDrag : bd                 (float)         []
    
      - brushMass : bm                 (float)         []
    
      - displayQuality : dq            (float)         []
    
      - doProject : dp                 (int)           []
    
      - dragBrushSize : dbs            (unicode)       []
    
      - drawAsMesh : dam               (bool)          []
    
      - exists : ex                    (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - inputSamples : inputSamples    (int)           []
    
      - paintAtDepth : pd              (bool)          []
    
      - pixelMode : pxm                (int)           []
    
      - pressureMapping1 : pm1         (int)           []
    
      - pressureMapping2 : pm2         (int)           []
    
      - pressureMapping3 : pm3         (int)           []
    
      - pressureMax1 : px1             (float)         []
    
      - pressureMax2 : px2             (float)         []
    
      - pressureMax3 : px3             (float)         []
    
      - pressureMin1 : ps1             (float)         []
    
      - pressureMin2 : ps2             (float)         []
    
      - pressureMin3 : ps3             (float)         []
    
      - sampleSeparation : sp          (float)         []
    
      - setSelection : ss              (bool)          []
    
      - surfaceOffset : sof            (float)         []
    
      - usePressure : usp              (bool)          []
    
    
    Derived from mel command `maya.cmds.dynPaintCtx`
    """

    pass


def rollCtx(*args, **kwargs):
    """
    Create, edit, or query a roll context.
    
    Flags:
      - alternateContext : ac          (bool)          []
    
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
      - rollScale : rs                 (float)         [create,query,edit]
          In degrees of rotation per 100 pixels of cursor drag.Flag can appear in Create mode of commandFlag can have multiple
          arguments, passed either as a tuple or a list.
    
      - toolName : tn                  (unicode)       []
    
    
    Derived from mel command `maya.cmds.rollCtx`
    """

    pass


def polyCreateFacetCtx(*args, **kwargs):
    """
    Create a new context to create polygonal objects In query mode, return type is based on queried flag.
    
    Flags:
      - append : ap                    (bool)          [create,query,edit]
          Allows to switch to polyAppendFacetCtx tool
    
      - exists : ex                    (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - maximumNumberOfPoints : mp     (int)           [create,query,edit]
          Allows the ability to set a upper bound on the number of points in interactively place before polygon is created. A
          value less than 2 will mean that there is no upper bound.Flag can appear in Create mode of commandFlag can have multiple
          arguments, passed either as a tuple or a list.
    
      - planarConstraint : pc          (bool)          [create,query,edit]
          allows/avoid new facet to be non-planar.If on, all new points will be projected onto current facet plane.
    
      - subdivision : s                (int)           [create,query,edit]
          number of sub-edges created for each new edge. Default is 1.
    
      - texture : tx                   (int)           []
    
    
    Derived from mel command `maya.cmds.polyCreateFacetCtx`
    """

    pass


def boxZoomCtx(*args, **kwargs):
    """
    This command can be used to create, edit, or query a box zoom context. If this context is used on a perspective camera,
    the field of view and view direction are changed. If the camera is orthographic, the orthographic width and eye point
    are changed. The left and middle mouse interactively zoom the view. The control key can be used to enable box zoom. A
    box starting from left to right will zoom in, and a box starting from right to left will zoom out.
    
    Flags:
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
      - zoomScale : zs                 (float)         [create,query,edit]
          Scale the zoom.Flag can appear in Create mode of commandFlag can have multiple arguments, passed either as a tuple or a
          list.
    
    
    Derived from mel command `maya.cmds.boxZoomCtx`
    """

    pass


def dragAttrContext(*args, **kwargs):
    """
    The dragAttrContext allows a user to manipulate the attributes of an object by using a virtual slider within the
    viewport. The virtual slider is used by dragging in a viewport with the middle mouse button. The speed at which the
    attributes are changed can be controlled by holding down the Ctrl key to slow it down and the Shift key to speed it up.
    
    Flags:
      - connectTo : ct                 (PyNode)        [create,query,edit]
          Specifies an attribute to which to connect the context. This is a multi-use flag, but all attributes used must be from
          one object.
    
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.
    
      - reset : r                      (bool)          [create,edit]
          Resets the list of attributes to which the context is connected.Flag can appear in Create mode of commandFlag can have
          multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.dragAttrContext`
    """

    pass


def snapshotModifyKeyCtx(*args, **kwargs):
    """
    Creates a context for inserting/delete keys on an editable motion trail
    
    Flags:
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
    
    Derived from mel command `maya.cmds.snapshotModifyKeyCtx`
    """

    pass


def texSelectContext(*args, **kwargs):
    """
    Command used to register the texSelectCtx tool.
    
    Flags:
      - exists : ex                    (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
    
    Derived from mel command `maya.cmds.texSelectContext`
    """

    pass


def dynParticleCtx(*args, **kwargs):
    """
    The particle context command creates a particle context. The particle context provides an interactive means to create
    particle objects. The particle context command also provides an interactive means to set the option values, through the
    Tool Property Sheet, for the "particle" command that the context will issue. In query mode, return type is based on
    queried flag.
    
    Flags:
      - conserve : c                   (float)         [query,edit]
          Conservation of momentum control (between 0 and 1). For smaller values, the field will tend to erase any existing
          velocity the object has (in other words, will not conserve momentum from frame to frame). A value of 1 (the default)
          corresponds to the true physical law of conservation of momentum.
    
      - cursorPlacement : cp           (bool)          [query,edit]
          Use the cursor to place the lower left and upper right of the grid.
    
      - exists : ex                    (bool)          []
    
      - grid : gr                      (bool)          [query,edit]
          Create a particle grid.
    
      - gridSpacing : grs              (float)         [query,edit]
          Spacing between particles in the grid.
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - jitterRadius : jr              (float)         [query,edit]
          Max radius from the center to place the particle instances.
    
      - lowerLeftX : llx               (float)         [query,edit]
          Lower left X position of the particle grid.
    
      - lowerLeftY : lly               (float)         [query,edit]
          Lower left Y position of the particle grid.
    
      - lowerLeftZ : llz               (float)         [query,edit]
          Lower left Z position of the particle grid.
    
      - name : n                       (unicode)       []
    
      - nucleus : nc                   (bool)          [query,edit]
          If set true then an nParticle is generated with a nucleus node connection. Otherwise a standard particle is created.
    
      - numJitters : nj                (int)           [query,edit]
          Number of jitters (instances) per particle.
    
      - particleName : pn              (unicode)       [query,edit]
          Particle name.
    
      - sketch : sk                    (bool)          [query,edit]
          Create particles in sketch mode.
    
      - sketchInterval : ski           (int)           [query,edit]
          Interval between particles, when in sketch mode.
    
      - textPlacement : tp             (bool)          [query,edit]
          Use the textfields to specify the lower left and upper right of/ the grid.
    
      - upperRightX : urx              (float)         [query,edit]
          Upper right X position of the particle grid.
    
      - upperRightY : ury              (float)         [query,edit]
          Upper right Y position of the particle grid.
    
      - upperZ : urz                   (float)         [query,edit]
          Upper right Z position of the particle grid.Flag can appear in Create mode of commandFlag can have multiple arguments,
          passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.dynParticleCtx`
    """

    pass


def selectKeyframeRegionCtx(*args, **kwargs):
    """
    This command creates a context which may be used to select keyframes within the keyframe region of the dope sheet editor
    
    Flags:
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.Flag can appear in Create mode of commandFlag can have multiple
          arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.selectKeyframeRegionCtx`
    """

    pass


def createPolyPrismCtx(*args, **kwargs):
    """
    Flags:
      - attachToNumSides : ans         (bool)          []
    
      - attachToSubdivisionsCap : asc  (bool)          []
    
      - attachToSubdivisionsHeight : ash (bool)          []
    
      - axis : ax                      (int)           []
    
      - createUVs : cuv                (int)           []
    
      - doDragEdit : dde               (bool)          []
    
      - doSubdivisionsCapsEdit : dsc   (bool)          []
    
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - length : ln                    (float)         []
    
      - name : n                       (unicode)       []
    
      - numberOfSides : ns             (int)           []
    
      - sideLength : sl                (float)         []
    
      - subdivisionsCap : sc           (int)           []
    
      - subdivisionsHeight : sh        (int)           []
    
    
    Derived from mel command `maya.cmds.createPolyPrismCtx`
    """

    pass


def selectContext(*args, **kwargs):
    """
    Creates a context to perform selection.
    
    Flags:
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.Flag can appear in Create mode of commandFlag can have multiple
          arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.selectContext`
    """

    pass


def scaleKeyCtx(*args, **kwargs):
    """
    This command creates a context which may be used to scale keyframes within the graph editor
    
    Flags:
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.
    
      - scaleSpecifiedKeys : ssk       (bool)          [query,edit]
          Determines if only the specified keys should be scaled. If false, the non-selected keys will be adjusted during the
          scale. The default is true.Flag can appear in Create mode of commandFlag can have multiple arguments, passed either as a
          tuple or a list.
    
      - type : typ                     (unicode)       [query,edit]
          rect | manip Specifies the type of scale manipulator to use (Note: "rect" is a manipulator style context, and "manip" is
          a gestural style context)
    
    
    Derived from mel command `maya.cmds.scaleKeyCtx`
    """

    pass


def orbitCtx(*args, **kwargs):
    """
    Create, edit, or query an orbit context.
    
    Flags:
      - alternateContext : ac          (bool)          []
    
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - localOrbit : lo                (bool)          [create,query,edit]
          Orbit around the camera's center of interest.Flag can appear in Create mode of commandFlag can have multiple arguments,
          passed either as a tuple or a list.
    
      - name : n                       (unicode)       []
    
      - orbitScale : os                (float)         [create,query,edit]
          In degrees of rotation per 100 pixels of cursor drag.
    
      - toolName : tn                  (unicode)       []
    
    
    Derived from mel command `maya.cmds.orbitCtx`
    """

    pass


def modelCurrentTimeCtx(*args, **kwargs):
    """
    This command creates a context which may be used to change current time within the model views.
    
    Flags:
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.
    
      - percent : per                  (float)         [query,edit]
          Percent of the screen space that represents the full time slider range (default is 50%)Flag can appear in Create mode of
          commandFlag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.modelCurrentTimeCtx`
    """

    pass


def curveAddPtCtx(*args, **kwargs):
    """
    The curveAddPtCtx command creates a new curve add points context, which adds either control vertices (CVs) or edit
    points to an existing curve.
    
    Flags:
      - exists : ex                    (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
    
    Derived from mel command `maya.cmds.curveAddPtCtx`
    """

    pass


def artFluidAttrCtx(*args, **kwargs):
    """
    This command is used to paint properties (such as density) of selected fluid volumes. In query mode, return type is
    based on queried flag.
    
    Flags:
      - accopacity : aco               (bool)          [create,query,edit]
          Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When
          queried, it returns a boolean.
    
      - activeListChangedProc : alp    (unicode)       []
    
      - afterStrokeCmd : asc           (unicode)       []
    
      - alphaclamp : alc               (unicode)       []
    
      - alphaclamplower : acl          (float)         []
    
      - alphaclampupper : acu          (float)         []
    
      - attrSelected : asl             (unicode)       []
    
      - autoSave : autoSave            (unicode)       [create,query,edit]
          A MEL command to save the fluid state. Called before an event which could overwrite unsaved values of painted fluid
          properties. Such events include: changing current time, changing the current paintable property, and exiting the paint
          tool. (To turn auto-save off, pass in an empty-valued string argument: e.g., "".)
    
      - beforeStrokeCmd : bsc          (unicode)       []
    
      - brushalignment : bra           (bool)          [create,query,edit]
          Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector.
          C: Default is true. Q: When queried, it returns a boolean.
    
      - brushfeedback : brf            (bool)          [create,query,edit]
          Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
    
      - clamp : cl                     (unicode)       []
    
      - clamplower : cll               (float)         []
    
      - clampupper : clu               (float)         []
    
      - clear : clr                    (bool)          [create,edit]
          Floods all cvs/vertices to the current value.
    
      - colorAlphaValue : cl1          (float)         []
    
      - colorRGBAValue : cl4           (float, float, float, float) []
    
      - colorRGBValue : cl3            (float, float, float) []
    
      - colorRamp : cr                 (unicode)       []
    
      - colorfeedback : cf             (bool)          []
    
      - colorfeedbackOverride : cfo    (bool)          []
    
      - colorrangelower : crl          (float)         []
    
      - colorrangeupper : cru          (float)         []
    
      - currentPaintableFluid : cpf    (unicode)       [query]
          Query the name of the fluid on which this context is currently painting. Returns string.Flag can appear in Create mode
          of commandFlag can have multiple arguments, passed either as a tuple or a list.
    
      - dataTypeIndex : dti            (int)           []
    
      - delaySelectionChanged : dsc    (bool)          [create,query,edit]
          Internal use only. Under normal conditions, the tool responds to changes to the selection list so it can update its list
          of paintable geometry. When -dsl true is used, the tool will not update its paintable list until a corresponding -dsl
          false is called.
    
      - disablelighting : dl           (bool)          []
    
      - displayAsRender : dar          (bool)          [create,query,edit]
          When true, sets the "Shaded Display" attribute of the fluid to "AsRender": all fluid properties displayed as hardware
          rendered. When false, displays only the currently selected paintable attribute of the fluid.
    
      - displayVelocity : dv           (bool)          [create,query,edit]
          Turns on/off velocity display, independently of the above "dar/displayAsRender" setting. Use this flag to enable
          velocity display while only displaying density, for example.
    
      - doAutoSave : das               (bool)          [edit]
          Execute the -autoSave command if there are unsaved painted fluid properties.
    
      - dragSlider : dsl               (unicode)       [create,edit]
          Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The
          string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C:
          Default is "none".
    
      - duringStrokeCmd : dsk          (unicode)       []
    
      - dynclonemode : dcm             (bool)          []
    
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - expandfilename : eef           (bool)          [create,edit]
          If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the
          name as it is. C: Default is true.
    
      - exportaspectratio : ear        (float)         []
    
      - exportfilemode : efm           (unicode)       [create,query,edit]
          Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is
          "luminance/rgb". Q: When queried, it returns a string.
    
      - exportfilesave : esf           (unicode)       [edit]
          Exports the attribute map and saves to a specified file.
    
      - exportfilesizex : fsx          (int)           [create,query,edit]
          Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
    
      - exportfilesizey : fsy          (int)           [create,query,edit]
          Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
    
      - exportfiletype : eft           (unicode)       [create,query,edit]
          Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit"
          "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
    
      - filterNodes : fon              (bool)          []
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - importfileload : ifl           (unicode)       [edit]
          Load the attribute map a specified file.
    
      - importfilemode : ifm           (unicode)       [create,query,edit]
          Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C:
          Default is "alpha". Q: When queried, it returns a string.
    
      - importreassign : irm           (bool)          [create,query,edit]
          Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within
          Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a boolean.
    
      - interactiveUpdate : iu         (bool)          []
    
      - lastRecorderCmd : lrc          (unicode)       []
    
      - lastStampName : lsn            (unicode)       []
    
      - lowerradius : lr               (float)         [create,query,edit]
          Sets the lower size of the brush (only apply on tablet).
    
      - makeStroke : mst               (int)           []
    
      - mappressure : mp               (unicode)       [create,query,edit]
          Sets the tablet pressure mapping when the table is used. There are four options: "none" - the pressure has no effect,
          "opacity" - the pressure is mapped to the opacity, "radius" - the is mapped to modify the radius of the brush, "both" -
          the pressure modifies both the opacity and the radius. C: Default is "none". Q: When queried, it returns a string.
    
      - maxvalue : mxv                 (float)         []
    
      - minvalue : miv                 (float)         []
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.
    
      - objattrArray : oaa             (unicode)       []
    
      - opacity : op                   (float)         [create,query,edit]
          Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
    
      - outline : o                    (bool)          [create,query,edit]
          Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
    
      - outwhilepaint : owp            (bool)          [create,query,edit]
          Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a
          boolean.
    
      - paintNodeArray : pna           (unicode)       []
    
      - paintattrselected : pas        (unicode)       []
    
      - paintmode : pm                 (unicode)       [create,query,edit]
          Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried,
          it returns a string.
    
      - paintoperationtype : pot       (unicode)       []
    
      - pickColor : pcm                (bool)          []
    
      - pickValue : pv                 (bool)          []
    
      - playbackCursor : plc           (float, float)  []
    
      - playbackPressure : plp         (float)         []
    
      - preserveclonesource : pcs      (bool)          []
    
      - profileShapeFile : psf         (unicode)       [query,edit]
          Passes a name of the image file for the stamp shape profile.
    
      - projective : prm               (bool)          [create,query,edit]
          Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
    
      - property : p                   (unicode)       [create,query,edit]
          Specifies a property to paint on the fluid. Valid values are "color", "density", "densityAndColor," "densityAndFuel,"
          "temperature," "fuel", "velocity".
    
      - radius : r                     (float)         [create,query,edit]
          Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
    
      - rampMaxColor : rxc             (float, float, float) []
    
      - rampMinColor : rmc             (float, float, float) []
    
      - record : rec                   (bool)          []
    
      - reflection : rn                (bool)          [create,query,edit]
          Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
    
      - reflectionaboutorigin : rno    (bool)          []
    
      - reflectionaxis : ra            (unicode)       [create,query,edit]
          Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it
          returns a string.
    
      - rgbValue : rgb                 (float, float, float) [create,query,edit]
          Specifies the values of the red, green, and blue components of the color to use when painting the property "color."
    
      - screenRadius : scR             (float)         []
    
      - selectclonesource : scs        (bool)          []
    
      - selectedattroper : sao         (unicode)       []
    
      - showactive : sa                (bool)          [create,query,edit]
          Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
    
      - stampDepth : stD               (float)         []
    
      - stampProfile : stP             (unicode)       [create,query,edit]
          Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "soft",
          "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
    
      - stampSpacing : stS             (float)         []
    
      - strokesmooth : ssm             (unicode)       []
    
      - surfaceConformedBrushVertices : scv (bool)          [create,query,edit]
          Enables/disables the the display of the effective brush area as affected vertices.
    
      - tablet : tab                   (bool)          [query]
          Returns true if the tablet device is present, false if it is absent
    
      - tangentOutline : to            (bool)          [create,query,edit]
          Enables/disables the display of the brush circle tangent to the surface.
    
      - toolOffProc : tfp              (unicode)       []
    
      - toolOnProc : top               (unicode)       []
    
      - useColorRamp : ucr             (bool)          []
    
      - useMaxMinColor : umc           (bool)          []
    
      - useStrokeDirection : usd       (bool)          [create,query,edit]
          Applicable only during "velocity" painting. Specifies whether the value of the painted velocity should come from the
          direction of the brush stroke, overriding the value specified by the -v/-velocity flag.
    
      - usepressure : up               (bool)          [create,query,edit]
          Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
    
      - value : val                    (float)         []
    
      - velocity : v                   (float, float, float) [create,query,edit]
          Specifies the values of the x, y, and z components of the velocity to use when painting the property "velocity".
    
      - whichTool : wst                (unicode)       []
    
      - worldRadius : wlR              (float)         []
    
    
    Derived from mel command `maya.cmds.artFluidAttrCtx`
    """

    pass


def manipScaleContext(*args, **kwargs):
    """
    This command can be used to create, edit, or query a scale manip context.
    
    Flags:
      - activeHandle : ah              (int)           [query,edit]
          Sets the default active handle for the manip. That is, the handle which should be initially active when the tool is
          activated. Values can be: 0 - X axis handle is active1 - Y axis handle is active2 - Z axis handle is active3 - Center
          handle (all axes) is active (default)
    
      - alignAlong : aa                (float, float, float) [create,edit]
          Aligns active handle along vector.
    
      - editPivotMode : epm            (bool)          [query]
          Returns true manipulator is in edit pivot mode
    
      - editPivotPosition : epp        (bool)          [query]
          Returns the current position of the edit pivot manipulator.
    
      - exists : ex                    (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - mode : m                       (int)           [query,edit]
          Translate mode: 0 - Object Space1 - Local Space2 - World Space (default)3 - Move Along Vertex Normal4 - Move Along
          Rotation Axis5 - Move Along Live Object Axis6 - Custom Axis Orientation
    
      - orientAxes : oa                (float, float, float) [query,edit]
          Orients manipulator rotating around axes by specified angles
    
      - orientTowards : ot             (float, float, float) [create,edit]
          Orients active handle towards world point
    
      - position : p                   (bool)          [query]
          Returns the current position of the manipulator
    
      - postDragCommand : pod          (script, <type 'unicode'>) [create,edit]
          Specifies a command and a node type. The command will be executed at the end of a drag when a node of the specified type
          is in the selection.
    
      - preDragCommand : prd           (script, <type 'unicode'>) [create,edit]
          Specifies a command and a node type. The command will be executed at the start of a drag when a node of the specified
          type is in the selection.
    
      - preserveChildPosition : pcp    (bool)          [query,edit]
          When false, the children objects move when their parent is rotated. When true, the worldspace position of the children
          will be maintained as the parent is moved. Default is false.Flag can appear in Create mode of commandFlag can have
          multiple arguments, passed either as a tuple or a list.
    
      - preserveUV : puv               (bool)          []
    
      - reflection : rfl               (bool)          []
          This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.
    
      - reflectionAbout : rab          (int)           []
          This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.
    
      - reflectionAxis : rfa           (int)           []
          This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.
    
      - reflectionTolerance : rft      (float)         []
          This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.
    
      - snap : s                       (bool)          []
    
      - snapRelative : sr              (bool)          []
    
      - snapValue : sv                 (float)         []
    
      - useManipPivot : ump            (bool)          []
    
      - useObjectPivot : uop           (bool)          []
    
    
    Derived from mel command `maya.cmds.manipScaleContext`
    """

    pass


def snapTogetherCtx(*args, **kwargs):
    """
    The snapTogetherCtx command creates a tool for snapping surfaces together.
    
    Flags:
      - clearSelection : cs            (bool)          [create,query,edit]
          Sets whether the tool should clear the selection on entry to the tool. Default true.
    
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.
    
      - setOrientation : so            (bool)          [create,query,edit]
          Sets whether the tool should orient as well as moving an item. Default true.
    
      - snapPolygonFace : spf          (bool)          [create,query,edit]
          Sets whether the tool should snap the cursor to polygon face centers. Default false.Flag can appear in Create mode of
          commandFlag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.snapTogetherCtx`
    """

    pass


def paramDimContext(*args, **kwargs):
    """
    Command used to register the paramDimCtx tool.
    
    Flags:
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
    
    Derived from mel command `maya.cmds.paramDimContext`
    """

    pass


def keyframeRegionMoveKeyCtx(*args, **kwargs):
    """
    This command creates a context which may be used to move keyframes within the keyframe region of the dope sheet editor
    
    Flags:
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.
    
      - option : o                     (unicode)       [create,query,edit]
          Valid values are "move," "insert," "over," and "segmentOver". Specifies the keyframe -option to use. When you "move" a
          key, the key will not cross over (in time) any keys before or after it. When you "insert" a key, all keys before or
          after (depending upon the -timeChange value) will be moved an equivalent amount. When you "over" a key, the key is
          allowed to move to any time (as long as a key is not there already). When you "segmentOver" a set of keys (this option
          only has a noticeable effect when more than one key is being moved) the first key (in time) and last key define a
          segment (unless you specify a time range). That segment is then allowed to move over other keys, and keys will be moved
          to make room for the segment.Flag can appear in Create mode of commandFlag can have multiple arguments, passed either as
          a tuple or a list.
    
    
    Derived from mel command `maya.cmds.keyframeRegionMoveKeyCtx`
    """

    pass


def artUserPaintCtx(*args, **kwargs):
    """
    This is a context command to set the flags on the artAttrContext, which is the base context for attribute painting
    operations. All commands require the name of the context as the last argument as this provides the name of the context
    to create, edit or query. This command executes a scriptable paint (Maya Artisan). It allows the user to apply mel
    commands/scripts to modify cvs' attributes for all cvs under the paint brush.
    
    Flags:
      - accopacity : aco               (bool)          [create,query,edit]
          Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When
          queried, it returns a boolean.
    
      - activeListChangedProc : alp    (unicode)       [create,query,edit]
          Accpts a string which contains a MEL command that is invoked whenever the active list changes. There may be some
          situations where the UI, for example, needs to be updated, when objects are selected/deselected in the scene. In query
          mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
    
      - afterStrokeCmd : asc           (unicode)       [create,query,edit]
          The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When
          queried, it returns the current command
    
      - alphaclamp : alc               (unicode)       [create,query,edit]
          Specifies if the weight value should be alpha clamped to the lower and upper bounds. There are four options here: "none"
          - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both"
          - clamps to the lower and upper bounds. C: Default is "none". Q: When queried, it returns a string.
    
      - alphaclamplower : acl          (float)         [create,query,edit]
          Specifies the lower bound for the alpha values. C: Default is 0.0. Q: When queried, it returns a float.
    
      - alphaclampupper : acu          (float)         [create,query,edit]
          Specifies the upper bound for the alpha values. C: Default is 1.0. Q: When queried, it returns a float.
    
      - attrSelected : asl             (unicode)       [query]
          Returns a name of the currently selected attribute. Q: When queried, it returns a string.
    
      - beforeStrokeCmd : bsc          (unicode)       [create,query,edit]
          The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q:
          When queried, it returns the current command
    
      - brushalignment : bra           (bool)          [create,query,edit]
          Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector.
          C: Default is true. Q: When queried, it returns a boolean.
    
      - brushfeedback : brf            (bool)          [create,query,edit]
          Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
    
      - chunkCommand : cc              (unicode)       []
    
      - clamp : cl                     (unicode)       [create,query,edit]
          Specifies if the weight value should be clamped to the lower and upper bounds. There are four options here: "none" - no
          clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both" -
          clamps to the lower and upper bounds. C: Default is "none". Q: When queried, it returns a string.
    
      - clamplower : cll               (float)         [create,query,edit]
          Specifies the lower bound for the values. C: Default is 0.0. Q: When queried, it returns a float.
    
      - clampupper : clu               (float)         [create,query,edit]
          Specifies the upper bound for the values. C: Default is 1.0. Q: When queried, it returns a float.
    
      - clear : clr                    (bool)          [create,edit]
          Floods all cvs/vertices to the current value.
    
      - colorAlphaValue : cl1          (float)         []
    
      - colorRGBAValue : cl4           (float, float, float, float) []
    
      - colorRGBValue : cl3            (float, float, float) []
    
      - colorRamp : cr                 (unicode)       [create,query,edit]
          Allows a user defined color ramp to be used to map values to colors.
    
      - colorfeedback : cf             (bool)          [create,query,edit]
          Sets on/off the color feedback display. C: Default is FALSE. Q: When queried, it returns a boolean.
    
      - colorfeedbackOverride : cfo    (bool)          []
    
      - colorrangelower : crl          (float)         [create,query,edit]
          Specifies the value which maps to black when color feedback mode is on C: Default is 0.0. Q: When queried, it returns a
          float.
    
      - colorrangeupper : cru          (float)         [create,query,edit]
          Specifies the value which maps to the maximum color when color feedback mode is on C: Default is 1.0. Q: When queried,
          it returns a float.
    
      - dataTypeIndex : dti            (int)           [query,edit]
          When the selected paintable attribute is a vectorArray, it specifies which field to paint on.
    
      - disablelighting : dl           (bool)          [create,query,edit]
          If color feedback is on, this flag determines whether lighting is disabled or not for the surfaces that are affected C:
          Default is FALSE. Q: When queried, it returns a boolean.
    
      - dragSlider : dsl               (unicode)       [create,edit]
          Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The
          string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C:
          Default is "none".
    
      - duringStrokeCmd : dsk          (unicode)       [create,query,edit]
          The passed string is executed as a MEL command during the stroke, each time the mouse is dragged. C: Default is no
          command. Q: When queried, it returns the current command
    
      - dynclonemode : dcm             (bool)          []
    
      - exists : ex                    (bool)          [create]
          Returns true or false depending upon whether the specified object exists. Other flags are ignored.
    
      - expandfilename : eef           (bool)          [create,edit]
          If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the
          name as it is. C: Default is true.
    
      - exportaspectratio : ear        (float)         []
    
      - exportfilemode : efm           (unicode)       [create,query,edit]
          Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is
          "luminance/rgb". Q: When queried, it returns a string.
    
      - exportfilesave : esf           (unicode)       [edit]
          Exports the attribute map and saves to a specified file.
    
      - exportfilesizex : fsx          (int)           [create,query,edit]
          Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
    
      - exportfilesizey : fsy          (int)           [create,query,edit]
          Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
    
      - exportfiletype : eft           (unicode)       [create,query,edit]
          Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit"
          "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
    
      - filterNodes : fon              (bool)          [edit]
          Sets the node filter.
    
      - finalizeCmd : fc               (unicode)       [create,query,edit]
          Specifies the name of the mel script/procedure which is called at the end of each stroke. Q: When queried, it returns a
          string.
    
      - fullpaths : fp                 (bool)          [create,query,edit]
          Specifies whether full path names should be used when surface names are passed to scripts. If false, just the surface
          name is passed. C: Default is false Q: When queried, it returns a boolean.Flag can appear in Create mode of commandFlag
          can have multiple arguments, passed either as a tuple or a list.
    
      - getArrayAttrCommand : gac      (unicode)       [create,query,edit]
          Specifies the name of the mel script/procedure which is called once for every surface that is selected for painting.
          This procedure returns a string, which is interpreted as a list of names referring to double array attributes on some
          dependency node. Q: When queried, it returns a string.
    
      - getSurfaceCommand : gsc        (unicode)       [create,query,edit]
          Specifies the name of the mel script/procedure which is called once for every dependency node on the selection list,
          whenever Artisan processes the selection list. It returns the name of the surface to paint on. Q: When queried, it
          returns a string.
    
      - getValueCommand : gvc          (unicode)       [create,query,edit]
          Specifies the name of the mel script/procedure which is called every time a value on the surface is needed by the
          scriptable paint tool. Q: When queried, it returns a string.
    
      - history : ch                   (bool)          [create]
          If this is a tool command, turn the construction history on for the tool in question.
    
      - image1 : i1                    (unicode)       [create,query,edit]
    
      - image2 : i2                    (unicode)       [create,query,edit]
    
      - image3 : i3                    (unicode)       [create,query,edit]
          Contexts support up to three icons that represent the tool associated with the context.
    
      - importfileload : ifl           (unicode)       [edit]
          Load the attribute map a specified file.
    
      - importfilemode : ifm           (unicode)       [create,query,edit]
          Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C:
          Default is "alpha". Q: When queried, it returns a string.
    
      - importreassign : irm           (bool)          [create,query,edit]
          Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within
          Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a boolean.
    
      - initializeCmd : ic             (unicode)       [create,query,edit]
          Specifies the name of the mel script/procedure which is called in the beginning of each stroke. Q: When queried, it
          returns a string.
    
      - interactiveUpdate : iu         (bool)          [create,query,edit]
          Specifies how often to transfer the painted values into the attribute. TRUE: transfer them "continuously" (many times
          per stroke) FALSE: transfer them only at the end of a stroke (on mouse button release) C: Default is TRUE. Q: When
          queried, it returns a boolean.
    
      - lastRecorderCmd : lrc          (unicode)       []
    
      - lastStampName : lsn            (unicode)       []
    
      - lowerradius : lr               (float)         [create,query,edit]
          Sets the lower size of the brush (only apply on tablet).
    
      - makeStroke : mst               (int)           []
    
      - mappressure : mp               (unicode)       [create,query,edit]
          Sets the tablet pressure mapping when the table is used. There are four options: "none" - the pressure has no effect,
          "opacity" - the pressure is mapped to the opacity, "radius" - the is mapped to modify the radius of the brush, "both" -
          the pressure modifies both the opacity and the radius. C: Default is "none". Q: When queried, it returns a string.
    
      - maxvalue : mxv                 (float)         [create,query,edit]
          Specifies the maximum value for each attribute. C: Default is 1.0. Q: When queried, it returns a float.
    
      - minvalue : miv                 (float)         [create,query,edit]
          Specifies the minimum value for each attribute. C: Default is 0.0. Q: When queried, it returns a float.
    
      - name : n                       (unicode)       [create]
          If this is a tool command, name the tool appropriately.
    
      - objattrArray : oaa             (unicode)       [query]
          An array of all paintable attributes. Each element of the array is a string with the following information:
          NodeType.NodeName.AttributeName.MenuType \*MenuType: type(level) of the item in the Menu (UI). Q: When queried, it
          returns a string.
    
      - opacity : op                   (float)         [create,query,edit]
          Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
    
      - outline : o                    (bool)          [create,query,edit]
          Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
    
      - outwhilepaint : owp            (bool)          [create,query,edit]
          Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a
          boolean.
    
      - paintNodeArray : pna           (unicode)       [query]
          An array of paintable nodes. Q: When queried, it returns a string.
    
      - paintattrselected : pas        (unicode)       [edit]
          An array of selected paintable attributes. Each element of the array is a string with the following information:
          NodeType.NodeName.AttributeName.
    
      - paintmode : pm                 (unicode)       [create,query,edit]
          Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried,
          it returns a string.
    
      - paintoperationtype : pot       (unicode)       []
    
      - pickColor : pcm                (bool)          []
    
      - pickValue : pv                 (bool)          []
    
      - playbackCursor : plc           (float, float)  []
    
      - playbackPressure : plp         (float)         []
    
      - preserveclonesource : pcs      (bool)          []
    
      - profileShapeFile : psf         (unicode)       [query,edit]
          Passes a name of the image file for the stamp shape profile.
    
      - projective : prm               (bool)          [create,query,edit]
          Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
    
      - radius : r                     (float)         [create,query,edit]
          Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
    
      - rampMaxColor : rxc             (float, float, float) [create,query,edit]
          Defines a special color to be used when the value is greater than or equal to the maximum value.
    
      - rampMinColor : rmc             (float, float, float) [create,query,edit]
          Defines a special color to be used when the value is less than or equal to the minimum value.
    
      - record : rec                   (bool)          []
    
      - reflection : rn                (bool)          [create,query,edit]
          Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
    
      - reflectionaboutorigin : rno    (bool)          []
    
      - reflectionaxis : ra            (unicode)       [create,query,edit]
          Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it
          returns a string.
    
      - screenRadius : scR             (float)         []
    
      - selectclonesource : scs        (bool)          []
    
      - selectedattroper : sao         (unicode)       [create,query,edit]
          Sets the edit weight operation. Four edit weights operations are provided : "absolute" - the value of the weight is
          replaced by the current one, "additive" - the value of the weight is added to the current one, "scale" - the value of
          the weight is multiplied by the current one, "smooth" - the value of the weight is divided by the current one. C:
          Default is "absolute". Q: When queried, it returns a string.
    
      - setValueCommand : svc          (unicode)       [create,query,edit]
          Specifies the name of the mel script/procedure which is called every time a value on the surface is changed. Q: When
          queried, it returns a string.
    
      - showactive : sa                (bool)          [create,query,edit]
          Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
    
      - stampDepth : stD               (float)         []
    
      - stampProfile : stP             (unicode)       [create,query,edit]
          Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "soft",
          "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
    
      - stampSpacing : stS             (float)         []
    
      - strokesmooth : ssm             (unicode)       []
    
      - surfaceConformedBrushVertices : scv (bool)          [create,query,edit]
          Enables/disables the the display of the effective brush area as affected vertices.
    
      - tablet : tab                   (bool)          [query]
          Returns true if the tablet device is present, false if it is absent
    
      - tangentOutline : to            (bool)          [create,query,edit]
          Enables/disables the display of the brush circle tangent to the surface.
    
      - toolCleanupCmd : tcc           (unicode)       [create,query,edit]
          Specifies the name of the mel script/procedure which is called when this tool is exited. Q: When queried, it returns a
          string.
    
      - toolOffProc : tfp              (unicode)       [create,query,edit]
          Accepts a strings describing the name of a MEL procedure which is invoked whenever the tool is turned off. For example,
          cloth invokes "clothPaintToolOff" when the cloth paint tool is turned on. Define this callback if your tool requires
          special functionality when your tool is deactivated. It is typical that if you implement a toolOffProc you will want to
          implement a toolOnProc as well (see the -toolOnProc flag. In query mode, the name of the currently registered MEL
          command is returned and this will be an empty string if none is defined.
    
      - toolOnProc : top               (unicode)       [create,query,edit]
          Accepts a strings describing the name of a MEL procedure which is invoked whenever the tool is turned on. For example,
          cloth invokes "clothPaintToolOn" when the cloth paint tool is turned on. Define this callback if your tool requires
          special functionality when your tool is activated. It is typical that if you implement a toolOnProc you will want to
          implement a toolOffProc as well (see the -toolOffProc flag. In query mode, the name of the currently registered MEL
          command is returned and this will be an empty string if none is defined.
    
      - toolSetupCmd : tsc             (unicode)       [create,query,edit]
          Specifies the name of the mel script/procedure which is called once for every selected surface when an initial click is
          received on that surface. Q: When queried, it returns a string.
    
      - useColorRamp : ucr             (bool)          [create,query,edit]
          Specifies whether the user defined color ramp should be used to map values from to colors. If this is turned off, the
          default greyscale feedback will be used.
    
      - useMaxMinColor : umc           (bool)          [create,query,edit]
          Specifies whether the out of range colors should be used. See rampMinColor and rampMaxColor flags for further details.
    
      - usepressure : up               (bool)          [create,query,edit]
          Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
    
      - value : val                    (float)         [create,query,edit]
          Specifies the value for each attribute. C: Default is 0.0. Q: When queried, it returns a float.
    
      - whichTool : wst                (unicode)       [create,query,edit]
          The string defines the name of the tool to be used for the Artisan context. An example is "artClothPaint". In query
          mode, the tool name for the given context is returned. Note: due to the way MEL works, always specify the -query flag
          last when specifying a flag which takes arguments.
    
      - worldRadius : wlR              (float)         []
    
    
    Derived from mel command `maya.cmds.artUserPaintCtx`
    """

    pass


def dynSelectCtx(*args, **kwargs):
    """
    Flags:
      - enable : enb                   (bool)          []
    
      - exists : ex                    (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
    
    Derived from mel command `maya.cmds.dynSelectCtx`
    """

    pass


def curveBezierCtx(*args, **kwargs):
    """
    Flags:
      - degree : d                     (int)           []
    
      - exists : ex                    (bool)          []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - manipMode : mm                 (unicode)       []
    
      - name : n                       (unicode)       []
    
      - preserveShape : ps             (bool)          []
    
      - preserveShapeFraction : pf     (float)         []
    
      - refit : rf                     (bool)          []
    
      - selectMode : slm               (unicode)       []
    
      - uniform : un                   (bool)          []
    
    
    Derived from mel command `maya.cmds.curveBezierCtx`
    """

    pass


def createPolyPlaneCtx(*args, **kwargs):
    """
    Flags:
      - attachToSubdivisionsAll : asa  (bool)          []
    
      - attachToSubdivisionsHeight : ash (bool)          []
    
      - attachToSubdivisionsWidth : asw (bool)          []
    
      - axis : ax                      (int)           []
    
      - createUVs : cuv                (int)           []
    
      - doDragEdit : dde               (bool)          []
    
      - doSubdivisionsCapsEdit : dsc   (bool)          []
    
      - exists : ex                    (bool)          []
    
      - height : h                     (float)         []
    
      - history : ch                   (bool)          []
    
      - image1 : i1                    (unicode)       []
    
      - image2 : i2                    (unicode)       []
    
      - image3 : i3                    (unicode)       []
    
      - name : n                       (unicode)       []
    
      - subdivisionsHeight : sh        (int)           []
    
      - subdivisionsWidth : sw         (int)           []
    
      - width : w                      (float)         []
    
    
    Derived from mel command `maya.cmds.createPolyPlaneCtx`
    """

    pass



