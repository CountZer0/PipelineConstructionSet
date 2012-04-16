"""
pyfbsdk
"""
def FBAudioFmt_AppendFormat(pFormat,pChannels,pBits,pRate):
    """
    pFormat : FBAudioFmt
    pChannels : int
    pBits : int
    pRate : int
    """
    pass

def FBAudioFmt_AppendFormat(pFormat,pSrcFormat):
    """
    pFormat : FBAudioFmt
    pSrcFormat : FBAudioFmt
    """
    pass

def FBAudioFmt_GetBitsValue(pFormat):
    """
    pFormat : FBAudioFmt
    """
    pass

def FBAudioFmt_GetBytesValue(pFormat):
    """
    pFormat : FBAudioFmt
    """
    pass

def FBAudioFmt_GetChannelValue(pFormat):
    """
    pFormat : FBAudioFmt
    """
    pass

def FBAudioFmt_GetDefaultFormat():
    """
    """
    pass

def FBAudioFmt_GetRateValue(pFormat):
    """
    pFormat : FBAudioFmt
    """
    pass

def FBAudioFmt_RemoveFormat(pFormat,pChannels,pBits,pRate):
    """
    pFormat : FBAudioFmt
    pChannels : int
    pBits : int
    pRate : int
    """
    pass

def FBAudioFmt_RemoveFormat(pFormat,pSrcFormat):
    """
    pFormat : FBAudioFmt
    pSrcFormat : FBAudioFmt
    """
    pass

def FBAudioFmt_TestFormat(pSrcFormat,pChannels,pBits,pRate):
    """
    pSrcFormat : FBAudioFmt
    pChannels : int
    pBits : int
    pRate : int
    """
    pass

def FBCreateObject(pGroupName,pEntryName,pName,p3,nth):
    """
    FBCreateObject.

    pGroupName : Set the name of the Group. 
    pEntryName : Set the name of the Entry. 
    pName : Set the name of the Object to create. 
    p3 : Data to pass to object creator function. 
    nth : Set the occurence of the object to remove. 
    """
    pass

def FBFindModelByName(pModelName,pParent):
    """
    Find a model in the hierarchy.
    Searches the scene for a model, based on the model's unique name.

    pModelName : Name of model to search for. 
    pParent : Root model to search from (default=NULL(root)). 
    return : A handle onto the model that was found, returns NULL if no model was found by the search. 
    """
    pass

def FBFindObjectsByName(pNamePattern,pList,pIncludeNamespace,pModelsOnly):
    """
    FBFindObjectsByName.
    This function will query the system for objects fulfilling a particular name pattern

    pNamePattern : Indicate the name pattern to search. This pattern can contain any amount of *. (ex: *tr*mod*scene ) 
    pList : List that contains the objects 
    pIncludeNamespace : Does the search use the complete name (with namespace) 
    pModelsOnly : Is the search on models or all types of objects 
    """
    pass

def FBFindObjectsByNamespace(pNamePattern,pList):
    """
    FBFindObjectsByName.
    This function will query the system for objects fulfilling a particular namespace pattern

    pNamePattern : Indicate the name pattern to search. This pattern can contain any amount of *. (ex: *tr*mod*scene ) 
    pList : List that contains the objects 
    """
    pass

def FBGetCharacterExternalSolverCount():
    """
    Get character external solver count.

    return : Number of external character solver available. 
    """
    pass

def FBGetCharacterExternalSolverIndex(pName):
    """
    Get character external solver index.

    pName : Name of external solver. 
    return : Index of external solver specified at the provided name. 
    """
    pass

def FBGetCharacterExternalSolverName(pIndex):
    """
    Get character external solver name.

    pIndex : Index of external solver. 
    return : Name of the external solver specified at the provided index. 
    """
    pass

def FBGetCharactersKeyingMode():
    """
    return Character Manipulation/Keying Mode

    return : Keying Mode 
    """
    pass

def FBGetEffectorBodyPart(pEffectorId):
    """
    return BodyPart ID from Effector.

    pEffectorId : Effector ID. 
    return : ID of the BodyPart the effector is in. 
    """
    pass

def FBGetMultiLangText(pContext,pKey,pFlagReturnKey):
    """
    Name lookup in the context of an object.
    Most application objects have an internal name which differs from the name shown by the GUI. This will often be the case for the names of an object's properties.The way that support for multiple languages has been implemented is using conversion tables that will map the internal name to a localized name. Since the same internal name might mean different things for different objects, we can provide a context to help the lookup process.In this case, the context is a class object instance. When the lookup fails within a context, we sucessively try a lookup using the parent classes in the object hierarchy.It is important to note that for given property, it only knows about its internal name. The localized name is not attached to the property object itself as it resides elsewhere, in a lookup table. This is also the case for any other application object.The lookup table used to find the localized, or GUI name, of an object is dependent on the current language used. This information is available via the class FBMultiLangManager, which can indicate which language are availables and provides methode to query and change the current language.Python sample code: 
@code
    from pyfbsdk import *

    # Let's pick the first camera present in the system.
    lCamera = FBSystem().Cameras[0]

    # We know that cameras have a property named 'LockMode'.
    lPropInternalName = lCamera.PropertyList.Find( 'LockMode' )
    if lPropInternalName:
        print 'Actual property name, as defined internally: '%s'' % lPropInternalName.GetName()
        print 'Property name as shown by the GUI: '%s'' % FBGetMultiLangText( lCamera, lPropInternalName.GetName())
    
        lPropLocalizedName = lCamera.PropertyList.Find( FBGetMultiLangText( lCamera, lPropInternalName.GetName()))
        if lPropLocalizedName and lPropInternalName.GetName() == lPropLocalizedName.GetName():
            print 'Found the same property using both the internal (%s) and localized name (%s).' % (
                lPropLocalizedName.GetName(),
                FBGetMultiLangText( lCamera, lPropInternalName.GetName()))
@endcode

C++ sample code: 
@code
    // Let's pick the first camera present in the system.
    HFBCamera lCamera = FBSystem().Cameras[0];

    // We know that cameras have a property named 'LockMode'.
    HFBProperty lPropInternalName = lCamera->PropertyList.Find( 'LockMode' );
    if( lPropInternalName )
    {
        FBTrace( 'Actual property name, as defined internally: '%s'\n', lPropInternalName->GetName());
        FBTrace( 'Property name as shown by the GUI: '%s'\n', FBGetMultiLangText( lCamera, lPropInternalName->GetName()));
    
        HFBProperty lPropLocalizedName = lCamera->PropertyList.Find( FBGetMultiLangText( lCamera, lPropInternalName->GetName()));
        if( lPropLocalizedName && stricmp( lPropInternalName->GetName(), lPropLocalizedName->GetName()) == 0 )
        {
            FBTrace( 'Found the same property using both the internal (%s) and localized name (%s).\n',
                lPropLocalizedName->GetName(),
                FBGetMultiLangText( lCamera, lPropInternalName->GetName()));
        }
    }
@endcode

    pContext : Object which dictates the context of the lookup. 
    pKey : String to look up. 
    pFlagReturnKey : Should the lookup fail, will return the key instead of an empty string. 
    return : The corresponding string if the lookup was succesfull. If not will return an empty string if pFlagReturnKey was false. Otherwise will return the key string. 
    """
    pass

def FBGetMultiLangText(pContext,pKey,pFlagReturnKey):
    """
    Name lookup in a user defined context context.
    This version of the function is a little less useful as the context string, if not empty, will usually refer to internal class names of objects which is not easily available to the outside world.As a general rule, an SDK object whose class is 'FBObject' will be wrapping an internal object of class 'KObject'. For example an 'FBCamera' is a wrapper around a 'KCamera' object. Similarily an 'FBConstraint' wll wrap a 'KConstraint'. This pattern is not universal and may differ at times, so it will not always be applicable. There are also cases where an 'FB' objects has no corresponding 'K' object, such as in the case of an 'FBSystem' object.On lookup there are potentially two searches made: a first one, using the context if one was provided. Should the first search fail, a second search will be done without using the context.Again the lookup result is dependant on the current language selected, as indicated by the class FBMultiLangManager.The following sample code shows 2 cases that do not use context, and 2 cases that are using a context which are internal class names.Python sample code: 
@code
    from pyfbsdk import *

    print FBGetMultiLangText( '', 'CharacterExtension' )            # Will return 'Character Extension'.
    print FBGetMultiLangText( '', 'TranslationMax' )                # Will return 'Max Freedom'.
    print FBGetMultiLangText( 'KConstraintUIName', 'Parent-Child' ) # Will return 'Parent/Child'.
    print FBGetMultiLangText( 'KCamera', 'FieldOfView' )            # Will return 'Field Of View'.
@endcode

C++ sample code: 
@code
    // Will return 'Character Extension'.
    FBTrace( '%s\n', FBGetMultiLangText( '', 'CharacterExtension' ));

    // Will return 'Max Freedom'.
    FBTrace( '%s\n', FBGetMultiLangText( '', 'TranslationMax' ));

    // Will return 'Parent/Child'.
    FBTrace( '%s\n', FBGetMultiLangText( 'KConstraintUIName', 'Parent-Child' ));

    // Will return 'Field Of View'.
    FBTrace( '%s\n', FBGetMultiLangText( 'KCamera', 'FieldOfView' ));
@endcode

    pContext : String which dictates the context of the lookup. 
    pKey : String to look up. 
    pFlagReturnKey : Should the lookup fail, will return the key instead of an empty string. 
    return : The corresponding string if the lookup was succesfull. If not will return an empty string if pFlagReturnKey was false. Otherwise will return the key string. 
    """
    pass

def FBGetSelectedModels(pList,pParent,pSelected):
    """
    Find all models that are selected (if <b>pSelected</b> is true) Searches recursively from a root model for models that are selected, and adds them to a list of models.

    pList : List to add found models to. 
    pParent : Root model to look from (default=NULL(root)). 
    pSelected : <b>true</b> to find selected models, <b>false</b> to find unselected models(default=true). 
    """
    pass

def FBLoadFbxPrimitivesModel(pModelName):
    """
    Load a model.

    pModelName : Name of primitive model to load. 
    return : A handle onto the model that was loaded, returns NULL if no model was found. 
    """
    pass

def FBMessageBox(pBoxTitle,pMessage,pButton1Str,pButton2Str,pButton3Str,pDefaultButton,pScrolledMessage):
    """
    Dialog popup box.
    Opens a message box containing a message and up to three buttons. Waits for the user to click a button.

    pBoxTitle : Title of message box. 
    pMessage : Message to place in box. 
    pButton1Str : String for first button (Cannot be NULL). 
    pButton2Str : String for second button (NULL will not create a button). 
    pButton3Str : String for third button (NULL will not create a button). 
    pDefaultButton : Indicates the default (pre-selected) button (default is 0). 
    pScrolledMessage : Scroll message (default is 0). 
    return : The number of the button selected. 
    """
    pass

def FBModelTransactionBegin():
    """
    FBModelTransactionBegin.
    This set of functions speeds up the process of batch operations on models.

    """
    pass

def FBModelTransactionEnd():
    """
    FBModelTransactionEnd.
    This set of functions speeds up the process of batch operations on models.

    """
    pass

def FBPopNormalTool(pToolName,pSetFocus):
    """
    This function is used to bring up a specific tool in the GUI.

    pToolName : The name of the tool as shown in the Open Reality menu. 
    pSetFocus : Indicate if the tool will have the focus. 
    return : If the tool was brought up successfully. 
    """
    pass

def FBSelectObjectsByNamespace(pNameSpaceName,pSelect,pSearchExclusive):
    """
    FBSelectObjectsByNamespace.
    This function will select objects in the current scene according to the parameters you provide

    pNameSpaceName : Indicate the name to search for selection/deselection. 
    pSelect : Indicate if we select or unselect the objects 
    pSearchExclusive : "true" will select object that are exclusive to that namespace(pNameSpaceName), "false" will select object that could be part of that namespace as well as others namespace. 
    """
    pass

def FBSleep(MilliSeconds):
    """
    Sleep function Puts system to sleep for specified time.

    MilliSeconds : Time to sleep for. 
    """
    pass

def FBTrace(pFormatString,p1):
    """
    This function prints useful debugging strings in the console.
    By passing the argument '-console' when launching MotionBuilder, it is possible to print formatted messages, as a printf would. On Mac OSX, the strings are simply sent to stderr.

    pFormatString : A printf-style format string, to use the following arguments in the list. 
    p1 : ...
    """
    pass

def FBMessageBoxWithCheck(pBoxTitle,pMessage,pButton1Str,pButton2Str,pButton3Str,pCheckBoxStr,pCheckBoxValue,pDefaultButton,pScrolledMessage):
    """
    Dialog popup box with 'don't show again' option.
    Opens a message box containing a message and up to three buttons. Waits for the user to click a button. This dialog also gives the user the option of never showing the dialog again.

    pBoxTitle : Title of message box. 
    pMessage : Message to place in box. 
    pButton1Str : String for first button (Cannot be None). 
    pButton2Str : String for second button (None will not create a button). 
    pButton3Str : String for third button (None will not create a button). 
    pCheckBoxStr : Check box string (Cannot be None). 
    pCheckBoxValue : Check box value. 
    pDefaultButton : Indicates the default (pre-selected) button (default is 0). 
    pScrolledMessage : Scroll message (default is False). 
    return : A tuple containing the index of the button selected and the boolean value of the check box. 
    """
    pass

def FBMessageBoxGetUserValue(pBoxTitle,pMessage,pValue,pValueType,pButton1Str,pButton2Str,pButton3Str,pDefaultButton):
    """
    Dialog popup box to get user input.
    Opens a message box, with up to three buttons, asking the user to enter data. The type of data to be entered is specified by the <b>pValue</b> and <b>pValueType</b> parameters.

    pBoxTitle : Title of message box. 
    pMessage : Message to place in box. 
    pValue : Value entered by user (must correspond with pValueType). 
    pValueType : Type of pointer specified in pValue. 
    pButton1Str : String for first button (Cannot be None). 
    pButton2Str : String for second button (None will not create a button). 
    pButton3Str : String for third button (None will not create a button). 
    pDefaultButton : Indicates the default (pre-selected) button(default=0). 
    return : A tuple containing the index of the button selected and the value entered by the user, if any. 
    """
    pass

def FBConnect(pSrc,pDst,pConnectionType):
    """
    Request the connection two FBPlug objects.

    pSrc : Source plug. 
    pDst : Destination plug. 
    pConnectionType : Type of connection, taken from FBConnectionType. 
    return : A boolean indicating success (True) or failure (False). 
    """
    pass

def FBDisconnect(pSrc,pDst):
    """
    Connect two FBPlug objects.

    pSrc : Source plug. 
    pDst : Destination plug. 
    return : A boolean indicating success (True) or failure (False). 
    """
    pass

class Enumeration:
    """
    Enumeration
    """
    pass

class object:
    """
    object
    """
    pass

class FBInputKey (object):
    """
    Keyboard inputs.     
        
    """
    kFBKeyReturn=property(doc="Return.         ")
    kFBKeyBackSpace=property(doc="Backspace.         ")
    kFBKeyTab=property(doc="Tab.         ")
    kFBKeyEscape=property(doc="Escape.         ")
    kFBKeyPageUp=property(doc="Page Up.         ")
    kFBKeyPageDown=property(doc="Page Down.         ")
    kFBKeyEnd=property(doc="End.         ")
    kFBKeyHome=property(doc="Home.         ")
    kFBKeyLeft=property(doc="Left.         ")
    kFBKeyUp=property(doc="Up.         ")
    kFBKeyRight=property(doc="Right.         ")
    kFBKeyDown=property(doc="Down.         ")
    kFBKeyIns=property(doc="Insert.         ")
    kFBKeyDel=property(doc="Delete.         ")
    kFBKeyF1=property(doc="F1.         ")
    kFBKeyF2=property(doc="F2.         ")
    kFBKeyF3=property(doc="F3.         ")
    kFBKeyF4=property(doc="F4.         ")
    kFBKeyF5=property(doc="F5.         ")
    kFBKeyF6=property(doc="F6.         ")
    kFBKeyF7=property(doc="F7.         ")
    kFBKeyF8=property(doc="F8.         ")
    kFBKeyF9=property(doc="F9.         ")
    kFBKeyF10=property(doc="F10.         ")
    kFBKeyF11=property(doc="F11.         ")
    kFBKeyF12=property(doc="F12.         ")
    pass

class FBTransportPlaySpeed (object):
    """
    Available transport control play speed.     
        
    """
    kFBSpeed_1_10x=property(doc="1/10x.         ")
    kFBSpeed_1_5x=property(doc="1/5x         ")
    kFBSpeed_1_4x=property(doc="1/4x         ")
    kFBSpeed_1_3x=property(doc="1/3x         ")
    kFBSpeed_1_2x=property(doc="1/2x         ")
    kFBSpeed_1x=property(doc="1x         ")
    kFBSpeed_ALL_FR=property(doc="All frames.         ")
    kFBSpeed_2x=property(doc="2x         ")
    kFBSpeed_3x=property(doc="3x         ")
    kFBSpeed_4x=property(doc="4x         ")
    kFBSpeed_5x=property(doc="5x         ")
    kFBSpeed_10x=property(doc="10x         ")
    pass

class FBStoryClipSolveMode (object):
    """
    Solve Modes for story character clips.     
        
    """
    kFBStoryClipRetargetSkeleton=property(doc="Solve retarget skeleton.         ")
    kFBStoryClipAnimSkeleton=property(doc="Solve skeleton animation.         ")
    kFBStoryClipAnimFkIk=property(doc="Solve forward and inverse kinematic animation.         ")
    kFBStoryClipAnimSkeletonIk=property(doc="Solve skeleton inverse kinematic animation.         ")
    pass

class FBEventAnimationNodeType (object):
    """
    Event based on animation node.     
    Types of transformation.     
    """
    kFBEventAnimationNodeDataChange=property(doc="        ")
    kFBEventAnimationNodeConstraintChange=property(doc="        ")
    kFBEventAnimationNodeNone=property(doc="        ")
    pass

class FBTangentConstantMode (object):
    """
    Different constant modes for the tangents.     
        
    """
    kFBTangentConstantModeNormal=property(doc="The tangent will contain the value of the current keyframe until the next keyframe.         ")
    kFBTangentConstantModeNext=property(doc="The tangent will contain the value of the next keyframe.         ")
    pass

class FBPropertyListModelTemplateBinding (object):
    """
        
        
    """
    pass

class FBStoryTrackType (object):
    """
    Types for new story tracks.     
        
    """
    kFBStoryTrackAnimation=property(doc="Animation track.         ")
    kFBStoryTrackCamera=property(doc="Camera animation track.         ")
    kFBStoryTrackCharacter=property(doc="Character animation track.         ")
    kFBStoryTrackConstraint=property(doc="Constraint track.         ")
    kFBStoryTrackCommand=property(doc="Command track.         ")
    kFBStoryTrackShot=property(doc="Shot track.         ")
    kFBStoryTrackAudio=property(doc="Audio track.         ")
    kFBStoryTrackVideo=property(doc="Video track.         ")
    kFBStoryTrackUnknown=property(doc="        ")
    pass

class FBCharacterResetProperties (object):
    """
    Character Reset Properties Type.     
        
    """
    kFBCharacterResetPropertiesAll=property(doc="        ")
    kFBCharacterResetPropertiesSolving=property(doc="        ")
    kFBCharacterResetPropertiesDefinition=property(doc="        ")
    pass

class FBMarkerType (object):
    """
    Type of the marker.     
        
    """
    kFBMarkerTypeStandard=property(doc="Standard.         ")
    kFBMarkerTypeOptical=property(doc="Optical.         ")
    kFBMarkerTypeFKEffector=property(doc="FK effector.         ")
    kFBMarkerTypeIKEffector=property(doc="IK effector.         ")
    pass

class FBPropertyListUVIndex (object):
    """
        
        
    """
    pass

class FBModelShadingMode (object):
    """
    Modes for model shading.     
        
    """
    kFBModelShadingDefault=property(doc="Default shading.         ")
    kFBModelShadingWire=property(doc="Wireframe shading.         ")
    kFBModelShadingFlat=property(doc="Flat shading.         ")
    kFBModelShadingLight=property(doc="Lighted shading.         ")
    kFBModelShadingHard=property(doc="Hard shading.         ")
    kFBModelShadingTexture=property(doc="Textured shading.         ")
    kFBModelShadingAll=property(doc="Lighted, shaded, textured shading.         ")
    pass

class FBCameraSamplingType (object):
    """
    Antialiasing sampling types.     
        
    """
    kFBSamplingUniform=property(doc="Uniform sampling.         ")
    kFBSamplingStochastic=property(doc="Stochastic sampling.         ")
    pass

class FBCellStyle (object):
    """
    Different styles of spreadsheet cell styles.     
        
    """
    kFBCellStyleDefault=property(doc="Default cell style.         ")
    kFBCellStyleString=property(doc="String.         ")
    kFBCellStyleDouble=property(doc="Double.         ")
    kFBCellStyleInteger=property(doc="Integer.         ")
    kFBCellStyleButton=property(doc="Button.         ")
    kFBCellStyle2StatesButton=property(doc="2 state button.         ")
    kFBCellStyle3StatesButton=property(doc="3 state button.         ")
    kFBCellStyleMenu=property(doc="Menu.         ")
    kFBCellStyleVoid=property(doc="Void (no value).         ")
    kFBCellStyleView=property(doc="View (user definable, you need to specify the view using FBSpread::SetCellView()).         ")
    kFBCellStyleTime=property(doc="Time.         ")
    pass

class FBBatchOnTakeExist (object):
    """
    Different actions to perform when a take already exist while in a batch process.     
        
    """
    kFBBatchOnTakeExistOverwrite=property(doc="Overwrite the take.         ")
    kFBBatchOnTakeExistSkip=property(doc="Skip the take.         ")
    pass

class FBImageFormat (object):
    """
    Image formats.     
        
    """
    kFBImageFormatRGBA32=property(doc="        ")
    kFBImageFormatRGB24=property(doc="        ")
    kFBImageFormatBGRA32=property(doc="        ")
    kFBImageFormatBGR24=property(doc="        ")
    kFBImageFormatBGR16=property(doc="        ")
    kFBImageFormatABGR32=property(doc="        ")
    kFBImageFormatARGB32=property(doc="        ")
    kFBImageFormatUnknown=property(doc="        ")
    pass

class FBAttenuationType (object):
    """
    Light attenuation types.     
        
    """
    kFBAttenuationNone=property(doc="No attenuation.         ")
    kFBAttenuationLinear=property(doc="Linear attenuation.         ")
    kFBAttenuationQuadratic=property(doc="Quadratic attenuation.         ")
    pass

class FBFilePopupStyle (object):
    """
    Different types of file popup windows.     
        
    """
    kFBFilePopupOpen=property(doc="Open file popup (Shows 'Open Directory').         ")
    kFBFilePopupSave=property(doc="Save file popup (Shows 'Save Directory').         ")
    pass

class FBFbxManagerState (object):
    """
    This enumeration indicate the current state of the FBFbxManager.     
    The manager can only do one action at a time.     
    """
    kFBFbxManagerStateIdle=property(doc="The manager is ready to start a process.         ")
    kFBFbxManagerStateLoading=property(doc="A load process is in progress.         ")
    kFBFbxManagerStateMerging=property(doc="A merge process is in progress.         ")
    kFBFbxManagerStateSaving=property(doc="A save process is in process.         ")
    pass

class FBCameraSafeAreaMode (object):
    """
    Safe area modes.     
        
    """
    kFBSafeAreaSquare=property(doc="Square safe area.         ")
    kFBSafeAreaRound=property(doc="Round safe area.         ")
    pass

class FBPickInfosList (object):
    """
    FBPickInfosList class.     
    This class implements a special sort of list that can only contains a pick info which is a tuple<FBModel, FBVector3d>. A pick info give the position (FBVector3d) and the model (FBModel) that was pick on screen.To users FBPickInfosList behave like a typle, since it is not possible to add new objects in the list. Only methods or function that uses FBPickInfosList as argument can insert new objects. Users can query the content of the list with the bracket operator. 
@code
    # Supported list protocol methods:
    l = FBPickInfosList()
    len(l)

    # tuple unpacking of pick infos.
    model, vector = l[0]
@endcode

     
    """
    def FBPickInfosList(self):
        """
        Constructor.

        """
        pass

    def __len__(self):
        """
        Returns the number of elements.
        Corresponds to python: len(object)

        """
        pass

    def __getitem__(self,pIndex):
        """
        Returns the ith component Corresponds to python: print l[1].

        pIndex : Index of the components to get 
        return : PickInfos element value. A Pick info is a tuple<FBModel, FBVector3d> 
        """
        pass

    pass

class FBTextStyle (object):
    """
    Text appearance styles.     
        
    """
    kFBTextStyleNone=property(doc="Normal.         ")
    kFBTextStyleBold=property(doc="Bold.         ")
    kFBTextStyleItalic=property(doc="Italic.         ")
    kFBTextStyleUnderlined=property(doc="Underlined.         ")
    pass

class FBCameraMatrixType (object):
    """
    Camera matrix types.     
        
    """
    kFBProjection=property(doc="Projection View matrix (OpenGL).         ")
    kFBModelView=property(doc="Model View matrix (OpenGL).         ")
    pass

class FBTime (object):
    """
    Time data structure.     
        
    """
    def FBTime(self,pTime):
        """
        pTime : long
        """
        pass

    def FBTime(self,pHour,pMinute,pSecond,pFrame,pField,pTimeMode,pFramerate):
        """
        Constructor.

        pHour : Hour value. 
        pMinute : Minute value. 
        pSecond : Second value. 
        pFrame : Frame value. 
        pField : Field value. 
        pTimeMode : Time mode(default=kFBTimeModeDefault). 
        pFramerate : Custom framerate value in case of pTimeMode = kFBTimeModeCustom. 
        """
        pass

    def Get(self):
        """
        Get time value (long).

        return : Time value as long. 
        """
        pass

    def Get(self):
        """
        Get time value (long).

        return : Time value as long. 
        """
        pass

    def GetFrame(self,pCummul,pTimeMode,pFramerate):
        """
        Get the frame count.
        With this function, it is possible to obtain the cumulative and local frame counts.

        pCummul : Cumulative frame count (<b>true</b> ), or local frame count (<b>false</b> )(default is false). 
        pTimeMode : Time mode to get the constant (default is kFBTimeModeDefault). 
        pFramerate : Custom framerate value in case of pTimeMode = kFBTimeModeCustom. 
        return : Frames per second constant for the specified time mode. 
        """
        pass

    def GetMilliSeconds(self):
        """
        Get milliseconds for time.

        return : MilliSeconds value. 
        """
        pass

    def GetSecondDouble(self):
        """
        Get seconds as double.

        return : Seconds in double form. 
        """
        pass

    def GetTimeString(self):
        """
        Get time as a string.

        return : String value of time. 
        """
        pass

    def Set(self,pTime):
        """
        Set time value from a long.

        pTime : Time value to set. 
        """
        pass

    def SetMilliSeconds(self,pMilliSeconds):
        """
        Set milliseconds time.

        pMilliSeconds : MilliSeconds value. 
        """
        pass

    def SetSecondDouble(self,pTime):
        """
        Set seconds from double.

        pTime : Time to set seconds from. 
        """
        pass

    def SetTime(self,pHour,pMinute,pSecond,pFrame,pField,pTimeMode,pFramerate):
        """
        Set time (from separate values).

        pHour : Hour value. 
        pMinute : Minute value(default=0). 
        pSecond : Second value(default=0). 
        pFrame : Frame value(default=0). 
        pField : Field value(default=0). 
        pTimeMode : Time mode to get time as(default=kFBTimeModeDefault). 
        pFramerate : Custom framerate value in case of pTimeMode = kFBTimeModeCustom. 
        """
        pass

    def SetTimeString(self,pTime):
        """
        Set time from string.

        pTime : String to set time from. 
        """
        pass

    pass

class FBComponentList (object):
    """
    FBComponentList class.     
    This class implements a special sort of list that can only contain instances of FBComponent objects. To users it behaves as a tuple, since it is not possible to add new objects in the list. Only methods or function that uses FBComponentList as argument can insert new objects. Users can query the content of the list with the bracket operator. 
@code
    # Supported list protocol methods:
    l = FBComponentList()
    len(l)
    print l[0]
@endcode

     
    """
    def FBComponentList(self):
        """
        Constructor.

        """
        pass

    def __len__(self):
        """
        Returns the number of elements.
        Corresponds to python: len(object)

        """
        pass

    def __getitem__(self,pIndex):
        """
        Returns the ith component Corresponds to python: print l[1].

        pIndex : Index of the components to get 
        return : FBComponent element value 
        """
        pass

    pass

class FBModelRotationOrder (object):
    """
    Ways to apply Rotation.     
        
    """
    kFBEulerXYZ=property(doc="XYZ Euler Order.         ")
    kFBEulerXZY=property(doc="XZY Euler Order.         ")
    kFBEulerYZX=property(doc="YZX Euler Order.         ")
    kFBEulerYXZ=property(doc="YXZ Euler Order.         ")
    kFBEulerZXY=property(doc="ZXY Euler Order.         ")
    kFBEulerZYX=property(doc="ZYX Euler Order.         ")
    kFBSphericXYZ=property(doc="Spheric XYZ Order.         ")
    pass

class FBFogMode (object):
    """
    Fog falloff modes.     
        
    """
    kFBFogModeLinear=property(doc="Linear falloff.         ")
    kFBFogModeExponential=property(doc="Exponential falloff.         ")
    kFBFogModeSquareExponential=property(doc="Squared exponential falloff.         ")
    pass

class FBClusterMode (object):
    """
    Different clustering modes.     
        
    """
    kFBClusterNormalize=property(doc="Normalize (values between 0.0 and 1.0 ).         ")
    kFBClusterAdditive=property(doc="Add the values together.         ")
    kFBClusterTotal100=property(doc="The balanced values will add up to 100 percent.         ")
    pass

class FBSkeletonNodeId (object):
    """
    All Skeleton nodes.     
        
    """
    kFBSkeletonInvalidIndex=property(doc="        ")
    kFBSkeletonHipsIndex=property(doc="        ")
    kFBSkeletonLeftHipIndex=property(doc="        ")
    kFBSkeletonLeftKneeIndex=property(doc="        ")
    kFBSkeletonLeftAnkleIndex=property(doc="        ")
    kFBSkeletonLeftFootIndex=property(doc="        ")
    kFBSkeletonRightHipIndex=property(doc="        ")
    kFBSkeletonRightKneeIndex=property(doc="        ")
    kFBSkeletonRightAnkleIndex=property(doc="        ")
    kFBSkeletonRightFootIndex=property(doc="        ")
    kFBSkeletonWaistIndex=property(doc="        ")
    kFBSkeletonChestIndex=property(doc="        ")
    kFBSkeletonLeftCollarIndex=property(doc="        ")
    kFBSkeletonLeftShoulderIndex=property(doc="        ")
    kFBSkeletonLeftElbowIndex=property(doc="        ")
    kFBSkeletonLeftWristIndex=property(doc="        ")
    kFBSkeletonRightCollarIndex=property(doc="        ")
    kFBSkeletonRightShoulderIndex=property(doc="        ")
    kFBSkeletonRightElbowIndex=property(doc="        ")
    kFBSkeletonRightWristIndex=property(doc="        ")
    kFBSkeletonNeckIndex=property(doc="        ")
    kFBSkeletonHeadIndex=property(doc="        ")
    kFBSkeletonLeftThumbAIndex=property(doc="        ")
    kFBSkeletonLeftThumbBIndex=property(doc="        ")
    kFBSkeletonLeftThumbCIndex=property(doc="        ")
    kFBSkeletonLeftIndexAIndex=property(doc="        ")
    kFBSkeletonLeftIndexBIndex=property(doc="        ")
    kFBSkeletonLeftIndexCIndex=property(doc="        ")
    kFBSkeletonLeftMiddleAIndex=property(doc="        ")
    kFBSkeletonLeftMiddleBIndex=property(doc="        ")
    kFBSkeletonLeftMiddleCIndex=property(doc="        ")
    kFBSkeletonLeftRingAIndex=property(doc="        ")
    kFBSkeletonLeftRingBIndex=property(doc="        ")
    kFBSkeletonLeftRingCIndex=property(doc="        ")
    kFBSkeletonLeftPinkyAIndex=property(doc="        ")
    kFBSkeletonLeftPinkyBIndex=property(doc="        ")
    kFBSkeletonLeftPinkyCIndex=property(doc="        ")
    kFBSkeletonRightThumbAIndex=property(doc="        ")
    kFBSkeletonRightThumbBIndex=property(doc="        ")
    kFBSkeletonRightThumbCIndex=property(doc="        ")
    kFBSkeletonRightIndexAIndex=property(doc="        ")
    kFBSkeletonRightIndexBIndex=property(doc="        ")
    kFBSkeletonRightIndexCIndex=property(doc="        ")
    kFBSkeletonRightMiddleAIndex=property(doc="        ")
    kFBSkeletonRightMiddleBIndex=property(doc="        ")
    kFBSkeletonRightMiddleCIndex=property(doc="        ")
    kFBSkeletonRightRingAIndex=property(doc="        ")
    kFBSkeletonRightRingBIndex=property(doc="        ")
    kFBSkeletonRightRingCIndex=property(doc="        ")
    kFBSkeletonRightPinkyAIndex=property(doc="        ")
    kFBSkeletonRightPinkyBIndex=property(doc="        ")
    kFBSkeletonRightPinkyCIndex=property(doc="        ")
    kFBSkeletonReferenceIndex=property(doc="        ")
    kFBSkeletonLastIndex=property(doc="        ")
    pass

class FBModelList (object):
    """
    FBModelList class.     
    This class implements a special sort of list that can only contain instances of FBModel objects. Users can query the content of the list with the bracket operator. 
@code
    # Supported list protocol methods:
    l = FBModelList()
    len(l)
    print l[0]
@endcode

     
    """
    def FBModelList(self):
        """
        Constructor.

        """
        pass

    def GetCount(self):
        """
        Get number of models in list.

        """
        pass

    def count(self):
        """
        Get number of models in list.

        """
        pass

    def GetModel(self,pIndex):
        """
        Get the ith model in list.

        pIndex : index of modle to get (0 based). 
        return : The pIndex model 
        """
        pass

    def Add(self,pModel):
        """
        Append a new modle at the end of the list.

        pModel : model to add to the list. 
        """
        pass

    def append(self,pModel):
        """
        Append a new modle at the end of the list.

        pModel : model to add to the list. 
        """
        pass

    def Clear(self):
        """
        Empty the list from all models.

        """
        pass

    def __len__(self):
        """
        Returns the number of elements.
        Corresponds to python: len(object)

        """
        pass

    def __getitem__(self,pIndex):
        """
        Returns the ith component Corresponds to python: print l[1].

        pIndex : Index of the components to get 
        return : Model element value 
        """
        pass

    pass

class FBConnectionType (object):
    """
    Connection types available between plugs.     
        
    """
    kFBConnectionTypeNone=property(doc="Default connection type.         ")
    kFBConnectionTypeSystem=property(doc="System connection type.         ")
    kFBConnectionTypeUnidirectional=property(doc="Unidirectional connection type.         ")
    pass

class FBAssetMngFileOptions (object):
    """
    Behavior of the application when working with managed files.     
        
    """
    kFileCheckOutOnLoad=property(doc="Check out file automatically on load.         ")
    kFileCheckOutOnLoad_Ask=property(doc="Ask for checkout on load.         ")
    kFileUploadOnSave=property(doc="Upload file automatically on save.         ")
    kFileUploadOnSave_Ask=property(doc="Ask for upload on save.         ")
    kFileAddOnNewSave=property(doc="Add new file automatically on save.         ")
    kFileAddOnNewSave_Ask=property(doc="Ask for adding new file on save.         ")
    kFileCheckInOnClose=property(doc="Check in file automatically when closing it.         ")
    kFileCheckInOnClose_Ask=property(doc="Ask for check in file when closing it.         ")
    kFileOptionsAll=property(doc="        ")
    pass

class FBFloorContactID (object):
    """
    Floor contact for the given index.     
        
    """
    FBLeftHandMemberIndex=property(doc="        ")
    FBRightHandMemberIndex=property(doc="        ")
    FBLeftFootMemberIndex=property(doc="        ")
    FBRightFootMemberIndex=property(doc="        ")
    FBLastCharacterMember=property(doc="        ")
    pass

class FBMarkerLook (object):
    """
    Look of the marker.     
        
    """
    kFBMarkerLookCube=property(doc="Cube.         ")
    kFBMarkerLookHardCross=property(doc="Thick cross.         ")
    kFBMarkerLookLightCross=property(doc="Wireframe cross.         ")
    kFBMarkerLookSphere=property(doc="Sphere.         ")
    kFBMarkerLookCapsule=property(doc="Capsule.         ")
    pass

class FBPythonWrapper (object):
    """
    Base class of FBPlug in Python.     
    This class act as a bridge between the ORSDK C++ world and the Python world. Since each Python objects wrap a ORSDK object we need a way to notify Python if the ORSDK object is destroyed.OnUnbind is used in this way: it notifies the user when the wrapped ORSDK objects is destroyed.     
    """
    OnUnbind=property(doc="<b>Event:</b> Will notifier the user when the corresponding ORSDK objects is unbound from the PythonObject.         ")
    pass

class FBDeviceSamplingMode (object):
    """
    Recording types.     
    The different values for this will control the way the keys are added when the device is being recorded. There are four different types of recording keys for devices:Hardware Timestamping. This case is when the hardware provides timestamps with each packet.Hardware Frequency. The hardware is guaranteed to provide packets at a given frequency.Auto Frequency Packets are coming in at a fixed, unknown frequency. The recorded data will be resampled to be equidistant.Software Timestamping. The application will provide a timestamp for each packet depending on when it receives the data.     
    """
    kFBHardwareTimestamp=property(doc="Device supplies timestamp.         ")
    kFBHardwareFrequency=property(doc="Device is running at known, fixed frequency.         ")
    kFBAutoFrequency=property(doc="Device is running at unknown, fixed frequency.         ")
    kFBSoftwareTimestamp=property(doc="The software will timestamp packets as they arrive.         ")
    pass

class FBCameraFocusDistanceSource (object):
    """
    Focus distance sources.     
        
    """
    kFBFocusDistanceCameraInterest=property(doc="Interest as source.         ")
    kFBFocusDistanceSpecificDistance=property(doc="Specific distance as source.         ")
    pass

class FBPropertyFlag (object):
    """
    Available flags for FBProperty objects.     
    Property flags are not saved into FBX files.     
    """
    kFBPropertyFlagNotSet=property(doc="        ")
    kFBPropertyFlagHideProperty=property(doc="        ")
    kFBPropertyFlagForceStaticProperty=property(doc="        ")
    kFBPropertyFlagDisableProperty=property(doc="        ")
    kFBPropertyFlagAnimated=property(doc="        ")
    kFBPropertyFlagNotSavable=property(doc="        ")
    kFBPropertyFlagReadOnly=property(doc="        ")
    kFBPropertyFlagNotUserDeletable=property(doc="        ")
    pass

class FBButtonState (object):
    """
    Possible button states.     
    Currently, only two button states are possible.     
    """
    kFBButtonState0=property(doc="State is 0, usually meaning not active.         ")
    kFBButtonState1=property(doc="State is 1, usually meaning active.         ")
    pass

class FBAssetMngMenuOptions (object):
    """
    Show or hide version control menu items.     
    Let you specify which functionalities will be available from the menus.     
    """
    kMenuOpenFromDatabase=property(doc="File -> Open from database.         ")
    kMenuAddToDatabase=property(doc="File -> Add to database.         ")
    kMenuUploadToDatabase=property(doc="File -> Upload to database.         ")
    kMenuGetLatest=property(doc="Version Control -> Get Latest.         ")
    kMenuCheckIn=property(doc="Version Control -> Check In.         ")
    kMenuCheckOut=property(doc="Version Control -> Check Out.         ")
    kMenuUndoCheckOut=property(doc="Version Control -> Undo Check Out.         ")
    kMenuShowHistory=property(doc="Version Control -> Show History.         ")
    kMenuShowProperties=property(doc="Version Control -> Show Properties.         ")
    kMenuShowExplorer=property(doc="Version Control -> Show Explorer.         ")
    kMenuShowReferenceMng=property(doc="Version Control -> Show Reference Manager.         ")
    kMenuShowSettings=property(doc="Version Control -> Show Settings.         ")
    kMenuEnable=property(doc="Version Control -> Disable Version Control Integration.         ")
    kMenuFileAll=property(doc="Support all elements from the File menu.         ")
    kMenuSourceControlAll=property(doc="Support all elements from the Version Control menu.         ")
    kMenuSourceControlMin=property(doc="Support only the basics functionalities.         ")
    kMenuAll=property(doc="Support everything.         ")
    pass

class FBVideoRenderDepth (object):
    """
    Enum FBVideoRenderDepth.     
        
    """
    FBVideoRender24Bits=property(doc="24 bits         ")
    FBVideoRender32Bits=property(doc="32 bits         ")
    FBVideoRenderDepthCount=property(doc="Depth Count.         ")
    pass

class FBVector3d (object):
    """
    Vector3d class.     
    This class creates a list like object, which can be modified using the list protocol method. But unlike lists, its length is fixed: it always contain 3 floating point values. Thus it does not support the any list methods that would affect its length. The values within can be changed, usually via the bracket operator.
@code
    # Supported list protocol methods:
    color = FBColor()
    len(color)
    print color[0]
    color[0] = 1.0
@endcode

 Slicing is not supported by this object.     
    """
    def FBVector3d(self):
        """
        Constructor.
        Default constructor, all 3 values within are set to 0.0.

        """
        pass

    def FBVector3d(self,pVector3d):
        """
        Constructor.
        Copy constructor. Copy values from another instance.

        pVector3d : FBVector3d
        """
        pass

    def FBVector3d(self,pX,pY,pZ):
        """
        Constructor.
        Explicitely construct a vector by specifying its values.

        pX : float
        pY : float
        pZ : float
        """
        pass

    def FBVector3d(self,p0):
        """
        Constructor.
        A vector can be built from any python object with supports the tuple interface and is of a lenght of 3.

        p0 : tuple< float, float, float >
        """
        pass

    def __len__(self):
        """
        Returns the number of elements.
        Corresponds to python: len(object)

        """
        pass

    def __getitem__(self,pIndex):
        """
        Returns the ith component Corresponds to python: print v[1].

        pIndex : Index of the components to get (0 to 2) 
        return : Color component value. 
        """
        pass

    def __setitem__(self,pIndex,pComponentValue):
        """
        Sets the ith components Corresponds to python: v[1] = 0.5.

        pIndex : Index of the components to set (0 to 2) 
        pComponentValue : Value of component to set 
        """
        pass

    pass

class FBIconPosition (object):
    """
    Different icon positions possible.     
        
    """
    kFBIconLeft=property(doc="Icon on left of text.         ")
    kFBIconTop=property(doc="Icon on top of text.         ")
    pass

class FBPropertyListStoryDetails (object):
    """
        
        
    """
    pass

class FBPlotAllowed (object):
    """
    FBPlotAllowed.     
        
    """
    kFBPlotAllowed_None=property(doc="        ")
    kFBPlotAllowed_Skeleton=property(doc="        ")
    kFBPlotAllowed_ControlRig=property(doc="        ")
    kFBPlotAllowed_Both=property(doc="        ")
    pass

class FBObjectStatus (object):
    """
    Available lifetime status for any component.     
        
    """
    kFBStatusNone=property(doc="No special status, default value.         ")
    kFBStatusCreating=property(doc="Object is in creation operations.         ")
    kFBStatusStoring=property(doc="Object is in storing operations.         ")
    kFBStatusRetrieving=property(doc="Object is in retrieving operations.         ")
    kFBStatusMerging=property(doc="Object is in Merging operations.         ")
    kFBStatusDestroying=property(doc="Object is in destruction operations.         ")
    kFBStatusOwnedByUndo=property(doc="Object is owned by undo framework.         ")
    pass

class FBPathTangeantMode (object):
    """
    Tangeant modes available for path keys.     
        
    """
    kFBPathTangeantInvalid=property(doc="Invalid tangeant.         ")
    kFBPathTangeantLinear=property(doc="Linear tangeant.         ")
    kFBPathTangeantCubic=property(doc="Cubic tangeant.         ")
    kFBPathTangeantAuto=property(doc="Automatic-cubic tangeant.         ")
    kFBPathTangeantUser=property(doc="User-cubic tangeant.         ")
    pass

class FBRSType (object):
    """
    RS type for serial port.     
        
    """
    kFBRS232=property(doc="RS-232 serial protocol.         ")
    kFBRS422=property(doc="RS-422 serial protocol.         ")
    pass

class FBFilterManager (object):
    """
    Filter manager.     
    This class provides list of all available filter types and a factory method in order to create an instance of the desired filter type.This manager will list both built-in and plug-in filters.See the class FBFilter for more details.Filter type names are not localised, and are the same as presented in the GUI.The following sample code shows how to use C++ or Python to create an instance of the orfilter_template filter and set one of its property. For the sample code to work, the plugin must have been compiled and copied in the plugins folder prior to the application startup.Sample C++ code: 
@code
    // Create a filter of a known type. In this case the sample filter
    // provided with the samples: orfilter_template.

    FBFilterManager lFilterManager;

    HFBFilter lFilter = lFilterManager.CreateFilter( 'OR - Filter Template' );

    // Set one of the filter property:
    FBPropertyDouble* lPropDouble = (FBPropertyDouble*)lFilter->PropertyList.Find( 'Test Double' );
    if( lPropDouble )
    {
        (*lPropDouble) = 2.0;
    }

    // Now we can apply the filter on an FCurve.
    // ...

    // And when we are done, destroy it.
    lFilter->FBDelete();
    lFilter = NULL;
@endcode

Sample Python code: 
@code
    from pyfbsdk import *

    # Create a filter of a known type. In this case the sample filter
    # provided with the samples: orfilter_template.

    lFilterManager = FBFilterManager()

    lFilter = lFilterManager.CreateFilter( 'OR - Filter Template' );

    # Set one of the filter property:
    lPropDouble = lFilter.PropertyList.Find( 'Test Double' );
    if lPropDouble: lPropDouble.Data = 2.0

    # Now we can apply the filter on an FCurve.
    # ...

    # And when we are done, destroy it.
    lFilter.FBDelete()
@endcode

     
    """
    def FBFilterManager(self):
        """
        Constructor.

        """
        pass

    def CreateFilter(self,pFilterTypeName):
        """
        Create a filter instance according to the filter type requested.

        pFilterTypeName : String describing the type of the desired filter, as obtained from list FilterTypeNames. 
        return : A pointer to a filter instance, or a NULL if the type name was invalid. 
        """
        pass

    FilterTypeNames=property(doc="List of available filters.         ")
    pass

class FBManipulatorTransformType (object):
    """
    Manipulator transform stles.     
        
    """
    kFBManipulatorTransformNone=property(doc="No manipulator.         ")
    kFBManipulatorTransformTranslation=property(doc="Translation manipulator.         ")
    kFBManipulatorTransformRotation=property(doc="Rotation manipulator.         ")
    kFBManipulatorTransformScaling=property(doc="Scaling manipulator.         ")
    pass

class FBCameraResolutionMode (object):
    """
    Resolution modes.     
        
    """
    kFBResolutionCustom=property(doc="Custom resolution mode or From Camera as a render setting.         ")
    kFBResolutionD1NTSC=property(doc="D1 NTSC.         ")
    kFBResolutionNTSC=property(doc="NTSC.         ")
    kFBResolutionPAL=property(doc="PAL.         ")
    kFBResolutionD1PAL=property(doc="D1 PAL.         ")
    kFBResolutionHD=property(doc="HD 1920x1080.         ")
    kFBResolution640x480=property(doc="640x480.         ")
    kFBResolution320x200=property(doc="320x200.         ")
    kFBResolution320x240=property(doc="320x240.         ")
    kFBResolution128x128=property(doc="128x128.         ")
    kFBResolutionFullScreen=property(doc="FullScreen.         ")
    pass

class FBGeometryUVMappingMode (object):
    """
    Different type of UV mapping possible.     
        
    """
    kFBUVMappingModeNone=property(doc="No mapping.         ")
    kFBUVMappingModeVertex=property(doc="Vertex mapping.         ")
    kFBUVMappingModeSurface=property(doc="Surface mapping.         ")
    kFBUVMappingModeRaw=property(doc="Raw mapping.         ")
    pass

class FBCommandState (object):
    """
    FBCommandState.     
        
    """
    kFBCommandStateStandard=property(doc="Standard.         ")
    kFBCommandStateMute=property(doc="Mute.         ")
    kFBCommandStateSolo=property(doc="Solo.         ")
    kFBCommandStateMuteBecauseSolo=property(doc="Mute because of solo.         ")
    kFBCommandStateHidden=property(doc="Hidden.         ")
    pass

class FBCharacterContactBehaviour (object):
    """
    Character Contact Behaviour.     
        
    """
    kFBParamContactNeverSync=property(doc="        ")
    kFBParamContactSyncOnKey=property(doc="        ")
    kFBParamContactAlwaysSync=property(doc="        ")
    kFBLastContactBehaviour=property(doc="        ")
    pass

class FBViewerMode (object):
    """
    Different viewer modes for the 3D viewer.     
        
    """
    kFBViewerModeOneWindow=property(doc="View one pane.         ")
    kFBViewerModeTwoWindow=property(doc="View two panes.         ")
    kFBViewerModeThreeWindow=property(doc="View three panes.         ")
    kFBViewerModeFourWindow=property(doc="View four panes.         ")
    kFBViewerModeSchematic=property(doc="Schematic view.         ")
    pass

class FBCameraViewPlaneMode (object):
    """
    Camera plane viewing modes.     
        
    """
    kFBViewPlaneDisabled=property(doc="Camera plane disabled.         ")
    kFBViewPlaneAlways=property(doc="Always draw camera plane.         ")
    kFBViewPlaneWhenMedia=property(doc="Camera plane when media.         ")
    pass

class FBVideoStorageMode (object):
    """
    Video storage modes.     
        
    """
    kFBVideoStorageDisk=property(doc="Storage on disk.         ")
    kFBVideoStorageMemory=property(doc="Storage in memory.         ")
    kFBVideoStorageFreeRunning=property(doc="Free running (always playing).         ")
    pass

class FBPropertyListBox (object):
    """
        
        
    """
    pass

class FBVideoRenderFieldMode (object):
    """
    Enum FBVideoRenderFieldMode.     
        
    """
    FBFieldModeNoField=property(doc="No Field.         ")
    FBFieldModeField0=property(doc="Field 0.         ")
    FBFieldModeField1=property(doc="Field 1.         ")
    FBFieldModeHalfField0=property(doc="Half Field 0.         ")
    FBFieldModeHalfField1=property(doc="Half Field 1.         ")
    FBFieldModeCount=property(doc="Count.         ")
    pass

class FBInputModifier (object):
    """
    Input Modifiers (Ctrl, Alt, Shift).     
        
    """
    kFBKeyNone=property(doc="No modifier.         ")
    kFBKeyShift=property(doc="Shift was pressed.         ")
    kFBKeyCtrl=property(doc="Control was pressed.         ")
    kFBKeyAlt=property(doc="Alt was pressed.         ")
    pass

class FBGeometryArrayID (object):
    """
    ID to use when requesting a specific array of data for a model.     
        
    """
    kFBGeometryArrayID_Point=property(doc="ID to the Point array.         ")
    kFBGeometryArrayID_NormalByPoint=property(doc="ID to the Normal by Point array.         ")
    kFBGeometryArrayID_Tangent=property(doc="ID to the Tangent array.         ")
    kFBGeometryArrayID_Binormal=property(doc="ID to the Binormal array.         ")
    pass

class FBObjectFlag (object):
    """
    Available flags for any component.     
        
    """
    kFBFlagSelectable=property(doc="Can be selected.         ")
    kFBFlagDeletable=property(doc="Can be deleted.         ")
    kFBFlagSavable=property(doc="Can be saved.         ")
    kFBFlagVisible=property(doc="Can be visible.         ")
    kFBFlagClonable=property(doc="Can be cloned.         ")
    kFBFlagSystem=property(doc="Created from System (not from user).         ")
    kFBFlagNewable=property(doc="Deleted on File->New.         ")
    kFBFlagRenamable=property(doc="Can be renamed.         ")
    kFBFlagMergeable=property(doc="Can be merged.         ")
    kFBFlagBrowsable=property(doc="Visible in the Scene Navigator/Schematic View/Property View/Model View.         ")
    kFBFlagDetachable=property(doc="Object can be 'detached'. Used by the apply manager contextual menu.         ")
    kFBFlagUndoable=property(doc="Object can undo its actions and states.         ")
    kFBFlagKeyable=property(doc="Object can Key his property. (System Camera can't).         ")
    kFBFlagAllocated=property(doc="Object is allocated, so it must call 'delete this' on destroy.         ")
    kFBFlagStory=property(doc="Object created/used by the Story tool. Useful flag for filtering Story objects.         ")
    kFBFlagStorable6=property(doc="System/Obsolete.         ")
    kFBFlagStorableData6=property(doc="System/Obsolete.         ")
    kFBFlagUniqueName=property(doc="Object unique name can be added to the unique name list (at first, only RootNode have this flag).         ")
    pass

class FBCallback (object):
    """
    This class is used for the internal callback framework and is not meant to be used by clients.     
        
    """
    Wrapper=property(doc="<b>Read Property:</b> Pyfbsdk Wrapper that is the owner of the callback.         ")
    EventType=property(doc="<b>Read Property:</b> Event type to which this callback is connected.         ")
    Callback=property(doc="<b>Read Property:</b> Python callback that will called when the FBCallback is executed.         ")
    pass

class FBEvent (object):
    """
    Base Event class.     
    All events in the Open Reality SDK inherit from this class.     
    """
    def FBEvent(self,pEvent):
        """
        Constructor.
        Receives an object of type HKEvent that the corresponding callback will receive as a parameter.

        pEvent : Internal event to obtain information from. 
        """
        pass

    Type=property(doc="<b>Read Only Property:</b> Type of event.         ")
    pass

class FBCameraFrameSizeMode (object):
    """
    Frame size modes.     
        
    """
    kFBFrameSizeWindow=property(doc="Frame size of window.         ")
    kFBFrameSizeFixedRatio=property(doc="Fixed ratio.         ")
    kFBFrameSizeFixedResolution=property(doc="Fixed resolution.         ")
    kFBFrameSizeFixedWidthResolution=property(doc="Fixed width resolution.         ")
    kFBFrameSizeFixedHeightResolution=property(doc="Fixed height resolution.         ")
    pass

class FBDragAndDropState (object):
    """
    State of Drag and Drop.     
        
    """
    kFBDragAndDropBegin=property(doc="Begin a drag and drop sequence.         ")
    kFBDragAndDropDrag=property(doc="Dragging.         ")
    kFBDragAndDropDrop=property(doc="Dropping.         ")
    kFBDragAndDropEnd=property(doc="End of drag and drop.         ")
    kFBDragOnEmpty=property(doc="Empty the drag and drop stack.         ")
    kFBDragOnEmptyDrop=property(doc="Dropping empty stack.         ")
    pass

class FBObjectPoseOptions (object):
    """
    FBObjectPoseOptions class.     
    This class exposes the object used to store the options for operations on object poses.     
    """
    def FBObjectPoseOptions(self):
        """
        Constructor.

        """
        pass

    def ClearFlag(self):
        """
        Clear all flags.

        """
        pass

    def GetFlag(self,pFlag):
        """
        Get a flag value.

        pFlag : Flag to get. 
        return : Value of the flag. 
        """
        pass

    def SetFlag(self,pFlag,pValue):
        """
        Set a flag value.

        pFlag : Flag to set. 
        pValue : Value to set. 
        """
        pass

    mPoseTransformType=property(doc="Transform type (Local, Global or LocalRef).         ")
    mReferenceGRM=property(doc="Global rotation matrix of reference object.         ")
    mReferenceGSM=property(doc="Global scaling matrix of reference object.         ")
    mReferenceGT=property(doc="Global translation vector of reference object.         ")
    pass

class FBMultiLangManager (object):
    """
    Language manager.     
    The class FBMultiLangManager indicates the supported languages and allows to query and change the current language.The support for localization is done using conversion tables from internal names to language specific names, so that they can be used in the GUI and other human readable contexts.At this time, changing the current language will not affect the GUI. Only calls to functions 'FBGetMultiLangText()' will be affected.The following sample code lists the names of the supported languages:Python sample code: 
@code
    from pyfbsdk import *

    lManager = FBMultiLangManager()
    print 'Current localization language: ', lManager.GetCurrentLanguage()
    print 'Supported languages:'
    for lLanguage in lManager.Languages:
        print '  ', lLanguage
@endcode

C++ sample code: 
@code
    FBMultiLangManager lManager;
    FBTrace( 'Current localization language: %s\n', lManager.GetCurrentLanguage());
    FBTrace( 'Supported languages:\n' );

    int lIdx = 0;
    while( lIdx < lManager.Languages.GetCount())
    {
        FBTrace( '  %s\n', lManager.Languages[lIdx++] );
    }
@endcode

     
    """
    def FBMultiLangManager(self):
        """
        Constructor.

        """
        pass

    def GetCurrentLanguage(self):
        """
        Obtain the current language.
        Query the current language used for the GUI.

        return : Will return the string associated with the current language used. 
        """
        pass

    def SetCurrentLanguage(self,pLanguage):
        """
        Set the current language.
        Change the current language to another available language.

        pLanguage : The string corresponding to the desired language, as defined in property Languages. 
        return : Indicate if the change of language was successful. 
        """
        pass

    Languages=property(doc="List of available languages.         ")
    pass

class FBModelTemplateStyle (object):
    """
    Model template styles When creating model templates, this parameter will affect the actual model created (associated with the model template).     
        
    """
    kFBModelTemplateNone=property(doc="No style.         ")
    kFBModelTemplateNull=property(doc="Null.         ")
    kFBModelTemplateMarker=property(doc="Marker.         ")
    kFBModelTemplateRoot=property(doc="Root (3 axes).         ")
    kFBModelTemplateSensor=property(doc="Yellow magnetic sensor.         ")
    kFBModelTemplateSkeleton=property(doc="Skeleton limb.         ")
    kFBModelTemplateCamera=property(doc="Camera.         ")
    kFBModelTemplateGeometry=property(doc="Generic geometry.         ")
    kFBModelTemplateCameraInterest=property(doc="Camera interest.         ")
    kFBModelTemplateLight=property(doc="Light.         ")
    kFBModelTemplateOptical=property(doc="Optical model (not supported yet).         ")
    pass

class FBTangentMode (object):
    """
    Methods of tangent calculation.     
    This is only relevant when interpolation is CUBIC.     
    """
    kFBTangentModeAuto=property(doc="This is the equivalent to a cardinal spline with no parametrization.         ")
    kFBTangentModeTCB=property(doc="TCB spline (3 parameters: TENSION, CONTINUITY, BIAS).         ")
    kFBTangentModeUser=property(doc="Used to represent all splines with no lost data (HERMITE, BEZIER, CATMUL, etc.).         ")
    kFBTangentModeBreak=property(doc="Like USER but left slope may differ from right.         ")
    pass

class FBGeometryArrayElementType (object):
    """
    Type of data when requesting an array.     
        
    """
    kFBGeometryArrayElementType_Float3=property(doc="Each element is an array of 3 float.         ")
    kFBGeometryArrayElementType_Float4=property(doc="Each element is an array of 4 float.         ")
    pass

class FBBatchFileFormat (object):
    """
    Different file formats for the batch.     
        
    """
    kFBBatchFileFormatTRC=property(doc="File format for Motion Analysis TRC.         ")
    kFBBatchFileFormatC3D=property(doc="File format for Vicon C3D.         ")
    kFBBatchFileFormatAMC=property(doc="File format for Acclaim AMC.         ")
    kFBBatchFileFormatBVH=property(doc="File format for Biovision BVH.         ")
    kFBBatchFileFormatHTR=property(doc="File format for Motion Analysis HTR.         ")
    kFBBatchFileFormatFBX=property(doc="File format for FBX (animation only).         ")
    pass

class FBImageInterleaveType (object):
    """
    Image field interleave types.     
        
    """
    kFBImageInterleaveTypeFullFrame=property(doc="        ")
    kFBImageInterleaveTypeOdd=property(doc="        ")
    kFBImageInterleaveTypeEven=property(doc="        ")
    kFBImageInterleaveTypeAverage=property(doc="        ")
    pass

class FBTextureMapping (object):
    """
    Texture mapping modes.     
    How the texture is mapped.     
    """
    kFBTextureMappingUV=property(doc="UV mapping.         ")
    kFBTextureMappingXY=property(doc="XY mapping.         ")
    kFBTextureMappingYZ=property(doc="YZ mapping.         ")
    kFBTextureMappingXZ=property(doc="XZ mapping.         ")
    kFBTextureMappingSpherical=property(doc="Spherical mapping.         ")
    kFBTextureMappingCylindrical=property(doc="Cylindrical mapping.         ")
    kFBTextureMappingEnvironment=property(doc="Environment mapping.         ")
    kFBTextureMappingProjection=property(doc="Projection mapping.         ")
    pass

class FBPropertyType (object):
    """
    Property types.     
        
    """
    kFBPT_unknown=property(doc="unknow.         ")
    kFBPT_int=property(doc="int.         ")
    kFBPT_bool=property(doc="bool.         ")
    kFBPT_float=property(doc="float.         ")
    kFBPT_double=property(doc="double.         ")
    kFBPT_charptr=property(doc="charptr.         ")
    kFBPT_enum=property(doc="enum.         ")
    kFBPT_Time=property(doc="time.         ")
    kFBPT_object=property(doc="object.         ")
    kFBPT_event=property(doc="event.         ")
    kFBPT_stringlist=property(doc="stringlist.         ")
    kFBPT_Vector4D=property(doc="vector4d.         ")
    kFBPT_Vector3D=property(doc="vector3d.         ")
    kFBPT_ColorRGB=property(doc="colorrgb.         ")
    kFBPT_ColorRGBA=property(doc="colorrgba.         ")
    kFBPT_Action=property(doc="action.         ")
    kFBPT_Reference=property(doc="reference.         ")
    kFBPT_TimeSpan=property(doc="timespan.         ")
    kFBPT_kReference=property(doc="kReference.         ")
    kFBPT_Vector2D=property(doc="vector2d.         ")
    pass

class FBNamespaceAction (object):
    """
    Namespace flags.     
        
    """
    kFBConcatNamespace=property(doc="Use to add a namespace name to object.         ")
    kFBReplaceNamespace=property(doc="Use to replace a define namespace.         ")
    kFBRemoveAllNamespace=property(doc="Remove all the namespace name.         ")
    pass

class FBColorAndAlpha (object):
    """
    FBColorAndAlpha class.     
    Color and alpha vector.This class creates a list like object, which can be modified using the list protocol method. But unlike lists, its length is fixed: it always contain 4 floating point values. Thus it does not support the any list methods that would affect its length. The values within can be changed, usually via the bracket operator. 
@code
    # Supported list protocol methods:
    color = FBColorAndAlpha()
    len(color)
    print color[0]
    color[0] = 1.0
@endcode

 Slicing is not supported by this object.     
    """
    def FBColorAndAlpha(self):
        """
        Constructor.
        Default constructor, all values within are set to 0.0, except for the Alpha value which is set to 1.0.

        """
        pass

    def FBColorAndAlpha(self,pColor):
        """
        Constructor.
        Copy constructor. Copy values from another instance.

        pColor : FBColor
        """
        pass

    def FBColorAndAlpha(self,pR,pG,pB,pAlpha):
        """
        Constructor.
        Explicitely construct a vector by specifying its RGBA values. Should the Alpha value not be relevant, just set it to 1.0.

        pR : float
        pG : float
        pB : float
        pAlpha : float
        """
        pass

    def FBColorAndAlpha(self,p0):
        """
        Constructor.
        A vector can be built from any python object with supports the tuple interface and is of a lenght of 4.

        p0 : tuple< float, float, float, float >
        """
        pass

    def FBColorAndAlpha(self):
        """
        Constructor.

        """
        pass

    def FBColorAndAlpha(self,pValue):
        """
        Constructor from array.

        pValue : Array to take values from. 
        """
        pass

    def FBColorAndAlpha(self,pRed,pGreen,pBlue,pAlpha):
        """
        Constructor.

        pRed : Red component. 
        pGreen : Green component. 
        pBlue : Blue component. 
        pAlpha : Alpha component(default=1.0). 
        """
        pass

    def FBColorAndAlpha(self,pValue):
        """
        Constructor from FBColor.

        pValue : FBColor to take values from. 
        """
        pass

    def FBColorAndAlpha(self,pVector):
        """
        Copy Constructor.

        pVector : FBColorAndAlpha
        """
        pass

    def __len__(self):
        """
        Returns the number of elements.
        Corresponds to python: len(object)

        """
        pass

    def __getitem__(self,pIndex):
        """
        Returns the ith component Corresponds to python: print color[1].

        pIndex : Index of the components to get (0:Red, 1:Green, 2:Blue) 
        return : Color component value. 
        """
        pass

    def __setitem__(self,pIndex,pComponentValue):
        """
        Sets the ith components Corresponds to python: color[1] = 0.5.

        pIndex : Index of the components to set (0:Red, 1:Green, 2:Blue) 
        pComponentValue : Value of component to set 
        """
        pass

    pass

class FBCharacterPoseFlag (object):
    """
    Character Pose Options flags.     
        
    """
    kFBCharacterPoseNoFlag=property(doc="        ")
    kFBCharacterPoseMirror=property(doc="        ")
    kFBCharacterPoseGravity=property(doc="        ")
    kFBCharacterPoseMatchTX=property(doc="        ")
    kFBCharacterPoseMatchTY=property(doc="        ")
    kFBCharacterPoseMatchTZ=property(doc="        ")
    kFBCharacterPoseMatchR=property(doc="        ")
    kFBCharacterPoseMatchPivot=property(doc="        ")
    kFBCharacterPoseUseKeyingGroup=property(doc="        ")
    pass

class FBBatchOnContainsBatchTakes (object):
    """
    Different actions to perform when a scene already contains batch takes while in a batch process.     
        
    """
    kFBBatchOnContainsBatchTakesSaveBatchTakesOnly=property(doc="Save only the batch takes.         ")
    kFBBatchOnContainsBatchTakesSaveAllTakes=property(doc="Save all the takes.         ")
    pass

class FBConstraintInfo (object):
    """
    Constraint information class.     
    This data structure is passed to the real-time evaluation callback for a constraint (AnimationNodeNotify()).     
    """
    def GetSnapRequested(self):
        """
        Was a 'snap' requested?

        return : <b>true</b> if 'snap' was requeststed. 
        """
        pass

    def GetZeroRequested(self):
        """
        Was a 'zero' requested?

        return : <b>true</b> if 'zero' was requeststed. 
        """
        pass

    pass

class FBCommType (object):
    """
    Communications type.     
    Different base types of communications. There is always the 'other' type in order to use another type of communication.     
    """
    kFBCommTypeNone=property(doc="A non-communicating device.         ")
    kFBCommTypeSerial=property(doc="Serial communications.         ")
    kFBCommTypeNetworkTCP=property(doc="Network (TCP) device.         ")
    kFBCommTypeNetworkUDP=property(doc="Network (UDP) device.         ")
    kFBCommTypeSharedMemory=property(doc="Accessing shared memory.         ")
    kFBCommTypeSimulator=property(doc="Software simulator.         ")
    kFBCommTypeOther=property(doc="Any other type of communications.         ")
    pass

class FBPropertyListTextureId (object):
    """
        
        
    """
    pass

class FBCharacterRollSolver (object):
    """
    Character Roll Solver version.     
        
    """
    kFBParamRollSolver70=property(doc="        ")
    kFBParamRollSolver75=property(doc="        ")
    kFBLastRollSolver=property(doc="        ")
    pass

class FBCharacterPoseOptions (object):
    """
    FBCharacterPoseOptions class.     
    This class exposes the object used to store the options for operations on object poses. Before using a FBCharacterPoseOptions, you need to specify the various members of the object. Here are the default values of a FBCharacterPoseOptions object: mCharacterPoseKeyingMode = kFBCharacterPoseKeyingModeFullBody mModelToMatch = NULL mMirrorPlaneType = kFBMirrorPlaneTypeAuto mMirrorPlaneEquation = 1.0, 0.0, 0.0, 0.0 mMirrorPlaneTiltAngle = 90.0 mMirrorPlanePanAngle = 0.0 Flag = kFBCharacterPoseNoFlag You need to change at least the Flag value by using SetFlag() to set how the pose will be paste; see the FBCharacterPoseFlag enum for the various options.     
    """
    def FBCharacterPoseOptions(self):
        """
        Constructor.

        """
        pass

    def ClearFlag(self):
        """
        Clear all flags.

        """
        pass

    def GetFlag(self,pFlag):
        """
        Get a flag value.

        pFlag : Flag to get. 
        return : Value of the flag. 
        """
        pass

    def SetFlag(self,pFlag,pValue):
        """
        Set a flag value.

        pFlag : Flag to set. 
        pValue : Value to set. 
        """
        pass

    mCharacterPoseKeyingMode=property(doc="CharacterPoseKeyingMode (FullBody or BodyPart).         ")
    mMirrorPlaneEquation=property(doc="Mirror plane equation (used when mMirrorPlaneType = kFBMirrorPlaneTypeEquation).         ")
    mMirrorPlanePanAngle=property(doc="Mirror plane pan angle in degrees (used when mMirrorPlaneType = kFBMirrorPlaneTypeUser).         ")
    mMirrorPlaneTiltAngle=property(doc="Mirror plane tilt angle in degrees (used when mMirrorPlaneType = kFBMirrorPlaneTypeUser).         ")
    mMirrorPlaneType=property(doc="Mirror plane type.         ")
    mModelToMatch=property(doc="Model to match.         ")
    pass

class FBVideoFormat (object):
    """
    Video color modes.     
        
    """
    kFBVideoFormat_Any=property(doc="        ")
    kFBVideoFormat_Other=property(doc="        ")
    kFBVideoFormat_RGBA_32=property(doc="        ")
    kFBVideoFormat_RGB_24=property(doc="        ")
    kFBVideoFormat_BGRA_32=property(doc="        ")
    kFBVideoFormat_BGR_24=property(doc="        ")
    kFBVideoFormat_BGR_16=property(doc="        ")
    kFBVideoFormat_ABGR_32=property(doc="        ")
    kFBVideoFormat_ARGB_32=property(doc="        ")
    kFBVideoFormat_422=property(doc="        ")
    pass

class FBInterpolatorCurveType (object):
    """
    Types of interpolator for an FCurve.     
        
    """
    kFBInterpolatorCurveLinearIn=property(doc="        ")
    kFBInterpolatorCurveLinearOut=property(doc="        ")
    kFBInterpolatorCurveSmoothIn=property(doc="        ")
    kFBInterpolatorCurveSmoothOut=property(doc="        ")
    kFBInterpolatorCurveSlowIn=property(doc="        ")
    kFBInterpolatorCurveSlowOut=property(doc="        ")
    kFBInterpolatorCurveFastIn=property(doc="        ")
    kFBInterpolatorCurveFastOut=property(doc="        ")
    kFBInterpolatorCurveLast=property(doc="        ")
    pass

class FBSceneChangeType (object):
    """
    Types of model selection events.     
        
    """
    kFBSceneChangeNone=property(doc="Unknown event.         ")
    kFBSceneChangeDestroy=property(doc="Object destroyed.         ")
    kFBSceneChangeAttach=property(doc="Object attached.         ")
    kFBSceneChangeDetach=property(doc="Object detached.         ")
    kFBSceneChangeAddChild=property(doc="Child added.         ")
    kFBSceneChangeRemoveChild=property(doc="Child removed.         ")
    kFBSceneChangeSelect=property(doc="Object selection.         ")
    kFBSceneChangeUnselect=property(doc="Object deselection.         ")
    kFBSceneChangeRename=property(doc="Before object rename.         ")
    kFBSceneChangeRenamePrefix=property(doc="Before object rename prefix.         ")
    kFBSceneChangeRenameUnique=property(doc="Before object rename unique.         ")
    kFBSceneChangeRenameUniquePrefix=property(doc="Before object rename unique prefix.         ")
    kFBSceneChangeRenamed=property(doc="After object rename.         ")
    kFBSceneChangeRenamedPrefix=property(doc="After object rename prefix.         ")
    kFBSceneChangeRenamedUnique=property(doc="After object rename unique.         ")
    kFBSceneChangeRenamedUniquePrefix=property(doc="After object rename unique prefix.         ")
    kFBSceneChangeSoftSelect=property(doc="Soft selection.         ")
    kFBSceneChangeSoftUnselect=property(doc="Soft deselection.         ")
    kFBSceneChangeHardSelect=property(doc="Hard selection.         ")
    kFBSceneChangeActivate=property(doc="Activate.         ")
    kFBSceneChangeDeactivate=property(doc="Deactivate.         ")
    kFBSceneChangeLoadBegin=property(doc="Begin loading file.         ")
    kFBSceneChangeLoadEnd=property(doc="End loading file.         ")
    kFBSceneChangeClearBegin=property(doc="Begin clearing file (file new).         ")
    kFBSceneChangeClearEnd=property(doc="End clearing file (file new).         ")
    kFBSceneChangeTransactionBegin=property(doc="Begin transaction.         ")
    kFBSceneChangeTransactionEnd=property(doc="End transaction.         ")
    kFBSceneChangeReSelect=property(doc="Re-selection.         ")
    kFBSceneChangeChangeName=property(doc="Object change name.         ")
    kFBSceneChangeChangedName=property(doc="Object changed name.         ")
    kFBSceneChangePreParent=property(doc="Before object parenting.         ")
    kFBSceneChangePreUnparent=property(doc="Before object unparenting.         ")
    kFBSceneChangeFocus=property(doc="Object have focus.         ")
    kFBSceneChangeChangedParent=property(doc="Object changed parent.         ")
    kFBSceneChangeReorder=property(doc="Object reorder.         ")
    kFBSceneChangeReordered=property(doc="Object reordered.         ")
    pass

class FBZSortMode (object):
    """
    Z sorting Mode.     
        
    """
    kFBZSortNone=property(doc="None.         ")
    kFBZSortFirstLayer=property(doc="First Layer.         ")
    kFBZSortFirstLayerFastBufferRegion=property(doc="Fisrt Layer Fast Buffer Region.         ")
    kFBZSortConvexGeometry=property(doc="Convex Geometry.         ")
    kFBZSortConvexGeometryFastBufferRegion=property(doc="Convex Geometry Fast Buffer Region.         ")
    kFBZSortFrontToBack=property(doc="Front to Back.         ")
    kFBZSortBackToFront=property(doc="Back to Front.         ")
    kFBZSortCount=property(doc="Count.         ")
    pass

class FBRenderOptions (object):
    """
        
        
    """
    def FBRenderOptions(self,pOptions):
        """
        pOptions : HKRenderOptions
        """
        pass

    def GetRenderFrameId(self):
        """
        Get Render Frame ID.

        return : This return a new ID each time a new frame is drawn. 
        """
        pass

    pass

class FBShadowType (object):
    """
    Shadow types.     
    The different types of shadow mapping.     
    """
    kFBShadowTypeShadowPlanar=property(doc="Use this shadow type to create darkened shadow areas only on planar surfaces.         ")
    kFBShadowTypeShadowProjectiveTexture=property(doc="Uses a texture projection to create a shadow.         ")
    kFBShadowTypeLightMapProjectiveTexture=property(doc="Uses a texture projection as a shadow.         ")
    kFBShadowTypeZShadowProjectiveTexture=property(doc="Similar to the Projective Shadow, except that it uses a boolean algorithm to create a self-shadow.         ")
    kFBShadowTypeZLightMapProjectiveTexture=property(doc="Similar to the Projective Light Map except that it uses a boolean algorithm to create a self-shadow.         ")
    pass

class FBPropertyListModel (object):
    """
        
        
    """
    pass

class FBImageInterpolationType (object):
    """
    Image interpolation types.     
        
    """
    kFBImageInterpolationTypeNone=property(doc="        ")
    kFBImageInterpolationTypeDuplicate=property(doc="        ")
    kFBImageInterpolationTypeLinear=property(doc="        ")
    pass

class FBModelTransformationMatrix (object):
    """
    Types of transformation vector/matrices possible.     
        
    """
    kModelTransformation=property(doc="Transformation.         ")
    kModelRotation=property(doc="Rotation.         ")
    kModelTranslation=property(doc="Translation.         ")
    kModelScaling=property(doc="Scaling.         ")
    kModelInverse_Transformation=property(doc="Inverse transformation.         ")
    kModelInverse_Rotation=property(doc="Inverse rotation.         ")
    kModelInverse_Translation=property(doc="Inverse translation.         ")
    kModelInverse_Scaling=property(doc="Inverse scaling.         ")
    kModelCenter=property(doc="Center.         ")
    kModelAll=property(doc="        ")
    pass

class FBGenerationMode (object):
    """
    Generation modes for optical model.     
        
    """
    kFBGenerationNone=property(doc="No re-generation.         ")
    kFBGenerationFast=property(doc="Fast re-generation.         ")
    pass

class FBTakeChangeType (object):
    """
    Types of take change events.     
        
    """
    kFBTakeChangeAdded=property(doc="        ")
    kFBTakeChangeRemoved=property(doc="        ")
    kFBTakeChangeOpened=property(doc="        ")
    kFBTakeChangeClosed=property(doc="        ")
    kFBTakeChangeRenamed=property(doc="        ")
    kFBTakeChangeUpdated=property(doc="        ")
    kFBTakeChangeMoved=property(doc="        ")
    kFBTakeChangeNone=property(doc="        ")
    pass

class FBMenuItemType (object):
    """
    Types of menu items available.     
        
    """
    kFBMenuItemMotionImport=property(doc="Motion Files->Import.         ")
    kFBMenuItemSceneImport=property(doc="Scenes->Import.         ")
    kFBMenuItemMotionExport=property(doc="Motion Files->Export.         ")
    kFBMenuItemSceneExport=property(doc="Scenes->Export.         ")
    pass

class FBVector2d (object):
    """
    Vector2d class.     
    This class creates a list like object, which can be modified using the list protocol method. But unlike lists, its length is fixed: it always contain 2 floating point values. Thus it does not support the any list methods that would affect its length. The values within can be changed, usually via the bracket operator.
@code
    # Supported list protocol methods:
    color = FBColor()
    len(color)
    print color[0]
    color[0] = 1.0
@endcode

 Slicing is not supported by this object.     
    """
    def FBVector2d(self):
        """
        Constructor.
        Default constructor, both values within are set to 0.0.

        """
        pass

    def FBVector2d(self,pVector2d):
        """
        Constructor.
        Copy constructor. Copy values from another instance.

        pVector2d : FBVector2d
        """
        pass

    def FBVector2d(self,pX,pY):
        """
        Constructor.
        Explicitely construct a vector by specifying its values.

        pX : float
        pY : float
        """
        pass

    def FBVector2d(self,p0):
        """
        Constructor.
        A vector can be built from any python object with supports the tuple interface and is of a lenght of 2.

        p0 : tuple< float, float >
        """
        pass

    def __len__(self):
        """
        Returns the number of elements.
        Corresponds to python: len(object)

        """
        pass

    def __getitem__(self,pIndex):
        """
        Returns the ith component Corresponds to python: print v[1].

        pIndex : Index of the components to get (0 to 1) 
        return : Color component value. 
        """
        pass

    def __setitem__(self,pIndex,pComponentValue):
        """
        Sets the ith components Corresponds to python: v[1] = 0.5.

        pIndex : Index of the components to set (0 to 1) 
        pComponentValue : Value of component to set 
        """
        pass

    pass

class FBBatchStatus (object):
    """
    Different return values of the Batch process.     
        
    """
    kFBBatchStatusSuccess=property(doc="        ")
    kFBBatchStatusError=property(doc="        ")
    kFBBatchStatusCharacterNotSpecified=property(doc="        ")
    kFBBatchStatusCharacterNotCharacterized=property(doc="        ")
    kFBBatchStatusCharacterHasNoReference=property(doc="        ")
    kFBBatchStatusInputActorNotSpecified=property(doc="        ")
    kFBBatchStatusActorInputMarkersetNotSpecified=property(doc="        ")
    kFBBatchStatusActorInputMarkersetHasNoReferenceModel=property(doc="        ")
    kFBBatchStatusActorInputMarkersetNotCorrectlyAssociated=property(doc="        ")
    kFBBatchStatusInputCharacterNotCharacterized=property(doc="        ")
    kFBBatchStatusInputCharacterHasNoReference=property(doc="        ")
    kFBBatchStatusInputDirectoryNotValid=property(doc="        ")
    kFBBatchStatusAsfSkeletonFileNotSpecified=property(doc="        ")
    kFBBatchStatusCantOpenAsfSkeletonFile=property(doc="        ")
    kFBBatchStatusOutputDirectoryNotValid=property(doc="        ")
    pass

class FBBodyPartId (object):
    """
    Body part for character.     
        
    """
    kFBCtrlSetPartNone=property(doc="No part selected.         ")
    kFBCtrlSetPartHips=property(doc="Hips Body Part.         ")
    kFBCtrlSetPartChest=property(doc="Chest Body Part.         ")
    kFBCtrlSetPartLeftArm=property(doc="Left Arm Body Part.         ")
    kFBCtrlSetPartRightArm=property(doc="Right Arm Body Part.         ")
    kFBCtrlSetPartLeftLeg=property(doc="Left Leg Body Part.         ")
    kFBCtrlSetPartRightLeg=property(doc="Right Leg Body Part.         ")
    kFBCtrlSetPartHead=property(doc="Head Body Part.         ")
    kFBCtrlSetPartLeftHand=property(doc="Left Hand Body Part.         ")
    kFBCtrlSetPartRightHand=property(doc="Right Hand Body Part.         ")
    kFBCtrlSetPartLeftFoot=property(doc="Left Foot Body Part.         ")
    kFBCtrlSetPartRightFoot=property(doc="Right Foot Body Part.         ")
    kFBLastCtrlSetPartIndex=property(doc="Part count.         ")
    pass

class FBTextureUsage (object):
    """
    Texture usage modes.     
    What the texture is used for.     
    """
    kFBTextureUsageAll=property(doc="All types of texture usage.         ")
    kFBTextureUsageColor=property(doc="Color map.         ")
    kFBTextureUsageShadowMap=property(doc="Shadow map.         ")
    kFBTextureUsageLightMap=property(doc="Light map.         ")
    kFBTextureUsageSphericalReflection=property(doc="Spherical reflection map.         ")
    kFBTextureUsageSphereMap=property(doc="Spherical map.         ")
    pass

class FBAttachType (object):
    """
    Types of attachments between UI regions.     
        
    """
    kFBAttachLeft=property(doc="Attach to left [min(x1,x2)].         ")
    kFBAttachRight=property(doc="Attach to right [max(x1,x2)].         ")
    kFBAttachTop=property(doc="Attach to top [min(y1,y2)].         ")
    kFBAttachBottom=property(doc="Attach to bottom [max(y1,y2)].         ")
    kFBAttachWidth=property(doc="Attach to width [abs(x2-x1)].         ")
    kFBAttachHeight=property(doc="Attach to height [abs(y2-y1)].         ")
    kFBAttachCenter=property(doc="Attach to center [center(x1,y1,x2,y2)].         ")
    kFBAttachNone=property(doc="No attachment.         ")
    pass

class FBTextJustify (object):
    """
    Text justification styles.     
        
    """
    kFBTextJustifyLeft=property(doc="Left justify.         ")
    kFBTextJustifyRight=property(doc="Right justify.         ")
    kFBTextJustifyCenter=property(doc="Center alignment.         ")
    pass

class FBShaderManager (object):
    """
    Shader manager.     
    This class provides access to the list of available shaders, both system shaders and user shaders. The list comes in two versions:ShaderTypeNames : which gives the internal names of the shaders,ShaderTypeNamesLocalized : uses the GUI names of the shaders.Both of these lists will have the same number of elements. The strings at position i in the lists refer to the same shader type. In cases where there is no localized version of the shader name, the internal name will be used in ShaderTypeNamesLocalized, thus ensuring consistency between the two lists.It also provides a generic shader creation method that uses the shader type name, internal or localized, to create the new shader instance.The destruction of shaders is achieved by calling the FBDelete method of a shader instance.The list of all the instantiated shaders can be obtained from instances of classes FBSystem or FBScene. Both classes have a Shaders property which lists the existing shader instances.Strings are used instead of enum, define or typedef values to refer to shader types as this proves to be more flexible.The system has a default shader of type 'Lighted'. Do not attempt to destroy it.The use of localized names in shader creation is non portable as it is dependent of the current language used by the application. The name may also change from one version to another. Using the internal name is the only way to ensure portable shader creation.Sample C++ code: 
@code
    // This could be a constant value in the code, coming from a custom
    // registry or simply coming from one of the list ShaderTypeNames
    // or ShaderTypeNamesLocalized.
    char* lDesiredShaderTypeName = 'MyShader';

    // Shader creation.
    HFBShader lShader = NULL;
    FBShaderManager lShaderManager;

    if( lShaderManager.ShaderTypeNames.Find( lDesiredShaderTypeName ) != -1 ||
        lShaderManager.ShaderTypeNamesLocalized.Find( lDesiredShaderTypeName ) != -1 )
    {
        lShader = lShaderManager.CreateShader( lDesiredShaderTypeName );

        // Change its name, as the default name will be the type name.
        if( lShader )
        {
            lShader->Name = 'My new shader';
        }
        else
        {
            // Warn about creation failure on a correctly registered
            // shader type.
        }
    }
    else
    {
        // Warn about an unknown shader type.
    }

    //
    // Do some work with the shader...
    // 

    if( lShader )
    {
        lShader->FBDelete();
    }
@endcode

In the previous code sample, the lookup in the manager list is not necessary, as the call to CreateShader would have failed nonetheless and returned a NULL pointer.Sample Python code: 
@code
    from pyfbsdk import *

    lShaderManager = FBShaderManager()

    # This code will create one instance of each of the
    # available shader type, changing its name to add the
    # 'My ' prefix.
    for lShaderTypeName in lShaderManager.ShaderTypeNames:
        lShader = lShaderManager.CreateShader( lShaderTypeName )
        if lShader:
            lShader.Name = 'My %s' % lShader.Name
            print 'Created new shader '%s'' % lShader.Name
        else:
            print 'Unable to create shader of type '%s'' % lShaderTypeName
@endcode

     
    """
    def FBShaderManager(self):
        """
        Constructor.

        """
        pass

    def CreateShader(self,pShaderTypeName):
        """
        Creates a shader according to the shader type provided.
        This method provides a generic way of creating shaders using the type name, internal or localized. The name of the new shader will be the same as the type name used, subject to changes according to the system's unique name policy.

        pShaderTypeName : Name of the type of shader desired. 
        return : A pointer to the newly created shader object, or a NULL pointer if the type name was not recognised. 
        """
        pass

    ShaderTypeNames=property(doc="List of available shaders.         ")
    ShaderTypeNamesLocalized=property(doc="List of available shaders.         ")
    pass

class FBMirrorPlaneType (object):
    """
    Mirror Plane Type.     
        
    """
    kFBMirrorPlaneTypeInvalid=property(doc="        ")
    kFBMirrorPlaneTypeAuto=property(doc="        ")
    kFBMirrorPlaneTypeZY=property(doc="        ")
    kFBMirrorPlaneTypeXY=property(doc="        ")
    kFBMirrorPlaneTypeXZ=property(doc="        ")
    kFBMirrorPlaneTypeUser=property(doc="        ")
    kFBMirrorPlaneTypeEquation=property(doc="        ")
    kFBMirrorPlaneTypeCount=property(doc="        ")
    pass

class FBStoryTrackRefMode (object):
    """
    References Modes for story animation tracks.     
        
    """
    kFBStoryTrackOverride=property(doc="Override track.         ")
    kFBStoryTrackAdditive=property(doc="Additive track.         ")
    pass

class FBTimeMode (object):
    """
    Different time modes available.     
        
    """
    kFBTimeModeDefault=property(doc="Default Time Mode.         ")
    kFBTimeModeCinema=property(doc="24         ")
    kFBTimeModePAL=property(doc="25         ")
    kFBTimeMode30Frames=property(doc="30         ")
    kFBTimeModeNTSC_Drop=property(doc="29.97002617         ")
    kFBTimeMode50Frames=property(doc="50         ")
    kFBTimeMode60Frames=property(doc="60         ")
    kFBTimeMode100Frames=property(doc="100         ")
    kFBTimeMode120Frames=property(doc="120         ")
    kFBTimeModeFullFrame=property(doc="Full frame.         ")
    kFBTimeModeCinemaND=property(doc="23.976020936 fps         ")
    kFBTimeModeCustom=property(doc="Custom framerate.         ")
    pass

class FBButtonLook (object):
    """
    Button look.     
        
    """
    kFBLookNormal=property(doc="        ")
    kFBLookColorChange=property(doc="        ")
    kFBLookPush=property(doc="        ")
    kFBLookFlat=property(doc="        ")
    kFBLookAlphaBackground=property(doc="        ")
    pass

class FBElementAction (object):
    """
    Enumeration that describe the different actions available on a scene element depending on the current context.     
        
    """
    kFBElementActionSave=property(doc="Save the element (when saving).         ")
    kFBElementActionAppend=property(doc="Append the elements to the current scene elements (when loading or merging).         ")
    kFBElementActionMerge=property(doc="Merge the elements from the file in the current scene (when merging).         ")
    kFBElementActionDiscard=property(doc="Do not consider the element (when loading, merging and saving).         ")
    pass

class FBPopupInputType (object):
    """
    User input types for a popup.     
        
    """
    kFBPopupBool=property(doc="Boolean input.         ")
    kFBPopupChar=property(doc="Character input.         ")
    kFBPopupString=property(doc="String input.         ")
    kFBPopupInt=property(doc="Integer input.         ")
    kFBPopupFloat=property(doc="Float input.         ")
    kFBPopupDouble=property(doc="Double input.         ")
    kFBPopupPassword=property(doc="Password input (String with '*'s).         ")
    pass

class FBPropertyListStoryTrack (object):
    """
        
        
    """
    pass

class FBPropertyListDeviceInstrument (object):
    """
    List of instruments.     
        
    """
    pass

class FBMarkerResolutionLevel (object):
    """
    Resolution of marker mesh sphere and capsule (Quality).     
        
    """
    kFBMarkerLowResolution=property(doc="Lowest resolution.         ")
    kFBMarkerMediumResolution=property(doc="Medium resolution.         ")
    kFBMarkerHighResolution=property(doc="Highest resolution.         ")
    pass

class FBSkeletonState (object):
    """
        
        
    """
    def GetNodeMatrix(self,pSkeletonId,pSkeletonGlobalMatrix):
        """
        Returned global matrix associated to the given Index.

        pSkeletonId : Index of the skeleton Node 
        pSkeletonGlobalMatrix : returned global matrix of the index Given 
        """
        pass

    pass

class FBPoseType (object):
    """
    Types of pose.     
        
    """
    kFBBindPose=property(doc="Bind pose.         ")
    kFBRestPose=property(doc="Rest pose.         ")
    pass

class FBCameraApertureMode (object):
    """
    Aperture modes.     
        
    """
    kFBApertureVertical=property(doc="Vertical aperture varies.         ")
    kFBApertureHorizontal=property(doc="Horizontal aperture varies.         ")
    kFBApertureVertHoriz=property(doc="Vertical and horizontal aperture varies.         ")
    kFBApertureFocalLength=property(doc="Focal Length aperture varies.         ")
    pass

class FBPropertyListFCurveKey (object):
    """
    List of FCurveKey.     
        
    """
    pass

class FBRotationFilter (object):
    """
    Rotation filters.     
        
    """
    kFBRotationFilterNone=property(doc="        ")
    kFBRotationFilterGimbleKiller=property(doc="        ")
    kFBRotationFilterUnroll=property(doc="        ")
    pass

class FBControllerMode (object):
    """
    Controller modes for optical model.     
        
    """
    kFBControllerNone=property(doc="No controller mode.         ")
    kFBControllerLabelling=property(doc="Labelling controller.         ")
    kFBControllerSegment=property(doc="Segment controller.         ")
    kFBControllerRigidBody=property(doc="Rigid body controller.         ")
    pass

class FBFbxManagerLoadAnimationMethod (object):
    """
    This enumeration is used to choose how to load an animation file on a character.     
        
    """
    kFBFbxManagerLoadConnect=property(doc="Only connect the loaded character as an input.         ")
    kFBFbxManagerLoadCopy=property(doc="Copy keys from loaded character to target character.         ")
    kFBFbxManagerLoadRetarget=property(doc="Retarget (copy and correct) keys from loaded character to target character.         ")
    kFBFbxManagerLoadPlotIfSampled=property(doc="If loaded animation seems sampled, plot animation from loaded character to target character; else retarget.         ")
    kFBFbxManagerLoadPlot=property(doc="Plot animation from loaded character to target character.         ")
    pass

class FBCommPortType (object):
    """
    Communication port type.     
        
    """
    kFBPhysical=property(doc="Physical.         ")
    kFBVirtual=property(doc="Virtual.         ")
    kFBInternal=property(doc="Internal.         ")
    pass

class FBTangentClampMode (object):
    """
    Different clamping modes for the tangents.     
        
    """
    kFBTangentClampModeNone=property(doc="The tangent will act normally.         ")
    kFBTangentClampModeClamped=property(doc="The tangent will be flattened when the key is placed at the same value as an adjacent key.         ")
    pass

class FBManipulatorPickType (object):
    """
    Types of manipulator picking.     
        
    """
    FBPickObjects=property(doc="Pick objects.         ")
    FBPickPoints=property(doc="Pick points.         ")
    FBPickSurfaces=property(doc="Pick surfaces.         ")
    pass

class FBPropertyListStoryFolder (object):
    """
        
        
    """
    pass

class FBColor (object):
    """
    FBColor class.     
    Color vector.This class creates a list like object, which can be modified using the list protocol method. But unlike lists, its length is fixed: it always contain 3 floating point values. Thus it does not support the any list methods that would affect its length. The values within can be changed, usually via the bracket operator. 
@code
    # Supported list protocol methods:
    color = FBColor()
    len(color)
    print color[0]
    color[0] = 1.0
@endcode

 Slicing is not supported by this object.     
    """
    def FBColor(self):
        """
        Constructor.
        Default constructor, all values within are set to 0.0, except for the Alpha value which is set to 1.0.

        """
        pass

    def FBColor(self,pColor):
        """
        Constructor.
        Copy constructor. Copy values from another instance.

        pColor : FBColor
        """
        pass

    def FBColor(self,pR,pG,pB):
        """
        Constructor.
        Explicitely construct a vector by specifying its RGBA values. Should the Alpha value not be relevant, just set it to 1.0.

        pR : float
        pG : float
        pB : float
        """
        pass

    def FBColor(self,p0):
        """
        Constructor.
        A vector can be built from any python object with supports the tuple interface and is of a lenght of 3.

        p0 : tuple< float, float, float >
        """
        pass

    def FBColor(self):
        """
        Constructor.

        """
        pass

    def FBColor(self,pValue):
        """
        Constructor from array.

        pValue : Array to take values from. 
        """
        pass

    def FBColor(self,pRed,pGreen,pBlue):
        """
        Constructor.

        pRed : Red component. 
        pGreen : Green component. 
        pBlue : Blue component. 
        """
        pass

    def FBColor(self,pVector):
        """
        Copy Constructor.

        pVector : FBColor
        """
        pass

    def __len__(self):
        """
        Returns the number of elements.
        Corresponds to python: len(object)

        """
        pass

    def __getitem__(self,pIndex):
        """
        Returns the ith component Corresponds to python: print color[1].

        pIndex : Index of the components to get (0:Red, 1:Green, 2:Blue) 
        return : Color component value. 
        """
        pass

    def __setitem__(self,pIndex,pComponentValue):
        """
        Sets the ith components Corresponds to python: color[1] = 0.5.

        pIndex : Index of the components to set (0:Red, 1:Green, 2:Blue) 
        pComponentValue : Value of component to set 
        """
        pass

    pass

class FBAlphaSource (object):
    """
    Shader transparency computation.     
    There are different way to compute transparency, and this lists the supported options.     
    """
    kFBAlphaSourceNoAlpha=property(doc="No transparency.         ")
    kFBAlphaSourceAccurateAlpha=property(doc="Accurate Transparency.         ")
    kFBAlphaSourceTransluscentAlpha=property(doc="Translucent.         ")
    kFBAlphaSourceMatteAlpha=property(doc="Matte.         ")
    kFBAlphaSource2DTransparency=property(doc="2D Transparency.         ")
    kFBAlphaSourceAdditiveAlpha=property(doc="Additive Transparency.         ")
    kFBAlphaSourceTransluscentZSortAlpha=property(doc="Translucent(Models Z Sort).         ")
    pass

class FBConsoleChannelType (object):
    """
    Console channel types.     
        
    """
    kFBConsoleNull=property(doc="Generic type.         ")
    kFBConsoleButton=property(doc="Button.         ")
    kFBConsoleSlider=property(doc="Slider.         ")
    kFBConsoleTransport=property(doc="Transport.         ")
    kFBConsoleEncoder=property(doc="Generic encoder.         ")
    kFBConsoleKey=property(doc="Key.         ")
    kFBConsoleDisplay=property(doc="Display.         ")
    kFBConsoleJoystick=property(doc="Joystick.         ")
    pass

class FBPropertyListMaterialId (object):
    """
        
        
    """
    pass

class FBEffectorId (object):
    """
    All effector nodes.     
        
    """
    kFBInvalidEffectorId=property(doc="        ")
    kFBHipsEffectorId=property(doc="        ")
    kFBLeftAnkleEffectorId=property(doc="        ")
    kFBRightAnkleEffectorId=property(doc="        ")
    kFBLeftWristEffectorId=property(doc="        ")
    kFBRightWristEffectorId=property(doc="        ")
    kFBLeftKneeEffectorId=property(doc="        ")
    kFBRightKneeEffectorId=property(doc="        ")
    kFBLeftElbowEffectorId=property(doc="        ")
    kFBRightElbowEffectorId=property(doc="        ")
    kFBChestOriginEffectorId=property(doc="        ")
    kFBChestEndEffectorId=property(doc="        ")
    kFBLeftFootEffectorId=property(doc="        ")
    kFBRightFootEffectorId=property(doc="        ")
    kFBLeftShoulderEffectorId=property(doc="        ")
    kFBRightShoulderEffectorId=property(doc="        ")
    kFBHeadEffectorId=property(doc="        ")
    kFBLeftHipEffectorId=property(doc="        ")
    kFBRightHipEffectorId=property(doc="        ")
    kFBLeftHandEffectorId=property(doc="        ")
    kFBRightHandEffectorId=property(doc="        ")
    kFBLeftHandThumbEffectorId=property(doc="        ")
    kFBLeftHandIndexEffectorId=property(doc="        ")
    kFBLeftHandMiddleEffectorId=property(doc="        ")
    kFBLeftHandRingEffectorId=property(doc="        ")
    kFBLeftHandPinkyEffectorId=property(doc="        ")
    kFBLeftHandExtraFingerEffectorId=property(doc="        ")
    kFBRightHandThumbEffectorId=property(doc="        ")
    kFBRightHandIndexEffectorId=property(doc="        ")
    kFBRightHandMiddleEffectorId=property(doc="        ")
    kFBRightHandRingEffectorId=property(doc="        ")
    kFBRightHandPinkyEffectorId=property(doc="        ")
    kFBRightHandExtraFingerEffectorId=property(doc="        ")
    kFBLeftFootThumbEffectorId=property(doc="        ")
    kFBLeftFootIndexEffectorId=property(doc="        ")
    kFBLeftFootMiddleEffectorId=property(doc="        ")
    kFBLeftFootRingEffectorId=property(doc="        ")
    kFBLeftFootPinkyEffectorId=property(doc="        ")
    kFBLeftFootExtraFingerEffectorId=property(doc="        ")
    kFBRightFootThumbEffectorId=property(doc="        ")
    kFBRightFootIndexEffectorId=property(doc="        ")
    kFBRightFootMiddleEffectorId=property(doc="        ")
    kFBRightFootRingEffectorId=property(doc="        ")
    kFBRightFootPinkyEffectorId=property(doc="        ")
    kFBRightFootExtraFingerEffectorId=property(doc="        ")
    kFBLastEffectorId=property(doc="        ")
    pass

class FBCharacterPlotWhere (object):
    """
    Where to plot a character.     
        
    """
    kFBCharacterPlotOnControlRig=property(doc="        ")
    kFBCharacterPlotOnSkeleton=property(doc="        ")
    pass

class FBCharacterKeyingMode (object):
    """
    Character keying modes.     
        
    """
    kFBCharacterKeyingFullBody=property(doc="        ")
    kFBCharacterKeyingBodyPart=property(doc="        ")
    kFBCharacterKeyingSelection=property(doc="        ")
    pass

class FBVideoRenderViewingMode (object):
    """
    Enum FBVideoRenderViewingMode.     
        
    """
    FBViewingModeStandard=property(doc="Standard.         ")
    FBViewingModeModelsOnly=property(doc="Model Only.         ")
    FBViewingModeXRay=property(doc="X-Ray.         ")
    FBViewingModeCurrent=property(doc="Current.         ")
    FBViewingModeCount=property(doc="Count.         ")
    pass

class FBObjectPoseOptionsFlag (object):
    """
    ObjectPoseOptions flags.     
        
    """
    kFBObjectPoseOptionsNoFlag=property(doc="        ")
    kFBObjectPoseOptionsTranslationX=property(doc="        ")
    kFBObjectPoseOptionsTranslationY=property(doc="        ")
    kFBObjectPoseOptionsTranslationZ=property(doc="        ")
    kFBObjectPoseOptionsRotation=property(doc="        ")
    kFBObjectPoseOptionsScaling=property(doc="        ")
    pass

class FBVertex (object):
    """
    Vertex class.     
    Similar in use to FBVector4d 
@code
    # Supported list protocol methods:
    v = FBVertex()
    len(v)
    print v[0]
    v[0] = 1.0
@endcode

Slicing is not supported by this object.     
    """
    def FBVertex(self):
        """
        """
        pass

    def FBVertex(self,p0):
        """
        p0 : FBVertex
        """
        pass

    def __len__(self):
        """
        Returns the number of elements.
        Corresponds to python: len(object)

        """
        pass

    def __getitem__(self,pIndex):
        """
        Returns the ith component Corresponds to python: print v[1].

        pIndex : Index of the components to get (0 to 1) 
        return : Color component value. 
        """
        pass

    def __setitem__(self,pIndex,pComponentValue):
        """
        Sets the ith components Corresponds to python: v[1] = 0.5.

        pIndex : Index of the components to set (0 to 1) 
        pComponentValue : Value of component to set 
        """
        pass

    pass

class FBStoryClipCompMode (object):
    """
    Compensation Modes for story character clips.     
        
    """
    kFBStoryClipOff=property(doc="No compensation.         ")
    kFBStoryClipAuto=property(doc="Automatic compensation.         ")
    kFBStoryClipUser=property(doc="User defined compensation.         ")
    pass

class FBPropertyListStoryClip (object):
    """
        
        
    """
    pass

class FBClipEnd (object):
    """
    Clip end actions.     
        
    """
    kFBClipEndEnd=property(doc="On clip end stop clip.         ")
    kFBClipEndLoop=property(doc="On clip end loop clip.         ")
    pass

class FBInterpolation (object):
    """
    Types of interpolation for an FCurve.     
        
    """
    kFBInterpolationConstant=property(doc="Constant interpolation.         ")
    kFBInterpolationLinear=property(doc="Linear interpolation.         ")
    kFBInterpolationCubic=property(doc="Cubic interpolation.         ")
    pass

class FBPropertyListModelTemplate (object):
    """
        
        
    """
    pass

class FBSplitStyle (object):
    """
    Type of split style (sub-division) for layout.     
        
    """
    kFBNoSplit=property(doc="No split.         ")
    kFBHSplit=property(doc="Horizontal split.         ")
    kFBVSplit=property(doc="Vertical split.         ")
    kFBHVSplit=property(doc="Horizontal and Vertical split.         ")
    pass

class FBVideoCodecManager (object):
    """
    Video Codec manager class.     
    Use to set or get codec used and codec params     
    """
    def GetCodecIdList(self,pFileFormatInfo,pCodecList):
        """
        GetCodecIdList.
        Get all codec id available for a given file format.

        pFileFormatInfo : file format description string (AVI, MOV...) 
        pCodecList : Codec list id 
        """
        pass

    def GetDefaultCodec(self,pFileFormatInfo):
        """
        GetDefaultCodec.
        Get the default codec id for a given file format. This is the codec that will be used if codec mode is FBVideoCodecUseDefault

        pFileFormatInfo : file format description string (AVI, MOV...) 
        """
        pass

    def SetDefaultCodec(self,pFileFormatInfo,pCodecId):
        """
        SetDefaultCodec.
        Set the default codec id for a given file format. This is the codec that will be used if codec mode is FBVideoCodecUseDefault

        pFileFormatInfo : file format description string (AVI, MOV...) 
        pCodecId : the codec id to set as default 
        """
        pass

    VideoCodecMode=property(doc="<b>Read Write Property:</b> This decide how the system behaves when ask to render a file (codec dialog, uncompress, use default codec)         ")
    pass

class FBPlayMode (object):
    """
    Play modes.     
        
    """
    kFBPlayModeNoPlay=property(doc="No play (most common).         ")
    kFBPlayModePreviewToEnd=property(doc="Preview clip until end.         ")
    kFBPlayModePlay=property(doc="Play clip.         ")
    kFBPlayModeLoop=property(doc="Loop clip.         ")
    kFBPlayModePlayToEnd=property(doc="Play clip to end.         ")
    pass

class FBVideoGrabOptions (object):
    """
    Video Grabbing Options.     
    Contain options to control how the grabbing process will occur.     
    """
    TimeSpan=property(doc="<b>Read Write Property:</b> Start and stop selection time to grab.         ")
    TimeSteps=property(doc="<b>Read Write Property:</b> Time step length between each grab.         ")
    CameraResolution=property(doc="<b>Read Write Property:</b> Camera Resolution.         ")
    BitsPerPixel=property(doc="<b>Read Write Property:</b> Video grab color depth.         ")
    FieldMode=property(doc="<b>Read Write Property:</b> Video grab field mode.         ")
    ViewingMode=property(doc="<b>Read Write Property:</b> Video grab viewing mode.         ")
    OutputFileName=property(doc="<b>Read Write Property:</b> Grabbing destination file.         ")
    ShowSafeArea=property(doc="<b>Read Write Property:</b> If true, display safe area.         ")
    ShowTimeCode=property(doc="<b>Read Write Property:</b> If true, display time code information.         ")
    ShowCameraLabel=property(doc="<b>Read Write Property:</b> If true, display camera label information.         ")
    AntiAliasing=property(doc="<b>Read Write Property:</b> If true, video frames will be anti-aliased.         ")
    RenderAudio=property(doc="<b>Read Write Property:</b> If true and there's audio in the scene, add audio to the output file.         ")
    AudioRenderFormat=property(doc="<b>PRead Write roperty:</b> Audio render format.         ")
    StillImageCompression=property(doc="<b>Property:</b> Compression ratio for image(jpg) 0-100 where 0=Greatest compression, 100=Least Compression.         ")
    pass

class FBAddRegionParam (object):
    """
    This class provide a placeholder to put values necessary to create a Region with FBLayout.AddRegion.     
    Each region components: X, Y, Width and Height needs its own FBAddRegionParam. ex: x = FBAddRegionParam(0,FBAttachType.kFBAttachLeft,'') y = FBAddRegionParam(0,FBAttachType.kFBAttachTop,'') w = FBAddRegionParam(0,FBAttachType.kFBAttachRight,'') h = FBAddRegionParam(25,FBAttachType.kFBAttachNone,'') mainLyt.AddRegion('main','main', x, y, w, h)     
    """
    def FBAddRegionParam(self,pPos,pType,pRelative,pMult):
        """
        Initialize a region params.

        pPos : Offset in pixel according depending on the use of FBAddRegionParam (X, Y, W or H) 
        pType : Type of Attachment. 
        pRelative : Name of Region to attach relative to. 
        pMult : Multiplier of relative value. 
        """
        pass

    mPos=property(doc="<b>Read Property:</b> Offset in pixel according depending on the use of FBAddRegionParam (X, Y, W or H).         ")
    mType=property(doc="<b>Read Property:</b> Type of Attachment.         ")
    mRelative=property(doc="<b>Read Property:</b> Name of Region to attach relative to.         ")
    mMult=property(doc="<b>Read Property:</b> Multiplier of relative value.         ")
    pass

class FBImageType (object):
    """
    Image types.     
        
    """
    kFBImageTypeFrame=property(doc="        ")
    kFBImageTypeField=property(doc="        ")
    pass

class FBBatchProcessType (object):
    """
    Different process type for the batch.     
        
    """
    kFBBatchProcessTypeLoad=property(doc="Load the files and plot the character with every take.         ")
    kFBBatchProcessTypeSave=property(doc="Save the takes in different files.         ")
    kFBBatchProcessTypeConvert=property(doc="Does the load and save.         ")
    pass

class FBStoryClipShowGhostMode (object):
    """
    Show Ghost Modes for story animation clips.     
        
    """
    kFBStoryClipAlways=property(doc="Always show the ghost.         ")
    kFBStoryClipTimeCursor=property(doc="Show the ghost only on time cursor.         ")
    pass

class FBTransportSnapMode (object):
    """
    Available snap methods for the transport control.     
        
    """
    kFBTransportSnapModeNoSnap=property(doc="No snapping is applied.         ")
    kFBTransportSnapModeSnapOnFrames=property(doc="Snaps to an exact frame when modifying the current time.         ")
    kFBTransportSnapModePlayOnFrames=property(doc="When playing, plays to exact frames.         ")
    kFBTransportSnapModeSnapAndPlayOnFrames=property(doc="Combines both Snap and Play on frames modes.         ")
    pass

class FBVideoInterlaceMode (object):
    """
    Video interlace modes.     
        
    """
    kFBVideoInterlaceNone=property(doc="No interacling.         ")
    kFBVideoInterlaceHalfFrameEven=property(doc="Half frame (even field).         ")
    kFBVideoInterlaceHalfFrameOdd=property(doc="Half frame (odd field).         ")
    kFBVideoInterlaceFullFrameEven=property(doc="Full frame (even field).         ")
    kFBVideoInterlaceFullFrameOdd=property(doc="Full frame (odd field).         ")
    pass

class FBPlotOptions (object):
    """
    Option parameters for plotting.     
        
    """
    def FBPlotOptions(self):
        """
        Constructor.

        """
        pass

    PlotAllTakes=property(doc="<b>Read Write Property:</b> Should we plot all takes?         ")
    PlotOnFrame=property(doc="<b>Read Write Property:</b> Should we plot on frame?         ")
    PlotPeriod=property(doc="<b>Read Write Property:</b> The plot period (1/fps).         ")
    RotationFilterToApply=property(doc="<b>Read Write Property:</b> The rotation filter to apply.         ")
    UseConstantKeyReducer=property(doc="<b>Read Write Property:</b> Should we use a constant key reducer with the filter?         ")
    ConstantKeyReducerKeepOneKey=property(doc="<b>Read Write Property:</b> Should the constant key reducer keep at least one key?         ")
    PlotTranslationOnRootOnly=property(doc="<b>Read Write Property:</b> Should we plot the translation on root only?         ")
    PreciseTimeDiscontinuities=property(doc="<b>Read Write Property:</b> Should we plot the translation on root only?         ")
    pass

class FBSurfaceType (object):
    """
    Surface types.     
        
    """
    kFBSurfaceTypeBezier=property(doc="Bezier surface.         ")
    kFBSurfaceTypeBezierQuadric=property(doc="Bezier Quadric surface.         ")
    kFBSurfaceTypeCardinal=property(doc="Cardinal surface.         ")
    kFBSurfaceTypeBspline=property(doc="BSpline surface.         ")
    kFBSurfaceTypeLinear=property(doc="Linear surface.         ")
    pass

class FBPropertyListComponent (object):
    """
    
@code
   # Supported list protocol methods:    
    len(propertyListComponent)
    component= propertyListComponent[0]
    propertyListComponent[0] = my_component
 
    if my_competent in propertyListComponent:
       print 'it is contained!'

    del propertyListComponent[0]
@endcode

     
        
    """
    def __len__(self):
        """
        Returns the number of elements.
        Corresponds to python: len(object)

        return : number of elements in list. 
        """
        pass

    def __getitem__(self,pIndex):
        """
        Returns the ith component Corresponds to python: print v[1].

        pIndex : Index of the components to get (0 to 2) 
        return : FBComponent component value. 
        """
        pass

    def __setitem__(self,pIndex,pComponentValue):
        """
        Sets the ith components Corresponds to python: v[1] = my_component.

        pIndex : Index of the components to set 
        pComponentValue : a FBComponent to set 
        """
        pass

    def __contains__(self,pComponent):
        """
        Check if a FCComponent is already in PropertyList Corresponds to python: if object in propertyList:.

        pComponent : Component to check for inclusion 
        return : Is the Component contain or not? 
        """
        pass

    def append(self,pComp):
        """
        Append new FBComponent at end of list.

        pComp : to append 
        """
        pass

    def count(self):
        """
        Returns the number of elements.
        Corresponds to python: del propertyList[2]

        return : number of elements in list. 
        """
        pass

    def insert(self,pIndex,pComp):
        """
        Insert a new element in list.

        pIndex : Index where to insert component 
        pComp : Component to append 
        """
        pass

    def remove(self,pIndex):
        """
        Remove an element in list.

        pIndex : Index where to remove element. 
        """
        pass

    def pop(self):
        """
        Remove last element of list.

        return : Returns the element that was removed. 
        """
        pass

    def pop(self,pIndex):
        """
        Remove an element in list.

        pIndex : Index where to remove element. 
        return : Returns the element that was removed. 
        """
        pass

    pass

class FBPropertyListPrimitiveVertexCount (object):
    """
        
        
    """
    pass

class FBVideoProxyMode (object):
    """
    Video proxy modes.     
        
    """
    kFBVideoProxyNone=property(doc="No video proxy.         ")
    kFBVideoProxyOnPlay=property(doc="Video proxy on play.         ")
    kFBVideoProxyAlways=property(doc="Always video proxy.         ")
    pass

class FBCameraType (object):
    """
    Focus distance types.     
        
    """
    kFBCameraTypePerspective=property(doc="Interest as source.         ")
    kFBCameraTypeOrthogonal=property(doc="Specific distance as source.         ")
    pass

class FBTimeSpan (object):
    """
    TimeSpan class.     
        
    """
    def FBTimeSpan(self,pStart,pStop):
        """
        Constructor.

        pStart : Start time(default=0). 
        pStop : Stop time(default=0). 
        """
        pass

    def GetDirection(self):
        """
        Get the direction of the timespan.
        Returns 1 if positive, -1 otherwise.

        return : Direction of timespan. 
        """
        pass

    def GetDuration(self):
        """
        Get the unsigned duration value of a timespan.

        return : <b>Unsigned</b> duration of the timespan. 
        """
        pass

    def GetSignedDuration(self):
        """
        Get the signed duration value of a timespan.

        return : <b>Signed</b> duration of the timespan. 
        """
        pass

    def GetStart(self):
        """
        Get the start/stop time.

        return : Start/Stop time. 
        """
        pass

    def GetStart(self):
        """
        Get the start/stop time.

        return : Start/Stop time. 
        """
        pass

    def GetStop(self):
        """
        Get the start/stop time.

        return : Start/Stop time. 
        """
        pass

    def GetStop(self):
        """
        Get the start/stop time.

        return : Start/Stop time. 
        """
        pass

    def Set(self,pStart,pStop):
        """
        Set the TimeSpan.

        pStart : Start time. 
        pStop : Stop time. 
        """
        pass

    pass

class FBLightType (object):
    """
    Light types.     
        
    """
    kFBLightTypePoint=property(doc="Point light.         ")
    kFBLightTypeInfinite=property(doc="Infinite light (plane).         ")
    kFBLightTypeSpot=property(doc="Spotlight.         ")
    pass

class FBEventName (object):
    """
    These events are used internally by the Python Callback mecanism.     
    These are not meant to be manipulated by a user.     
    """
    kFBEventActivate=property(doc="        ")
    kFBEventShow=property(doc="        ")
    kFBEventDragAndDrop=property(doc="        ")
    kFBEventInput=property(doc="        ")
    kFBEventMenu=property(doc="        ")
    kFBEventTreeSelect=property(doc="        ")
    kFBEventExpose=property(doc="        ")
    kFBEventResize=property(doc="        ")
    kFBEventTransaction=property(doc="        ")
    kFBEventDoubleClick=property(doc="        ")
    kFBEventOnClick=property(doc="        ")
    kFBEventEnter=property(doc="        ")
    kFBEventExit=property(doc="        ")
    kFBEventIdle=property(doc="        ")
    kFBEventChange=property(doc="        ")
    kFBEventCellChange=property(doc="        ")
    kFBEventRowClick=property(doc="        ")
    kFBEventColumnClick=property(doc="        ")
    kFBEventTreeExpanding=property(doc="        ")
    kFBEventTreeExpanded=property(doc="        ")
    kFBEventTreeCollapsing=property(doc="        ")
    kFBEventTreeCollapsed=property(doc="        ")
    kFBEventFileNewCompleted=property(doc="        ")
    kFBEventFileNew=property(doc="        ")
    kFBEventFileOpenCompleted=property(doc="        ")
    kFBEventFileOpen=property(doc="        ")
    kFBEventFileSaveCompleted=property(doc="        ")
    kFBEventFileSave=property(doc="        ")
    kFBEventFileExit=property(doc="        ")
    kFBEventUnbindSDK=property(doc="        ")
    pass

class FBStoryTrackBodyPart (object):
    """
    Body Parts for story track character.     
        
    """
    kFBStoryTrackBodyPartNone=property(doc="        ")
    kFBStoryTrackBodyPartAll=property(doc="        ")
    kFBStoryTrackBodyPartUpperBody=property(doc="        ")
    kFBStoryTrackBodyPartLeftArm=property(doc="        ")
    kFBStoryTrackBodyPartLeftShoulder=property(doc="        ")
    kFBStoryTrackBodyPartLeftHand=property(doc="        ")
    kFBStoryTrackBodyPartRightArm=property(doc="        ")
    kFBStoryTrackBodyPartRightShoulder=property(doc="        ")
    kFBStoryTrackBodyPartRightHand=property(doc="        ")
    kFBStoryTrackBodyPartHead=property(doc="        ")
    kFBStoryTrackBodyPartLowerBody=property(doc="        ")
    kFBStoryTrackBodyPartLeftLeg=property(doc="        ")
    kFBStoryTrackBodyPartLeftFoot=property(doc="        ")
    kFBStoryTrackBodyPartRightLeg=property(doc="        ")
    kFBStoryTrackBodyPartRightFoot=property(doc="        ")
    kFBStoryTrackBodyPartProps=property(doc="        ")
    kFBStoryTrackBodyPartExtensions=property(doc="        ")
    pass

class FBCameraDistanceMode (object):
    """
    Camera plane distance modes.     
        
    """
    kFBDistModeRelativeToInterest=property(doc="Camera plane distance relative to interest.         ")
    kFBDistModeAbsoluteFromCamera=property(doc="Camera plane distance absolute from camera.         ")
    pass

class FBObjectPoseMirrorOptions (object):
    """
    FBObjectPoseMirrorOptions class.     
    This class exposes the object used to store the options for the mirror of an object pose.     
    """
    def FBObjectPoseMirrorOptions(self):
        """
        Constructor.

        """
        pass

    def ClearFlag(self):
        """
        Clear all flags.

        """
        pass

    def GetFlag(self,pFlag):
        """
        Get a flag value.

        pFlag : Flag to get. 
        return : Value of the flag. 
        """
        pass

    def SetFlag(self,pFlag,pValue):
        """
        Set a flag value.

        pFlag : Flag to set. 
        pValue : Value to set. 
        """
        pass

    mMirrorPlaneEquation=property(doc="Equation of the mirror plane.         ")
    pass

class FBListStyle (object):
    """
    List style or direction.     
        
    """
    kFBDropDownList=property(doc="Drop down list.         ")
    kFBVerticalList=property(doc="Vertical list.         ")
    pass

class FBCameraFilmBackType (object):
    """
    Filmback types.     
        
    """
    kFBFilmBackCustom=property(doc="Custom Filmback.         ")
    kFBFilmBack16mmTheatrical=property(doc="16mm Theatrical.         ")
    kFBFilmBackSuper16mm=property(doc="Super16mm.         ")
    kFBFilmBack35mmAcademy=property(doc="35mm Academy.         ")
    kFBFilmBack35mmTVProjection=property(doc="35mm TV Projection.         ")
    kFBFilmBack35mmFullAperture=property(doc="35mm Full Aperture.         ")
    kFBFilmBack35mm185Projection=property(doc="35mm 185 Projection.         ")
    kFBFilmBack35mmAnamorphic=property(doc="35mm Anamorphic.         ")
    kFBFilmBack70mmProjection=property(doc="70mm Projection.         ")
    kFBFilmBackVistaVision=property(doc="Vista Vision.         ")
    kFBFilmBackDynavision=property(doc="Dynavision.         ")
    kFBFilmBackIMAX=property(doc="IMAX.         ")
    pass

class FBSurfaceMode (object):
    """
    Surface modes.     
        
    """
    kFBSurfaceModeRaw=property(doc="Raw data.         ")
    kFBSurfaceModeLowNoNormals=property(doc="Low quality, no normals.         ")
    kFBSurfaceModeLow=property(doc="Low quality.         ")
    kFBSurfaceModeHighNoNormals=property(doc="High quality, no normals.         ")
    kFBSurfaceModeHigh=property(doc="High quality.         ")
    pass

class FBStringList (object):
    """
    String list.     
        
    """
    def FBStringList(self):
        """
        Constructor.

        """
        pass

    def Add(self,S,pRef):
        """
        Add a string to the list.

        S : String to add to list. 
        pRef : Reference to store with string (default = 0) 
        return : Index where item was stored. 
        """
        pass

    def Clear(self):
        """
        Clear the list (remove all the items).

        """
        pass

    def Find(self,pRef):
        """
        Find the index where <b>pRef</b> is stored.

        pRef : Reference to look for. 
        return : Index at which <b>pRef</b> can be found. 
        """
        pass

    def Find(self,S):
        """
        Find the index with the string <b>S</b>.

        S : String to search for. 
        return : Index where <b>S</b> is stored. 
        """
        pass

    def GetAt(self,pIndex):
        """
        Get the string at <b>pIndex</b>.

        pIndex : Index to get string at. 
        return : String at <b>pIndex</b>. 
        """
        pass

    def GetReferenceAt(self,pIndex):
        """
        Get the reference store with the string at <b>pIndex</b>.

        pIndex : Index to get reference at. 
        return : Reference stored with value at <b>pIndex</b>. 
        """
        pass

    def IndexOf(self,S):
        """
        Get the index of a string.

        S : String to look for. 
        return : Index where string <b>S</b> was found. 
        """
        pass

    def InsertAt(self,pIndex,S,pRef):
        """
        Insert an entry at <b>pIndex</b>.

        pIndex : Index where item is to be inserted. 
        S : String to insert. 
        pRef : Reference to store with string(default=0). 
        """
        pass

    def Remove(self,S):
        """
        Remove a string from the list.

        S : String to remove from the list. 
        return : Index where item was found. 
        """
        pass

    def RemoveAt(self,pIndex):
        """
        Remove an entry at <b>pIndex</b>.

        pIndex : Index where item is to be removed from. 
        """
        pass

    def SetAt(self,pIndex,pString):
        """
        Set the string at <b>pIndex</b>.

        pIndex : Index where string is to be set. 
        pString : String to set value at <b>pIndex</b> with. 
        """
        pass

    def SetReferenceAt(self,pIndex,pRef):
        """
        Set the reference stored with the string at <b>pIndex</b>.

        pIndex : Index to store reference at. 
        pRef : Reference to store at <b>pIndex</b>. 
        """
        pass

    def Sort(self):
        """
        Sort the string list (ascending).

        """
        pass

    pass

class FBRenderingPass (object):
    """
    Rendering Pass.     
    Use with FBShader::RenderingPass properties to make the shader be called at any pass. Passes will be called in the order of the enum.     
    """
    kFBPassInvalid=property(doc="No pass selected.         ")
    kFBPassPreRender=property(doc="Before anything.         ")
    kFBPassFlat=property(doc="Lighting off.         ")
    kFBPassLighted=property(doc="Lighting on.         ")
    kFBPassMatte=property(doc="Alpha > 0.5 will show up.         ")
    kFBPassZTranslucent=property(doc="Writes to depth buffer.         ")
    kFBPassZTranslucentAlphaTest=property(doc="Writes to depth buffer where Alpha > 0.5.         ")
    kFBPassTranslucent=property(doc="Models are blended.         ")
    kFBPassAddColor=property(doc="Models are blended additively.         ")
    kFBPassTranslucentZSort=property(doc="Models are sorted and blended.         ")
    kFBPassPostRender=property(doc="After everything.         ")
    pass

class FBTakeSpanOnLoad (object):
    """
    This enumeration indicate the how to set the take start and end points on after a load.     
        
    """
    kFBLeaveAsIs=property(doc="Use the current take's start and end point as defined before the load.         ")
    kFBImportFromFile=property(doc="Set the current take's span according what is set in the loaded file.         ")
    kFBFrameAnimation=property(doc="Have the take's span match the first and last key in the take.         ")
    pass

class FBUseChnMode (object):
    """
    Use Channel modes.     
        
    """
    kFBUseChannelLeftOnly=property(doc="Left channel will be played in both speakers.         ")
    kFBUseChannelRightOnly=property(doc="Right channel will be played in both speakers.         ")
    kFBUseChannelBoth=property(doc="Default mode, where each channel play in its respective speaker.         ")
    pass

class FBEffectorSetID (object):
    """
    Effector ID identifier.     
        
    """
    FBEffectorSetDefault=property(doc="        ")
    FBEffectorSetAux1=property(doc="        ")
    FBEffectorSetAux2=property(doc="        ")
    FBEffectorSetAux3=property(doc="        ")
    FBEffectorSetAux4=property(doc="        ")
    FBEffectorSetAux5=property(doc="        ")
    FBEffectorSetAux6=property(doc="        ")
    EFBffectorSetAux7=property(doc="        ")
    FBEffectorSetAux8=property(doc="        ")
    FBEffectorSetAux9=property(doc="        ")
    FBEffectorSetAux10=property(doc="        ")
    FBEffectorSetAux11=property(doc="        ")
    FBEffectorSetAux12=property(doc="        ")
    FBEffectorSetAux13=property(doc="        ")
    FBEffectorSetAux14=property(doc="        ")
    FBLastEffectorSetIndex=property(doc="        ")
    pass

class FBDeckTransportMode (object):
    """
    FBDeckTransportMode.     
        
    """
    kFBDeckTransportNone=property(doc="No transport interaction.         ")
    kFBDeckTransportSlave=property(doc="Slave to transport controls.         ")
    kFBDeckTransportMaster=property(doc="Transport master.         ")
    pass

class FBDisplayMode (object):
    """
    Model display options.     
        
    """
    kFBDisplayModeDefault=property(doc="Use default display mode.         ")
    kFBDisplayModeTexture=property(doc="Textures are displayed.         ")
    kFBDisplayModeHardShade=property(doc="Hard shading.         ")
    kFBDisplayModeFlatShade=property(doc="Flat shading.         ")
    kFBDisplayModeWireFrame=property(doc="Wire-frame rendering.         ")
    kFBDisplayModeCount=property(doc="End of enum, this value indicates the number of display modes available.         ")
    pass

class FBDeviceNotifyInfo (object):
    """
    Device Input and Output Notification information structure.     
    This structure is passed to the real-time device IO callback DeviceIONotify. It furnishes the device callback with the system time, local time, and sync counts for the current device cycle.     
    """
    def GetLocalTime(self):
        """
        Get local time.

        return : Current local time. 
        """
        pass

    def GetSyncCount(self):
        """
        Return the wanted timer sync count (internal or external).

        return : sync count or <b>-1</b> if no sync is present 
        """
        pass

    def GetSystemTime(self):
        """
        Get system time.

        return : Current system time. 
        """
        pass

    pass

class FBShaderModelInfo (object):
    """
        
        
    """
    def FBShaderModelInfo(self,pInfo,pGPS):
        """
        pInfo : HKModelRenderInfo
        pGPS : HIGraphicPrimitives
        """
        pass

    Model_Version=property(doc="<b>Read Write Property:</b> Shader version informations         ")
    Model=property(doc="<b>Read Write Property:</b> Shader mModel         ")
    pass

class FBGapMode (object):
    """
    Gap interpolation modes.     
        
    """
    kFBGapRigidBody=property(doc="Use rigid body information.         ")
    kFBGapConstant=property(doc="Constant interpolation.         ")
    kFBGapLinear=property(doc="Linear interpolation.         ")
    kFBGapBezier=property(doc="Bezier interpolation.         ")
    kFBGapCurve=property(doc="Cubic/curve interpolation.         ")
    kFBGapSample=property(doc="Sampled data.         ")
    pass

class FBTransportTimeFormat (object):
    """
    Available transport control time display.     
        
    """
    kFBTimeFormatTimecode=property(doc="Timecode time display mode.         ")
    kFBTimeFormatFrame=property(doc="Frame time display mode.         ")
    pass

class FBPropertyManager (object):
    """
    Property Manager.     
    The property manager exists in all FBComponent objects, and contains an array of all the registered properties. These properties may be SDK properties, internal properties or both.     
    """
    def FBPropertyManager(self):
        """
        Constructor.

        """
        pass

    def Find(self,pPropertyName,pMultilangLookup):
        """
        Find a property, based on its name.

        pPropertyName : Name of property to look for. 
        pMultilangLookup : When searching, indicate if the name lookup should also be done on the property name as shown in the GUI. (default = true) 
        return : Handle to property found. 
        """
        pass

    pass

class FBFilterType (object):
    """
    Filter types.     
    A filter can be of one or both types in order to process data on single or multiple curves of data. Ex: a gimble killer filter needs to be of type vector because the three curves are inter-dependant.     
    """
    kFBFilterNumber=property(doc="Filter single FCurves.         ")
    kFBFilterVector=property(doc="Filter a vector (3 FCurves).         ")
    pass

class FBBodyNodeId (object):
    """
    All body nodes.     
        
    """
    kFBInvalidNodeId=property(doc="        ")
    kFBHipsNodeId=property(doc="Required.         ")
    kFBLeftHipNodeId=property(doc="Required.         ")
    kFBLeftKneeNodeId=property(doc="Required.         ")
    kFBLeftAnkleNodeId=property(doc="Required.         ")
    kFBLeftFootNodeId=property(doc="        ")
    kFBRightHipNodeId=property(doc="Required.         ")
    kFBRightKneeNodeId=property(doc="Required.         ")
    kFBRightAnkleNodeId=property(doc="Required.         ")
    kFBRightFootNodeId=property(doc="        ")
    kFBWaistNodeId=property(doc="Required, Spine 0.         ")
    kFBChestNodeId=property(doc="Spine 1.         ")
    kFBLeftCollarNodeId=property(doc="        ")
    kFBLeftShoulderNodeId=property(doc="Required.         ")
    kFBLeftElbowNodeId=property(doc="Required.         ")
    kFBLeftWristNodeId=property(doc="Required.         ")
    kFBRightCollarNodeId=property(doc="        ")
    kFBRightShoulderNodeId=property(doc="Required.         ")
    kFBRightElbowNodeId=property(doc="Required.         ")
    kFBRightWristNodeId=property(doc="Required.         ")
    kFBNeckNodeId=property(doc="        ")
    kFBHeadNodeId=property(doc="Required.         ")
    kFBLeftHipRollNodeId=property(doc="        ")
    kFBLeftKneeRollNodeId=property(doc="        ")
    kFBRightHipRollNodeId=property(doc="        ")
    kFBRightKneeRollNodeId=property(doc="        ")
    kFBLeftShoulderRollNodeId=property(doc="        ")
    kFBLeftElbowRollNodeId=property(doc="        ")
    kFBRightShoulderRollNodeId=property(doc="        ")
    kFBRightElbowRollNodeId=property(doc="        ")
    kFBSpine2NodeId=property(doc="        ")
    kFBSpine3NodeId=property(doc="        ")
    kFBSpine4NodeId=property(doc="        ")
    kFBSpine5NodeId=property(doc="        ")
    kFBSpine6NodeId=property(doc="        ")
    kFBSpine7NodeId=property(doc="        ")
    kFBSpine8NodeId=property(doc="        ")
    kFBSpine9NodeId=property(doc="        ")
    kFBLeftThumbANodeId=property(doc="        ")
    kFBLeftThumbBNodeId=property(doc="        ")
    kFBLeftThumbCNodeId=property(doc="        ")
    kFBLeftIndexANodeId=property(doc="        ")
    kFBLeftIndexBNodeId=property(doc="        ")
    kFBLeftIndexCNodeId=property(doc="        ")
    kFBLeftMiddleANodeId=property(doc="        ")
    kFBLeftMiddleBNodeId=property(doc="        ")
    kFBLeftMiddleCNodeId=property(doc="        ")
    kFBLeftRingANodeId=property(doc="        ")
    kFBLeftRingBNodeId=property(doc="        ")
    kFBLeftRingCNodeId=property(doc="        ")
    kFBLeftPinkyANodeId=property(doc="        ")
    kFBLeftPinkyBNodeId=property(doc="        ")
    kFBLeftPinkyCNodeId=property(doc="        ")
    kFBRightThumbANodeId=property(doc="        ")
    kFBRightThumbBNodeId=property(doc="        ")
    kFBRightThumbCNodeId=property(doc="        ")
    kFBRightIndexANodeId=property(doc="        ")
    kFBRightIndexBNodeId=property(doc="        ")
    kFBRightIndexCNodeId=property(doc="        ")
    kFBRightMiddleANodeId=property(doc="        ")
    kFBRightMiddleBNodeId=property(doc="        ")
    kFBRightMiddleCNodeId=property(doc="        ")
    kFBRightRingANodeId=property(doc="        ")
    kFBRightRingBNodeId=property(doc="        ")
    kFBRightRingCNodeId=property(doc="        ")
    kFBRightPinkyANodeId=property(doc="        ")
    kFBRightPinkyBNodeId=property(doc="        ")
    kFBRightPinkyCNodeId=property(doc="        ")
    kFBReferenceNodeId=property(doc="        ")
    kFBLeftThumbInNodeId=property(doc="        ")
    kFBLeftThumbDNodeId=property(doc="        ")
    kFBLeftIndexInNodeId=property(doc="        ")
    kFBLeftIndexDNodeId=property(doc="        ")
    kFBLeftMiddleInNodeId=property(doc="        ")
    kFBLeftMiddleDNodeId=property(doc="        ")
    kFBLeftRingInNodeId=property(doc="        ")
    kFBLeftRingDNodeId=property(doc="        ")
    kFBLeftPinkyInNodeId=property(doc="        ")
    kFBLeftPinkyDNodeId=property(doc="        ")
    kFBRightThumbInNodeId=property(doc="        ")
    kFBRightThumbDNodeId=property(doc="        ")
    kFBRightIndexInNodeId=property(doc="        ")
    kFBRightIndexDNodeId=property(doc="        ")
    kFBRightMiddleInNodeId=property(doc="        ")
    kFBRightMiddleDNodeId=property(doc="        ")
    kFBRightRingInNodeId=property(doc="        ")
    kFBRightRingDNodeId=property(doc="        ")
    kFBRightPinkyInNodeId=property(doc="        ")
    kFBRightPinkyDNodeId=property(doc="        ")
    kFBLeftExtraFingerInNodeId=property(doc="New extra finger bone.         ")
    kFBLeftExtraFingerANodeId=property(doc="New extra finger bone.         ")
    kFBLeftExtraFingerBNodeId=property(doc="New extra finger bone.         ")
    kFBLeftExtraFingerCNodeId=property(doc="New extra finger bone.         ")
    kFBLeftExtraFingerDNodeId=property(doc="New extra finger bone.         ")
    kFBRightExtraFingerInNodeId=property(doc="New extra finger bone.         ")
    kFBRightExtraFingerANodeId=property(doc="New extra finger bone.         ")
    kFBRightExtraFingerBNodeId=property(doc="New extra finger bone.         ")
    kFBRightExtraFingerCNodeId=property(doc="New extra finger bone.         ")
    kFBRightExtraFingerDNodeId=property(doc="New extra finger bone.         ")
    kFBLeftFootThumbInNodeId=property(doc="        ")
    kFBLeftFootThumbANodeId=property(doc="        ")
    kFBLeftFootThumbBNodeId=property(doc="        ")
    kFBLeftFootThumbCNodeId=property(doc="        ")
    kFBLeftFootThumbDNodeId=property(doc="        ")
    kFBLeftFootIndexInNodeId=property(doc="        ")
    kFBLeftFootIndexANodeId=property(doc="        ")
    kFBLeftFootIndexBNodeId=property(doc="        ")
    kFBLeftFootIndexCNodeId=property(doc="        ")
    kFBLeftFootIndexDNodeId=property(doc="        ")
    kFBLeftFootMiddleInNodeId=property(doc="        ")
    kFBLeftFootMiddleANodeId=property(doc="        ")
    kFBLeftFootMiddleBNodeId=property(doc="        ")
    kFBLeftFootMiddleCNodeId=property(doc="        ")
    kFBLeftFootMiddleDNodeId=property(doc="        ")
    kFBLeftFootRingInNodeId=property(doc="        ")
    kFBLeftFootRingANodeId=property(doc="        ")
    kFBLeftFootRingBNodeId=property(doc="        ")
    kFBLeftFootRingCNodeId=property(doc="        ")
    kFBLeftFootRingDNodeId=property(doc="        ")
    kFBLeftFootPinkyInNodeId=property(doc="        ")
    kFBLeftFootPinkyANodeId=property(doc="        ")
    kFBLeftFootPinkyBNodeId=property(doc="        ")
    kFBLeftFootPinkyCNodeId=property(doc="        ")
    kFBLeftFootPinkyDNodeId=property(doc="        ")
    kFBRightFootThumbInNodeId=property(doc="        ")
    kFBRightFootThumbANodeId=property(doc="        ")
    kFBRightFootThumbBNodeId=property(doc="        ")
    kFBRightFootThumbCNodeId=property(doc="        ")
    kFBRightFootThumbDNodeId=property(doc="        ")
    kFBRightFootIndexInNodeId=property(doc="        ")
    kFBRightFootIndexANodeId=property(doc="        ")
    kFBRightFootIndexBNodeId=property(doc="        ")
    kFBRightFootIndexCNodeId=property(doc="        ")
    kFBRightFootIndexDNodeId=property(doc="        ")
    kFBRightFootMiddleInNodeId=property(doc="        ")
    kFBRightFootMiddleANodeId=property(doc="        ")
    kFBRightFootMiddleBNodeId=property(doc="        ")
    kFBRightFootMiddleCNodeId=property(doc="        ")
    kFBRightFootMiddleDNodeId=property(doc="        ")
    kFBRightFootRingInNodeId=property(doc="        ")
    kFBRightFootRingANodeId=property(doc="        ")
    kFBRightFootRingBNodeId=property(doc="        ")
    kFBRightFootRingCNodeId=property(doc="        ")
    kFBRightFootRingDNodeId=property(doc="        ")
    kFBRightFootPinkyInNodeId=property(doc="        ")
    kFBRightFootPinkyANodeId=property(doc="        ")
    kFBRightFootPinkyBNodeId=property(doc="        ")
    kFBRightFootPinkyCNodeId=property(doc="        ")
    kFBRightFootPinkyDNodeId=property(doc="        ")
    kFBLeftExtraFootFingerInNodeId=property(doc="New extra finger bone.         ")
    kFBLeftExtraFootFingerANodeId=property(doc="New extra finger bone.         ")
    kFBLeftExtraFootFingerBNodeId=property(doc="New extra finger bone.         ")
    kFBLeftExtraFootFingerCNodeId=property(doc="New extra finger bone.         ")
    kFBLeftExtraFootFingerDNodeId=property(doc="New extra finger bone.         ")
    kFBRightExtraFootFingerInNodeId=property(doc="New extra finger bone.         ")
    kFBRightExtraFootFingerANodeId=property(doc="New extra finger bone.         ")
    kFBRightExtraFootFingerBNodeId=property(doc="New extra finger bone.         ")
    kFBRightExtraFootFingerCNodeId=property(doc="New extra finger bone.         ")
    kFBRightExtraFootFingerDNodeId=property(doc="New extra finger bone.         ")
    kFBLeftHandNodeId=property(doc="        ")
    kFBRightHandNodeId=property(doc="        ")
    kFBNeck1NodeId=property(doc="        ")
    kFBNeck2NodeId=property(doc="        ")
    kFBNeck3NodeId=property(doc="        ")
    kFBNeck4NodeId=property(doc="        ")
    kFBNeck5NodeId=property(doc="        ")
    kFBNeck6NodeId=property(doc="        ")
    kFBNeck7NodeId=property(doc="        ")
    kFBNeck8NodeId=property(doc="        ")
    kFBNeck9NodeId=property(doc="        ")
    kFBLastNodeId=property(doc="        ")
    pass

class FBBorderStyle (object):
    """
    Different border types available.     
        
    """
    kFBNoBorder=property(doc="No border.         ")
    kFBStandardBorder=property(doc="Standard border.         ")
    kFBEmbossBorder=property(doc="Embossed border.         ")
    kFBEmbossSmoothBorder=property(doc="Smooth border.         ")
    kFBEmbossEdgeSmoothBorder=property(doc="Edged smooth border.         ")
    kFBEmbossSmoothEdgeBorder=property(doc="Smoothed edges border.         ")
    kFBStandardSmoothBorder=property(doc="Standard smooth border.         ")
    kFBStandardEdgeSmoothBorder=property(doc="Standard edged smooth border.         ")
    kFBStandardSmoothEdgeBorder=property(doc="Standard smoothed edges border.         ")
    kFBHighlightBorder=property(doc="Highlight border.         ")
    kFBPickingBorder=property(doc="Picking border.         ")
    pass

class FBCharacterHipsTranslationMode (object):
    """
    Character Hips Translation modes.     
        
    """
    kFBParamHipsTranslationWorldRigid=property(doc="        ")
    kFBParamHipsTranslationBodyRigid=property(doc="        ")
    kFBLastHipsTranslationMode=property(doc="        ")
    pass

class FBTransportMode (object):
    """
    Transport modes.     
        
    """
    kFBTransportPlay=property(doc="        ")
    kFBTransportPlayPrepare=property(doc="!< Play mode         ")
    kFBTransportPlayReady=property(doc="        ")
    kFBTransportStop=property(doc="        ")
    kFBTransportStopPost=property(doc="!< Stop mode         ")
    kFBTransportStopReady=property(doc="        ")
    kFBTransportShuttle=property(doc="        ")
    kFBTransportShuttlePrepare=property(doc="!< Shuttle mode         ")
    kFBTransportShuttleReady=property(doc="        ")
    kFBTransportPlayReverse=property(doc="        ")
    kFBTransportPlayReversePrepare=property(doc="!< Play reverse.         ")
    kFBTransportPlayReverseReady=property(doc="        ")
    kFBTransportJog=property(doc="        ")
    kFBTransportJogPrepare=property(doc="!< Jog.         ")
    kFBTransportJogReady=property(doc="        ")
    kFBTransportGoto=property(doc="        ")
    kFBTransportGotoPrepare=property(doc="!< Goto.         ")
    kFBTransportGotoReady=property(doc="        ")
    kFBTransportStepForward=property(doc="        ")
    kFBTransportStepForwardPrepare=property(doc="!< Step forward         ")
    kFBTransportStepForwardReady=property(doc="        ")
    kFBTransportStepBackward=property(doc="        ")
    kFBTransportStepBackwardPrepare=property(doc="!< Step backward.         ")
    kFBTransportStepBackwardReady=property(doc="        ")
    pass

class FBCharacterInputType (object):
    """
    Character Input/Output types.     
        
    """
    kFBCharacterInputActor=property(doc="        ")
    kFBCharacterInputCharacter=property(doc="        ")
    kFBCharacterInputMarkerSet=property(doc="        ")
    kFBCharacterOutputMarkerSet=property(doc="        ")
    kFBCharacterInputStance=property(doc="        ")
    pass

class FBUndoManager (object):
    """
    Access to global undo and redo functionality.     
    Users have the possibility of undoing and redoing actions performed using the GUI, and interacting with the undo and redo stacks with custom actions.All undo/redo related functions should only be called inside UI event callback. Users should call TransactionBegin()/TransactionEnd() in pairs, Transaction stack must be closed before UI event callback return.This class cannot be used as a base class.     
    """
    def FBUndoManager(self):
        """
        Constructor.

        """
        pass

    def ActiveOperation(self):
        """
        Determine if an undo operation is in action.

        return : true the Undo Manager is performing an Undo or a Redo operation. 
        """
        pass

    def Clear(self):
        """
        Clear the undo and redo stacks.

        return : A boolean value indicating success (true) or failure (false). 
        """
        pass

    def Redo(self):
        """
        Redo last undone action.

        """
        pass

    def TransactionAddModelTRS(self,pModel):
        """
        Add Transaction if transaction stack is open.
        Quick Function to add Model TRS in Undo Stack

        pModel : Model to backup TRS 
        return : true if add transaction successfully. 
        """
        pass

    def TransactionAddObjectDestroy(self,pObject):
        """
        Add Transaction if transaction stack is open.
        Function to add object to destroy in Undo Stack

        pObject : Object to backup 
        return : true if add transaction successfully. 
        """
        pass

    def TransactionAddProperty(self,pProperty):
        """
        Add Transaction if transaction stack is open.
        Quick Function to add property value in Undo Stack

        pProperty : Property to backup 
        return : true if add transaction successfully. 
        """
        pass

    def TransactionBegin(self,pTransactionName):
        """
        Open transaction stack for adding transactions.
        Users should call TransactionBegin()/TransactionEnd() in pairs, Transaction stack must be closed before UI event callback return.

        pTransactionName : Name of Transaction. 
        return : true if open transaction stack successfully. 
        """
        pass

    def TransactionEnd(self):
        """
        Close transaction stack.
        Users should call TransactionBegin()/TransactionEnd() in pairs, Transaction stack must be closed before UI event callback return.

        return : true if transaction close successfully. 
        """
        pass

    def TransactionIsOpen(self):
        """
        Query if transaction stack is already open.

        return : true if transaction is already open. 
        """
        pass

    def Undo(self,pNoRedo):
        """
        Undo last action.

        pNoRedo : If true, once the action is undone, it cannot be redone. 
        """
        pass

    pass

class FBRigidBodyMode (object):
    """
    Rigid body modes.     
        
    """
    kFBRigidBodyFast=property(doc="Fast rigid body mode.         ")
    kFBRigidBodyBest=property(doc="Best rigid body mode.         ")
    pass

class FBPoseTransformType (object):
    """
    Transform mode of pose.     
        
    """
    kFBPoseTransformInvalid=property(doc="        ")
    kFBPoseTransformLocal=property(doc="        ")
    kFBPoseTransformGlobal=property(doc="        ")
    kFBPoseTransformLocalRef=property(doc="        ")
    kFBPoseTransformTypeCount=property(doc="        ")
    pass

class FBInsertSegmentMode (object):
    """
    Insert segment modes.     
        
    """
    kFBInsertSegmentWhole=property(doc="Insert whole.         ")
    kFBInsertSegmentToEnd=property(doc="Insert to end.         ")
    kFBInsertSegmentFromStart=property(doc="Insert from start.         ")
    pass

class FBKeyingGroupType (object):
    """
    Keying group types.     
        
    """
    kFBKeyingGroupGlobal=property(doc="All selected objects with the same properties as those defined in the keying group will be keyed.         ")
    kFBKeyingGroupObjectType=property(doc="All selected objects of the specified type in the keying group with the same properties as those defined in the keying group will be keyed.         ")
    kFBKeyingGroupLocal=property(doc="Only properties of objects specified in the keying group will be keyed.         ")
    pass

class FBBatchOptions (object):
    """
    Option parameters for the batch process.     
        
    """
    def FBBatchOptions(self):
        """
        Constructor.

        """
        pass

    InputFileFormat=property(doc="<b>Read Write Property:</b> File format of the input files.         ")
    OutputFileFormat=property(doc="<b>Read Write Property:</b> File format of the output files.         ")
    ProcessType=property(doc="<b>Read Write Property:</b> What process should be done? Load, Save or Both.         ")
    InputDirectory=property(doc="<b>Read Write Property:</b> The directory containning the input files.         ")
    OutputDirectory=property(doc="<b>Read Write Property:</b> The directory containning the output files.         ")
    SkeletonFile=property(doc="<b>Read Write Property:</b> The Skeleton file (for Acclaim AMC files).         ")
    Character=property(doc="<b>Read Write Property:</b> The character to receive the animation.         ")
    StartAnimationAtZero=property(doc="<b>Read Write Property:</b> Set the time of all loaded files to 0.         ")
    FrameAnimation=property(doc="<b>Read Write Property:</b> Set timeline start and end time to corespond with the start and end of animation.         ")
    OverwriteScaling=property(doc="<b>Read Write Property:</b> Set the scaling to a default setting of 1.0.         ")
    KeepDummyBones=property(doc="<b>Read Write Property:</b> To keep dummy bones.         ")
    WriteRate=property(doc="<b>Read Write Property:</b> Write frame rate in Acclaim AMC files.         ")
    WriteTranslation=property(doc="<b>Read Write Property:</b> Write translation animation data included with Acclaim AMC files.         ")
    PlotToCharacter=property(doc="<b>Read Write Property:</b> To plot the animation on the character.         ")
    PlotToControlSet=property(doc="<b>Read Write Property:</b> To plot the animation on the control set.         ")
    UseSingleTake=property(doc="<b>Read Write Property:</b> Use only one take to convert all files.         ")
    UseBatchSuffix=property(doc="<b>Read Write Property:</b> Add a batch suffix to the name of the files.         ")
    KeepCharacterConstraint=property(doc="<b>Read Write Property:</b> To keep the character constaint when saving.         ")
    OnTakeExistAction=property(doc="<b>Read Write Property:</b> Action to perform when a take already exist while in a batch process.         ")
    OnContainsBatchTakesAction=property(doc="<b>Read Write Property:</b> Action to perform when a scene already contains batch takes while in a batch process.         ")
    pass

class FBPlug (object):
    """
    Connections Basic Open Reality SDK Element.     
    Most elements that are available in the SDK inherit from this base class since FBComponent and FBProperty inherit from FBPlug. Basically, all objects can be connected together because they are all 'plugs'. To simplify the graph, you can think of a 'source' connection as a child, and a 'destination' connection as a parent. Also, it is correct to assume that a source affect/work on its destination. For example, a shader applyed on an object would be seen as the source while the object is the destination. So FBPlug is a set of functions that enables you to control those connections with flexibility and ease.     
    """
    def FBPlug(self):
        """
        Constructor.

        """
        pass

    def BeginChange(self):
        """
        Begins a change on multiple plugs.

        return : A boolean indicating success (True) or failure (False). 
        """
        pass

    def ClassName(self):
        """
        internal System vars.

        """
        pass

    def ConnectAt(self,pSrc,pSrc_DstIndex,pDst,pDst_SrcIndex,pConnectionType):
        """
        Make connection between to plug, specifying the connection index.
        (Deprecated)

        pSrc : Source plug. 
        pSrc_DstIndex : Index that tells where to add this destination connection in the source's connection list. 
        pDst : Destination plug. 
        pDst_SrcIndex : Index that tells where to add this source connection in the destination's connection list. 
        pConnectionType : Type of connection, taken from FBConnectionType. Default value should work in all cases. 
        return : A boolean indicating success (True) or failure (False). 
        """
        pass

    def ConnectDst(self,pDst,pConnectionType):
        """
        Add a destination connection.

        pDst : Destination plug. 
        pConnectionType : Type of connection, taken from FBConnectionType. Default value should work in all cases. 
        return : A boolean indicating success (True) or failure (False). 
        """
        pass

    def ConnectDstAt(self,pSrc_DstIndex,pDst,pConnectionType):
        """
        Add a destination connection.

        pSrc_DstIndex : Index that tells where to add this destination connection in the source's connection list. 
        pDst : Destination plug. 
        pConnectionType : Type of connection, taken from FBConnectionType. Default value should work in all cases. 
        return : A boolean indicating success (True) or failure (False). 
        """
        pass

    def ConnectSrc(self,pSrc,pConnectionType):
        """
        Add a source connection.

        pSrc : Source plug. 
        pConnectionType : Type of connection, taken from FBConnectionType. Default value should work in all cases. 
        return : A boolean indicating success (True) or failure (False). 
        """
        pass

    def ConnectSrcAt(self,pDst_SrcIndex,pSrc,pConnectionType):
        """
        Add a source connection.

        pDst_SrcIndex : Index that tells where to add this source connection in the destination's connection list. 
        pSrc : Source plug. 
        pConnectionType : Type of connection, taken from FBConnectionType. Default value should work in all cases. 
        return : A boolean indicating success (True) or failure (False). 
        """
        pass

    def DisconnectAllDst(self):
        """
        Remove all destination connections.

        """
        pass

    def DisconnectAllSrc(self):
        """
        Remove all source connections.

        """
        pass

    def DisconnectDst(self,pDst):
        """
        Remove a destination connection.

        pDst : Destination plug. 
        return : A boolean indicating success (True) or failure (False). 
        """
        pass

    def DisconnectDstAt(self,pIndex):
        """
        Remove a destination connection at a specifyed index.

        pIndex : Destination plug index. 
        return : A boolean indicating success (True) or failure (False). 
        """
        pass

    def DisconnectSrc(self,pSrc):
        """
        Remove a source connection.

        pSrc : Source plug. 
        return : A boolean indicating success (True) or failure (False). 
        """
        pass

    def DisconnectSrcAt(self,pIndex):
        """
        Remove a source connection at a specifyed index.

        pIndex : Source plug index. 
        return : A boolean indicating success (True) or failure (False). 
        """
        pass

    def EndChange(self):
        """
        Ends a change on multiple plugs.

        """
        pass

    def GetDst(self,pIndex):
        """
        Get a destination connection's plug at specifyed index.

        pIndex : Index of the destination connection's plug. 
        return : Destination plug at specifyed index. 
        """
        pass

    def GetDstCount(self):
        """
        Get destination connection count.

        return : Total destinations connections count. 
        """
        pass

    def GetDstType(self,pIndex):
        """
        Get a destination connection's type at specifyed index.

        pIndex : Index of the destination connection's type. 
        return : Destination connection's type at specifyed index. 
        """
        pass

    def GetOwned(self,pIndex):
        """
        Get the owned plug at specifyed index.

        pIndex : Index of the owned plug to get. 
        return : The owned plug at specifyed index. 
        """
        pass

    def GetOwnedCount(self):
        """
        Get the owned plug count.

        return : The owned plug count. 
        """
        pass

    def GetOwner(self):
        """
        Get the owner of this plug.
        Very useful for properties since they are plugs too.

        return : The owner of this plug. 
        """
        pass

    def GetOwnerCount(self):
        """
        Get the owner count of this plug.
        (Obsolete)

        return : The owner count of this plug (will always return 1). 
        """
        pass

    def GetSrc(self,pIndex):
        """
        Get a source connection's plug at specifyed index.

        pIndex : Index of the source connection's plug. 
        return : Source plug at specifyed index. 
        """
        pass

    def GetSrcCount(self):
        """
        Get source connection count.

        return : Total sources connections count. 
        """
        pass

    def GetSrcType(self,pIndex):
        """
        Get a source connection's type at specifyed index.

        pIndex : Index of the source connection's type. 
        return : Source connection's type at specifyed index. 
        """
        pass

    def Is(self,pTypeId):
        """
        Is( int pTypeId ).

        pTypeId : Type Identifiant. 
        return : True if Plug is a Instance of pTypeId. 
        """
        pass

    def IsSDKComponent(self):
        """
        Return whether or not item is an SDK component.

        """
        pass

    def MoveSrcAt(self,pIndex,pAtIndex):
        """
        Move source connection at pIndex to pAtIndex.

        pIndex : Plug current index. 
        pAtIndex : Plug new index. 
        return : A boolean indicating success (True) or failure (False). 
        """
        pass

    def MoveSrcAt(self,pSrc,pAtSrc):
        """
        Move source connection pSrc to the position of pAtSrc.

        pSrc : Plug. 
        pAtSrc : Plug that mark where we want to insert (will insert before this one). 
        return : A boolean indicating success (True) or failure (False). 
        """
        pass

    def ReplaceDstAt(self,pIndex,pDst):
        """
        Replace a destination connection at a specifyed index.

        pIndex : Destination plug index. 
        pDst : Plug that will replace the other at index. 
        return : A boolean indicating success (True) or failure (False). 
        """
        pass

    def ReplaceSrcAt(self,pIndex,pSrc):
        """
        Replace a source connection at a specifyed index.

        pIndex : Source plug index. 
        pSrc : Plug that will replace the other at index. 
        return : A boolean indicating success (True) or failure (False). 
        """
        pass

    def SwapSrc(self,pIndexA,pIndexB):
        """
        Swap source connection at index A with source connection at index B.

        pIndexA : Plug index. 
        pIndexB : Other plug index. 
        return : A boolean indicating success (True) or failure (False). 
        """
        pass

    pass

class FBCameraAntiAliasingMethod (object):
    """
    Antialiasing methods.     
        
    """
    kFBAntiAliasingSoftware=property(doc="Antaliasing in software.         ")
    kFBAntialiasingMultiSamplingOnyx=property(doc="Multisampling (only on Onyx).         ")
    pass

class FBVector4d (object):
    """
    Vector4d class.     
    This class creates a list like object, which can be modified using the list protocol method. But unlike lists, its length is fixed: it always contain 4 floating point values. Thus it does not support the any list methods that would affect its length. The values within can be changed, usually via the bracket operator.
@code
    # Supported list protocol methods:
    color = FBColor()
    len(color)
    print color[0]
    color[0] = 1.0    
@endcode

 Slicing is not supported by this object.     
    """
    def FBVector4d(self):
        """
        Constructor.
        Default constructor, all 4 values within are set to 0.0.

        """
        pass

    def FBVector4d(self,pVector4d):
        """
        Constructor.
        Copy constructor. Copy values from another instance.

        pVector4d : FBVector4d
        """
        pass

    def FBVector4d(self,pX,pY,pZ,pA):
        """
        Constructor.
        Explicitely construct a vector by specifying its values.

        pX : float
        pY : float
        pZ : float
        pA : float
        """
        pass

    def FBVector4d(self,p0):
        """
        Constructor.
        A vector can be built from any python object with supports the tuple interface and is of a lenght of 4.

        p0 : tuple< float, float, float, float >
        """
        pass

    def __len__(self):
        """
        Returns the number of elements.
        Corresponds to python: len(object)

        """
        pass

    def __getitem__(self,pIndex):
        """
        Returns the ith component Corresponds to python: print v[1].

        pIndex : Index of the components to get (0 to 3) 
        return : Color component value. 
        """
        pass

    def __setitem__(self,pIndex,pComponentValue):
        """
        Sets the ith components Corresponds to python: v[1] = 0.5.

        pIndex : Index of the components to set (0 to 3) 
        pComponentValue : Value of component to set 
        """
        pass

    pass

class FBSegmentMode (object):
    """
    Segment modes.     
        
    """
    kFBSegmentMarker=property(doc="Use marker.         ")
    kFBSegmentRigidBody=property(doc="Use rigid body.         ")
    kFBSegmentAll=property(doc="Use all.         ")
    pass

class FBButtonStyle (object):
    """
    Style of buttons.     
    Not all button styles are completely functional.     
    """
    kFBPushButton=property(doc="Normal button.         ")
    kFBBitmapButton=property(doc="Button with bitmap on it.         ")
    kFBRadioButton=property(doc="Radio button.         ")
    kFB2States=property(doc="2 state button (2 colors).         ")
    kFBCheckbox=property(doc="Check box.         ")
    kFBBitmap2States=property(doc="2 state button with 2 bitmaps.         ")
    pass

class FBOrientation (object):
    """
    General directions for UI components.     
        
    """
    kFBHorizontal=property(doc="Horizontal.         ")
    kFBVertical=property(doc="Vertical.         ")
    pass

class FBMatrix (object):
    """
    FBMatrix class.     
    Four x Four (double) Matrix.This class creates a list like object, which can be modified using the list protocol method. But unlike lists, its length is fixed: it always contain 16 floating point values. Thus it does not support the any list methods that would affect its length. The values within can be changed, usually via the bracket operator. 
@code
    # Supported list protocol methods:
    mat = FBMatrix()
    len(mat)
    print mat[13]
    mat[12] = 1.0
@endcode

 The implementation of this 4x4 matrix uses a simple list of 16 elements, not a list of 4 vectors of 4 elements.* Slicing is not supported by this object.     
    """
    def FBMatrix(self,pValue):
        """
        Constructor.

        pValue : Array to intialize matrix from. 
        """
        pass

    def FBMatrix(self,pMatrix):
        """
        Copy Constructor.

        pMatrix : Matrix to copy. 
        """
        pass

    def FBMatrix(self):
        """
        Constructor Initializes matrix to identity.

        """
        pass

    def FBMatrix(self,pValue):
        """
        Constructor.

        pValue : Array to intialize matrix from. 
        """
        pass

    def FBMatrix(self,pMatrix):
        """
        Copy Constructor.

        pMatrix : Matrix to copy. 
        """
        pass

    def Identity(self):
        """
        Load identity matrix.

        """
        pass

    def Set(self,pValue):
        """
        Set matrix from an array.

        pValue : Array to intialize matrix from. 
        """
        pass

    def __len__(self):
        """
        Returns the number of elements.
        Corresponds to python: len(object)

        """
        pass

    def __getitem__(self,pIndex):
        """
        Returns the ith component Corresponds to python: print matrix[1].

        pIndex : Index of the components to get (0 to 15) 
        return : Matrix element value 
        """
        pass

    def __setitem__(self,pIndex,pComponentValue):
        """
        Sets the ith components Corresponds to python: color[1] = 0.5.

        pIndex : Index of the components to set (0 to 15) 
        pComponentValue : Value of component to set 
        """
        pass

    pass

class FBConfigFile (object):
    """
    Interface to the application config files.     
    This class allows client code to generate, modify and query configuration files. Config files will be automatically created when needed. They will be located in the [APPLICATION]/bin/config folder or an explicitely specified folder depending on the constructor used.     
    """
    def FBConfigFile(self,pConfigFileName,pVirtualMode):
        """
        Constructor.
        This will open the desired config file from the [APPLICATION]/bin/config folder. The file will be created if it does not exists. By prefixing the character '@' to the file name, this will automatically prepend the current machine name to the config file, the way it is done for the other config files of the application.

        pConfigFileName : Name the config file to use. 
        pVirtualMode : Enable this to limit disk access, file will only be read at construction and written at destruction. 
        """
        pass

    def FBConfigFile(self,pConfigFileName,pConfigFilePath):
        """
        Constructor.
        This will open the desired config file in the designed folder. The file will be created if it does not exists. By prefixing the character '@' to the file name, this will automatically prepend the current machine name to the config file, the way it is done for the other config files of the application.

        pConfigFileName : Name the config file to use. 
        pConfigFilePath : Location where the file should reside. Missing directories will not be created. 
        """
        pass

    def ClearFile(self):
        """
        Remove all content from the config file.

        """
        pass

    def Get(self,pSectionName,pItemName,pDefaultValue):
        """
        Get an item's value.
        Get an item's value by looking inside a specific section of the config file.

        pSectionName : Name of the section. 
        pItemName : Name of the item. 
        pDefaultValue : Default value that will be returned if the item is not found. 
        return : The value assigned to the item in the specified section of the config file, or the default value if not found. 
        """
        pass

    def GetOrSet(self,pSectionName,pItemName,pValue,pComment):
        """
        Get a value from the config file and set it if it was not found.

        pSectionName : Name of the section. 
        pItemName : Name of the item. 
        pValue : Reference the the string that will contain the value of the item. If the item is not found in the file, it will be added with the initial value in this string. 
        pComment : Optional parameter that can be used to add a comment. 
        return : <b>true</b> if the value was found or added, or false if the item was not found and could not be added to the file. 
        """
        pass

    def Set(self,pSectionName,pItemName,pValue,pComment):
        """
        Set an item's value.
        Assign a value to an item in the config file. If the item does not exist, it will be created.

        pSectionName : Name of the section. 
        pItemName : Name of the item. 
        pValue : Value assigned to the item. 
        pComment : Optional parameter that can be used to add a comment. 
        return : <b>true</b> if the item was written to the config file, <b>false</b> otherwise. 
        """
        pass

    pass

class FBVideoCodecMode (object):
    """
    Enum FBVideoRenderDepth.     
        
    """
    FBVideoCodecAsk=property(doc="Pop codec selection dialog each render.         ")
    FBVideoCodecUncompressed=property(doc="Assume uncompressed codec.         ")
    FBVideoCodecStored=property(doc="Pop dialog and stored its value.         ")
    pass

class FBPickingMode (object):
    """
    3D picking mode.     
        
    """
    kFBPickingModeStandard=property(doc="Standard picking mode.         ")
    kFBPickingModeXRay=property(doc="X-Ray picking mode (obstructed models are displayed in overlay).         ")
    kFBPickingModeModelsOnly=property(doc="Models-only mode (no nulls or skeletons are displayed).         ")
    kFBPickingModeCount=property(doc="End of enum, this valued indicates the number of picking modes available.         ")
    pass

class FBGeometryMappingMode (object):
    """
    Different types of geometry mapping possible.     
        
    """
    kFBMappingModeUnique=property(doc="Unique mapping.         ")
    kFBMappingModeVertex=property(doc="Vertex mapping.         ")
    kFBMappingModeSurface=property(doc="Surface mapping.         ")
    pass

class FBConnectionAction (object):
    """
    Possible actions when a notify plug event occurs.     
        
    """
    kFBRequestConnectSrc=property(doc="Request connection of source to destination.         ")
    kFBRequestConnectDst=property(doc="Request connection of destination to source.         ")
    kFBConnectSrc=property(doc="Connect source to destination.         ")
    kFBConnectDst=property(doc="Connect destination to source.         ")
    kFBConnectedSrc=property(doc="Connected source to destination.         ")
    kFBConnectedDst=property(doc="Connected destination to source.         ")
    kFBDisconnectSrc=property(doc="Disconnect source from destination.         ")
    kFBDisconnectDst=property(doc="Disconnect destination from source.         ")
    kFBDisconnectedSrc=property(doc="Disconnected source from destination.         ")
    kFBDisconnectedDst=property(doc="Disconnected destination from source.         ")
    kFBBeginReplaceSrc=property(doc="Begin replace source during merge.         ")
    kFBEndReplaceSrc=property(doc="End replace source during merge.         ")
    kFBBeginReplaceDst=property(doc="Begin replace destination during merge.         ")
    kFBEndReplaceDst=property(doc="End replace destination during merge.         ")
    kFBReorderSrc=property(doc="Reorder of source.         ")
    kFBReorderedSrc=property(doc="Source has been reordered.         ")
    kFBBeginChange=property(doc="Begin change on destination.         ")
    kFBEndChange=property(doc="End change on destination.         ")
    kFBConnectedOwner=property(doc="Connected owner to destination.         ")
    kFBDisconnectOwner=property(doc="Disconnect owner from destination.         ")
    kFBCandidate=property(doc="Data candidate event, before the data is set.         ")
    kFBCandidated=property(doc="Data candidate event, after the data is set.         ")
    kFBCandidateGlobal=property(doc="Data candidate event, global candidate.         ")
    kFBDetached=property(doc="Component detached from scene.         ")
    kFBDestroy=property(doc="Component destroy.         ")
    kFBSelect=property(doc="Component selection.         ")
    kFBUnselect=property(doc="Component de-selection.         ")
    kFBReselect=property(doc="Component re-selection.         ")
    kFBRename=property(doc="Component is going to be renamed.         ")
    kFBRenamed=property(doc="Component has been renamed.         ")
    kFBPrefixRename=property(doc="Component prefix is going to be renamed.         ")
    kFBPrefixRenamed=property(doc="Component prefix has been renamed.         ")
    kFBDescription=property(doc="Component description event.         ")
    kFBConnect=property(doc="        ")
    kFBConnected=property(doc="        ")
    kFBDisconnect=property(doc="        ")
    kFBDisconnected=property(doc="        ")
    pass

class FBRecalcMarkerSetOffset (object):
    """
    Recalculate MarkerSet offset for?     
        
    """
    kFBRecalcMarkerSetOffsetTR=property(doc="Recalculate MarkerSet offset for TR.         ")
    kFBRecalcMarkerSetOffsetROnly=property(doc="Recalculate MarkerSet offset for R Only.         ")
    pass

class FBTextureBlendMode (object):
    """
    Texture blend modes.     
    How the texture is blended with another.     
    """
    kFBTextureBlendTranslucent=property(doc="Layer transparency.         ")
    kFBTextureBlendAdditive=property(doc="Layer addition.         ")
    kFBTextureBlendModulate=property(doc="Layer multiplication.         ")
    kFBTextureBlendModulate2=property(doc="Layer multiplication + brightness.         ")
    pass

class FBInputType (object):
    """
    Types of input events.     
        
    """
    kFBKeyPress=property(doc="A keyboard key was pressed.         ")
    kFBKeyRelease=property(doc="A keyboard key was released.         ")
    kFBButtonPress=property(doc="A mouse button was pressed.         ")
    kFBButtonRelease=property(doc="A mouse button was released.         ")
    kFBMotionNotify=property(doc="The mouse has been moved.         ")
    kFBButtonDoubleClick=property(doc="A mouse button was double clicked.         ")
    kFBMouseEnter=property(doc="The mouse pointer is entering the window.         ")
    kFBMouseLeave=property(doc="The mouse pointer is leaving the window.         ")
    kFBMouseWheelNotify=property(doc="The mouse wheel has moved.         ")
    kFBDragging=property(doc="The mouse is dragging items.         ")
    kFBDropping=property(doc="The mouse is dropping items.         ")
    kFBKeyPressRaw=property(doc="A keyboard key was pressed.         ")
    kFBKeyReleaseRaw=property(doc="A keyboard key was released.         ")
    kFBUnknownInput=property(doc="The internal event could not be translated.         ")
    pass

class FBDisplayWhat (object):
    """
    Model display mask This mask determines what types of models are displayed by the renderer.     
        
    """
    kFBDisplayNone=property(doc="Nothing is displayed.         ")
    kFBDisplayNull=property(doc="Null models are displayed.         ")
    kFBDisplayMarker=property(doc="Markers are displayed.         ")
    kFBDisplaySkeleton=property(doc="Skeletons and bones are displayed.         ")
    kFBDisplayCenter=property(doc="Centers are displayed.         ")
    kFBDisplayLight=property(doc="Lights are displayed.         ")
    kFBDisplayCamera=property(doc="Cameras are displayed.         ")
    kFBDisplay3dIcon=property(doc="3D icons are displayed (3D icons are 3D elements that do not exist in the scene).         ")
    kFBDisplayAll=property(doc="Everything is displayed.         ")
    pass

class FBPropertyListStorySubTrack (object):
    """
        
        
    """
    pass

class FBTriggerStyle (object):
    """
    Audio clips' trigger styles.     
        
    """
    kFBTriggerStyleContinue=property(doc="Previously triggered clips that are still playing won't be stopped and mixing will occur.         ")
    kFBTriggerStyleCut=property(doc="Previously triggered clips that are still playing will be stopped.         ")
    kFBTriggerStyleToggle=property(doc="If a previously triggered clip is playing, it will only be stopped, otherwise a new starts playing. No mixing and no loop.         ")
    pass

class FBPropertyListPivot (object):
    """
        
        
    """
    pass

class FBPropertyListVertexIndex (object):
    """
        
        
    """
    pass

class FBDeviceKeyboardKey (object):
    """
    Keyboard keys (for input).     
        
    """
    kFBDKeyPageUp=property(doc="Page Up.         ")
    kFBDKeyPageDown=property(doc="Page Down.         ")
    kFBDKeyEnd=property(doc="End.         ")
    kFBDKeyHome=property(doc="Home.         ")
    kFBDKeyArrowLeft=property(doc="Left.         ")
    kFBDKeyArrowUp=property(doc="Up.         ")
    kFBDKeyArrowRight=property(doc="Right.         ")
    kFBDKeyArrowDown=property(doc="Down.         ")
    kFBDKeyReturn=property(doc="Return.         ")
    kFBDKeyEscape=property(doc="Escape.         ")
    kFBDKeySpace=property(doc="Space bar.         ")
    kFBDKey1=property(doc="'1'.         ")
    kFBDKey2=property(doc="'2'.         ")
    kFBDKey3=property(doc="'3'.         ")
    kFBDKey4=property(doc="'4'.         ")
    kFBDKey5=property(doc="'5'.         ")
    kFBDKey6=property(doc="'6'.         ")
    kFBDKey7=property(doc="'7'.         ")
    kFBDKey8=property(doc="'8'.         ")
    kFBDKey9=property(doc="'9'.         ")
    kFBDKey0=property(doc="'0'.         ")
    kFBDKeyF1=property(doc="'F1'.         ")
    kFBDKeyF2=property(doc="'F2'.         ")
    kFBDKeyF3=property(doc="'F3'.         ")
    kFBDKeyF4=property(doc="'F4'.         ")
    kFBDKeyF5=property(doc="'F5'         ")
    kFBDKeyF6=property(doc="'F6'.         ")
    kFBDKeyF7=property(doc="'F7'.         ")
    kFBDKeyF8=property(doc="'F8'.         ")
    kFBDKeyF9=property(doc="'F9'.         ")
    kFBDKeyF10=property(doc="'F10'.         ")
    kFBDKeyF11=property(doc="'F11'.         ")
    kFBDKeyF12=property(doc="'F12'.         ")
    pass

class FBFCurveKey (object):
    """
    KeyFrame for an FCurve.     
        
    """
    def FBFCurveKey(self,pFCurve,pKeyIndex):
        """
        Constructor.

        pFCurve : Parent FCurve (default is NULL). 
        pKeyIndex : Key frame index (default is 1). 
        """
        pass

    def FBFCurveKey(self,pFCurveKey):
        """
        Constructor.

        pFCurveKey : FCurveKey to copy information from. 
        """
        pass

    Bias=property(doc="<b>Read Write Property:</b> Bias (TCB).         ")
    Continuity=property(doc="<b>Read Write Property:</b> Continuity (TCB).         ")
    Interpolation=property(doc="<b>Read Write Property:</b> Type of interpolation.         ")
    LeftBezierTangent=property(doc="<b>Read Write Property:</b> Left bezier tangent         ")
    LeftDerivative=property(doc="<b>Read Write Property:</b> Left derivative, in units/seconds.         ")
    LeftTangentWeight=property(doc="<b>Read Write Property:</b> Left tangent weight         ")
    RightBezierTangent=property(doc="<b>Read Write Property:</b> Right bezier tangent         ")
    RightDerivative=property(doc="<b>Read Write Property:</b> Right derivative, in units/seconds.         ")
    RightTangentWeight=property(doc="<b>Read Write Property:</b> Right tangent weight         ")
    TangentBreak=property(doc="<b>Read Write Property:</b> Tangent's break status         ")
    TangentClampMode=property(doc="<b>Read Write Property:</b> Tangent's clamp method.         ")
    TangentConstantMode=property(doc="<b>Read Write Property:</b> Tangent's constant mode         ")
    TangentMode=property(doc="<b>Read Write Property:</b> Tangeant calculation method.         ")
    Tension=property(doc="<b>Read Write Property:</b> Tension (TCB).         ")
    Time=property(doc="<b>Read Write Property:</b> Time of key.         ")
    Value=property(doc="<b>Read Write Property:</b> Value of Key         ")
    pass

class FBParity (object):
    """
    Parity modes.     
        
    """
    kFBParityNone=property(doc="No parity.         ")
    kFBParityOdd=property(doc="Odd parity.         ")
    kFBParityEven=property(doc="Even parity.         ")
    pass

class FBTimeReferential (object):
    """
    FBCommandState.     
        
    """
    kFBTimeReferentialAction=property(doc="Action.         ")
    kFBTimeReferentialShot=property(doc="Shot.         ")
    kFBTimeReferentialEdit=property(doc="Edit.         ")
    pass

class FBEvaluateInfo (object):
    """
    AnimationNodeNotify evaluation information.     
    This structure is passed to the AnimationNodeNotify calls (in Constraints, Devices, and Boxes), giving the connectors information with regards to the start or stop times of the evaluation. In general, only the start time is of interest for the current evaluation cycle. The advantage of the structure is to have a common time for the evaluation of all the elements in the scene.     
    """
    def GetEvaluationID(self):
        """
        Return the wanted timer sync count (internal or external).

        return : sync count or <b>-1</b> if no sync is present 
        """
        pass

    def GetLocalStart(self):
        """
        Return local (scene) start time.

        return : Local start time. 
        """
        pass

    def GetLocalStop(self):
        """
        Return local (scene) stop time.

        return : Local stop time. 
        """
        pass

    def GetSyncCount(self):
        """
        Return the wanted timer sync count (internal or external).

        return : sync count or <b>-1</b> if no sync is present 
        """
        pass

    def GetSystemStart(self):
        """
        Return system start time.

        return : System start time. 
        """
        pass

    def GetSystemStop(self):
        """
        Return system start time.

        return : System stop time. 
        """
        pass

    def IsStop(self):
        """
        Is local time stopped? (ie: no animation).

        return : <b>true</b> if local time is stopped. 
        """
        pass

    pass

class FBObjectPoseMirrorOptionsFlag (object):
    """
    ObjectPoseMirrorOptions flags.     
        
    """
    kFBObjectPoseMirrorOptionsNoFlag=property(doc="        ")
    kFBObjectPoseMirrorOptionsUpdateLocal=property(doc="        ")
    kFBObjectPoseMirrorOptionsUpdateLocalMirrorParent=property(doc="        ")
    kFBObjectPoseMirrorOptionsUpdateLocalRef=property(doc="        ")
    kFBObjectPoseMirrorOptionsUpdateLocalRefMirrorRef=property(doc="        ")
    pass

class FBControlSetType (object):
    """
    Character ControlSet type.     
        
    """
    kFBControlSetTypeNone=property(doc="        ")
    kFBControlSetTypeFKIK=property(doc="        ")
    kFBControlSetTypeIKOnly=property(doc="        ")
    pass

class FBTCPIPSocketType (object):
    """
    Types of TCP/IP Sockets.     
        
    """
    kFBTCPIP_Stream=property(doc="Streaming data (TCP).         ")
    kFBTCPIP_DGRAM=property(doc="Datagrams (UDP).         ")
    kFBTCPIP_RAW=property(doc="Raw data (TCP).         ")
    pass

class FBAccessMode (object):
    """
    pyfbsdk     
    Data access modes.     
    """
    kFBAccessModeDisk=property(doc="Access data directly to disk using a cache system.         ")
    kFBAccessModeMemory=property(doc="Access data from memory, which means that it will copyed entirely into it.         ")
    pass

class FBViewingOptions (object):
    """
    Viewing options for rendering.     
    The FBRenderer allows to get and set those options.     
    """
    DisplayMode=property(doc="<b>Read Write Property:</b> Current Shading mode         ")
    DisplayWhat=property(doc="<b>Read Write Property:</b> current display mask.         ")
    PickingMode=property(doc="<b>Read Write Property:</b> Reference to the current picking mode.         ")
    ShowTimeCode=property(doc="<b>Read Write Property:</b> Show Time Code when rendering.         ")
    ShowSafeArea=property(doc="<b>Read Write Property:</b> Show Safe Area when rendering.         ")
    ShowCameraLabel=property(doc="<b>Read Write Property:</b> Show Camera Label when rendering.         ")
    pass

class FBPropertyListNormalIndex (object):
    """
        
        
    """
    pass

class FBShadowFrameType (object):
    """
    Shadow calculation methods.     
        
    """
    kFBShadowFrameTypeShadowReceiver=property(doc="Bases the shadow calculation on the shadow of the receiver.         ")
    kFBShadowFrameTypeShadowCaster=property(doc="Bases the shadow calculation on the shadow of the caster.         ")
    kFBShadowFrameTypeShadowCubeMap=property(doc="Undocumented or unsupported.         ")
    pass

class FBCharacterPoseKeyingMode (object):
    """
    Character Pose Keying Mode.     
        
    """
    kFBCharacterPoseKeyingModeInvalid=property(doc="        ")
    kFBCharacterPoseKeyingModeFullBody=property(doc="        ")
    kFBCharacterPoseKeyingModeBodyPart=property(doc="        ")
    kFBCharacterPoseKeyingModeCount=property(doc="        ")
    pass

class FBPropertyListAnimationNode (object):
    """
    List of animation nodes.     
        
    """
    def FindByLabel(self,pNodeLabel):
        """
        Returns the animation node from its label.

        pNodeLabel : Label of the searched animation node. 
        return : AnimationNode found. 
        """
        pass

    pass

class FBPropertyListCharacterFace (FBPropertyListComponent):
    """
        
        
    """
    def FBPropertyListCharacterFace(self):
        """
        """
        pass

    pass

class FBPropertyListObjectPose (FBPropertyListComponent):
    """
        
        
    """
    def FBPropertyListObjectPose(self):
        """
        """
        pass

    pass

class FBProperty (FBPlug):
    """
    Generic application property.     
    FBProperty objects cannot be instantiated by the user. Reference to a property can be obtained either via an instance of a FBComponent object, or by calling the method 'Find()' of a FBPropertyManager. The class FBComponent has a FBPropertyManager data member named 'PropertyList'.When accessing a FBProperty object via its containing object, you can get or set (assuming it is not read-only) its value directly:       lObject.Visibility = True   When accessing a property reference directly, its value is obtained via it's 'Data' member.       lProp = lObject.PropertyList.Find( 'Visibility' )      if lProp: lProp.Data = True   The methods 'PropertyCreate()' and 'PropertyRemove' of the class FBComponent can be used to modify an object's set of properties.     
    """
    def FBProperty(self):
        """
        Constructor.

        """
        pass

    def GetMax(self):
        """
        GetMax.

        return : Maximum value for the property. 
        """
        pass

    def GetMin(self):
        """
        GetMin.

        return : Minimum value for the property. 
        """
        pass

    def GetName(self):
        """
        Get the property's name.

        return : The property's name. 
        """
        pass

    def GetPropertyFlag(self,pFlag):
        """
        GetPropertyFlag.

        pFlag : Flag to test if it is True or False. 
        return : If the flag is True, the function returns True and vice-versa. 
        """
        pass

    def GetPropertyFlags(self):
        """
        GetPropertyFlags.

        return : Return all flags at once. 
        """
        pass

    def GetPropertyType(self):
        """
        Get the property's type.

        return : The property's type. 
        """
        pass

    def GetPropertyTypeName(self):
        """
        Get the property's type name.

        return : The property's type name. 
        """
        pass

    def IsAnimatable(self):
        """
        Verify if property is of this type.

        return : <b>true</b> if property is of type. 
        """
        pass

    def IsInternal(self):
        """
        Verify if property is of this type.

        return : <b>true</b> if property is of type. 
        """
        pass

    def IsList(self):
        """
        Verify if property is of this type.

        return : <b>true</b> if property is of type. 
        """
        pass

    def IsMaxClamp(self):
        """
        Indicate if maximum value clamping will be applied on user input value.

        return : <b>true</b> if property the value will be clamped to a maximum value. 
        """
        pass

    def IsMinClamp(self):
        """
        Indicate if minimum value clamping will be applied on user input value.

        return : <b>true</b> if property the value will be clamped to a minimum value. 
        """
        pass

    def IsObjectList(self):
        """
        Indicate if is an instance of FBPropertyListObject.

        """
        pass

    def IsReadOnly(self):
        """
        Is property read-only?

        return : <b>true</b> if property is read-only. 
        """
        pass

    def IsReferenceProperty(self):
        """
        Verify if property is of this type.

        return : <b>true</b> if property is of type. 
        """
        pass

    def IsUserProperty(self):
        """
        Verify if property is of this type.

        return : <b>true</b> if property is of type. 
        """
        pass

    def SetMax(self,pMax,pForceMaxClamp):
        """
        SetMax.

        pMax : Maximum value of the property. 
        pForceMaxClamp : Force clamping to maximum value of the property. 
        """
        pass

    def SetMin(self,pMin,pForceMinClamp):
        """
        SetMin.

        pMin : Minimum value of the property. 
        pForceMinClamp : Force clamping to minimum value of the property. 
        """
        pass

    Name=property(doc="<b>Read Property:</b> The property's name.         ")
    Data=property(doc="<b>Read Write Property:</b> The property data value. Type of this depends on the subclass of FBProperty (ex: in a FBPropertyInt, Data is of type int).         ")
    pass

class FBPropertyListDeck (FBPropertyListComponent):
    """
        
        
    """
    def FBPropertyListDeck(self):
        """
        """
        pass

    pass

class FBEventShow (FBEvent):
    """
    Show event class.     
        
    """
    def FBEventShow(self,pEvent):
        """
        Constructor.

        pEvent : Base event (internal) to obtain information from. 
        """
        pass

    Shown=property(doc="<b>Read Only Property:</b> Was layer just shown?         ")
    pass

class FBPropertyListVideoClip (FBPropertyListComponent):
    """
        
        
    """
    def FBPropertyListVideoClip(self):
        """
        """
        pass

    pass

class FBPropertyListTake (FBPropertyListComponent):
    """
        
        
    """
    def FBPropertyListTake(self):
        """
        """
        pass

    pass

class FBPropertyListLight (FBPropertyListComponent):
    """
        
        
    """
    def FBPropertyListLight(self):
        """
        """
        pass

    pass

class FBEventConnectionDataNotify (FBEvent):
    """
    Connection notify event class.     
        
    """
    def FBEventConnectionDataNotify(self,pEvent):
        """
        Constructor.

        pEvent : Base event (internal) to obtain information from. 
        """
        pass

    Action=property(doc="<b>Read Only Property:</b> Connection's action performed.         ")
    Plug=property(doc="<b>Read Only Property:</b> The plug involved in the action.         ")
    pass

class FBPropertyListCamera (FBPropertyListComponent):
    """
        
        
    """
    def FBPropertyListCamera(self):
        """
        """
        pass

    pass

class FBPropertyListMaterial (FBPropertyListComponent):
    """
        
        
    """
    def FBPropertyListMaterial(self):
        """
        """
        pass

    pass

class FBEventSpread (FBEvent):
    """
    Spreadsheet event.     
        
    """
    def FBEventSpread(self,pEvent):
        """
        Constructor.

        pEvent : Base event (internal) to obtain information from. 
        """
        pass

    Action=property(doc="<b>Read Only Property:</b> Action associated to the spread event.         ")
    Column=property(doc="<b>Read Only Property:</b> Column of event.         ")
    Row=property(doc="<b>Read Only Property:</b> Row of event.         ")
    pass

class FBEventConnectionStateNotify (FBEvent):
    """
    Connection notify event class.     
        
    """
    def FBEventConnectionStateNotify(self,pEvent):
        """
        Constructor.

        pEvent : Base event (internal) to obtain information from. 
        """
        pass

    Action=property(doc="<b>Read Only Property:</b> Connection's action performed.         ")
    Plug=property(doc="<b>Read Only Property:</b> The plug involved in the action.         ")
    pass

class FBPropertyListPose (FBPropertyListComponent):
    """
        
        
    """
    def FBPropertyListPose(self):
        """
        """
        pass

    pass

class FBEventInput (FBEvent):
    """
    Input event class.     
        
    """
    def FBEventInput(self,pEvent):
        """
        Constructor.

        pEvent : Base event (internal) to obtain information from. 
        """
        pass

    InputType=property(doc="<b>Read Only Property:</b> Input type.         ")
    Key=property(doc="<b>Read Only Property:</b> Input key.         ")
    KeyState=property(doc="<b>Read Only Property:</b> State of key.         ")
    MouseButton=property(doc="<b>Read Only Property:</b> Mouse Button.         ")
    X=property(doc="<b>Read Only Property:</b> Mouse X Position.         ")
    Y=property(doc="<b>Read Only Property:</b> Mouse Y Position.         ")
    pass

class FBPropertyListAudioClip (FBPropertyListComponent):
    """
        
        
    """
    def FBPropertyListAudioClip(self):
        """
        """
        pass

    pass

class FBPropertyListUserObject (FBPropertyListComponent):
    """
        
        
    """
    def FBPropertyListUserObject(self):
        """
        """
        pass

    pass

class FBPropertyListCharacter (FBPropertyListComponent):
    """
        
        
    """
    def FBPropertyListCharacter(self):
        """
        """
        pass

    pass

class FBPropertyListPhysicalProperties (FBPropertyListComponent):
    """
        
        
    """
    def FBPropertyListPhysicalProperties(self):
        """
        """
        pass

    pass

class FBPropertyListShader (FBPropertyListComponent):
    """
        
        
    """
    def FBPropertyListShader(self):
        """
        """
        pass

    pass

class FBPropertyListObject (FBPropertyListComponent):
    """
    List-like structure fo system elements.     
    This container supports most of the list interface, but is limited to contain only FBComponent objects. New objects can be added, or objects in the list can be removed. The cardinality of the list and the use of the contained object will vary according the container object type. This class supports slice access for query, but not for assignment.     
    """
    def FBPropertyListObject(self):
        """
        Constructor.

        """
        pass

    def SetSingleConnect(self,pSingleConnect):
        """
        Set if the connection is single or multiple.

        pSingleConnect : set to true for only one connection allowed. 
        """
        pass

    def GetSingleConnect(self):
        """
        Get if the connection support only one connection.

        return : true is the connection support only one connection. 
        """
        pass

    pass

class FBPropertyListControlSet (FBPropertyListComponent):
    """
        
        
    """
    def FBPropertyListControlSet(self):
        """
        """
        pass

    pass

class FBPropertyListAudioIn (FBPropertyListComponent):
    """
        
        
    """
    def FBPropertyListAudioIn(self):
        """
        """
        pass

    pass

class FBEventResize (FBEvent):
    """
    Event sent to a control that resizes.     
        
    """
    def FBEventResize(self,pEvent):
        """
        Constructor.

        pEvent : Base event (internal) to obtain information from. 
        """
        pass

    Height=property(doc="<b>Property:</b> New Height of the window.         ")
    Width=property(doc="<b>Property:</b> New Width of the window.         ")
    pass

class FBEventMenu (FBEvent):
    """
    Menu event.     
        
    """
    def FBEventMenu(self,pEvent):
        """
        Constructor.

        pEvent : Base event object. 
        """
        pass

    Id=property(doc="<b>Read Write Property:</b> Id number for menu item.         ")
    Name=property(doc="<b>Read Write Property:</b> Name of menu item.         ")
    pass

class FBPropertyListAudioOut (FBPropertyListComponent):
    """
        
        
    """
    def FBPropertyListAudioOut(self):
        """
        """
        pass

    pass

class FBEventDragAndDrop (FBEvent):
    """
    Drag and drop interface.     
        
    """
    def FBEventDragAndDrop(self,pEvent):
        """
        Constructor.

        pEvent : Base event (internal) to obtain information from. 
        """
        pass

    def Accept(self):
        """
        Accept a drag and drop sequence.
        This will cause the region in question to accept a drag and drop action when this event occurs.

        """
        pass

    def Add(self,pComponent,pId):
        """
        Add an item to the drag and drop list.

        pComponent : Item to add to the list. 
        pId : User-defined reference for the item (default = 0 ). 
        """
        pass

    def Clear(self):
        """
        Clear drag and drop list.

        """
        pass

    def Get(self,pIndex):
        """
        Get the FBComponent specified by <b>pIndex</b> from the Drag and Drop list.

        pIndex : Index in list where to get FBComponent. 
        return : Handle to FBComponent in list at <b>pIndex</b>. 
        """
        pass

    def GetCount(self):
        """
        Get the number of items in the DragAndDrop list.

        return : Number of items in DragAndDrop list. 
        """
        pass

    Components=property(doc="<b>Read Property:</b> List of components drop. (it acces the same data as FBEventDragAndDrop.Get)         ")
    Data=property(doc="<b>Property:</b> User specified reference. (for example, FBSpread:row)         ")
    PosX=property(doc="<b>Property:</b> X position of mouse.         ")
    PosY=property(doc="<b>Property:</b> Y position of mouse.         ")
    State=property(doc="<b>Property:</b> Drag and drop sub-event.         ")
    pass

class FBPropertyListActorFace (FBPropertyListComponent):
    """
        
        
    """
    def FBPropertyListActorFace(self):
        """
        """
        pass

    pass

class FBPropertyListActor (FBPropertyListComponent):
    """
        
        
    """
    def FBPropertyListActor(self):
        """
        """
        pass

    pass

class FBPropertyListMarkerSet (FBPropertyListComponent):
    """
        
        
    """
    def FBPropertyListMarkerSet(self):
        """
        """
        pass

    pass

class FBEventSceneChange (FBEvent):
    """
    Select model event class.     
    This event occurs every time a model is:(un)selectedaddeddestroyedrenamed, etc..     
    """
    def FBEventSceneChange(self,pEvent):
        """
        Constructor.

        pEvent : Base event (internal) to obtain information from. 
        """
        pass

    ChildComponent=property(doc="<b>Read Only Property:</b> Child component of the event.         ")
    Component=property(doc="<b>Read Only Property:</b> Modified component         ")
    Type=property(doc="<b>Read Only Property:</b> Type of selection event.         ")
    pass

class FBPropertyListGroup (FBPropertyListComponent):
    """
        
        
    """
    def FBPropertyListGroup(self):
        """
        """
        pass

    pass

class FBPropertyListConstraintSolver (FBPropertyListComponent):
    """
        
        
    """
    def FBPropertyListConstraintSolver(self):
        """
        """
        pass

    pass

class FBPropertyListSet (FBPropertyListComponent):
    """
        
        
    """
    def FBPropertyListSet(self):
        """
        """
        pass

    pass

class FBPropertyListCharacterPose (FBPropertyListComponent):
    """
        
        
    """
    def FBPropertyListCharacterPose(self):
        """
        """
        pass

    pass

class FBEventDblClick (FBEvent):
    """
    Input event class.     
        
    """
    def FBEventDblClick(self,pEvent):
        """
        Constructor.

        pEvent : Base event (internal) to obtain information from. 
        """
        pass

    Selection=property(doc="<b>Read Only Property:</b> Id of selection.         ")
    pass

class FBPropertyListVideoOut (FBPropertyListComponent):
    """
        
        
    """
    def FBPropertyListVideoOut(self):
        """
        """
        pass

    pass

class FBPropertyListFolder (FBPropertyListComponent):
    """
        
        
    """
    def FBPropertyListFolder(self):
        """
        """
        pass

    pass

class FBEventTakeChange (FBEvent):
    """
    Take change event class.     
    This event occurs every time a take is:addeddestroyedrenamedselected, etc.     
    """
    def FBEventTakeChange(self,pEvent):
        """
        Constructor.

        pEvent : Base event (internal) to obtain information from. 
        """
        pass

    Take=property(doc="<b>Read Only Property:</b> The take modified.         ")
    Type=property(doc="<b>Read Only Property:</b> Type of take change event.         ")
    pass

class FBEventTree (FBEvent):
    """
    FBTree node event.     
        
    """
    def FBEventTree(self,pEvent):
        """
        Constructor.

        pEvent : Base event (internal) to obtain information from. 
        """
        pass

    TreeNode=property(doc="<b>Read Write Property:</b> Tree node.         ")
    Why=property(doc="<b>Read Write Property:</b> Reason of the event.         ")
    pass

class FBPropertyListConstraint (FBPropertyListComponent):
    """
        
        
    """
    def FBPropertyListConstraint(self):
        """
        """
        pass

    pass

class FBPropertyListHandle (FBPropertyListComponent):
    """
        
        
    """
    def FBPropertyListHandle(self):
        """
        """
        pass

    pass

class FBEventTransaction (FBEvent):
    """
    Transaction event.     
        
    """
    def FBEventTransaction(self,pEvent):
        """
        Constructor.

        pEvent : Base event object. 
        """
        pass

    IsBeginTransaction=property(doc="<b>Read Only Property:</b> Tells if the transaction is at begin.         ")
    pass

class FBPropertyListTexture (FBPropertyListComponent):
    """
        
        
    """
    def FBPropertyListTexture(self):
        """
        """
        pass

    pass

class FBEventConnectionNotify (FBEvent):
    """
    Connection notify event class.     
        
    """
    def FBEventConnectionNotify(self,pEvent):
        """
        Constructor.

        pEvent : Base event (internal) to obtain information from. 
        """
        pass

    Action=property(doc="<b>Read Only Property:</b> Connection's action performed.         ")
    ConnectionType=property(doc="<b>Read Only Property:</b> Connection's type.         ")
    DstPlug=property(doc="<b>Read Only Property:</b> The destination plug involved in the action.         ")
    NewPlug=property(doc="<b>Read Only Property:</b> New plug created by the action. (Mostly used by merge/replace)         ")
    SrcIndex=property(doc="<b>Read Only Property:</b> Index of the source in the destination component.         ")
    SrcPlug=property(doc="<b>Read Only Property:</b> The source plug involved in the action.         ")
    pass

class FBPropertyListVideoIn (FBPropertyListComponent):
    """
        
        
    """
    def FBPropertyListVideoIn(self):
        """
        """
        pass

    pass

class FBPropertyListDevice (FBPropertyListComponent):
    """
        
        
    """
    def FBPropertyListDevice(self):
        """
        """
        pass

    pass

class FBComponent (FBPlug):
    """
    Basic Open Reality SDK Element.     
    There are 2 reasons for the existence of this base class: 1- To encapsulate internal application object so that they can be exposed to the Open Reality SDK. 2- To be used as the base class of an object that has one or more FBProperty-type data members. The FBComponent class is used to encapsulate objects which have FBProperty data members.     
    """
    def FBComponent(self):
        """
        Constructor.

        """
        pass

    def ClassName(self):
        """
        Get the class name.

        return : The class name (i.e. "FBComponent"). 
        """
        pass

    def DisableObjectFlags(self,pFlags):
        """
        Disable a specific Object Flags.

        pFlags : Flags to disable. 
        """
        pass

    def EnableObjectFlags(self,pFlags):
        """
        Enable a specific Object Flags.

        pFlags : Flags to enable. 
        """
        pass

    def FBCreate(self):
        """
        Open Reality Creation function.

        return : Outcome of creation (true/false). 
        """
        pass

    def FBDelete(self):
        """
        Open Reality Deletion function.

        """
        pass

    def FBDestroy(self):
        """
        Open Reality Destruction function.

        """
        pass

    def GetObjectFlags(self):
        """
        Get all Object Flags (concatenated).

        return : Get all object flags in one call. Flags can be concatenated. 
        """
        pass

    def GetObjectStatus(self,pStatus):
        """
        Check to see if an object status is enabled.

        pStatus : Status to query. 
        """
        pass

    def HasObjectFlags(self,pFlags):
        """
        Check to see if a specific object flag is enabled.

        pFlags : Flags to check if they are present. 
        return : True if all flags in pFlags are enabled. 
        """
        pass

    def Is(self,pTypeId):
        """
        Returns true if object is of type TypeId.

        pTypeId : TypeId to compare object to. 
        return : Result of the comparison. 
        """
        pass

    def ProcessNamespaceHierarchy(self,pNamespaceAction,pNamespaceName,pReplaceTo,pAddRight):
        """
        ProcessNamespaceHierarchy.
        This function is a recursive function that will go through the whole hierarchy(childs) to add/replace the prefix If you need to work on a single object, use the ProcessObjectPrefix function

        pNamespaceAction : Indicate which operation to do on the hierarchy(childs). 
        pNamespaceName : Indicate the Namespace name on Add/Delete or the prefix to replace in case of replace 
        pReplaceTo : Indicate the new Namespace Name or NULL in case of Add or delete 
        pAddRight : indicate if we add the namespace on right most or left most side or other namespace 
        """
        pass

    def ProcessObjectNamespace(self,pNamespaceAction,pNamespaceName,pReplaceTo,pAddRight):
        """
        ProcessObjectNamespace.
        This function is the same as ProcessNamespaceHierarchy except that it will apply only on the current object and won't be apply to the object childs

        pNamespaceAction : FBNamespaceAction
        pNamespaceName : str
        pReplaceTo : str
        pAddRight : bool
        """
        pass

    def PropertyAdd(self,Property):
        """
        Add a Property to the component's Property manager.

        Property : The property to add to the property manager. 
        return : Index in the property array where <b>Property</b> was inserted. 
        """
        pass

    def PropertyCreate(self,pName,pType,pDataType,pAnimatable,pIsUser,pReferenceSource):
        """
        Create user or dynamic property.

        pName : The name of the property. 
        pType : Type of the property see enum FBPropertyType. 
        pDataType : DataType of the property is a text define in ANIMATIONNODE_TYPE_??? in fbdata.h. 
        pAnimatable : To specify if the property can be animated. 
        pIsUser : To specify if the property is available as a custom property or dynamic and attached to the object. 
        pReferenceSource : Use that param to specify the property that a reference refer to. 
        """
        pass

    def PropertyRemove(self,Property):
        """
        Remove a Property from the component's Property manager.
        If the property was dynamically allocated, it will be deleted

        Property : The property to remove from the property manager. 
        """
        pass

    def SetObjectFlags(self,pFlags):
        """
        SetObjectFlags.

        pFlags : Set flags values. Important note: this function overwrite all flags with those passed in parameter. 
        """
        pass

    def SetObjectStatus(self,pStatus,pValue):
        """
        Enable/Disable a specific Object Status.

        pStatus : Status to change. 
        pValue : Value to change the status to. 
        """
        pass

    Components=property(doc="<b>List:</b> List of components.         ")
    LongName=property(doc="<b>Read Write Property:</b> Name and namespace for object.         ")
    Name=property(doc="<b>Read Write Property:</b> Unique name of object.         ")
    Parents=property(doc="<b>List:</b> Parents.         ")
    PropertyList=property(doc="<b>Read Only Property:</b> Manages all of the properties for the component.         ")
    Selected=property(doc="<b>Read Write Property:</b> Selected property.         ")
    pass

class FBEventActivate (FBEvent):
    """
    Activation event.     
        
    """
    def FBEventActivate(self,pEvent):
        """
        Constructor.

        pEvent : Base event (internal) to obtain information from. 
        """
        pass

    Data=property(doc="<b>Read Write Property:</b> Generic data of event.         ")
    pass

class FBPropertyListCharacterExtension (FBPropertyListComponent):
    """
    Character extension property list.     
        
    """
    def FBPropertyListCharacterExtension(self):
        """
        """
        pass

    pass

class FBEventExpose (FBEvent):
    """
    Event sent when a control needs to be displayed.     
        
    """
    def FBEventExpose(self,pEvent):
        """
        Constructor.

        pEvent : Base event (internal) to obtain information from. 
        """
        pass

    pass

class FBPropertyListNote (FBPropertyListComponent):
    """
        
        
    """
    def FBPropertyListNote(self):
        """
        """
        pass

    pass

class FBEventTreeSelect (FBEvent):
    """
    FBTree selection event.     
        
    """
    def FBEventTreeSelect(self,pEvent):
        """
        Constructor.

        pEvent : Base event (internal) to obtain information from. 
        """
        pass

    TreeNode=property(doc="<b>Read Write Property:</b> Selected tree node.         ")
    pass

class FBAssetMng (FBComponent):
    """
    The FBAssetMng class.     
        
    """
    def FBAssetMng(self,pName):
        """
        Constructor.

        pName : Name of Command. 
        """
        pass

    def BrowseForFile(self):
        """
        Let the user browse the asset database to select a file.

        return : A file object representing the file that was selected, or NULL if none. 
        """
        pass

    def BrowseForFolder(self):
        """
        Let the user browse the asset database to select a folder.

        return : A HFBAssetFolder object representing the folder that was selected, or NULL if none. 
        """
        pass

    def CheckAvailability(self):
        """
        Check if this manager can be used on the computer.

        """
        pass

    def CreateServerPath(self,pServerPath):
        """
        Create a folder path on the server side by adding each missing folders.

        pServerPath : The path to create on the server side. 
        return : A HFBAssetFolder object representing the deepest folder of the path. 
        """
        pass

    def FileIsManaged(self,pFilename):
        """
        Is the specified local file managed (ie.
        also present in the database).

        pFilename : Path to the file on the local disk. 
        return : A boolean indicating if the file is managed or not. 
        """
        pass

    def GetAssetFile(self,pServerFilename):
        """
        Get a file object using it's server path.

        pServerFilename : Path to the file on the server. 
        return : An HFBAssetFile object, or NULL if the file was not found. 
        """
        pass

    def GetAssetFileFromLocalPath(self,pLocalFilename):
        """
        Get a file object using it's local path.

        pLocalFilename : Path to the file on the local disk. 
        return : An HFBAssetFile object, or NULL if the file was not found or no mapping could be done. 
        """
        pass

    def GetAssetFolder(self,pServerPath):
        """
        Get a folder object using it's server path.

        pServerPath : Path the the folder on the server. 
        return : An HFBAssetFolder object, or NULL if the folder was not found. 
        """
        pass

    def GetAssetFolderFromLocalPath(self,pLocalPath):
        """
        Get a folder object using it's local path.

        pLocalPath : Path to the folder on the local disk. 
        return : An HFBAssetFolder object, or NULL if the folder was not found or no mapping could be done. 
        """
        pass

    def GetFileOptions(self):
        """
        Get the file options (i.e.
        what to do when loading, saving or closing managed files).

        return : The options. 
        """
        pass

    def Initialize(self):
        """
        Initialize the connection to the server.

        return : <b>True</b> if the connection was established, <b>false</b> otherwise. 
        """
        pass

    def MapLocalPathToServerPath(self,pLocalPath):
        """
        Convert the local path to a server path by using managed paths mapping.

        pLocalPath : Local path to be mapped. 
        return : A string with the resulting server path, will be empty if the mapping fail. 
        """
        pass

    def ShowSettings(self):
        """
        Display a dialog that let the user changes settings.

        """
        pass

    def WithinManagedPath(self,pLocalPath):
        """
        Is the specified local path below a managed path.

        pLocalPath : Local path to be checked. 
        return : A boolean indicating if the path is within a managed path or not. 
        """
        pass

    Description=property(doc="<b>Read Write Property:</b> Description of the manager.         ")
    LastError=property(doc="Last error string.         ")
    MenuFlags=property(doc="<b>Read Write Property:</b> Flags specifing which menu items are added by the manager.         ")
    Name=property(doc="<b>Read Write Property:</b> Unique Name.         ")
    pass

class FBAnimationNode (FBComponent):
    """
        
        
    """
    def FBAnimationNode(self,pName):
        """
        Constructor.

        pName : Name of animation node (default is NULL). 
        """
        pass

    def ConvertGlobalToNodeTime(self,pKeyTime):
        """
        Convert global time to node time.
        (NOTE: Only used in the context of a story clip)

        pKeyTime : Time of the key to convert. 
        """
        pass

    def ConvertNodeToGlobalTime(self,pKeyTime):
        """
        Convert node time to global time.
        (NOTE: Only used in the context of a story clip)

        pKeyTime : Time of the key to convert. 
        """
        pass

    def GetAnimationToPlay(self):
        """
        Get animation node to play from.

        return : Animation node to be played. 
        """
        pass

    def GetAnimationToRecord(self):
        """
        Get animation node to record to.

        return : Animation node to record to. 
        """
        pass

    def GetDataDoubleArrayCount(self):
        """
        If the DataPtr is of numeric value type .
        .. get the size of the array ex: Light Intensity:1, Translation 3

        return : Size of DataPtr array. 
        """
        pass

    def GetSizeOfData(self):
        """
        Get sizeof void Data Ptr.

        """
        pass

    def IsKey(self):
        """
        Verifies if there is a key at the current.

        return : <b>true</b> if there is a key at the current time. 
        """
        pass

    def KeyAdd(self,pTime,pData):
        """
        Add a key to the animation node.

        pTime : Time to add key at. 
        pData : Value of data to add at <b>pTime</b>. 
        """
        pass

    def KeyAdd(self,pData):
        """
        Add a key to the animation node at current time.

        pData : Value of data to add. 
        """
        pass

    def KeyCandidate(self):
        """
        Keys the current candidate values for current time.

        """
        pass

    def KeyRemove(self):
        """
        Remove key at current time.

        """
        pass

    def SetCandidate(self,Data):
        """
        Set the current candidate values for current time.

        Data : float
        return : <b>true</b> if successful. 
        """
        pass

    def WriteData(self,Data,pEvaluateInfo,pInfoType):
        """
        Write data to animation node.

        Data : Data to write to animation node. 
        pEvaluateInfo : Node evaluation information (access to system and local time). 
        pInfoType : Type of information being written (default is live). 
        return : Status of animation node. 
        """
        pass

    DefaultInterpolation=property(doc="<b>Read Write Property:</b> Default type of interpolation.         ")
    FCurve=property(doc="<b>Read Write Property:</b> FCurve for animation.         ")
    KeyCount=property(doc="<b>Read Only Property:</b> Number of keys.         ")
    Label=property(doc="<b>Read Write Property:</b> Label (UI Name).         ")
    Live=property(doc="<b>Read Write Property:</b> Is animation live?         ")
    Nodes=property(doc="<b>List:</b> List of animation nodes.         ")
    RecordMode=property(doc="<b>Read Write Property:</b> Is the node in recording mode (device connectors)?         ")
    UserName=property(doc="<b>Read Only Property:</b> Name of animation node.         ")
    pass

class FBPropertyColor (FBProperty):
    """
    FBPropertyColor class.     
    Similar in use to FBPropertyVector3d 
@code
    # Supported list protocol methods:
    c = FBPropertyColor()
    len(c)
    print c[0]
    c[0] = 1.0
    print c.Data
    c.Data=FBColor(1.0,0.5,0.5)
@endcode

Slicing is not supported by this object.     
    """
    def __len__(self):
        """
        Returns the number of elements.
        Corresponds to python: len(object)

        """
        pass

    def __getitem__(self,pIndex):
        """
        Returns the ith component Corresponds to python: print c[1].

        pIndex : Index of the components to get (0 to 1) 
        return : Color component value. 
        """
        pass

    def __setitem__(self,pIndex,pComponentValue):
        """
        Sets the ith components Corresponds to python: c[1] = 0.5.

        pIndex : Index of the components to set (0 to 1) 
        pComponentValue : Value of component to set 
        """
        pass

    Data=property(doc="<b>Read Write Property:</b> The property data value. Type of this depends on the subclass of FBProperty (ex: in a FBPropertyInt, Data is of type int).         ")
    pass

class FBFilter (FBComponent):
    """
    Filter class.     
    Filters are objects which can be applied on a FCurve, or the animation node associated with an animated object property, to modify shape and number of keys. Filters can be created from the GUI, using the Filters tool, or programmatically with an instance of a FBFilterManager.The filter properties can be found in the object's PropertyList data member. They will use the same name, and be of the same type, as what can be seen in the GUI.Instances of FBFilter should be created with the help of the class FBFilterManager. Only internal application code should call the FBFilter's class constructor.Sample C++ code: 
@code
    FBFilterManager lFilterManager;

    // Create a filter instace.
    HFBFilter lFilter = lFilterManager.CreateFilter( 'Key Reducing' );

    if( lFilter )
    {
        // Create a FCurve and populate it with keys.
        FBFCurve lCurve( 'Temp Curve' );
        for( int lIdx = 1; lIdx < 10; ++lIdx )
        {
            FBTime lTime( 0, 0, 0, lIdx * 5 );
            lCurve.KeyAdd( lTime, lIdx * 5 );
        }

        FBTrace( 'Keys before: %d\n', lCurve.Keys.GetCount() ); // Should be 9.

        // Apply the key reducing filter.
        lFilter->Apply( &lCurve );

        FBTrace( 'Keys after: %d\n', lCurve.Keys.GetCount() ); // Should be 2.
    }
@endcode

Sample Python code: 
@code
    from pyfbsdk import *

    # Find a given model in the scene.
    lModel = FBFindModelByName( 'Cube' )

    if lModel:
        # Create a Key Reducing filter.
        lFilter = FBFilterManager().CreateFilter( 'Key Reducing' )

        if lFilter:
            # Set the filter's precision to 2.0, and apply it to
            # the object's translation animation.
            lFilter.PropertyList.Find( 'Precision' ).Data = 2.0
            lFilter.Apply( lModel.Translation.GetAnimationNode(), True )
@endcode

     
    """
    def FBFilter(self):
        """
        Constructor.

        """
        pass

    def Apply(self,pCurve):
        """
        Apply the filter to an FCurve.
        This is one of the two apply method that is meant to be called by client code. The FCurve can be a standalone independant FCurve, or can be associated to an object's animated property.

        pCurve : FCurve to apply filter to. 
        return : <b>true</b> if successful. 
        """
        pass

    def Apply(self,pNode,pRecursive):
        """
        Apply the filter to an animation node.
        This is the other apply method and it can be used on an object's animation node.

        pNode : Node to apply filter to. 
        pRecursive : Recursively apply filter on child nodes? 
        return : <b>true</b> if successful. 
        """
        pass

    def Reset(self):
        """
        Reset properties.

        """
        pass

    Start=property(doc="<b>Read Write Property:</b> Start time of the filtering region         ")
    Stop=property(doc="<b>Read Write Property:</b> Stop time of the filtering region         ")
    pass

class FBPropertyComponent (FBProperty):
    """
        
        
    """
    Data=property(doc="<b>Read Write Property:</b> The property data value. Type of this depends on the subclass of FBProperty (ex: in a FBPropertyInt, Data is of type int).         ")
    pass

class FBSet (FBComponent):
    """
    Objects Set class.     
    This class is an interface to manipulate object sets in the scene. Note: an item cannot be in two FBSet objects at once. Also, an FBGroup cannot contain FBSet objects, although an FBSet object can contain an FBGRoup.     
    """
    def FBSet(self,pName):
        """
        Constructor.

        pName : Set name. 
        """
        pass

    def Contains(self,pComponent):
        """
        Contains.

        pComponent : Component to verify if it is in the Group 
        return : 0 if the component is not in the FBSet, 1 if it is in this FBSet, 2 if it is in another FBSet 
        """
        pass

    def FBDelete(self):
        """
        Virtual FBDelete function.

        """
        pass

    def Select(self,pSelect):
        """
        Select.

        pSelect : If <b>true</b>, set contents will be selected. 
        """
        pass

    Items=property(doc="<b>List:</b> Items in the set.         ")
    Pickable=property(doc="<b>Read Write Property:</b> Controls if objects in the set are pickable.         ")
    Transformable=property(doc="<b>Read Write Property:</b> Controls if objects in the set are transformable.         ")
    Visibility=property(doc="<b>Read Write Property:</b> Visibility of set (animatable).         ")
    pass

class FBPropertyStringList (FBProperty):
    """
    
@code
   # Supported list protocol methods:    
    len(propertyListComponent)
    component= propertyListComponent[0]
    propertyListComponent[0] = my_component
 
    if my_competent in propertyListComponent:
       print 'it is contained!'

    del propertyListComponent[0]
@endcode

     
        
    """
    def FBPropertyStringList(self):
        """
        Constructor.

        """
        pass

    def __len__(self):
        """
        Returns the number of elements.
        Corresponds to python: len(object)

        return : number of elements in list. 
        """
        pass

    def __getitem__(self,pIndex):
        """
        Returns the ith component Corresponds to python: print v[1].

        pIndex : Index of the components to get (0 to 2) 
        return : str component value. 
        """
        pass

    def __setitem__(self,pIndex,pValue):
        """
        Sets the ith components Corresponds to python: v[1] = my_component.

        pIndex : Index of the components to set 
        pValue : a str to set 
        """
        pass

    def __contains__(self,pValue):
        """
        Check if a FCComponent is already in PropertyList Corresponds to python: if object in propertyList:.

        pValue : Component to check for inclusion 
        return : Is the String contained or not? 
        """
        pass

    def append(self,pValue):
        """
        Append new str at end of list.

        pValue : to append 
        """
        pass

    def count(self):
        """
        Returns the number of elements.
        Corresponds to python: del propertyList[2]

        return : number of elements in list. 
        """
        pass

    def insert(self,pIndex,pValue):
        """
        Insert a new element in list.

        pIndex : Index where to insert string 
        pValue : String to append 
        """
        pass

    def remove(self,pIndex):
        """
        Remove an element in list.

        pIndex : Index where to remove element. 
        """
        pass

    def pop(self):
        """
        Remove last element of list.

        return : Returns the element that was removed. 
        """
        pass

    def pop(self,pIndex):
        """
        Remove an element in list.

        pIndex : Index where to remove element. 
        return : Returns the element that was removed. 
        """
        pass

    def findFromReference(self,pReference):
        """
        Find the index of an element from its attached reference.

        pReference : Reference of searched object. 
        return : Returns the index of the element corresponding to reference. 
        """
        pass

    def setReferenceAt(self,pReference):
        """
        Sets the reference value of an object.

        pReference : Reference of the object. 
        """
        pass

    def getReferenceAt(self,pIndex):
        """
        Retrieve the reference of an object at ith position.

        pIndex : Index of the object to find reference. 
        return : Returns the reference of the object. 
        """
        pass

    pass

class FBActorFace (FBComponent):
    """
    ActorFace class.     
    <b>These classes are under development and may change dramatically between versions.</b>     
    """
    def FBActorFace(self,pName):
        """
        Constructor.

        pName : Name of new actor face. 
        """
        pass

    def FBDelete(self):
        """
        Actual Actor Face destructor.
        This method is used to delete the actual actor face object represented by an instance of FBActorFace.

        """
        pass

    def PlotAnimation(self):
        """
        Plot the animation of the actor face.

        return : True if the operation completed successfully. 
        """
        pass

    pass

class FBStoryFolder (FBComponent):
    """
    Story Folder class.     
    With folders, you can group tracks together and create different timelines.     
    """
    def FBStoryFolder(self,pParentFolder):
        """
        Constructor.

        pParentFolder : If NULL, parent will be the global root folder, according to its type. 
        """
        pass

    def FBDelete(self):
        """
        Virtual FBDelete function.

        """
        pass

    Childs=property(doc="<b>List:</b> Children folders of this folder.         ")
    Label=property(doc="<b>Read Write Property:</b> Label to display for this story folder.         ")
    Mute=property(doc="<b>Read Write Property:</b> If true, this story folder will be muted.         ")
    Parent=property(doc="<b>Read Only Property:</b> Object pointing to the folder's parent.         ")
    Solo=property(doc="<b>Read Write Property:</b> If true, this story folder will be the only one to play.         ")
    Tracks=property(doc="<b>List:</b> Tracks of this folder.         ")
    pass

class FBStoryClip (FBComponent):
    """
    Story Clip class.     
    Clips represents media, at a specific time, for a specific duration, in a track.     
    """
    def FBStoryClip(self,pClipObject,pTrack,pTime):
        """
        Constructor.

        pClipObject : Object (media data) for the clip. 
        pTrack : The track in which we create the clip. 
        pTime : Time where the clip should begin. 
        """
        pass

    def FBStoryClip(self,pFilePath,pTrack,pTime):
        """
        Constructor.

        pFilePath : Media file path to create clip with. 
        pTrack : The track in which we create the clip. 
        pTime : Time where the clip should begin. 
        """
        pass

    def Clone(self):
        """
        Clone the clip.

        """
        pass

    def ExportToFile(self,pOutputFile):
        """
        ExportToFile.
        Export animation clip to disk file.

        pOutputFile : Output file path name. 
        return : Returns true if successful. 
        """
        pass

    def FBDelete(self):
        """
        Virtual FBDelete function.

        """
        pass

    def GetAffectedAnimationNodes(self,pAffectedAnimationNodes,pClipObject):
        """
        GetAffectedAnimationNodes.
        Get the list of animation nodes affected by this story clip, for a specific object.

        pAffectedAnimationNodes : Array of affected animation nodes, will be filled by the function. 
        pClipObject : The object for which we search for affected animation nodes. 
        """
        pass

    def GetAffectedObjects(self,pAffectedObjects):
        """
        GetAffectedObjects.
        Get the list of objects affected by this story clip.

        pAffectedObjects : Array of affected objects, will be filled by the function. 
        """
        pass

    def Match(self):
        """
        Match.
        Match the animation clip with the specified pivot property.

        """
        pass

    def Move(self,pDelta,pForce):
        """
        Move.
        Move the clip of a delta offset.

        pDelta : Delta time to apply to the clip. 
        pForce : Force clip to find the nearest position if the move fail. 
        return : Return the delta between the new and previous clip's position. 
        """
        pass

    def MoveTo(self,pTime,pForce):
        """
        MoveTo.
        Move the clip to the specified time.

        pTime : Time where to put the clip. 
        pForce : Force clip to find the nearest position if the move fail. 
        return : Returns the new clip's time position. 
        """
        pass

    def Razor(self,pTime):
        """
        Razor.
        Cut (razor) the clip at the specified time.

        pTime : Time where to cut. This time is local to the track, not to the clip. 
        return : Returns the new clip generated by the razor action (right part). 
        """
        pass

    AutoLoop=property(doc="<b>Read Write Property:</b> If true, clip will automatically loop         ")
    Color=property(doc="<b>Read Write Property:</b> Color of the clip.         ")
    Ghost=property(doc="<b>Read Write Property:</b> Show ghosts         ")
    GhostModel=property(doc="<b>Read Write Property:</b> Show ghost of models         ")
    GhostPivot=property(doc="<b>Read Write Property:</b> Show ghost of match object         ")
    GhostTravelling=property(doc="<b>Read Write Property:</b> Show ghost of clip vector or traveling node         ")
    Loop=property(doc="<b>Read Write Property:</b> If true, loop clip's animation         ")
    LoopTranslation=property(doc="<b>Read Write Property:</b> Animation clip's loop translation.         ")
    MarkIn=property(doc="<b>Read Write Property:</b> Start time inside the clip.         ")
    MarkOut=property(doc="<b>Read Write Property:</b> Stop time inside the clip.         ")
    Offset=property(doc="<b>Read Write Property:</b> First loop time offset.         ")
    Pivots=property(doc="<b>List:</b> Pivots models (Generally, only one model is necessary)         ")
    PostBlend=property(doc="<b>Read Write Property:</b> Start/Stop time of the post-blend phase.         ")
    PreBlend=property(doc="<b>Read Write Property:</b> Start/Stop time of the pre-blend phase.         ")
    Rotation=property(doc="<b>Read Write Property:</b> Animation clip's rotation offset.         ")
    Scale=property(doc="<b>Read Write Property:</b> Animation clip's scaling (some don't support this property)         ")
    ShotActionStart=property(doc="<b>Read Write Property:</b> If not in locked shot mode (time discontinuity enabled), this time can be different from the Clip->Start property.         ")
    ShotActionStop=property(doc="<b>Read Write Property:</b> If not in locked shot mode (time discontinuity enabled), this time can be different from the Clip->Start property.         ")
    ShotBackplate=property(doc="<b>Read Write Property:</b> The backplate used for that specific shot.         ")
    ShotCamera=property(doc="<b>Read Write Property:</b> The camera used for that specific shot.         ")
    ShotFrontplate=property(doc="<b>Read Write Property:</b> The frontplate used for that specific shot.         ")
    ShowBackplate=property(doc="<b>Read Write Property:</b> Enable/Disable the shot backplate.         ")
    ShowFrontplate=property(doc="<b>Read Write Property:</b> Enable/Disable the shot frontplate.         ")
    ShowGhostClipMode=property(doc="<b>Read Write Property:</b> Show the ghost depending on the time. See FBStoryClipShowGhostMode         ")
    SolvingMode=property(doc="<b>Read Write Property:</b> Solve Modes for story character clips. See FBStoryClipSolveMode         ")
    Speed=property(doc="<b>Read Write Property:</b> Speed of the clip.         ")
    Start=property(doc="<b>Read Write Property:</b> Start time of the clip local to its track.         ")
    Stop=property(doc="<b>Read Write Property:</b> Stop time of the clip local to its track.         ")
    Translation=property(doc="<b>Read Write Property:</b> Animation clip's translation offset.         ")
    pass

class FBAudioIn (FBComponent):
    """
    Audio In class.     
    Properties of this class are work in progress, but you can still list them and get their names.     
    """
    def FBAudioIn(self):
        """
        Constructor.

        """
        pass

    pass

class FBStoryTrack (FBComponent):
    """
    Story Track class.     
    Tracks are containers for clips (medias), have a specific type which offer different functions.     
    """
    def FBStoryTrack(self,pTrackType,pFolder):
        """
        Constructor.

        pTrackType : Type of the track to be created. 
        pFolder : If NULL, parent will be the global root folder. 
        """
        pass

    def FBStoryTrack(self,pSource,pFolder):
        """
        Constructor.

        pSource : Source of the track to be created based on media component type. 
        pFolder : If NULL, parent will be the global root folder. 
        """
        pass

    def AddClip(self,pClip,pTime):
        """
        AddClip Add the clip to the track.

        pClip : FBComponent
        pTime : FBTime
        """
        pass

    def ChangeDetailsBegin(self):
        """
        ChangeDetailsBegin.
        You must call this function before adding/removing any object to the Details list or it won't work.

        """
        pass

    def ChangeDetailsEnd(self):
        """
        ChangeDetailsEnd.
        You must call this function after adding/removing any object to the Details list or it won't work.

        """
        pass

    def CopyTakeIntoTrack(self,pTimeSpan,pTake,pOutputOffset,pMakeUndoable):
        """
        CopyTakeIntoTrack Copy animation from the specified take for affected objects of the track.

        pTimeSpan : Time span for the clip to create. 
        pTake : Take to get the animation from. 
        pOutputOffset : Time offset for the clip if necessary. 
        pMakeUndoable : If the operation should be undoable. 
        return : Created story clip if the operation succeeded otherwize NULL. 
        """
        pass

    def EnableBodyPart(self,pPart,pEnable):
        """
        EnableBodyPart.

        pPart : Which part to enable/disable. 
        pEnable : If True, this will enable the body part solving while false will disable it. Enable a specific body part for character solving. 
        """
        pass

    def FBDelete(self):
        """
        Virtual FBDelete function.

        """
        pass

    def IsBodyPartEnabled(self,pPart):
        """
        IsBodyPartEnabled.
        Is a specific body part is enabled.

        pPart : FBStoryTrackBodyPart
        """
        pass

    AcceptKey=property(doc="<b>Read Write Property:</b> Allow track to accept keys         ")
    AudioOutIndex=property(doc="<b>Read Write Property:</b> Audio Output's index to use.         ")
    CharacterIndex=property(doc="<b>Read Write Property:</b> Character's index to use.         ")
    Clips=property(doc="<b>List:</b> Clips contained in this track.         ")
    Details=property(doc="<b>List:</b> All objects associated to this track for processing.         ")
    Ghost=property(doc="<b>Read Write Property:</b> Show ghosts         ")
    GhostModel=property(doc="<b>Read Write Property:</b> Show ghost of models         ")
    GhostPivot=property(doc="<b>Read Write Property:</b> Show ghost of match object         ")
    GhostTravelling=property(doc="<b>Read Write Property:</b> Show ghost of clip vector or traveling node         ")
    Label=property(doc="<b>Read Write Property:</b> Label to display for this story track.         ")
    Mute=property(doc="<b>Read Write Property:</b> If true, this track wont' play.         ")
    OffsetEnable=property(doc="<b>Read Write Property:</b> When enabled, allow clip to be offset         ")
    ParentFolder=property(doc="<b>Read Only Property:</b> Parent folder.         ")
    ParentTrack=property(doc="<b>Read Only Property:</b> Parent track, if the track is of Character or Animation type.         ")
    PassThrough=property(doc="<b>Read Write Property:</b> Enable passthrough of animation if there is no clip on track animation is taken from other tracks of take         ")
    ReferenceMode=property(doc="<b>Read Write Property:</b> Track composition mode, kFBStoryTrackOverride or kFBStoryTrackAdditive         ")
    ShowBackplate=property(doc="<b>Read Write Property:</b> If true, the backplate will be shown.         ")
    ShowFrontplate=property(doc="<b>Read Write Property:</b> If true, the frontplate will be shown.         ")
    Solo=property(doc="<b>Read Write Property:</b> If true, this track will be the only one to play.         ")
    SubTracks=property(doc="<b>List:</b> Only Character and Animation tracks can have sub-tracks.         ")
    TrackVideo=property(doc="<b>Read Only Property:</b> This FBVideo can be used as a texture.         ")
    Type=property(doc="<b>Read Only Property:</b> Type of the track         ")
    Weight=property(doc="<b>Read Write Property:</b> Control the blend amount.         ")
    pass

class FBPropertyFloat (FBProperty):
    """
        
        
    """
    Data=property(doc="<b>Read Write Property:</b> The property data value. Type of this depends on the subclass of FBProperty (ex: in a FBPropertyInt, Data is of type int).         ")
    pass

class FBConstraintManager (FBComponent):
    """
    Constraint manager.     
        
    """
    def FBConstraintManager(self):
        """
        Constructor.

        """
        pass

    def TypeCreateConstraint(self,pTypeIndex):
        """
        Create a constraint.
        Given the index in the registry, this will create an instance of this constraint. Note that this constraint is not automatically added to the constraint tool, and must be added manually in order to use in the 'Constraints' tool.

        pTypeIndex : Index of constraint type. 
        return : Newly created constraint. 
        """
        pass

    def TypeGetCount(self):
        """
        Get the number of registered constraint types.

        return : Number of registered constraint types. 
        """
        pass

    def TypeGetName(self,pTypeIndex):
        """
        Get the name of a registered type of constraint.
        This will search in the registry for a constraint at the index <b>pTypeIndex</b>.

        pTypeIndex : Index of a constraint type. 
        return : Name of constraint type. 
        """
        pass

    pass

class FBPropertyEnum (FBProperty):
    """
    Enumeration property.     
    Certain properties have strings associated with the integer values they may possess. FBModel's ShadingMode property is one of those example. The actual underlying value of the property is numerical, but it is represented by a string value in the GUI. User can create this type of property via the GUI by creating a list property. The names added to the list can be obtained via the 'EnumList()' method.     
    """
    def EnumList(self,pIdx):
        """
        pIdx : int
        """
        pass

    Data=property(doc="Return the string associated with the index. Will return None when no value is associated.         ")
    pass

class FBPropertyInt (FBProperty):
    """
        
        
    """
    Data=property(doc="<b>Read Write Property:</b> The property data value. Type of this depends on the subclass of FBProperty (ex: in a FBPropertyInt, Data is of type int).         ")
    pass

class FBPose (FBComponent):
    """
    Pose class.     
        
    """
    def FBPose(self,pName):
        """
        Constructor.

        pName : Name of pose. 
        """
        pass

    def AddNode(self,pObject,pMatrix,pIsLocalMatrix):
        """
        Add a new pose node.

        pObject : The object for which we are creating the pose information. 
        pMatrix : The transformation of the object we want to save. 
        pIsLocalMatrix : Is the matrix a local matrix? 
        """
        pass

    def Find(self,pNodeName):
        """
        Look in this pose if the given node is present.

        pNodeName : Name of the node we are looking for. 
        return : -1 if the node is not in the list or it's position. 
        """
        pass

    def GetNodeCount(self):
        """
        Returns the number of pose nodes stored.

        """
        pass

    def GetNodeMatrix(self,pIndex):
        """
        Get the pose node matrix.

        pIndex : Index of the node. 
        return : a reference to the node's Matrix. 
        """
        pass

    def GetNodeName(self,pIndex):
        """
        Get the pose node at specified index.

        pIndex : Index of the node. 
        """
        pass

    def GetNodeObject(self,pIndex):
        """
        Get the pose node object.

        pIndex : Index of the node. 
        return : a pointer to the node's Object. 
        """
        pass

    def IsNodeLocalMatrix(self,pIndex):
        """
        Get the type of the Matrix for a given node.

        pIndex : Index of the node. 
        return : true if the matrix is defined in Local coordinate space. 
        """
        pass

    def RemoveNode(self,pIndex):
        """
        Remove the pose node at specified index.

        pIndex : Index of the node to be removed. 
        """
        pass

    def SetIsNodeLocalMatrix(self,pIndex,pIsNodeLocalMatrix):
        """
        Set the type of the Matrix for a given node.

        pIndex : Index of the node. 
        pIsNodeLocalMatrix : True if the matrix of the node is a local matrix. 
        """
        pass

    def SetNodeMatrix(self,pIndex,pMatrix):
        """
        Set the pose node matrix.

        pIndex : Index of the node. 
        pMatrix : Matrix to set for this pose node. 
        """
        pass

    def SetNodeObject(self,pIndex,pObject):
        """
        Set the pose node object.

        pIndex : Index of the node. 
        pObject : Object to associate with this pose node. 
        """
        pass

    Type=property(doc="<b>Read Only Property:</b> Type of the pose (bind pose or rest pose)         ")
    pass

class FBFolder (FBComponent):
    """
    Folder class.     
    This class is an interface to manipulate folders in the scene.     
    """
    def FBFolder(self,pName,pComponent):
        """
        Constructor.

        pName : Name to assign to new folder. 
        pComponent : Object used to determine folder's category. 
        """
        pass

    def FBDelete(self):
        """
        Virtual FBDelete function.

        """
        pass

    Items=property(doc="<b>List:</b> List of components in the folder.         ")
    pass

class FBPlayerControl (FBComponent):
    """
    Player control.     
    Interface to use the transport controls.     
    """
    def FBPlayerControl(self):
        """
        Constructor.

        """
        pass

    def GetPlaySpeed(self):
        """
        Get Play Speed .

        return : <b>transport</b> current playback speed. 
        """
        pass

    def GetTransportFps(self):
        """
        Get the UI frame rate use for display configure in the system.

        return : current FrameRate selected for the system. 
        """
        pass

    def GetTransportFpsValue(self):
        """
        Get the UI frame rate value.

        return : current FrameRate value based on the selected FBTimeMode for the system. 
        """
        pass

    def GetTransportMode(self):
        """
        Get Transport Mode.

        return : Current mode of the transport controls. 
        """
        pass

    def Goto(self,pTime):
        """
        Goto a time specified by <b>pTime</b>.

        pTime : Time to jump to. 
        return : <b>true</b> if successful. 
        """
        pass

    def GotoEnd(self):
        """
        GotoEnd button (FastForward).

        return : <b>true</b> if successful. 
        """
        pass

    def GotoNextKey(self):
        """
        Go to the next key.

        """
        pass

    def GotoPreviousKey(self):
        """
        Go to the previous key.

        """
        pass

    def GotoStart(self):
        """
        GotoStart button (Rewind).

        return : <b>true</b> if successful. 
        """
        pass

    def Key(self):
        """
        Key default data.
        Key all selected data.

        """
        pass

    def Play(self,pUseMarkers):
        """
        Play button.

        pUseMarkers : Play until next marker if <b>true</b>, ignore markers otherwise. 
        return : <b>true</b> if successful. 
        """
        pass

    def PlayReverse(self,pUseMarkers):
        """
        Play Reverse button.

        pUseMarkers : Play until next marker if <b>true</b>, ignore markers otherwise. 
        return : <b>true</b> if successful. 
        """
        pass

    def Record(self,pOverrideTake,pCopyData):
        """
        Begin recording.

        pOverrideTake : Write over current take?(default=false) 
        pCopyData : Unused. Necessary for compatibility(default=true). 
        return : <b>true</b> if successful. 
        """
        pass

    def SetPlaySpeed(self,pPlaySpeed):
        """
        Set Play Speed .

        pPlaySpeed : indicate the play speed when a play command occur. 
        """
        pass

    def SetTransportFps(self,pTimeMode,pCustom):
        """
        Set the system frame rate use for display.

        pTimeMode : Indicate the frame rate value to use base on the FBTimeMode values enum.(kFBTimeModeDefault will be stored in fps) 
        pCustom : Should the time mode be kFBTimeModeCustom, this is used to specify the custom framerate. 
        """
        pass

    def StepBackward(self):
        """
        Step one frame backward.

        return : <b>true</b> if successful. 
        """
        pass

    def StepForward(self):
        """
        Step one frame ahead.

        return : <b>true</b> if successful. 
        """
        pass

    def Stop(self):
        """
        Stop button.

        return : <b>true</b> if successful. 
        """
        pass

    IsPlaying=property(doc="<b>Read Only Property:</b> Is the transport control playing?         ")
    IsPlotting=property(doc="<b>Read Only Property:</b> Is there a plotting in progress?         ")
    IsRecording=property(doc="<b>Read Only Property:</b> Is there a recording in progress?         ")
    LoopActive=property(doc="<b>Read Write Property:</b> Is looping active?         ")
    LoopStart=property(doc="<b>Read Write Property:</b> Loop begin time.         ")
    LoopStop=property(doc="<b>Read Write Property:</b> Loop end time.         ")
    NextMarker=property(doc="<b>Read Only Property:</b> Next marked time.         ")
    PlotSamplingPeriod=property(doc="<b>Read Write Property:</b> Sampling period for the model plotting.         ")
    PreviousMarker=property(doc="<b>Read Only Property:</b> Previous marked time.         ")
    RecordingSamplingPeriod=property(doc="<b>Read Write Property:</b> Sampling period for the model recording.         ")
    SnapMode=property(doc="<b>Read Write Property:</b> Set the transport control snap mode.         ")
    TransportTimeFormat=property(doc="<b>Read Write Property:</b> Current Time Mode of the transport controls.         ")
    ZoomWindowStart=property(doc="<b>Read Write Property:</b> Starting time of the transport control zoom window.         ")
    ZoomWindowStop=property(doc="<b>Read Write Property:</b> Stopping time of the transport control zoom window.         ")
    pass

class FBGroup (FBComponent):
    """
    Objects Grouping class.     
    This class is an interface to manipulate object's grouping in the scene.     
    """
    def FBGroup(self,pName):
        """
        Constructor.

        pName : Group name. 
        """
        pass

    def Contains(self,pComponent):
        """
        Contains.

        pComponent : Component to verify if it is in the Group 
        return : True if the object is in the Group 
        """
        pass

    def FBDelete(self):
        """
        Virtual FBDelete function.

        """
        pass

    def Select(self,pSelect):
        """
        Select.

        pSelect : If <b>true</b>, group contents will be selected. 
        """
        pass

    Items=property(doc="<b>List:</b> Items in the group.         ")
    Pickable=property(doc="<b>Read Write Property:</b> Controls if objects in the group are pickable.         ")
    Show=property(doc="<b>Read Write Property:</b> Controls if objects in the group are displayed.         ")
    Transformable=property(doc="<b>Read Write Property:</b> Controls if objects in the group are transformable.         ")
    pass

class FBKeyingGroup (FBComponent):
    """
    KeyingGroup class.     
    This class is an interface to manipulate which properties will be keyed when active A derived class could control when the keying group should activate and what content should have For example a derived class could activate based one what is selected in the scene.To create a custom keying group, use the appropriate FBKeyingGroupType flag. Then, if it is a local keying group, call AddObjectDependency() to add an object to the keying group. You can then add properties belonging to the object you added with AddObjectDependency() using AddProperty().If you are creating an object type keying group, call SetObjectType() to specify what kind of object will be keyed by this keying group. Then, add a property from an object, the name of the property will be use by the keying group the find corresponding properties in selected object.If you create a global keying group, simply add properties from an object with AddProperty(). The name of the property will be used by the keying group to find corresponding properties in selected object.     
    """
    def FBKeyingGroup(self,pName,pType):
        """
        Constructor.

        pName : Group name. 
        pType : Keying group type. 
        """
        pass

    def AddObjectDependency(self,pObj):
        """
        AddObjectDependency An object dependency is the content of a keying group and will activate keying group when selected (activation only works if the keying group is a character extension).

        pObj : a Dependency of the keying group. 
        """
        pass

    def AddProperty(self,pProp):
        """
        Add property to be keyed when current keying group is active.

        pProp : Property to be added. 
        """
        pass

    def ClearAllItems(self):
        """
        ClearAllItems clear object dependency, properties and child keying group.

        """
        pass

    def FBDelete(self):
        """
        Virtual FBDelete function.

        """
        pass

    def FindPropertyIndex(self,pProp):
        """
        FindPropertyIndex.

        pProp : must be in the list (return -1 if not). 
        return : the index of pProp in the keyinggroup property list. 
        """
        pass

    def GetCumulativeProperty(self,pIndex,pStopAtVisible):
        """
        GetCumulativeProperty Same as GetSubKeyingGroup but recursive in child keying group.

        pIndex : index in the content Object Dependency list 
        pStopAtVisible : consider all keying group and stop to the first visible keying group. 
        return : he number of ObjectDependency of the keying group. 
        """
        pass

    def GetCumulativePropertyCount(self,pStopAtVisible):
        """
        GetCumulativePropertyCount Same as GetSubKeyingGroupCount but recursive in child keying group.

        pStopAtVisible : consider all keying group and stop to the first visible keying group. 
        return : he number of ObjectDependency of the keying group. 
        """
        pass

    def GetParentKeyingGroup(self,pIndex):
        """
        GetParentKeyingGroup.

        pIndex : is the index of the parent list of the current keying group. 
        return : the parent keying group. 
        """
        pass

    def GetParentKeyingGroupCount(self):
        """
        GetParentKeyingGroupCount.

        return : the number of parent. 
        """
        pass

    def GetProperty(self,pIndex):
        """
        GetProperty from the keyinggroup list.

        pIndex : index of the desired property. 
        return : property coresponding to pIndex. 
        """
        pass

    def GetPropertyCount(self):
        """
        GetPropertyCount.

        return : the number of properties in the keying group. 
        """
        pass

    def GetSubKeyingGroup(self,pIndex):
        """
        GetSubKeyingGroup.

        pIndex : index of the desired keying group child. 
        return : the the child at the index. 
        """
        pass

    def GetSubKeyingGroupCount(self):
        """
        GetSubKeyingGroupCount.

        return : the number of child keying group. 
        """
        pass

    def GetSubObject(self,pIndex):
        """
        GetSubObject.

        pIndex : index in the content Object Dependency list 
        return : the desired object at pIndex. 
        """
        pass

    def GetSubObjectCount(self):
        """
        GetSubObjectCount.

        return : the number of ObjectDependency of the keying group. 
        """
        pass

    def IsObjectDependency(self,pObj):
        """
        IsObjectDependency determine if the pObj is a dependency.

        pObj : an object to test the Dependency. 
        return : true if it depend. 
        """
        pass

    def IsObjectDependencySelected(self):
        """
        IsObjectDependencySelected.

        return : return true as soon as a Property Owner or another Object Dependency is Selected. 
        """
        pass

    def RemoveAllObjectDependency(self):
        """
        IsObjectDependencySelected empty the content list.

        """
        pass

    def RemoveAllProperties(self):
        """
        IsObjectDependencySelected empty the property list.

        """
        pass

    def RemoveAllSubKeyingGroup(self):
        """
        RemoveAllSubKeyingGroup empty the child keying group.

        """
        pass

    def RemoveObjectDependency(self,pObj):
        """
        RemoveObjectDependency An object dependency is the content of a keying group and will activate keying group when selected (activation only works if the keying group is a character extension).

        pObj : a Dependency of the keying group. 
        """
        pass

    def RemoveProperty(self,pProp):
        """
        RemoveProperty from the keyinggroup list.

        pProp : Property to be removed. 
        """
        pass

    def SetActive(self,pActive):
        """
        SetActive, activate the keying group.

        pActive : bool
        """
        pass

    def SetEnabled(self,pEnable):
        """
        SetEnabled, will make available the keying group in keying group list of the key control UI.

        pEnable : bool
        """
        pass

    def SetObjectType(self,pObject):
        """
        Set the object type filter for and object type keying group.

        pObject : Object that will be used to set the keying group object type. Use NULL to remove the filter. 
        """
        pass

    pass

class FBImage (FBComponent):
    """
    Image class.     
    Utility class used to load and get manipulate image data from disk or memory.     
    """
    def FBImage(self,pFileName):
        """
        Constructor.

        pFileName : Path to the image file. If pObject is not NULL, pFileName will be ignored. 
        """
        pass

    def Cleanup(self):
        """
        Cleanup image data, making it black.

        """
        pass

    def ConvertFormat(self,pNewFormat):
        """
        Convert the image data format to another format.

        pNewFormat : The new format to convert the image to. 
        return : Return true if the convert was successful. 
        """
        pass

    def ConvertSize(self,pWidth,pHeight):
        """
        Convert the image size.

        pWidth : New width of the image. 
        pHeight : New height of the image. 
        return : Return true if the convert was successful. 
        """
        pass

    def FBDelete(self):
        """
        Virtual FBDelete function.

        """
        pass

    def Init(self,pFormat,pWidth,pHeight):
        """
        Init.

        pFormat : Image format used to initialize data buffer. 
        pWidth : Image width in pixels. 
        pHeight : Image height in pixels. 
        """
        pass

    def IsCompressedTif(self,pFileName):
        """
        Query TIF file about its compressed status.

        pFileName : Full TIF file path name of the file to query. 
        return : Return true if the TIF file image data is compressed. 
        """
        pass

    def VerticalFlip(self):
        """
        Flip the image vertically.

        """
        pass

    def WriteToTif(self,pFileName,pComments,pCompressed):
        """
        Write image data to a TIF file on disk.

        pFileName : Full TIF file path name of the file to write. 
        pComments : Comments appended to the TIF file. 
        pCompressed : If true, the image data in the file will be compressed. 
        return : Return true if the image was successfully written on disk. 
        """
        pass

    Depth=property(doc="<b>Read Write Property:</b> Color depth of the image.         ")
    Format=property(doc="<b>Read Write Property:</b> Image data format.         ")
    Height=property(doc="<b>Read Write Property:</b> Height of the image in pixels.         ")
    InterleaveType=property(doc="<b>Read Only Property:</b> Image interleave type. Only meaningful if image type is field.         ")
    InterpolationType=property(doc="<b>Read Only Property:</b> Image interpolation type.         ")
    Type=property(doc="<b>Read Only Property:</b> Image type, refering to either frame or field.         ")
    Width=property(doc="<b>Read Write Property:</b> Width of the image in pixels.         ")
    pass

class FBPropertyAnimatable (FBProperty):
    """
    Animatable property base class.     
        
    """
    def FBPropertyAnimatable(self):
        """
        Constructor.

        """
        pass

    def GetAnimationNode(self):
        """
        Get the animation node for the property.

        return : Animation node for property. None is returned if property is not animated. 
        """
        pass

    def GetBox(self):
        """
        Get the owner box.

        return : Handle to the owning box (i.e. model). 
        """
        pass

    def GetDataTypeName(self):
        """
        Get the property datatype name.

        return : Datatype of property as a character string. 
        """
        pass

    def IsAnimated(self):
        """
        Is the property animated.
        This is true if the property has an FCurve associated to it.

        return : <b>true</b> if animated, <b>false</b> if not animated. 
        """
        pass

    def IsFocused(self):
        """
        Is the property focused (keyable).

        return : Current focus (keyable) state for the property. 
        """
        pass

    def Key(self):
        """
        Key the connector.

        """
        pass

    def SetAnimated(self,pState):
        """
        Set the animation state of the property.

        pState : State of animation for property, true to animate, false to remove curves. 
        """
        pass

    def SetFocus(self,pState):
        """
        Set the property's focus (keyable) state.

        pState : Focus (keyable) state to set for the property. 
        """
        pass

    Data=property(doc="<b>Read Write Property:</b> The property data value. Type of this depends on the subclass of FBPropertyAnimatable (ex: in a FBPropertyAnimatableInt, Data is of type int).         ")
    pass

class FBViewerInfos (FBComponent):
    """
    Scene information display.     
    By modifying the application configuration file, it is possible to display scene related information to the screen. This information will also be present in the rendered frames when creating AVIs or QuickTime files.To use this functionality, it is necessary to edit the config file [MACHINE]-Application.txt located in folder [APPLICATION]/bin/config. Look for the token 'ViewerInfoDisplay' in the section '[Display]' and set its value to 'Enable'.Instances of this class can only be obtained via a FBRenderer object. Do not attempt to create new instances.Do not attempt to destroy instances of this class. The application is the owner of these objects.     
    """
    def FBViewerInfos(self):
        """
        Constructor.

        """
        pass

    Visibility=property(doc="<b>Read Write Property:</b> Indicate if the information will be displayed or not.         ")
    pass

class FBRenderer (FBComponent):
    """
    Open Reality renderer interface.     
        
    """
    def FBRenderer(self):
        """
        Constructor.
        Client code cannot instantiate objects of this class. The FBSystem and FBScene classes provide access to the current renderer.

        """
        pass

    def FrameCurrentCameraWithModels(self,pAll):
        """
        Frame the current camera either with all models or with the currently selected models.

        pAll : true to frame with all models. 
        return : <b>true</b> if successful. 
        """
        pass

    def GetViewingOptions(self):
        """
        Obtain the current viewing options.

        return : A sctructure that can be queried and updated for a call to SetViewingOptions. 
        """
        pass

    def KeyboardInput(self,pKeyIndex,pKeyState,pIsTrigger):
        """
        Keyboard input.

        pKeyIndex : Key index. (See "enum FBDeviceKeyboardKey" above for supported keys) 
        pKeyState : Key state. (True == key is down, False == key is up) 
        pIsTrigger : When setting pKeyState to True, resets key state to False right after operation. 
        """
        pass

    def MouseInput(self,pX,pY,pInputType,pButtonKey,pModifier,pLayer):
        """
        Mouse input.

        pX : X position. 
        pY : Y position. 
        pInputType : Type of input. 
        pButtonKey : Button/Key pressed. 
        pModifier : Modifier pressed (CTRL/ALT/SHIFT). 
        pLayer : Rendering layer ID(default=-1). 
        return : <b>true</b> if successful. 
        """
        pass

    def Pick(self,pX,pY,pPickInfosList,pNeedIntersectPoistion):
        """
        Object picking.

        pX : X position. 
        pY : Y position. 
        pPickInfosList : The list of models hit, and the location of the hit. 
        pNeedIntersectPoistion : require valid intersection position if true, this will take more time to process, and not reliable with very dense mesh. 
        """
        pass

    def PreRender(self,pLayer):
        """
        PreRenders one frame (needed for some shaders) This functions destroys the frame buffer content and must be called every time a render is called the typical order of call must be Renderer->Prerender // at this point the frame buffer is garbage -Clear the ogl -Do your render functions Renderer->Render.

        pLayer : Rendering layer ID(default=-1). 
        return : <b>true</b> if successful. 
        """
        pass

    def Render(self,pLayer):
        """
        Renders one frame.

        pLayer : Rendering layer ID(default=-1). 
        return : <b>true</b> if successful. 
        """
        pass

    def RenderBegin(self,pX,pY,pW,pH):
        """
        RenderBegin.
        must be called before rendering can happen

        pX : X position where to render. 
        pY : Y position where to render. 
        pW : Width of render area. 
        pH : Hight of render area. 
        """
        pass

    def RenderEnd(self,pView):
        """
        RenderEnd.

        pView : If you want the renderer to draw artifacts, such as TimeCode, CameraLabel or SafeArea, you must provide the FBView on which the renderer draws on. 
        """
        pass

    def SetViewingOptions(self,pOptions):
        """
        Set the viewing options.

        pOptions : See FBViewingOptions for more detail. 
        """
        pass

    def SetViewport(self,pX,pY,pW,pH):
        """
        Must be called before inputing if the same renderer is used on multiple views/cameras in the same application.

        pX : X position where to render. 
        pY : Y position where to render. 
        pW : Width of render area. 
        pH : Hight of render area. 
        """
        pass

    AutoEvaluate=property(doc="<b>Read Write Property:</b> Indicate if a call to RenderBegin will also cause a re-evaluation of the scene.         ")
    Background=property(doc="<b>Read Write Property:</b> The renderer.         ")
    ClearColor=property(doc="<b>Read Write Property:</b> Clear color.         ")
    CurrentCamera=property(doc="<b>Read Write Property:</b> Current camera.         ")
    LayerCount=property(doc="<b>Read Write Property:</b> Number of sorting layers.         ")
    Scene=property(doc="<b>Read Write Property:</b> Scene that the renderer will use/draw         ")
    ViewerInfos=property(doc="<b>Read Only Property:</b> Used to display information about the current scene. Will be present in any rendered images.         ")
    ZSortMode=property(doc="<b>Read Write Property:</b> Z sorting method.         ")
    pass

class FBApplication (FBComponent):
    """
    Application class.     
    Permits the manipulation of the application. It should be noted that the Event registration is instanced based. When a FBApplication object is destroyed, all the event callbacks are unregistered. If you want to have a tool to be notified of events, it needs to have a FBApplication data member. Please note that the properties CurrentActor and CurrentCharacter cannot be non NULL at the same time. The character tool will work on only one item at a time. When no item is selected in the tool, both properties will be null.     
    """
    def FBApplication(self):
        """
        Constructor.

        """
        pass

    def ExecuteScript(self,pFilename):
        """
        Execute a python script file.

        pFilename : The script file to execute. 
        return : True if the script file was found and executed. 
        """
        pass

    def FBXFileAppend(self,pFilename,pImportingNamespace):
        """
        Append a file to the current scene.
        Same as File->Merge in the menus with all options set to append.

        pFilename : File to merge. 
        pImportingNamespace : namespace added to all objects in the loaded scene (default=NULL) 
        return : <b>true</b> if successful. 
        """
        pass

    def FBXFileMerge(self,pFilename,pImportingNamespace):
        """
        Merge a file with the current scene.
        Command File->Merge in the menus.

        pFilename : File to merge. 
        pImportingNamespace : namespace added to all objects in the loaded scene (default=NULL) 
        return : <b>true</b> if successful. 
        """
        pass

    def FBXFileOpen(self,pFilename,pImportingNamespace):
        """
        Open a file, replacing the current scene.
        Command File->Open in the menus.

        pFilename : File to open. 
        pImportingNamespace : namespace added to all objects in the loaded scene (default=NULL) 
        return : <b>true</b> if successful. 
        """
        pass

    def FBXFileSave(self,pFilename):
        """
        Save the file under another name.
        Command File->SaveAs in the menus.

        pFilename : Save file as <b>pFilename</b>. A value of NULL will use the current file name. 
        return : <b>true</b> if successful. 
        """
        pass

    def FileAppend(self,pFilename,pShowOptions,pImportingNamespace):
        """
        Append a file to the current scene.
        Same as File->Merge in the menus with all options set to append.

        pFilename : File to merge. 
        pShowOptions : <b>true</b> if options dialog is showed (default=false). 
        pImportingNamespace : namespace added to all objects in the loaded scene (default=NULL) 
        return : <b>true</b> if successful. 
        """
        pass

    def FileBatch(self,pBatchOptions,pPlotOptions):
        """
        Start a batch.
        Command FILE->BATCH in the menus.

        pBatchOptions : The options for the batch process (same as in the batch UI). 
        pPlotOptions : The options for plotting (same as in the plot UI)(default=NULL). 
        return : The status of the operation. 
        """
        pass

    def FileExit(self,pSave):
        """
        Quit application.
        Command FILE->EXIT in the menus.

        pSave : <b>true</b> if file is saved on exit(default=false). 
        """
        pass

    def FileExport(self,pFilename):
        """
        Export a motion file.
        Command FILE->EXPORT in the menus.

        pFilename : The file to create. To create two files at the same time (ex: .amc & .asf), separate the two files path with a comma ("Path1,Path2"). 
        return : True if the export succeeded. 
        """
        pass

    def FileImport(self,pFilename,pMatchModels):
        """
        Import a motion file.
        Command FILE->IMPORT in the menus.

        pFilename : The file to import. To import two files at the same time (ex: .amc & .asf), separate the two files path with a comma ("Path1,Path2"). 
        pMatchModels : If there is already a model in the scene with the same name, the model will not be created and we replace the animation of the given model. If there are models selected in the scene, only these models will be checked for a potential name match. If only one model is selected (ex: hips), this models and its hierarchy will be used. Every unmatched models will be created. 
        return : True if the import succeeded. 
        """
        pass

    def FileMerge(self,pFilename,pShowOptions,pImportingNamespace):
        """
        Merge a file with the current scene.
        Command File->Merge in the menus.

        pFilename : File to merge. 
        pShowOptions : <b>true</b> if options dialog is showed (default=false). 
        pImportingNamespace : namespace added to all objects in the loaded scene (default=NULL) 
        return : <b>true</b> if successful. 
        """
        pass

    def FileNew(self):
        """
        Command FILE->NEW in the menus.

        return : <b>true</b> if successful. 
        """
        pass

    def FileOpen(self,pFilename,pShowOptions,pImportingNamespace):
        """
        Open a file, replacing the current scene.
        Command File->Open in the menus.

        pFilename : File to open. 
        pShowOptions : <b>true</b> if options dialog is showed (default=false). 
        pImportingNamespace : namespace added to all objects in the loaded scene (default=NULL) 
        return : <b>true</b> if successful. 
        """
        pass

    def FileRender(self,pRenderOptions):
        """
        Render current scene to media file.
        Command FILE->RENDER in the menus.

        pRenderOptions : The options used when rendering the scene. If you don't specify them, current one are used. 
        """
        pass

    def FileSave(self,pFilename):
        """
        Save the file under another name.
        Command File->SaveAs in the menus.

        pFilename : Save file as <b>pFilename</b>. A value of NULL will use the current file name. 
        return : <b>true</b> if successful. 
        """
        pass

    def Maximize(self):
        """
        Maximize window (minimized).

        return : Operation was successful (<b>true</b> or <b>false</b>). 
        """
        pass

    def Minimize(self,pBlocking):
        """
        Minimize window.

        pBlocking : Is the minimization blocking operation (default =<b>true</b>). 
        return : Operation was successful (<b>true</b> or <b>false</b>). 
        """
        pass

    def SwitchViewerCamera(self,pCamera):
        """
        Switch the current viewer's camera.

        pCamera : Camera to switch current viewer to. 
        """
        pass

    CurrentActor=property(doc="<b>Read Write Property:</b> Indicate the current actor, as used by the character tool. Can be NULL.         ")
    CurrentCharacter=property(doc="<b>Read Write Property:</b> Indicate the current character, as used by the character tool. Can be NULL.         ")
    FBXFileName=property(doc="<b>Read Write Property:</b> Current scene filename.         ")
    OnFileExit=property(doc="<b>Event:</b> A File Exit as been requested, nothing has been destroyed yet.         ")
    OnFileMerge=property(doc="<b>Event:</b> A File Merge has been requested, nothing has been loaded yet.         ")
    OnFileNew=property(doc="<b>Event:</b> A File New has been requested, nothing has been destroyed yet.         ")
    OnFileNewCompleted=property(doc="<b>Event:</b> A File New has been completed.         ")
    OnFileOpen=property(doc="<b>Event:</b> A File Open has been requested, nothing has been loaded yet.         ")
    OnFileOpenCompleted=property(doc="<b>Event:</b> A File Open has been completed.         ")
    OnFileSave=property(doc="<b>Event:</b> A File Save has been requested, nothing has been saved yet.         ")
    OnFileSaveCompleted=property(doc="<b>Event:</b> A File Save has been completed.         ")
    pass

class FBAssetItem (FBComponent):
    """
    Base class for all managed assets.     
        
    """
    def FBAssetItem(self,pName):
        """
        Constructor.

        pName : Name of Command. 
        """
        pass

    def CheckIn(self,pComment,pKeepCheckedOut,pSilent):
        """
        Checks in this item and all its children (if this is a folder item).

        pComment : Comment to be applied for the check in. 
        pKeepCheckedOut : Flag that indicates whether the item will be kept checked out. 
        pSilent : If pSilent is set to true, no dialog will be displayed by this method. 
        return : A boolean indicating if the operation was successful. 
        """
        pass

    def CheckOut(self,pComment,pDontGetLocal,pSilent):
        """
        Checks out this item and it's childs (if this is a folder item) and makes them writeable on the local disk.

        pComment : Comment to be applied for the check out. 
        pDontGetLocal : Indicate if local copy should retrieved or not. 
        pSilent : If pSilent is set to true, no dialog will be displayed by this method. 
        return : A boolean indicating if the operation was successful. 
        """
        pass

    def GetLatest(self,pReplaceCheckedOut,pSilent):
        """
        Obtain the latest version of the item from the server.

        pReplaceCheckedOut : Whether to replace the checked out file or not. 
        pSilent : If pSilent is set to true, no dialog will be displayed by this method. 
        return : A boolean indicating if the operation was successful. 
        """
        pass

    def GetLocalPath(self):
        """
        Get the path to this item on the local hard disk.

        return : The path as an <b>FBString</b>. 
        """
        pass

    def GetName(self):
        """
        Get the name of this item (file name or folder name).

        return : The name of the item, as an FBString. 
        """
        pass

    def GetParent(self):
        """
        Get the parent folder of this item.

        return : An <b>HFBAssetFolder</b> if the parent was found, or NULL if this is the root item. 
        """
        pass

    def GetServerPath(self):
        """
        Get the path to this item on the database.

        return : The server path as an <b>FBString</b>. 
        """
        pass

    def ShowHistory(self):
        """
        Display a dialog with this item history.

        """
        pass

    def ShowProperties(self):
        """
        Display a dialog showing the properties of this item.

        """
        pass

    def UndoCheckOut(self,pReplaceLocalFile,pSilent):
        """
        Cancel the last check out operation.

        pReplaceLocalFile : Flag indicating if the local item(s) should be replaced by the server version. 
        pSilent : If pSilent is set to true, no dialog will be displayed by this method. 
        return : A boolean indicating if the operation was successful. 
        """
        pass

    LastError=property(doc="Last error string.         ")
    pass

class FBBox (FBComponent):
    """
    Box class.     
    A box is a fundamental building block in the application architecture. All animatable elements derive in some way from the main box class (either by deriving directly or owning a box).     
    """
    def FBBox(self,pName):
        """
        Constructor.

        pName : Box name. 
        """
        pass

    def AnimationNodeDestroy(self,pAnimationNode):
        """
        Destroy an animation node.

        pAnimationNode : Handle to the animation node to be destroyed. 
        return : <b>true</b> if destruction was successful. 
        """
        pass

    def AnimationNodeInGet(self):
        """
        Get the (IN/OUT) animation node for this box.

        return : A handle to the animation node for this box. 
        """
        pass

    def AnimationNodeIsUserData(self,pAnimationNode):
        """
        Is the animation node user data?

        pAnimationNode : Handle to the animation to be queried. 
        return : <b>true</b> if node is user data. 
        """
        pass

    def AnimationNodeOutGet(self):
        """
        Get the (IN/OUT) animation node for this box.

        return : A handle to the animation node for this box. 
        """
        pass

    Animatable=property(doc="<b>Read Write Property:</b> Is the box animatable.         ")
    Live=property(doc="<b>Read Write Property:</b> Is live?         ")
    RecordMode=property(doc="<b>Read Write Property:</b> Is recording?         ")
    UniqueName=property(doc="internal Unique name.         ")
    pass

class FBReferenceTime (FBComponent):
    """
    Reference time class.     
        
    """
    def FBReferenceTime(self):
        """
        Constructor.

        """
        pass

    def Add(self,pName):
        """
        Add a reference time to list.

        pName : Name of time to add the list. 
        return : Number of reference times after operation. 
        """
        pass

    def GetTime(self,pIndex,pSystem):
        """
        Get a reference time.

        pIndex : Index of reference to get. 
        pSystem : System time. 
        return : Reference time at <b>pIndex</b>. 
        """
        pass

    def Remove(self,pIndex):
        """
        Remove a reference time from the list.

        pIndex : Index of reference time to remove. 
        """
        pass

    def SetTime(self,pIndex,pReferenceTime,pSystem):
        """
        Set a reference time.

        pIndex : Index of reference time set. 
        pReferenceTime : Time to use as reference time. 
        pSystem : System time. 
        """
        pass

    Count=property(doc="<b>Read Only Property:</b> Number of reference times.         ")
    ItemIndex=property(doc="<b>Read Write Property:</b> Current reference time index.         ")
    pass

class FBPropertyVector2d (FBProperty):
    """
        
        
    """
    Data=property(doc="<b>Read Write Property:</b> The property data value. Type of this depends on the subclass of FBProperty (ex: in a FBPropertyInt, Data is of type int).         ")
    pass

class FBKeyControl (FBComponent):
    """
    Key control.     
    Interface to use the key controls tool.     
    """
    def FBKeyControl(self):
        """
        Constructor.

        """
        pass

    AutoKey=property(doc="<b>Read Write Property:</b> Enable/Disable Auto Key feature (key when moving 3D objects).         ")
    pass

class FBTake (FBComponent):
    """
    Take class.     
        
    """
    def FBTake(self,pName):
        """
        Constructor.

        pName : Name of take. 
        """
        pass

    def ClearAllProperties(self,pOnSelectedObjectsOnly):
        """
        Clear the animation on all the properties.

        pOnSelectedObjectsOnly : Specify if clear will be performed on all objects or only on the one that are currently selected. 
        """
        pass

    def CopyTake(self,pNewTakeName):
        """
        Copy the take.
        Will create a copy of the current take, with the current take data. This is analogous to creating a new take, and copying the current take data into it. The newly created take is automaticaly added to the scene.

        pNewTakeName : The name for the new take. 
        return : Handle to the newly created take. 
        """
        pass

    def CreateNewLayer(self):
        """
        Create a new layer.

        """
        pass

    def FBDelete(self):
        """
        Deletion method.
        Using this method to delete the take insure that the destruction process follows the same path as if the GUI had been used.

        """
        pass

    def GetCurrentLayer(self):
        """
        Get the current layer for the take.

        return : The current layer index. 
        """
        pass

    def GetLayerCount(self):
        """
        Get the layer count.

        return : The layer count. 
        """
        pass

    def GetLayerName(self,pLayerIndex):
        """
        Get the name of a layer at the specified index.

        pLayerIndex : The index of the layer whose name will be returned. 
        return : Layer name at the specified index. 
        """
        pass

    def PlotAllTakesOnSelected(self,pPlotPeriod):
        """
        Plot the animation on selected models for all takes.
        Will plot the animation for all takes on the selected models in the scene.

        pPlotPeriod : Period for the plot. 
        """
        pass

    def PlotAllTakesOnSelectedProperties(self,pPlotPeriod):
        """
        Plot the animation on selected properties for all takes.
        Will plot the animation for all takes on the selected properties in the scene.

        pPlotPeriod : Period for the plot. 
        """
        pass

    def PlotTakeOnSelected(self,pPlotPeriod):
        """
        Plot the animation on selected models.
        Will plot the animation of the take in question on the selected models in the scene.

        pPlotPeriod : Period for the plot. 
        """
        pass

    def PlotTakeOnSelectedProperties(self,pPlotPeriod):
        """
        Plot the animation on selected properties.
        Will plot the animation of the take in question on the selected properties in the scene.

        pPlotPeriod : Period for the plot. 
        """
        pass

    def RemoveLayer(self,pLayerIndex):
        """
        Remove a layer.

        pLayerIndex : Layer at the specified index will be removed. 
        """
        pass

    def SetCurrentLayer(self,pLayerIndex):
        """
        Set the current layer for the take.

        pLayerIndex : The layer index to be set as the current one. 
        """
        pass

    def SetLayerName(self,pLayerIndex,pName):
        """
        Set the name of a layer at the specified index.

        pLayerIndex : The index of the layer that will be assigned a new name. 
        pName : The new name of the layer. 
        """
        pass

    Comments=property(doc="<b>Read Write Property:</b> Take comments.         ")
    LocalTimeSpan=property(doc="<b>Read Write Property:</b> Local time span.         ")
    ReferenceTimeSpan=property(doc="<b>Read Write Property:</b> Reference time span.         ")
    pass

class FBControlSet (FBComponent):
    """
    Control set class.     
    <b>These classes are under development and may change dramatically between versions.</b>     
    """
    def FBControlSet(self,pName):
        """
        Constructor.

        pName : Name of new control set. 
        """
        pass

    def GetFKIndex(self,pModel):
        """
        Return The Index of the Given Model.

        pModel : Given Model to obtain Index 
        return : The Index of the Given Model. 
        """
        pass

    def GetFKModel(self,pIndex):
        """
        Return the object associated to the given Index.

        pIndex : Given Index to obtain Model 
        return : return the model at the specified Index. 
        """
        pass

    def GetFKName(self,pIndex):
        """
        return the name of FK Effector at the given index

        pIndex : Given Index 
        return : return the name of IK Effector Slot 
        """
        pass

    def GetIKEffectorIndex(self,pModel):
        """
        Return the Index of the Given Model.

        pModel : Given Model to Obtain Index 
        return : The Index of the Given Model. 
        """
        pass

    def GetIKEffectorModel(self,pEffectorIndex,pPivotIndex):
        """
        Return the object associated to the given Index.

        pEffectorIndex : Given Index to obtain Model 
        pPivotIndex : Index of effector pivot 
        return : return the model at the specified Index. 
        """
        pass

    def GetIKEffectorName(self,pEffectorIndex):
        """
        return the name of IK Effector

        pEffectorIndex : Given Index to obtain Name 
        return : the name of IK Effector 
        """
        pass

    def GetIKEffectorPivotCount(self,pEffectorIndex):
        """
        return the number of IK Effector Slot

        pEffectorIndex : FBEffectorId
        return : return the number of IK Effector Slot 
        """
        pass

    def GetReferenceModel(self):
        """
        Get the reference model associated with this Control Set.

        return : The reference model associated with the Control Set. 
        """
        pass

    def GetReferenceName(self):
        """
        Get the reference name associated with this Control Set.

        return : The reference name associated with the Control Set. 
        """
        pass

    ControlSetType=property(doc="<b>Read Property:</b> the control Set Type (FKIK or IK).         ")
    UseAxis=property(doc="<b>Read Write Property:</b> is using axis.         ")
    pass

class FBFbxTake (FBComponent):
    """
    Take class for Fbx import.     
    Take info for import of data from Fbx file.     
    """
    def FBFbxTake(self):
        """
        """
        pass

    Description=property(doc="<b>Read Write Property:</b> Take description.         ")
    Import=property(doc="<b>Read Write Property:</b> Import take?         ")
    ImportName=property(doc="<b>Read Write Property:</b> Destination name for take upon import.         ")
    Name=property(doc="<b>Read Write Property:</b> Name of take.         ")
    pass

class FBSystem (FBComponent):
    """
    System interface class.     
    This class permits the user to interact with the underlying system, as well as a few operating system calls.     
    """
    def FBSystem(self):
        """
        Constructor.

        """
        pass

    Cameras=property(doc="Deprecated FBSystem.Cameras: Use FBSystem.Scene.Cameras to access this property.         ")
    Materials=property(doc="Deprecated FBSystem.Materials: Use FBSystem.Scene.Materials to access this property.         ")
    Shaders=property(doc="Deprecated FBSystem.Shaders: Use FBSystem.Scene.Shaders to access this property.         ")
    Textures=property(doc="Deprecated FBSystem.Textures: Use FBSystem.Scene.Textures to access this property.         ")
    Takes=property(doc="Deprecated FBSystem.Takes: Use FBSystem.Scene.Takes to access this property.         ")
    Lights=property(doc="Deprecated FBSystem.Lights: Use FBSystem.Scene.Lights to access this property.         ")
    Devices=property(doc="Deprecated FBSystem.Devices: Use FBSystem.Scene.Devices to access this property.         ")
    ApplicationPath=property(doc="<b>Read Only Property:</b> Location where the application is installed.         ")
    AssetManager=property(doc="<b>Read Only Property:</b> Current asset manager.         ")
    AudioInputs=property(doc="<b>List:</b> Available audio inputs.         ")
    AudioOutputs=property(doc="<b>List:</b> Available audio outputs.         ")
    BuildId=property(doc="<b>Read Only Property:</b> Unique build Id String.         ")
    ComputerName=property(doc="<b>Read Only Property:</b> Computer name.         ")
    CurrentTake=property(doc="<b>Read Write Property:</b> Current take.         ")
    DesktopSize=property(doc="<b>Read Only Property:</b> The width and height of the desktop.         ")
    FrameRate=property(doc="<b>Read Only Property:</b> The frame rate of the viewer.         ")
    FullScreenViewer=property(doc="<b>Read Write Property:</b> Indicates that the viewer is in full screen mode.         ")
    LocalTime=property(doc="<b>Read Only Property:</b> Local time in take.         ")
    OnConnectionDataNotify=property(doc="<b>Event:</b> A data event occured between objects in the system.         ")
    OnConnectionNotify=property(doc="<b>Event:</b> A connection event occured between objects in the system.         ")
    OnConnectionStateNotify=property(doc="<b>Event:</b> A state change event occured between objects in the system.         ")
    OnUIIdle=property(doc="<b>Event:</b> User-interface idle.         ")
    PathImages=property(doc="<b>Read Only Property:</b> Path to images.         ")
    PathMeshs=property(doc="<b>Read Only Property:</b> Path to meshes         ")
    ProcessMemory=property(doc="<b>Read Only Property:</b> The size (MB) of process's working set memory.         ")
    ProcessMemoryPeak=property(doc="<b>Read Only Property:</b> The size (MB) of process's peak memory.         ")
    Renderer=property(doc="<b>Read Only Property:</b> Default renderer.         ")
    RootModel=property(doc="<b>Read Only Property:</b> Root model.         ")
    Scene=property(doc="<b>Read Only Property:</b> Scene.         ")
    SceneRootModel=property(doc="<b>Read Only Property:</b> Scene root model.         ")
    SystemTime=property(doc="<b>Read Only Property:</b> System time.         ")
    Version=property(doc="<b>Read Only Property:</b> Application version.         ")
    VideoInputs=property(doc="<b>List:</b> Available video inputs.         ")
    VideoOutputs=property(doc="<b>List:</b> Available video outputs.         ")
    pass

class FBScene (FBComponent):
    """
    Scene interface class.     
    This class permits the user to interact with the underlying scene, as well as a few operating system calls.     
    """
    def FBScene(self):
        """
        Constructor.
        Client code cannot instantiate objects of this class. The FBSystem class provides access to the current scene object.

        """
        pass

    def Clear(self):
        """
        Clear the elements part of the scene.
        Not those that belong to all the scenes. This method is being deprecated, please use FBApplication::FileNew() instead.

        """
        pass

    def Evaluate(self):
        """
        Evaluate the scene.

        return : <b>true</b> if successful. 
        """
        pass

    def EvaluateDeformations(self):
        """
        Evaluate the deformations of the scene.

        return : <b>true</b> if successful. 
        """
        pass

    def FBDelete(self):
        """
        Virtual FBDelete function.

        """
        pass

    ActorFaces=property(doc="<b>List:</b> ActorFaces in scene.         ")
    Actors=property(doc="<b>List:</b> Actors in scene.         ")
    AudioClips=property(doc="<b>List:</b> Audio clips in scene.         ")
    Cameras=property(doc="<b>List:</b> Cameras in scene.         ")
    CharacterExtensions=property(doc="<b>List:</b> Character extensions available in the scene.         ")
    CharacterFaces=property(doc="<b>List:</b> Character faces in scene.         ")
    CharacterPoses=property(doc="<b>List:</b> Character poses in scene.         ")
    Characters=property(doc="<b>List:</b> Characters in scene.         ")
    Components=property(doc="<b>List:</b> Generic List of components.         ")
    ConstraintSolvers=property(doc="<b>List:</b> Constraint Solvers present in the scene.         ")
    Constraints=property(doc="<b>List:</b> Constraints in scene.         ")
    ControlSets=property(doc="<b>List:</b> Control set rigs in scene.         ")
    Devices=property(doc="<b>List:</b> Devices for scene.         ")
    Folders=property(doc="<b>List:</b> Folders in scene.         ")
    Groups=property(doc="<b>List:</b> Groups available in the scene.         ")
    Handles=property(doc="<b>List:</b> Handles present in the scene.         ")
    Lights=property(doc="<b>List:</b> Lights in scene.         ")
    LocalTime=property(doc="<b>Read Write Property:</b> Local time in the scene.         ")
    MarkerSets=property(doc="<b>List:</b> Marker sets in scene.         ")
    Materials=property(doc="<b>List:</b> Materials for scene.         ")
    Notes=property(doc="<b>List:</b> Notes in scene.         ")
    ObjectPoses=property(doc="<b>List:</b> ObjectPoses in scene.         ")
    OnChange=property(doc="<b>Event:</b> Something in the scene has happened.(FBEventSceneChange)         ")
    OnTakeChange=property(doc="<b>Event:</b> Something related to a take has happened.(FBEventTakeChange)         ")
    PhysicalProperties=property(doc="<b>List:</b> PhysicalProperties present in the scene.         ")
    Poses=property(doc="<b>List:</b> Poses in scene.         ")
    Renderer=property(doc="<b>Read Only Property:</b> Local renderer         ")
    RootModel=property(doc="<b>Read Only Property:</b> Scene Root model for that scene         ")
    Sets=property(doc="<b>List:</b> Sets available in the scene.         ")
    Shaders=property(doc="<b>List:</b> Shaders for scene.         ")
    Takes=property(doc="<b>List:</b> Takes for scene.         ")
    Textures=property(doc="<b>List:</b> Textures for scene.         ")
    UserObjects=property(doc="<b>List:</b> User objects         ")
    VideoClips=property(doc="<b>List:</b> Video clips in scene.         ")
    pass

class FBSpreadPart (FBComponent):
    """
    Spreadsheet part.     
    Due to protected constructor, this can only be created by a child object.     
    """
    Column=property(doc="<b>Read Only Property:</b> Column number.         ")
    Enabled=property(doc="<b>Read Write Property:</b> Is SpreadPart enabled?         ")
    Justify=property(doc="<b>Read Write Property:</b> Text justification for SpreadPart         ")
    ReadOnly=property(doc="<b>Read Write Property:</b> Is SpreadPart read-only?         ")
    Row=property(doc="<b>Read Only Property:</b> Row number.         ")
    Style=property(doc="<b>Read Write Property:</b> Style of cell         ")
    pass

class FBAudioOut (FBComponent):
    """
    Audio Out class.     
    Properties of this class are work in progress, but you can still list them and get their names.     
    """
    def FBAudioOut(self):
        """
        Constructor.

        """
        pass

    pass

class FBMarkerSet (FBComponent):
    """
    Marker set class.     
    <b>These classes are under development and may change dramatically between versions.</b>     
    """
    def FBMarkerSet(self,pName):
        """
        Constructor.

        pName : Name of new marker set. 
        """
        pass

    def AddMarker(self,pNodeId,pModel,pIsOriented):
        """
        Add a marker to the marker set.

        pNodeId : Id of Actor skeleton node. For hand, use the "C" index (ex:kFBSkeletonLeftThumbCIndex, kFBSkeletonLeftMiddleCIndex...) 
        pModel : The model to be associated with the marker (Optional). 
        pIsOriented : Set marker to be oriented or not (Optional). 
        return : Index of the new marker. 
        """
        pass

    def BeginTransaction(self):
        """
        Specify that you are about to call a group of functions.

        """
        pass

    def EndTransaction(self):
        """
        Specify that you are done calling a group of functions.

        """
        pass

    def GetMarkerCount(self,pNodeId):
        """
        Get the number of marker in the set.

        pNodeId : If specified, obtain the number of marker for the specific node. 
        return : Total number of marker. 
        """
        pass

    def GetMarkerModel(self,pNodeId,pMarkerIndex):
        """
        Get the model associated with a marker.

        pNodeId : Id of Actor skeleton node. 
        pMarkerIndex : Index of marker. 
        return : The model associated with the marker. 
        """
        pass

    def GetMarkerName(self,pNodeId,pMarkerIndex):
        """
        Get the name of marker at index <b>pMarkerIndex</b>.

        pNodeId : Id of Actor skeleton node. 
        pMarkerIndex : Index of marker to access. 
        return : Name of marker at index <b>pMarkerIndex</b>. 
        """
        pass

    def GetMarkerOriented(self,pNodeId,pMarkerIndex):
        """
        Is marker orientated ?

        pNodeId : Id of Actor body node. 
        pMarkerIndex : Index of marker to access. 
        return : <b>True</b> if marker is oriented, <b>false</b> otherwise. 
        """
        pass

    def GetMarkerROffset(self,pNodeId,pMarkerIndex,pROffset):
        """
        Get/Set a marker rotation.

        pNodeId : Id of Actor skeleton node. 
        pMarkerIndex : Index of marker to access. 
        pROffset : Current or new value of the marker rotation. 
        """
        pass

    def GetMarkerSetVisibility(self):
        """
        Get the marker set visibility.

        return : 1 if all markers are visible, 2 if some are visible, 0 if none are visible. 
        """
        pass

    def GetMarkerTOffset(self,pNodeId,pMarkerIndex,pTOffset):
        """
        Get/Set a marker translation.

        pNodeId : Id of Actor skeleton node. 
        pMarkerIndex : Index of marker to access. 
        pTOffset : Current or new value of the marker translation. 
        """
        pass

    def GetMarkerUsed(self,pNodeId,pMarkerIndex):
        """
        Is marker used ?

        pNodeId : Id of Actor skeleton node. 
        pMarkerIndex : Index of marker to access. 
        return : <b>True</b> if marker is used, <b>false</b> otherwise. 
        """
        pass

    def GetReferenceModel(self):
        """
        Get the reference model associated with this marker set.

        return : The reference model associated with the marker set. 
        """
        pass

    def GetUsedMarkerCount(self,pNodeId):
        """
        Get the number of used marker in the set.

        pNodeId : If specified, obtain the number of used marker for the specific node. 
        return : Total number of used marker. 
        """
        pass

    def SetMarkerModel(self,pNodeId,pMarkerIndex,pModel):
        """
        Associate a model to a marker.

        pNodeId : Id of Actor skeleton node. 
        pMarkerIndex : Index of marker. 
        pModel : Model to be associated to the marker. 
        """
        pass

    def SetMarkerName(self,pNodeId,pMarkerIndex,pMarkerName):
        """
        Set the name of marker at index <b>pMarkerIndex</b>.

        pNodeId : Id of Actor skeleton node. 
        pMarkerIndex : Index of marker to access. 
        pMarkerName : New name to give to the marker. 
        """
        pass

    def SetMarkerOriented(self,pNodeId,pMarkerIndex,pIsOriented):
        """
        Set marker to be oriented or not.

        pNodeId : Id of Actor skeleton node. 
        pMarkerIndex : Index of marker to access. 
        pIsOriented : Oriented or not. 
        """
        pass

    def SetMarkerROffset(self,pNodeId,pMarkerIndex,pROffset):
        """
        Get/Set a marker rotation.

        pNodeId : Id of Actor skeleton node. 
        pMarkerIndex : Index of marker to access. 
        pROffset : Current or new value of the marker rotation. 
        """
        pass

    def SetMarkerSetVisibility(self,pVisibility):
        """
        Set the marker set visibility.

        pVisibility : True will make to markers visible, false will hide them. 
        """
        pass

    def SetMarkerTOffset(self,pNodeId,pMarkerIndex,pTOffset):
        """
        Get/Set a marker translation.

        pNodeId : Id of Actor skeleton node. 
        pMarkerIndex : Index of marker to access. 
        pTOffset : Current or new value of the marker translation. 
        """
        pass

    def SetMarkerUsed(self,pNodeId,pMarkerIndex,pUsed):
        """
        Set marker to be used or not.

        pNodeId : Id of Actor skeleton node. 
        pMarkerIndex : Index of marker to access. 
        pUsed : Used or not. 
        """
        pass

    def SetMultipleMarkerModels(self,pModelList):
        """
        Associate multiple models to markers, matching them by name.

        pModelList : A list of models to be matched with marker names. 
        return : True if at least one marker was matched. 
        """
        pass

    def SetReferenceModel(self,pReferenceModel):
        """
        Associate a model to a marker.

        pReferenceModel : Model to be associated to the marker. 
        """
        pass

    pass

class FBTreeNode (FBComponent):
    """
    A node in the tree view.     
        
    """
    def FBTreeNode(self,pTree):
        """
        Constructor.

        pTree : Parent tree. 
        """
        pass

    Reference=property(doc="<b>Read Write Property:</b> Data to be associated to this node.         ")
    pass

class FBDeformer (FBComponent):
    """
        
        
    """
    def FBDeformer(self,pName):
        """
        Constructor.

        pName : Name of deformer. 
        """
        pass

    pass

class FBFbxManager (FBComponent):
    """
    FBX interface for loading/saving files into the application.     
    This class permits the loading and saving of scene without using the user-interface. Each process is split into three steps, and between the first and second, the developer can setup the different options for each operation. For instance, when loading, LoadBegin() is called, the options for the file can then be set, and then Load() is called to begin the actual import of the data from the scene.The manager cannot perform 2 actions at the same time!     
    """
    def FBFbxManager(self):
        """
        Constructor.

        """
        pass

    def Load(self):
        """
        File load process.
        If the load is asynchronous, this will return right away, otherwise, this is the actual loading process of the file.

        return : <b>true</b> if successful. 
        """
        pass

    def LoadAnimationOnCharacter(self,pFileName,pCharacter,pReplaceRig,pCopyMissingExtensions,pUpdateLimits,pIgnoreConflicts,pTransferMethod,pPlotOptions,pProcessAnimationOnExtensions,pRetargetOnBaseLayer,pResetHierarchy):
        """
        Load a rig and its animation from a file.

        pFileName : File name. 
        pCharacter : Target character. 
        pReplaceRig : Set to true if the current rig should be replaced by the rig in the file. 
        pCopyMissingExtensions : Set to true if the character extensions on the rig in the file should be copied to the target rig. 
        pUpdateLimits : Set to true if we should change the limits on the target rig. 
        pIgnoreConflicts : Set to true to ignore conflicts between objects in character extensions and objects in the scene. Conflicting objects will be merged in the extension. 
        pTransferMethod : How should the animation should be tranfered on the target rig. 
        pPlotOptions : If the animation should be plotted on the target rig, these plot options will be used. Set to NULL if animation will not be plotted. 
        pProcessAnimationOnExtensions : Set to true if animation on character extensions should also be transferred. 
        pRetargetOnBaseLayer : If the transfer method is retarget, set this parameter to control where the retarget correction will be made (on base layer or on another layer). 
        pResetHierarchy : Set to true if we should reset the character hierarchy. 
        return : <b>true</b> if successful. 
        """
        pass

    def LoadBegin(self,p0,pFileMemoryLength,pMerge):
        """
        Begin the file load process.
        This is the first call when loading a file via the SDK IN MEMORY.

        p0 : Adress where the file is. 
        pFileMemoryLength : Length of the File. 
        pMerge : Indicate if we are merging or appending to the current scene. 
        return : <b>true</b> if successful. 
        """
        pass

    def LoadBegin(self,pFilename,pMerge):
        """
        Begin the file load process.
        This is the first call when loading a file via the SDK.

        pFilename : Name of file to load. 
        pMerge : Indicate if we are merging or appending to the current scene. 
        return : <b>true</b> if successful. 
        """
        pass

    def LoadEnd(self):
        """
        End the file load process.
        Regardless of the type of load (asynchronous or not, this will wait until the load is finished.

        return : <b>true</b> if successful. 
        """
        pass

    def LoadIsCompleted(self):
        """
        Query the file load process.

        return : <b>true</b> if file load is finished. 
        """
        pass

    def Save(self):
        """
        Actual file save process.

        return : <b>true</b> if successful. 
        """
        pass

    def SaveBegin(self,pFilename):
        """
        Begin the file save process.
        This is the first call when saving a file via the SDK.

        pFilename : Name of file to save. 
        return : <b>true</b> if successful. 
        """
        pass

    def SaveCharacterRigAndAnimation(self,pFileName,pCharacter,pSaveCharacter,pSaveRig,pSaveExtensions):
        """
        Save the rig and its animation in a file.

        pFileName : File name. 
        pCharacter : Character to save. 
        pSaveCharacter : Set to true if the character should be saved. 
        pSaveRig : Set to true if the rig (and its children) should be saved. 
        pSaveExtensions : Set to true if the character extensions (and their children) should be saved. 
        """
        pass

    def SaveEnd(self):
        """
        End the file save process.

        return : <b>true</b> if successful. 
        """
        pass

    def SetHistoryFromOptions(self,pHistoryFile):
        """
        Update a history config file with the current options.

        pHistoryFile : Indicate the name of the history file to use. If NULL the default system file will be used. This file will be created/read from the folder bin/config. Should the first character be a '@' it will be replaced by the machine name. Using the default value is equivalent to using the string "@History.txt" as an argument. 
        return : <b>true</b> if the options were indeed saved to the history file. 
        """
        pass

    def SetOptionsFromHistory(self,pHistoryFile):
        """
        Use the options saved to a history config file to setup the current options.

        pHistoryFile : Indicate the name of the history file to use. If NULL the default system file will be used. This file will be created/read from the folder bin/config. Should the first character be a '@' it will be replaced by the machine name. Using the default value is equivalent to using the string "@History.txt" as an argument. 
        return : <b>true</b> if the options were indeed set from the history file. 
        """
        pass

    ActorFaces=property(doc="<b>Read Write Property:</b> Handling of the Actor Faces elements.         ")
    ActorFacesAnimation=property(doc="<b>Read Write Property:</b> Handling of the Actor Faces animation.         ")
    Actors=property(doc="<b>Read Write Property:</b> Handling of the Actors elements.         ")
    Async=property(doc="<b>Read Write Property:</b> Use asynchronous operation. False by default.         ")
    Audio=property(doc="<b>Read Write Property:</b> Handling of the Audio elements.         ")
    BaseCameras=property(doc="<b>Read Write Property:</b> Consider base camera settings.         ")
    Bones=property(doc="<b>Read Write Property:</b> Handling of the Bones elements.         ")
    BonesAnimation=property(doc="<b>Read Write Property:</b> Handling of the Bones animation.         ")
    CameraSwitcherSettings=property(doc="<b>Read Write Property:</b> Consider camera switcher settings.         ")
    Cameras=property(doc="<b>Read Write Property:</b> Handling of the Cameras elements.         ")
    CamerasAnimation=property(doc="<b>Read Write Property:</b> Handling of the Cameras animation.         ")
    CharacterExtensions=property(doc="<b>Read Write Property:</b> Handling of the Character Extensions.         ")
    CharacterFaces=property(doc="<b>Read Write Property:</b> Handling of the Character Faces elements.         ")
    CharacterFacesAnimation=property(doc="<b>Read Write Property:</b> Handling of the Character Faces animation.         ")
    Characters=property(doc="<b>Read Write Property:</b> Handling of the Characters elements.         ")
    CharactersAnimation=property(doc="<b>Read Write Property:</b> Handling of the Characters animation.         ")
    ClearBeforeLoad=property(doc="<b>Read Write Property:</b> Clear the scene before load. False by default.         ")
    Constraints=property(doc="<b>Read Write Property:</b> Handling of the Constraints elements.         ")
    ConstraintsAnimation=property(doc="<b>Read Write Property:</b> Handling of the Constraints animation.         ")
    ConvertImageToTiff=property(doc="<b>Read Write Property:</b> Only considered if EmbedMedia is true. Will convert the embeded media to tiff format when possible.         ")
    CurrentCameraSettings=property(doc="<b>Read Write Property:</b> Consider current camera settings.         ")
    CustomImportNamespace=property(doc="<b>Read Write Property:</b> Namespace we append to every objects on a Load (import/open/merge)         ")
    Devices=property(doc="<b>Read Write Property:</b> Handling of the Devices elements.         ")
    DevicesAnimation=property(doc="<b>Read Write Property:</b> Handling of the Devices animation.         ")
    EmbedMedia=property(doc="<b>Read Write Property:</b> Embed all media in the FBX file itself. When saving in ASCII mode it is not possible to embed media.         ")
    GlobalLightingSettings=property(doc="<b>Read Write Property:</b> Consider global Lighting settings.         ")
    Groups=property(doc="<b>Read Write Property:</b> Handling of the Groups elements.         ")
    KeyingGroups=property(doc="<b>Read Write Property:</b> Handling of the Keying Groups elements.         ")
    Lights=property(doc="<b>Read Write Property:</b> Handling of the Lights elements.         ")
    LightsAnimation=property(doc="<b>Read Write Property:</b> Handling of the Lights animation.         ")
    Materials=property(doc="<b>Read Write Property:</b> Handling of the Materials elements.         ")
    MaterialsAnimation=property(doc="<b>Read Write Property:</b> Handling of the Materials animation.         ")
    Models=property(doc="<b>Read Write Property:</b> Handling of the Models elements.         ")
    ModelsAnimation=property(doc="<b>Read Write Property:</b> Handling of the Models animation.         ")
    Notes=property(doc="<b>Read Write Property:</b> Handling of the Notes elements.         ")
    NotesAnimation=property(doc="<b>Read Write Property:</b> Handling of the Notes animation.         ")
    OpticalData=property(doc="<b>Read Write Property:</b> Handling of the Optical Data elements.         ")
    PhysicalProperties=property(doc="<b>Read Write Property:</b> Handling of the Physical Properties elements.         ")
    PhysicalPropertiesAnimation=property(doc="<b>Read Write Property:</b> Handling of the Physical Properties animation.         ")
    Poses=property(doc="<b>Read Write Property:</b> Handling of the Poses elements.         ")
    Scene=property(doc="<b>Read Write Property:</b> This is the scene in wich you want to load         ")
    Scripts=property(doc="<b>Read Write Property:</b> Handling of the Scripts elements.         ")
    Selected=property(doc="<b>Read Write Property:</b> Indicate that only the selected models will be saved.         ")
    Sets=property(doc="<b>Read Write Property:</b> Handling of the Sets elements.         ")
    Shaders=property(doc="<b>Read Write Property:</b> Handling of the Shaders elements.         ")
    ShadersAnimation=property(doc="<b>Read Write Property:</b> Handling of the Shaders animation.         ")
    Solvers=property(doc="<b>Read Write Property:</b> Handling of the Solvers elements.         ")
    SolversAnimation=property(doc="<b>Read Write Property:</b> Handling of the Solvers animation.         ")
    State=property(doc="<b>Read Only Property:</b> Current state of the manager.         ")
    Story=property(doc="<b>Read Write Property:</b> Handling of the Story elements.         ")
    TakeSpan=property(doc="<b>Read Write Property:</b> Indicate how the take start and end point should be set. By default it is read from the file.         ")
    Takes=property(doc="<b>List:</b> Scene takes.         ")
    Textures=property(doc="<b>Read Write Property:</b> Handling of the Textures elements.         ")
    TexturesAnimation=property(doc="<b>Read Write Property:</b> Handling of the Textures animation.         ")
    TransportSettings=property(doc="<b>Read Write Property:</b> Consider transport control settings.         ")
    UseASCIIFormat=property(doc="<b>Read Write Property:</b> Indicate if the resulting FBX file will be in binary or ASCII mode.         ")
    Video=property(doc="<b>Read Write Property:</b> Handling of the Video elements.         ")
    pass

class FBPropertyVector3d (FBProperty):
    """
        
        
    """
    Data=property(doc="<b>Read Write Property:</b> The property data value. Type of this depends on the subclass of FBProperty (ex: in a FBPropertyInt, Data is of type int).         ")
    pass

class FBFCurve (FBComponent):
    """
    FCurve class.     
        
    """
    def FBFCurve(self):
        """
        Constructor.

        """
        pass

    def CreateInterpolatorCurve(self,pCurveType):
        """
        Create and interpolator curve.

        pCurveType : Interpolator curve type to create. 
        """
        pass

    def EditBegin(self,pKeyCount):
        """
        Setup function to begin adding keys.

        pKeyCount : Key to begin adding at(default is -1). 
        """
        pass

    def EditClear(self):
        """
        Empty FCurve of all keys.

        """
        pass

    def EditEnd(self,pKeyCount):
        """
        End key adding sequence.

        pKeyCount : Key to finish adding at (default is -1). 
        """
        pass

    def Evaluate(self,pTime):
        """
        Evaluate FCurve at <b>pTime</b>.

        pTime : Time at which FCurve is to be evaluated. 
        return : Value of FCurve at <b>pTime</b>. 
        """
        pass

    def KeyAdd(self,pTime,pValue):
        """
        Add a key at the specified time.

        pTime : Time at which to insert the key. 
        pValue : Value of the key. 
        return : The position of the new key in the list of FCurve keys. 
        """
        pass

    def KeyInsert(self,pTime,pInterpolation,pTangentMode):
        """
        Insert a key without affecting the curve shape.

        pTime : Time at which the key is to be inserted. 
        pInterpolation : Interpolation type of the inserted key. 
        pTangentMode : Tangent calculation method of the inserted key. 
        """
        pass

    def KeyRemove(self,pIndex):
        """
        Remove key at index.

        pIndex : Index of the key to remove. 
        return : If the removal was succesful or not. 
        """
        pass

    Keys=property(doc="<b>List:</b> Keys.         ")
    pass

class FBPropertyString (FBProperty):
    """
        
        
    """
    Data=property(doc="<b>Read Write Property:</b> The property data value. Type of this depends on the subclass of FBProperty (ex: in a FBPropertyInt, Data is of type int).         ")
    pass

class FBGeometry (FBComponent):
    """
    Geometry class.     
    This class groups all geometry related elements which are shared across the different subclasses (FBMesh, FBSurface, FBNurbs and FBPatch).Class FBGeometry has a property 'MaterialMappingMode' which can be one of three values. Depending on which is the current values there are different ways of getting the 'current' material.kFBMappingModeUnique: Meaning that there is only one material used for the whole model. The material used is the last one in the list of FBGeometry::Materials.kFBMappingModeVertex: Meaning that each vertex has its own material. Calling FBGeometry::VertexMaterialIdGet() will give you the index of the material used from the list FBGeometry::Materials.kFBMappingModeSurface: Meaning that each polygon of the model has its own material. Calling FBMesh::PolygonMaterialIdGet() will give you the index of the material used from the list FBGeometry::Materials.By default, models created with the GUI or the SDK use the mapping mode kFBMappingModeUnique. Doing a call to FBGeometry::VertexMaterialIdSet() (with valid vertex Id and material Id) will change the mapping mode to kFBMappingModeVertex. The equivalent is true when doing a call to method FBMesh::PolygonMaterialIdSet().     
    """
    def FBGeometry(self,pModel):
        """
        Constructor.

        pModel : Model to which the geometry belongs. 
        """
        pass

    def GeometryBegin(self):
        """
        Begin/End geometry mapping.

        return : <b>true</b> if successful. 
        """
        pass

    def GeometryEnd(self):
        """
        Begin/End geometry mapping.

        return : <b>true</b> if successful. 
        """
        pass

    def GetArrayElementAttributeMode(self,pArrayId):
        """
        Get the mapping mode for the array specified by the FBGeometryArrayID parameter.

        pArrayId : The ID of the array to get. 
        return : Mapping mode of the speficied array. 
        """
        pass

    def GetArrayElementType(self,pArrayId):
        """
        Get the type of element contained in the array specified by the FBGeometryArrayID parameter.

        pArrayId : The ID of the array to get. 
        return : Element type contained in the array. 
        """
        pass

    def VertexAdd(self,pVertex):
        """
        Add a vertex.

        pVertex : Vertex values used to add vertex. 
        return : Index where vertex was added. 
        """
        pass

    def VertexAdd(self,px,py,pz):
        """
        Add a vertex.

        px : X coordinate of vertex to add. 
        py : Y coordinate of vertex to add. 
        pz : Z coordinate of vertex to add. 
        return : Index where vertex was added. 
        """
        pass

    def VertexClear(self):
        """
        Clear all vertices.

        return : <b>true</b> if successful. 
        """
        pass

    def VertexCount(self):
        """
        Get the number of vertices in the geometry.

        return : Number of vertices in the geometry. 
        """
        pass

    def VertexGet(self,pIndex):
        """
        Get a vertex.

        pIndex : Index of vertex to get. 
        return : Vertex stored at <b>pIndex</b>. 
        """
        pass

    def VertexGetSelected(self,pIndex):
        """
        Get the selected state of a vertex.

        pIndex : The index of the vertex 
        return : true if the vertex is selected.false if not 
        """
        pass

    def VertexGetTransformable(self,pIndex):
        """
        Get the Transformable state of a vertex.

        pIndex : The index of the vertex 
        return : true if the vertex is Transformable.false if not 
        """
        pass

    def VertexGetVisible(self,pIndex):
        """
        Get the visible state of a vertex.

        pIndex : The index of the vertex 
        return : true if the vertex is visible.false if not 
        """
        pass

    def VertexInit(self,pSize):
        """
        Initialize vertex.

        pSize : Number of vertices to allocate. 
        """
        pass

    def VertexMaterialIdGet(self,pIndex):
        """
        Get vertex material id number.

        pIndex : Vertex to get material ID for(default=-1). 
        return : Material ID for vertex at <b>pIndex</b>. 
        """
        pass

    def VertexMaterialIdSet(self,pMaterialId,pIndex):
        """
        Set Material ID at a vertex.

        pMaterialId : Material ID to set. 
        pIndex : Index of vertex to set material ID for(default=-1). 
        return : <b>true</b> if successful. 
        """
        pass

    def VertexNormalGet(self,pIndex):
        """
        Get a normal at a vertex.

        pIndex : Vertex to get normal at(default=-1). 
        return : Normal of vertex at <b>pIndex</b>. 
        """
        pass

    def VertexNormalSet(self,pVertex,pIndex):
        """
        Set a normal at a vertex.

        pVertex : Normal to set. 
        pIndex : Index of vertex to set Normal at(default=-1). 
        return : <b>true</b> if successful. 
        """
        pass

    def VertexNormalSet(self,px,py,pz,pIndex):
        """
        Set a normal at a vertex.

        px : X coordinate of normal. 
        py : Y coordinate of normal. 
        pz : Z coordinate of normal. 
        pIndex : Index of vertex to set Normal at(default=-1). 
        return : <b>true</b> if successful. 
        """
        pass

    def VertexSet(self,pVertex,pIndex):
        """
        Set a vertex.

        pVertex : Vertex values used to set vertex. 
        pIndex : Index of vertex to affect (default=-1). 
        return : <b>true</b> if successful. 
        """
        pass

    def VertexSet(self,px,py,pz,pIndex):
        """
        Set a vertex.

        px : X coordinate to set. 
        py : Y coordinate to set. 
        pz : Z coordinate to set. 
        pIndex : Index of vertex to set(default=-1). 
        return : <b>true</b> if successful. 
        """
        pass

    def VertexSetSelected(self,pIndex,pState):
        """
        Set the selected state of a vertex.

        pIndex : The index of the vertex 
        pState : The true to selected, false to unselect 
        return : true if the vertex is selected.false if not 
        """
        pass

    def VertexSetVisible(self,pIndex,pState):
        """
        Set the visible state of a vertex.

        pIndex : The index of the vertex 
        pState : The true to visible, false to unselect 
        return : true if the vertex is visible.false if not 
        """
        pass

    def VertexUVGet(self,pIndex):
        """
        Get a UV coordinate.

        pIndex : Index of Vertex to get UV coordinate for(default=-1). 
        return : UV coordinate at <b>UVSetIndex</b>. 
        """
        pass

    def VertexUVSet(self,pUV,pIndex):
        """
        Set a UV coordinate.

        pUV : UV coordinate to set. 
        pIndex : Index of Vertex to affect with UV coordinate(default=-1). 
        return : <b>true</b> if successful. 
        """
        pass

    def VertexUVSet(self,pU,pV,pIndex):
        """
        Set a UV coordinate.

        pU : U coordinate to set. 
        pV : V coordinate to set. 
        pIndex : Index of Vertex to affect with UV coordinate(default=-1). 
        return : <b>true</b> if successful. 
        """
        pass

    FastTessellatorPolygon=property(doc="<b>Read Only Property:</b> Use this property to obtain the original model geometry as polygons         ")
    FastTessellatorStrip=property(doc="<b>Read Only Property:</b> Use this property to obtain a striped version of the model geometry ( see http://en.wikipedia.org/wiki/Triangle_strip )         ")
    MaterialMappingMode=property(doc="<b>Read Write Property:</b> Material mapping mode.         ")
    Materials=property(doc="<b>List:</b> Geometry materials.         ")
    TextureMappingMode=property(doc="<b>Read Write Property:</b> Texture mapping mode.         ")
    Textures=property(doc="<b>List:</b> Geometry textures.         ")
    UVMappingMode=property(doc="<b>Read Only Property:</b> UV mapping mode.         ")
    pass

class FBAudioClip (FBComponent):
    """
    Audio Clip class.     
    This class permits you to access audio clip's properties to read or change them.     
    """
    def FBAudioClip(self,pFileName,pSetToDefaultDest):
        """
        Constructor.

        pFileName : The complete file path of the media file to access. 
        pSetToDefaultDest : If true and the media file open successfully, it will automatically be connected to an output device. 
        """
        pass

    def FBDelete(self):
        """
        Virtual FBDelete function.

        """
        pass

    def Play(self,pStyle,pDestination):
        """
        Play audio clip now.

        pStyle : How the audio clip should be triggered. 
        pDestination : Where the audio clip should be played. If NULL, it will play on the default destination. 
        return : Return true if the buffer for the audio clip was successfully allocated so that you can hear the sound. 
        """
        pass

    def Stop(self,pDestination):
        """
        Stop any playing triggered audio clip on a specified destination.

        pDestination : Where the audio clip is playing. If NULL, the default destination will be used. 
        """
        pass

    AccessMode=property(doc="<b>Read Write Property:</b> Specify the media data access mode between disk or memory.         ")
    Destination=property(doc="<b>Read Write Property:</b> The audio output destination where the clip will be played.         ")
    Duration=property(doc="<b>Read Only Property:</b> Total duration of this audio clip.         ")
    Filename=property(doc="<b>Read Only Property:</b> Filename of media.         ")
    Format=property(doc="<b>Read Only Property:</b> Data format of media, including rate, bits and channels count. You can typecast it to a FBAudioFmt.         ")
    InPoint=property(doc="<b>Read Write Property:</b> When not used in the Story, this specify when the clips begin to play.         ")
    Scrubbing=property(doc="<b>Read Write Property:</b> Control which clip (one at a time) can shuttle when playing a various speeds.         ")
    UseChannelMode=property(doc="<b>Read Write Property:</b> Enables you to control which track are used with stereo clips.         ")
    pass

class FBVideoGrabber (FBComponent):
    """
    Video Grabber class.     
    Used to grab video frames generated with the FBRenderer.     
    """
    def FBVideoGrabber(self):
        """
        Constructor.

        """
        pass

    def BeginGrab(self):
        """
        BeginGrab.
        Begin video grabbing session.

        return : <b>True</b> if we can begin the grab session. 
        """
        pass

    def EndGrab(self):
        """
        EndGrab.
        Close video grabbing session.

        """
        pass

    def GetLastErrorMsg(self):
        """
        GetLastErrorMsg.

        return : If an error occured, this function returns the last error message, otherwise an empty string. 
        """
        pass

    def GetOptions(self):
        """
        GetOptions give you a copy of current grabbing options.

        return : Struct that contain all grabbing options. 
        """
        pass

    def GetStatistics(self):
        """
        GetStatistics.

        return : Struct that contain all grabbing statistics. 
        """
        pass

    def Grab(self):
        """
        Grab.
        Grab all specified video frames.

        """
        pass

    def RenderSnapshot(self,pWidth,pHeight,pCameraLabel,pTimeCode,pSafeArea,pAxis,pGrid,pFrontPlate,pBackPlate):
        """
        Render a snapshot of the actual display.

        pWidth : int
        pHeight : int
        pCameraLabel : bool
        pTimeCode : bool
        pSafeArea : bool
        pAxis : bool
        pGrid : bool
        pFrontPlate : bool
        pBackPlate : bool
        return : An FBimage containing data of the rendered snapshot. 
        """
        pass

    def ResetOptions(self):
        """
        SetDefaultOptions.
        This function reset all grabbing options to the default value.

        """
        pass

    def SetOptions(self,pOptions):
        """
        SetOptions.

        pOptions : Struct that contain all grabbing options. 
        """
        pass

    pass

class FBPropertyTime (FBProperty):
    """
        
        
    """
    Data=property(doc="<b>Read Write Property:</b> The property data value. Type of this depends on the subclass of FBProperty (ex: in a FBPropertyInt, Data is of type int).         ")
    pass

class FBStory (FBComponent):
    """
    Story Management class.     
    This class serve as a management control for the Story global settings and members.     
    """
    def FBStory(self):
        """
        Constructor.

        """
        pass

    LockedShot=property(doc="<b>Read Write Property:</b> If true, shots will be locked (no time discontinuity).         ")
    Mute=property(doc="<b>Read Write Property:</b> If true, the Story mode will be globally disabled.         ")
    RootEditFolder=property(doc="<b>Read Only Property:</b> Story's root edit folder         ")
    RootFolder=property(doc="<b>Read Only Property:</b> Story's root folder         ")
    pass

class FBPropertyAction (FBProperty):
    """
        
        
    """
    def FBPropertyAction(self):
        """
        Constructor.

        """
        pass

    pass

class FBPropertyColorAndAlpha (FBProperty):
    """
    FBPropertyColorAndAlpha class.     
    Similar in use to FBPropertyColor 
@code
    # Supported list protocol methods:
    c = FBPropertyColorAndAlpha()
    len(c)
    print c[0]
    c[0] = 1.0
    print c.Data
    c.Data=FBColorAndAlpha(1.0,0.5,0.5,1.0)
@endcode

Slicing is not supported by this object.     
    """
    def __len__(self):
        """
        Returns the number of elements.
        Corresponds to python: len(object)

        """
        pass

    def __getitem__(self,pIndex):
        """
        Returns the ith component Corresponds to python: print c[1].

        pIndex : Index of the components to get (0 to 1) 
        return : Color component value. 
        """
        pass

    def __setitem__(self,pIndex,pComponentValue):
        """
        Sets the ith components Corresponds to python: c[1] = 0.5.

        pIndex : Index of the components to set (0 to 1) 
        pComponentValue : Value of component to set 
        """
        pass

    Data=property(doc="<b>Read Write Property:</b> The property data value. Type of this depends on the subclass of FBProperty (ex: in a FBPropertyInt, Data is of type int).         ")
    pass

class FBCluster (FBComponent):
    """
    Cluster.     
    Weighting interface for meshes. This class is experimental.     
    """
    def FBCluster(self,pModel):
        """
        Constructor.

        pModel : Parent model in question. 
        """
        pass

    def ClusterBegin(self,pIndex):
        """
        Begin cluster definition.

        pIndex : Link index. 
        return : Index of last item(default=-1). 
        """
        pass

    def ClusterEnd(self,pQueryOnly):
        """
        End cluster definition.

        pQueryOnly : Were the operations on the cluster non-destructive? 
        return : 0, (Not implemented). 
        """
        pass

    def LinkClearUnused(self,pThreshold):
        """
        Remove all unused links.

        pThreshold : Weight value under which links are considered unused (default=-1). 
        """
        pass

    def LinkGetAssociateModel(self,pLinkNumber):
        """
        Get model associated with link.

        pLinkNumber : Nubmer value of link to get associated model from. 
        return : Model associated to link number <b>pLinkNumber</b>. 
        """
        pass

    def LinkGetCount(self):
        """
        Get number of links.

        return : Number of links. 
        """
        pass

    def LinkGetModel(self,pLinkNumber):
        """
        Get model from a link.

        pLinkNumber : Number value of link to get model from. 
        return : Model at link number <b>pLinkNumber</b>. 
        """
        pass

    def LinkGetName(self,pLinkNumber):
        """
        Get the name of a link.

        pLinkNumber : Number value of link to get name from. 
        return : Name of link number <b>pLinkNumber</b>. 
        """
        pass

    def LinkGetVertexIndex(self,pIndex):
        """
        Get current vertex at link.

        pIndex : Index of link to get vertex from. 
        return : Index value of the current vertex associated to link at index number <b>pIndex</b> 
        """
        pass

    def LinkRemove(self,pLinkNumber):
        """
        Remove a link.

        pLinkNumber : Number value of link to rename. 
        """
        pass

    def LinkSetCurrentVertex(self,pLinkIndex,pPointIndex):
        """
        Link at current vertex.

        pLinkIndex : Index of link to add vertex to. 
        pPointIndex : Index of vertex to add. 
        """
        pass

    def LinkSetModel(self,pModel):
        """
        Set model to a link.

        pModel : Model to set. 
        """
        pass

    def LinkSetName(self,pName,pLinkNumber):
        """
        Set the name of a link.

        pName : Name of the link. 
        pLinkNumber : Number value of link to name. 
        """
        pass

    def VertexAdd(self,pVertexIndex,pWeight):
        """
        Add a vertex to a cluster.

        pVertexIndex : Index of vertex to add. 
        pWeight : Weight to give to vertex. 
        """
        pass

    def VertexClear(self):
        """
        Clear all linked vertices.

        """
        pass

    def VertexGetCount(self):
        """
        Get the number of vertices.

        return : Number of vertices in a cluster. 
        """
        pass

    def VertexGetNumber(self,pIndex):
        """
        Get vertex number.

        pIndex : Index of link to get vertex from. 
        return : Number value of vertex at link number <b>pIndex</b> 
        """
        pass

    def VertexGetTransform(self,pPosition,pRotation,pScaling):
        """
        Get transform of a cluster set.

        pPosition : Position transform. 
        pRotation : Rotation transform. 
        pScaling : Scaling transform. 
        """
        pass

    def VertexGetWeight(self,pIndex):
        """
        Get vertex weight.

        pIndex : Index of link to get vertex from. 
        return : Weight of vertex found at link number <b>pIndex</b>. 
        """
        pass

    def VertexRemove(self,pVertexIndex):
        """
        Remove a vertex from a cluster.

        pVertexIndex : Index of vertex to remove. 
        """
        pass

    def VertexSetTransform(self,pPosition,pRotation,pScaling):
        """
        Set transform of a cluster set.

        pPosition : Position transform. 
        pRotation : Rotation transform. 
        pScaling : Scaling transform. 
        """
        pass

    def VertexSetWeight(self,pWeight,pIndex):
        """
        Set vertex weight.

        pWeight : Weight to give to vertex. 
        pIndex : Index of link to get vertex from. 
        """
        pass

    ClusterAccuracy=property(doc="<b>Read Write Property:</b> Cluster accuracy.         ")
    ClusterMode=property(doc="<b>Read Write Property:</b> Cluster mode.         ")
    pass

class FBDeck (FBComponent):
    """
    Deck class.     
        
    """
    def FBDeck(self,pName):
        """
        Constructor.

        pName : Name of deck. 
        """
        pass

    def CueAt(self,pTime):
        """
        Cue deck at a given time.

        pTime : Time to cue deck at. 
        """
        pass

    def DeckAutoCommandsNotify(self):
        """
        Deck auto commands notification.

        """
        pass

    def DeckStatusUpdateNotify(self):
        """
        Interface to IObject.
        Deck status update notification.

        """
        pass

    def Eject(self):
        """
        Eject tape.

        """
        pass

    def Forward(self):
        """
        Fast forward.

        """
        pass

    def GetTime(self):
        """
        Get the deck's time.

        return : Time of deck. 
        """
        pass

    def Play(self,pSpeed):
        """
        Play forwards.

        pSpeed : Playback speed (default is 1.0). 
        """
        pass

    def ReversePlay(self,pSpeed):
        """
        Play backwards.

        pSpeed : Playback speed(default is 1.0). 
        """
        pass

    def Rewind(self):
        """
        Rewind.

        """
        pass

    def StepBack(self):
        """
        Step backwards.

        """
        pass

    def StepForward(self):
        """
        Step forwards.

        """
        pass

    def Stop(self):
        """
        Stop.

        """
        pass

    def ThreadSync(self):
        """
        """
        pass

    CassetteInside=property(doc="<b>Read Only Property:</b> Is the cassette inside?         ")
    EE=property(doc="<b>Read Write Property:</b> Is EE on?         ")
    IconFilename=property(doc="<b>Read Write Property:</b> Filename of icon for deck.         ")
    Latency=property(doc="<b>Read Write Property:</b> Latency of response for the deck;         ")
    Offset=property(doc="<b>Read Write Property:</b> Current offset for the TC.         ")
    Online=property(doc="<b>Read Write Property:</b> Is deck online?         ")
    PlayingBackward=property(doc="<b>Read Only Property:</b> Playing backwards?         ")
    PlayingForward=property(doc="<b>Read Only Property:</b> Playing forward?         ")
    PostRoll=property(doc="<b>Read Write Property:</b> Post-Roll.         ")
    PreRoll=property(doc="<b>Read Write Property:</b> Pre-Roll.         ")
    StandBy=property(doc="<b>Read Write Property:</b> In standby mode?         ")
    TransportControl=property(doc="<b>Read Write Property:</b> Mode w/r to TC (None, Slave, Master );         ")
    UniqueName=property(doc="internal Unique name.         ")
    pass

class FBModelTemplate (FBComponent):
    """
    Model template class.     
    Model templates are 'placeholders' for animation input from devices. These generic 'models' can be any type of element, and permit the abstraction of the input from the actual type of model. In order to animate a model, one should bind the model to an animation node.     
    """
    def FBModelTemplate(self):
        """
        Constructor from parent object.

        """
        pass

    def FBModelTemplate(self,pPrefix,pName,pStyle):
        """
        Constructor (no parent) from prefix, name, and style.

        pPrefix : Location of model template in application object directory structure. 
        pName : Name of model template. 
        pStyle : Style of model template. 
        """
        pass

    Bindings=property(doc="<b>List:</b> Bindings for animation interface.         ")
    Children=property(doc="<b>List:</b> Children for object hierarchy.         ")
    DefaultRotation=property(doc="<b>Read Write Property:</b> Default rotation.         ")
    DefaultScaling=property(doc="<b>Read Write Property:</b> Default scaling.         ")
    DefaultTranslation=property(doc="<b>Read Write Property:</b> Default translation.         ")
    Model=property(doc="<b>Read Write Property:</b> Model being interfaced.         ")
    Prefix=property(doc="<b>Read Write Property:</b> Prefix of model template.         ")
    pass

class FBDeviceInstrument (FBComponent):
    """
    Instrument abstraction layer.     
        
    """
    def FBDeviceInstrument(self,pDevice):
        """
        Constructor.

        pDevice : Parent device. 
        """
        pass

    def InstrumentRecordFrame(self,pRecordTime,pNotifyInfo):
        """
        Record the data to the function curves for the instrument.

        pRecordTime : Time to record data at. 
        pNotifyInfo : Device notification information structure. 
        """
        pass

    def InstrumentWriteData(self,pEvaluateInfo,pInfoType):
        """
        Write data to instrument's connectors.
        In the evaluation engine callback, this will take the data in the instrument's temporary data holders and write it to the connectors.

        pEvaluateInfo : Evaluation information structure. 
        pInfoType : Status of connectors (default is set to CNT_STATUS_LIVE). 
        return : <b>true</b> if successful. 
        """
        pass

    Active=property(doc="<b>Read Write Property:</b> Is instrument active?         ")
    Device=property(doc="<b>Read Write Property:</b> Handle to owner device.         ")
    ModelTemplate=property(doc="<b>Read Write Property:</b> Model template to build instruments' structure.         ")
    pass

class FBPropertyDouble (FBProperty):
    """
        
        
    """
    Data=property(doc="<b>Read Write Property:</b> The property data value. Type of this depends on the subclass of FBProperty (ex: in a FBPropertyInt, Data is of type int).         ")
    pass

class FBPropertyBool (FBProperty):
    """
        
        
    """
    Data=property(doc="<b>Read Write Property:</b> The property data value. Type of this depends on the subclass of FBProperty (ex: in a FBPropertyInt, Data is of type int).         ")
    pass

class FBVisualComponent (FBComponent):
    """
    Visual Component base class.     
    All of the user interface elements available in the SDK derive from this class.     
    """
    def FBVisualComponent(self):
        """
        Constructor.

        """
        pass

    def AddChild(self,pChild,pId):
        """
        Add a child component.

        pChild : Visual component to add as a child. 
        pId : User reference number to associate with <b>pChild</b>(default=0). 
        return : Operation was successful (<b>true</b> or <b>false</b>). 
        """
        pass

    def GetChild(self,pId):
        """
        Get a child component.

        pId : User reference number to look for child with(default=0). 
        return : Handle to child (NULL if not found). 
        """
        pass

    def IsView(self):
        """
        Is component a view?

        return : <b>true</b> if component is a view. 
        """
        pass

    def Refresh(self,pNow):
        """
        Refresh component.

        pNow : Refresh immediately if <b>true</b> (default = <b>false</b>). 
        """
        pass

    def ViewExpose(self):
        """
        Exposed view callback function.

        """
        pass

    def ViewInput(self,pMouseX,pMouseY,pAction,pButtonKey,pModifier):
        """
        Input callback function.

        pMouseX : Mouse X position. 
        pMouseY : Mouse Y position. 
        pAction : Mouse action. 
        pButtonKey : Keyboard input. 
        pModifier : Keyboard intput modifier. 
        """
        pass

    RegionName=property(doc="<b>Read Write Property:</b> Region name.         ")
    RegionOffsetX=property(doc="<b>Read Write Property:</b> Region X offset.         ")
    RegionOffsetY=property(doc="<b>Read Write Property:</b> Region Y offset.         ")
    RegionOffsetWidth=property(doc="<b>Read Write Property:</b> Region width offset.         ")
    RegionOffsetHeight=property(doc="<b>Read Write Property:</b> Region height offset.         ")
    RegionRatioX=property(doc="<b>Read Write Property:</b> Ratio for X attachment.         ")
    RegionRatioY=property(doc="<b>Read Write Property:</b> Ratio for Y attachment.         ")
    RegionRatioWidth=property(doc="<b>Read Write Property:</b> Ratio for Width attachment.         ")
    RegionRatioHeight=property(doc="<b>Read Write Property:</b> Ratio for Height attachment.         ")
    RegionAttachTypeX=property(doc="<b>Read Write Property:</b> X Attachment type.         ")
    RegionAttachTypeY=property(doc="<b>Read Write Property:</b> Y Attachment type.         ")
    RegionAttachTypeWidth=property(doc="<b>Read Write Property:</b> Width Attachment type.         ")
    RegionAttachTypeHeight=property(doc="<b>Read Write Property:</b> Height Attachment type.         ")
    RegionAttachToX=property(doc="<b>Read Write Property</b> X Attachment source.         ")
    RegionAttachToY=property(doc="<b>Read Write Property:</b> Y Attachment source.         ")
    RegionAttachToWidth=property(doc="<b>Read Write Property:</b> Width Attachment source.         ")
    RegionAttachToHeight=property(doc="<b>Read Write Property:</b> Height Attachment source.         ")
    RegionPosMaxX=property(doc="<b>Read Write Property:</b> Region X position Max         ")
    RegionPosMinX=property(doc="<b>Read Write Property:</b> Region X position Min         ")
    RegionPosMaxY=property(doc="<b>Read Write Property:</b> Region Y position Max         ")
    RegionPosMinY=property(doc="<b>Read Write Property:</b> Region Y position Min         ")
    BorderCaption=property(doc="<b>Read Write Property:</b> Caption to display in border.         ")
    BorderShowCaption=property(doc="<b>Read Write Property:</b> Show caption?         ")
    BorderStyle=property(doc="<b>Read Write Property:</b> Style of border.         ")
    BorderInSet=property(doc="<b>Read Write Property:</b> Is border inset?         ")
    BorderWidth=property(doc="<b>Read Write Property:</b> Width of border.         ")
    BorderSpacing=property(doc="<b>Read Write Property:</b> Spacing of border.         ")
    BorderMaxAngle=property(doc="<b>Read Write Property:</b> Max angle for rounding.         ")
    BorderCornerRadius=property(doc="<b>Read Write Property:</b> Corner radius (rounded).         ")
    Caption=property(doc="<b>Property:</b> Widget caption.         ")
    Enabled=property(doc="<b>Read Write Property:</b> Is visual enabled?         ")
    Height=property(doc="<b>Read Write Property:</b> Height.         ")
    Hint=property(doc="<b>Read Write Property:</b> Hint to show.         ")
    Left=property(doc="<b>Read Write Property:</b> Left coordinate.         ")
    ReadOnly=property(doc="<b>Read Write Property:</b> Is visual component read only?         ")
    Top=property(doc="<b>Read Write Property:</b> Top coordinate.         ")
    Visible=property(doc="<b>Read Write Property:</b> Is visual component visible?         ")
    Width=property(doc="<b>Read Write Property:</b> Width.         ")
    pass

class FBPropertyVector4d (FBProperty):
    """
        
        
    """
    Data=property(doc="<b>Read Write Property:</b> The property data value. Type of this depends on the subclass of FBProperty (ex: in a FBPropertyInt, Data is of type int).         ")
    pass

class FBFastTessellator (FBComponent):
    """
    Fast tessellator class.     
        
    """
    ForceUVByVertex=property(doc="<b>Read Write Property:</b> true if the texture coordinates are forced buvertex instead of by polygon-vertex         ")
    HasChanged=property(doc="<b>Read Only Property:</b>         ")
    IsDeformable=property(doc="<b>Read Only Property:</b>         ")
    IsDrawable=property(doc="<b>Read Only Property:</b> true if the tesselated geometry has been computed for this frame         ")
    IsMesh=property(doc="<b>Read Only Property:</b> true if it's a mesh, false if it's a surface (nurbs or patch)         ")
    MaterialId=property(doc="<b>List:</b>         ")
    NormalIndex=property(doc="<b>List:</b>         ")
    NormalMode=property(doc="<b>Read Only Property:</b>         ")
    PrimitiveCount=property(doc="<b>Read Only Property:</b>         ")
    PrimitiveVertexCount=property(doc="<b>List:</b>         ")
    TextureId=property(doc="<b>List:</b>         ")
    UVIndex=property(doc="<b>List:</b>         ")
    VertexCount=property(doc="<b>Read Only Property:</b>         ")
    VertexIndex=property(doc="<b>List:</b>         ")
    pass

class FBSpread (FBVisualComponent):
    """
    Base spreadsheet class.     
        
    """
    def FBSpread(self):
        """
        Constructor.

        """
        pass

    def GetCellValue(self,pRow,pColumn):
        """
        Get a cell's value.

        pRow : Row of cell. 
        pColumn : Column of cell. 
        """
        pass

    def SetCellValue(self,pRow,pColumn,pValue):
        """
        Set a cell's value.
        This will also set the FBSpreadCell.Style to the type of pValue (kFBCellStyleInteger if pValue is an int, kFBCellStyleDouble if pValue is a float, kFBCellStyleString if pValue is a str).

        pRow : Row of cell. 
        pColumn : Column of cell. 
        pValue : Value of the cell (can be str, int or float) 
        """
        pass

    def GetSpreadCell(self,pRef,pColumn):
        """
        Get a cell from row and column numbers.

        pRef : Row reference. 
        pColumn : Column number. 
        return : A copy of the cell. 
        """
        pass

    def Clear(self):
        """
        Clear spreadsheet This function will empty spreadsheet of all its rows, columns and cells.

        """
        pass

    def ColumnAdd(self,pString,pRef):
        """
        Add a column.

        pString : Text to display with column. 
        pRef : User-define column reference number(default=0). 
        """
        pass

    def GetCellView(self,pRef,pColumn,pView):
        """
        Get a cell's internal toolkit view.

        pRef : Row of cell. 
        pColumn : Column of cell. 
        pView : Handle of view. 
        """
        pass

    def GetColumn(self,pColumn):
        """
        Get a column from a column number.

        pColumn : Column number. 
        return : A copy of column. 
        """
        pass

    def GetCurrentCell(self):
        """
        Get the current cell.

        return : A copy of the the current cell. 
        """
        pass

    def GetRow(self,pRef):
        """
        Get a row from a row reference.

        pRef : Reference to a row. 
        return : A copy of the row. 
        """
        pass

    def RowAdd(self,pString,pRef):
        """
        Add a row.

        pString : Text to display with row. 
        pRef : User-defined reference for row(default=0). 
        """
        pass

    def RowSort(self,pAscending):
        """
        Sort rows.

        pAscending : If <b>true</b>, sort ascending. 
        """
        pass

    def SetCellView(self,pRef,pColumn,pView):
        """
        Set a cell's internal toolkit view.

        pRef : Row of cell. 
        pColumn : Column of cell. 
        pView : View to use to set cell's view. 
        """
        pass

    Caption=property(doc="<b>Read Write Property:</b> Caption to display for spreadsheet.         ")
    Column=property(doc="<b>Read Write Property:</b> Current column.         ")
    MultiSelect=property(doc="<b>Read Write Property:</b> Can there be multiple selections?         ")
    OnCellChange=property(doc="<b>Event:</b> Cell value changed.         ")
    OnColumnClick=property(doc="<b>Event:</b> Column clicked.         ")
    OnDragAndDrop=property(doc="<b>Event:</b> Drag and drop event.         ")
    OnRowClick=property(doc="<b>Event:</b> Row clicked.         ")
    Row=property(doc="<b>Read Write Property:</b> Current row.         ")
    pass

class FBTexture (FBBox):
    """
    Texture class.     
        
    """
    def FBTexture(self,pName):
        """
        Constructor.

        pName : Name of texture media. Can be a NULL pointer. If set, this will create a FBVideo object used as the Video property. 
        """
        pass

    def Clone(self):
        """
        Clone the texture.
        This will duplicated the current texture.

        return : Newly created texture. 
        """
        pass

    def FBDelete(self):
        """
        Open Reality Deletion function.

        """
        pass

    def OGLInit(self,pRenderOptions):
        """
        pRenderOptions : FBRenderOptions
        """
        pass

    Alpha=property(doc="<b>Read Write Property:</b> Texture alpha value.         ")
    BlendMode=property(doc="<b>Read Write Property:</b> Texture blend mode.         ")
    Filename=property(doc="<b>Read Write Property:</b> Filename for texture.         ")
    Height=property(doc="<b>Read Only Property:</b> Height of texture.         ")
    Mapping=property(doc="<b>Read Write Property:</b> Texture mapping.         ")
    Rotation=property(doc="<b>Read Write Property:</b> Rotation coordinates.         ")
    Scaling=property(doc="<b>Read Write Property:</b> Scaling coordinates.         ")
    SwapUV=property(doc="<b>Read Write Property:</b> Swap UV coordinates?         ")
    Translation=property(doc="<b>Read Write Property:</b> Translation coordinates.         ")
    Usage=property(doc="<b>Read Write Property:</b> Texture usage.         ")
    UseMaterial=property(doc="<b>Read Write Property:</b> Use the material color?         ")
    Video=property(doc="<b>Read Write Property:</b> Media used for texturing.         ")
    Width=property(doc="<b>Read Only Property:</b> Width of texture.         ")
    pass

class FBShader (FBBox):
    """
    Shader class.     
        
    """
    def FBShader(self,pName):
        """
        Protected constructor.

        pName : Shader name. 
        """
        pass

    def Append(self,pModel):
        """
        Append shader to <b>pModel</b>.

        pModel : Model to append shader to. 
        """
        pass

    def CloneShaderParameter(self,pNewShader):
        """
        Clone shader.

        pNewShader : Shader to copy data to. 
        """
        pass

    def ReplaceAll(self,pModel):
        """
        Replace all shader in <b>pModel</b>.

        pModel : Model to replace all shader to. 
        """
        pass

    def ShaderNeedBeginRender(self):
        """
        Does the shader need a begin render call.

        """
        pass

    RenderingPass=property(doc="<b>Read Write Property:</b> Rendering pass object are shaded in.         ")
    ShaderDescription=property(doc="Description.         ")
    pass

class FBUserObject (FBBox):
    """
        
        
    """
    def FBUserObject(self,pName):
        """
        Constructor.

        pName : User object name. 
        """
        pass

    pass

class FBLayout (FBVisualComponent):
    """
    User interface layout class.     
    The user interface in MOTIONBUILDER is managed using layout objects (class FBLayout). Layouts are responsible for managing areas of the screen called regions. UI components such as buttons, viewers, and edit boxes are bound to regions. In other words, when a UI component is bound to a region, the region defines how big it is and how it behaves when the layout is resized.<b>Types of Layouts</b> With the different types of plugins available, there are different kinds of layouts, depending on where the plugin fits into the MOTIONBUILDER architecture. The following types of layouts exist: Device layouts. Constraint layouts. Manipulator layouts. Shader layouts.     
    """
    def FBLayout(self):
        """
        Constructor.

        """
        pass

    def AddRegion(self,pName,pTitle,pX,pXType,pXRelative,pMultX,pY,pYType,pYRelative,pMultY,pW,pWType,pWRelative,pMultW,pH,pHType,pHRelative,pMultH):
        """
        Add a region to the layout.

        pName : Name of region. 
        pTitle : Title to display. 
        pX : X: Position. 
        pXType : X: Type of Attachment. 
        pXRelative : X: Item to attach to. 
        pMultX : X: Multiplier of relative value. 
        pY : Y: Position. 
        pYType : Y: Type of Attachment. 
        pYRelative : Y: Item to attach to. 
        pMultY : Y: Multiplier of relative value. 
        pW : W: Width of region. 
        pWType : W: Type of Attachment. 
        pWRelative : W: Item to attach to. 
        pMultW : W: Multiplier of relative value. 
        pH : H: Height of region. 
        pHType : H: Type of Attachment. 
        pHRelative : H: Item to attach to. 
        pMultH : H: Multiplier of relative value. 
        return : Operation was successful (<b>true</b> or <b>false</b>). 
        """
        pass

    def ClearControl(self,pName):
        """
        Remove a control from a region in a visual component.

        pName : Name of region to remove control. 
        """
        pass

    def GetControl(self,pName):
        """
        Get control of a region in a visual component.

        pName : Name of region to find. 
        return : The component if it is found. 
        """
        pass

    def GetRegion(self,pName):
        """
        Verify if a region with <b>pName</b> exists.

        pName : Name of region to check. 
        return : Operation was successful (<b>true</b> or <b>false</b>). 
        """
        pass

    def GetRegionPositions(self,pName,pComputed,pX,pY,pW,pH):
        """
        Get region <b>pName</b> information (position and size).

        pName : Name of region. 
        pComputed : Is the information retrieved relative or absolute? 
        pX : Position in X of the region. 
        pY : Position in Y of the region. 
        pW : Width of the region. 
        pH : Height of the region. 
        return : Operation was successful (<b>true</b> or <b>false</b>). 
        """
        pass

    def GetSplitStyle(self,pName):
        """
        Get a region's splitstyle.

        pName : Name of Region to get splitstyle from. 
        return : Split style of specified region. 
        """
        pass

    def MoveRegion(self,pName,pX,pY):
        """
        Move a region.

        pName : Name of region to move. 
        pX : New X position. 
        pY : New Y position. 
        return : Operation was successful (<b>true</b> or <b>false</b>). 
        """
        pass

    def RemoveRegion(self,pName):
        """
        Remove a region.

        pName : Name of region to remove. 
        return : Operation was successful (<b>true</b> or <b>false</b>). 
        """
        pass

    def RenameRegion(self,pOldName,pNewName):
        """
        Rename a region.

        pOldName : Region's old name. 
        pNewName : Region's new name. 
        return : Operation was successful (<b>true</b> or <b>false</b>). 
        """
        pass

    def Restructure(self,pNoMove):
        """
        Force a recomputation of all region placements in the layout.

        pNoMove : bool
        """
        pass

    def SetAutoRestructure(self,pAutoRestructure):
        """
        Suspend all automatic layout recomputation.

        pAutoRestructure : If true, Suspend all automatic layout recomputation, else restore it. 
        """
        pass

    def SetBorder(self,pName,pType,pShowTitle,pInSet,pWidth,pSpacing,pMaxAngle,pCornerRadius):
        """
        Set border properties for a region.

        pName : Name of Region to change border properties. 
        pType : Border style to use. 
        pShowTitle : Show region title? 
        pInSet : Is region inset? 
        pWidth : Border width. 
        pSpacing : Border spacing. 
        pMaxAngle : Max angle for rounding. 
        pCornerRadius : Corner radius for rounding. 
        return : Operation was successful (<b>true</b> or <b>false</b>). 
        """
        pass

    def SetControl(self,pName,pComponent):
        """
        Set control of a region to a visual component.

        pName : Name of region to affect. 
        pComponent : Component to control region. 
        return : Operation was successful (<b>true</b> or <b>false</b>). 
        """
        pass

    def SetControl(self,pName,pComponent):
        """
        Set control of a region to a visual component.

        pName : Name of region to affect. 
        pComponent : Component to control region. 
        return : Operation was successful (<b>true</b> or <b>false</b>). 
        """
        pass

    def SetRegionTitle(self,pName,pTitle):
        """
        Set a region's title.

        pName : Name of region to change title. 
        pTitle : New title for region. 
        return : Operation was successful (<b>true</b> or <b>false</b>). 
        """
        pass

    def SetSplitStyle(self,pName,pRegionType):
        """
        Set a region's splitstyle.

        pName : Name of Region to set splitstyle. 
        pRegionType : Split style give to region. 
        return : Operation was successful (<b>true</b> or <b>false</b>). 
        """
        pass

    def SetView(self,pName,pComponent):
        """
        Set view.

        pName : Name of Region. 
        pComponent : Component to set as view. 
        return : Operation was successful (<b>true</b> or <b>false</b>). 
        """
        pass

    def SetView(self,pName,pComponent):
        """
        Set view.

        pName : Name of Region. 
        pComponent : Component to set as view. 
        return : Operation was successful (<b>true</b> or <b>false</b>). 
        """
        pass

    def SizeRegion(self,pName,pW,pH):
        """
        Change a region's size.

        pName : Name of region to resize. 
        pW : New region width. 
        pH : New region height. 
        return : Operation was successful (<b>true</b> or <b>false</b>). 
        """
        pass

    OnIdle=property(doc="<b>Event:</b> Idle.         ")
    OnInput=property(doc="<b>Event:</b> Input.         ")
    OnPaint=property(doc="<b>Event:</b> Paint layout.         ")
    OnResize=property(doc="<b>Event:</b> Resize layout.         ")
    OnShow=property(doc="<b>Event:</b> Show layout.         ")
    pass

class FBModel (FBBox):
    """
    Model class.     
        
    """
    def FBModel(self,pName):
        """
        Constructor.

        pName : Name of model. 
        """
        pass

    def Clone(self):
        """
        Clone the model.
        This will duplicate the current model.

        return : Newly created model. 
        """
        pass

    def FBDelete(self):
        """
        Open Reality Deletion function.

        """
        pass

    def FbxGetObjectSubType(self):
        """
        These function are used when saving the objects to a file.

        """
        pass

    def FbxGetObjectType(self):
        """
        These function are used when saving the objects to a file.

        """
        pass

    def GetBoundingBox(self,pMin,pMax):
        """
        Get the bounding box of the model.

        pMin : Minimum value of the bounding box. 
        pMax : Maximum value of the bounding box. 
        """
        pass

    def GetMatrix(self,pMatrix,pWhat,pGlobalInfo,pEvaluateInfo):
        """
        Get a matrix from the model.

        pMatrix : Matrix to fill with requested information. 
        pWhat : Type of information requested (default=transformation). 
        pGlobalInfo : <b>true</b> if it is GlobalInfo, <b>false</b> if Local (default=true). 
        pEvaluateInfo : EvaluateInfo, Take Display if none specified 
        """
        pass

    def GetSelectedPointsCount(self):
        """
        Get the number of selected points in the model.

        return : Number of selected points. 
        """
        pass

    def GetVector(self,pVector,pWhat,pGlobalInfo,pEvaluateInfo):
        """
        Get a vector from the model.

        pVector : Vector to fill with requested values. 
        pWhat : Type of information requested (default=translation, inverses not supported). 
        pGlobalInfo : <b>true</b> if it is GlobalInfo, <b>false</b> if Local (default=true). 
        pEvaluateInfo : EvaluateInfo, Take Display if none specified 
        """
        pass

    def ResetDisplayList(self):
        """
        ResetDisplayList.

        """
        pass

    def SetMatrix(self,pMatrix,pWhat,pGlobalInfo,pPushUndo,pEvaluateInfo):
        """
        Set a matrix for the model.

        pMatrix : Information to use to set the model's matrix. 
        pWhat : Type of matrix to set (default=transformation). 
        pGlobalInfo : <b>true</b> if it is GlobalInfo, <b>false</b> if Local (default=true). 
        pPushUndo : <b>true</b> if this operation is undoable, don't push undo in non UI thread. 
        pEvaluateInfo : EvaluateInfo, Take Display if none specified 
        """
        pass

    def SetVector(self,pVector,pWhat,pGlobalInfo,pPushUndo,pEvaluateInfo):
        """
        Set a vector for the model.

        pVector : Vector to use to set values. 
        pWhat : Type of information to set (default=translation, inverses not supported). 
        pGlobalInfo : <b>true</b> if it is GlobalInfo, <b>false</b> if Local (default=true). 
        pPushUndo : <b>true</b> if this operation is undoable, don't push undo in non UI thread. 
        pEvaluateInfo : EvaluateInfo, Take Display if none specified 
        """
        pass

    AnimationNode=property(doc="<b>Read Only Property:</b> Animation node of the model.         ")
    Children=property(doc="<b>List:</b> Children for model.         ")
    GeometricRotation=property(doc="<b>Read Write Property:</b> Geometric rotation.         ")
    GeometricScaling=property(doc="<b>Read Write Property:</b> Geometric scaling.         ")
    GeometricTranslation=property(doc="<b>Read Write Property:</b> Geometric translation.         ")
    Geometry=property(doc="<b>Read Only Property:</b> Geometry for the model.         ")
    Icon3D=property(doc="<b>Read Write Property:</b> Is model a 3D icon?         ")
    IsConstrained=property(doc="<b>Read Only Property:</b> Is model constrained?         ")
    IsDeformable=property(doc="<b>Read Write Property:</b> Is model deformable (weights)?         ")
    LookAt=property(doc="<b>Read Write Property:</b> Look at model (interest point).         ")
    Parent=property(doc="<b>Read Write Property:</b> Parent model.         ")
    Pickable=property(doc="<b>Read Write Property:</b> Indicate if a model can be picked in the viewer. This has a default value of 'true'.         ")
    PostRotation=property(doc="<b>Read Write Property:</b> Post Rotation (considered if RotationActive is true)         ")
    PreRotation=property(doc="<b>Read Write Property:</b> Pre Rotation (considered if RotationActive is true)         ")
    QuaternionInterpolate=property(doc="<b>Read Write Property:</b> Use quaternion interpolation.         ")
    Rotation=property(doc="<b>Read Write Property:</b> Lcl rotation.         ")
    RotationActive=property(doc="<b>Read Write Property:</b> Is model using Rotation Limits?         ")
    RotationMax=property(doc="<b>Read Write Property:</b> Max Rotation Limit (considered if RotationActive is true)         ")
    RotationMaxX=property(doc="<b>Read Write Property:</b> Is model using Maximum Rotation Limits On X?         ")
    RotationMaxY=property(doc="<b>Read Write Property:</b> Is model using Maximum Rotation Limits On Y?         ")
    RotationMaxZ=property(doc="<b>Read Write Property:</b> Is model using Maximum Rotation Limits On Z?         ")
    RotationMin=property(doc="<b>Read Write Property:</b> Min Rotation Limit (considered if RotationActive is true)         ")
    RotationMinX=property(doc="<b>Read Write Property:</b> Is model using Minimum Rotation Limits On X?         ")
    RotationMinY=property(doc="<b>Read Write Property:</b> Is model using Minimum Rotation Limits On Y?         ")
    RotationMinZ=property(doc="<b>Read Write Property:</b> Is model using Minimum Rotation Limits On Z?         ")
    RotationOrder=property(doc="<b>Read Write Property:</b> Rotation order.         ")
    RotationSpaceForLimitOnly=property(doc="<b>Read Write Property:</b> Apply Post Rotation Matrix only for Limits?         ")
    Scaling=property(doc="<b>Read Write Property:</b> Lcl scaling.         ")
    Scene=property(doc="<b>Read Only Property:</b> Scene containing the model.         ")
    Selected=property(doc="<b>Read Write Property:</b> Is model selected?         ")
    Shaders=property(doc="<b>List:</b> Shaders for model.         ")
    ShadingMode=property(doc="<b>Read Write Property:</b> Shading mode for the model.         ")
    Show=property(doc="<b>Read Write Property:</b> Indicate if the viewer should show the object, according to its visibility value. This has a default value of 'false'.         ")
    SoftSelected=property(doc="<b>Read Write Property:</b> Is model Soft selected?         ")
    Translation=property(doc="<b>Read Write Property:</b> Lcl translation.         ")
    UpVector=property(doc="<b>Read Write Property:</b> UpVector model.         ")
    Visibility=property(doc="<b>Read Write Property:</b> Visibility of model. This can be overriden by the 'Show' property.         ")
    pass

class FBEditVector (FBVisualComponent):
    """
    Vector edit widget.     
        
    """
    def FBEditVector(self):
        """
        Constructor.

        """
        pass

    OnChange=property(doc="<b>Event:</b> Vector value changed.         ")
    Value=property(doc="<b>Read Write Property:</b> Current value of vector.         ")
    pass

class FBObjectPose (FBPose):
    """
    FBObjectPose class.     
    This class exposes the object used to store the pose of objects.     
    """
    def FBObjectPose(self,pName):
        """
        Public constructor.
        This constructor is used to create a new object.

        pName : Object name. If pObject is not NULL, pName will be ignored. 
        """
        pass

    def AddStanceOffset(self,pObjectName,pStancePose,pPoseTransformType):
        """
        Add the StanceOffset to an object in the pose.

        pObjectName : Name of the object. 
        pStancePose : Pose representing the stance of all objects. 
        pPoseTransformType : Transform type in which to add the offset (Local, Global or LocalRef). 
        """
        pass

    def AddStanceOffsetAllObjects(self,pStancePose,pPoseTransformType):
        """
        Add the StanceOffset to all the objects in the pose.

        pStancePose : Pose representing the stance of all objects. 
        pPoseTransformType : Transform type in which to add the offset (Local, Global or LocalRef). 
        """
        pass

    def ClearPose(self):
        """
        Clear all the data of the pose.

        """
        pass

    def CopyFrom(self,pFromPose):
        """
        Copy everything from a given object.

        pFromPose : Pose from which to copy. 
        """
        pass

    def CopyObjectPose(self,pObjectName,pObject):
        """
        Copy the pose of all the properties of an object.

        pObjectName : Name of the object to store in the pose. 
        pObject : Object from which we'll read all the property values to store in the pose. 
        """
        pass

    def CopyPoseAllObjectsTransformFrom(self,pFromPose,pPoseTransformType):
        """
        Copy all the transforms from a given pose.

        pFromPose : Pose from which to copy the data. 
        pPoseTransformType : Transform type from which to copy the transform (Local, Global or LocalRef). 
        """
        pass

    def CopyPoseDataFrom(self,pFromPose):
        """
        Copy all the pose data from a given pose.

        pFromPose : Pose from which to copy the data. 
        """
        pass

    def CopyPoseTransformFrom(self,pFromPose,pObjectName,pPoseTransformType):
        """
        Copy the transforms of an object from a given pose.

        pFromPose : Pose from which to copy the data. 
        pObjectName : Name of object to copy the transform from. 
        pPoseTransformType : Transform type from which to copy the transform (Local, Global or LocalRef). 
        """
        pass

    def CopyPropertyPose(self,pObjectName,pProperty):
        """
        Copy the pose of a property of an object.

        pObjectName : Name of the object to store in the pose. 
        pProperty : Property from which we'll read the value to store in the pose. 
        """
        pass

    def CopyTransform(self,pObjectName,pObject,pObjectPoseOptions):
        """
        Copy the transform of an object.

        pObjectName : Name of the object to store in the pose. 
        pObject : Object from which we'll evaluate the transform values to store in the pose. 
        pObjectPoseOptions : PoseOptions used to specify the transform of the reference object (Default: Identity). 
        """
        pass

    def GetPropertyValue(self,pValue,pSize,pObjectName,pPropertyName):
        """
        Get the value of a property stored in the pose.

        pValue : Value to get. 
        pSize : Number of elements in pValue. 
        pObjectName : Name of the object to get the value. 
        pPropertyName : Name of the property to get the value. 
        """
        pass

    def GetTransform(self,pT,pRM,pSM,pObjectName,pPoseTransformType):
        """
        Get the transform of an object in the pose.

        pT : Translation to get. 
        pRM : Rotation to get. 
        pSM : Scaling to get. 
        pObjectName : Name of the object to get the transform. 
        pPoseTransformType : Transform type in which to set the transform (Local, Global or LocalRef). 
        return : True if the transform was found in the pose. 
        """
        pass

    def IsPropertyPoseable(self,pProperty):
        """
        Is the property poseable?

        pProperty : FBProperty
        return : True if the value of this property can be stored in the pose. 
        """
        pass

    def IsPropertyStored(self,pObjectName,pPropertyName):
        """
        Is the property stored in the pose?

        pObjectName : Name of the object. 
        pPropertyName : Name of the property. 
        return : True if the property is stored in the pose. 
        """
        pass

    def IsTransformStored(self,pObjectName,pPoseTransformType):
        """
        Is the transform of this object stored in the specified TransformType?

        pObjectName : Name of the object. 
        pPoseTransformType : Transform type in which to check. 
        return : True if the transform of this object is stored in the specified TransformType (Local, Global and LocalRef). 
        """
        pass

    def MirrorPose(self,pObjectName,pObjectPoseMirrorOptions):
        """
        Mirror the transform of an object in the pose.

        pObjectName : Name of the object to mirror. 
        pObjectPoseMirrorOptions : MirrorOptions used to specify the mirror plane. 
        """
        pass

    def MirrorPoseAllObjects(self,pObjectPoseMirrorOptions):
        """
        Mirror the transform of all objects in the pose.

        pObjectPoseMirrorOptions : MirrorOptions used to specify the mirror plane. 
        """
        pass

    def MultTransform(self,pObjectName,pGX,pTransformAttribute,pPoseTransformType):
        """
        Multiply the transform of an objects in the pose.

        pObjectName : Name of the object. 
        pGX : Transformation matrix to apply. 
        pTransformAttribute : Transform attribute to affect. Supported: T,R,S and Transformation. 
        pPoseTransformType : Transform type in which to mult the transform (Local, Global or LocalRef). 
        """
        pass

    def MultTransformAllObjects(self,pGX,pTransformAttribute,pPoseTransformType):
        """
        Multiply the transform of all objects in the pose.

        pGX : Transformation matrix to apply. 
        pTransformAttribute : Transform attribute to affect. Supported: T,R,S and Transformation. 
        pPoseTransformType : Transform type in which to mult the transform (Local, Global or LocalRef). 
        """
        pass

    def PasteObjectPose(self,pObjectName,pObject):
        """
        Paste the pose of all the properties of an object.

        pObjectName : Name of the object stored in the pose. 
        pObject : Object which will receive the values stored in the pose. 
        """
        pass

    def PastePropertyPose(self,pObjectName,pProperty):
        """
        Paste the pose of a property of an object.

        pObjectName : Name of the object stored in the pose. 
        pProperty : Property which will receive the value stored in the pose. 
        """
        pass

    def PasteTransform(self,pObjectName,pObject,pObjectPoseOptions):
        """
        Paste the transform of an object.

        pObjectName : Name of the object stored in the pose. 
        pObject : Object which will receive the transform values stored in the pose. 
        pObjectPoseOptions : PoseOptions used to specify the transform of the reference object, the TransformType and TransformAttributes to paste. 
        """
        pass

    def RemoveStanceOffset(self,pObjectName,pStancePose,pPoseTransformType):
        """
        Remove the StanceOffset from an object in the pose.

        pObjectName : Name of the object. 
        pStancePose : Pose representing the stance of all objects. 
        pPoseTransformType : Transform type in which to remove the offset (Local, Global or LocalRef). 
        """
        pass

    def RemoveStanceOffsetAllObjects(self,pStancePose,pPoseTransformType):
        """
        Remove the StanceOffset from all the objects in the pose.

        pStancePose : Pose representing the stance of all objects. 
        pPoseTransformType : Transform type in which to remove the offset (Local, Global or LocalRef). 
        """
        pass

    def SetPropertyValue(self,pObjectName,pPropertyName,pValue,pSize):
        """
        Set the value of a property in the pose.

        pObjectName : Name of the object to set the value. 
        pPropertyName : Name of the property to set the value. 
        pValue : Value to set. 
        pSize : Number of elements in pValue. 
        """
        pass

    def SetTransform(self,pT,pRM,pSM,pObjectName,pPoseTransformType):
        """
        Set the transform of an object in the pose.

        pT : Translation to set. 
        pRM : Rotation to set. 
        pSM : Scaling to set. 
        pObjectName : Name of the object to set the transform. 
        pPoseTransformType : Transform type in which to set the transform (Local, Global or LocalRef). 
        """
        pass

    pass

class FBEditProperty (FBVisualComponent):
    """
    Property editor widget.     
    This widget allows users to edit the values of a property without having to manually customize the GUI depending on the type of the property being edited.SDK objects can have three types of properties:An internal property which maps to an actual property that can be seen in the property editor tool of the application. This type of property is usually obtained from the PropertyList data member.SDK-only property which does not maps onto an existing property of the encapsulated object. The existence of these types of property is often to make the object interface simpler. All the FBPropertyList-types will fall into this category, except for FBPropertyListObjects.SDK property which maps onto an existing object property, but does so indirectly using function calls instead of direct property access. This is usually for historical reason. In this case the property will usually be present twice in the PropertyList: once as an SDK-Only property and another time as an internal property.Another limitation of this widget is that it can only display non hidden internal properties. To get around this issue, the property flag can be changed to unhide it. Doing so will also cause the property to be visible via the property tool. 
@code
       // In a tool header file...
       FBEditProperty mEditProperty;

       // In a tool source file...
       HFBModel lModel = FBFindModelByName( 'ModelName' );
       if( lModel )
       {
           HFBProperty lProperty = lModel->PropertyList.Find( 'RotationOrder' );
           if( lProperty &&
               lProperty->IsInternal() &&
               !lProperty->GetPropertyFlag( kFBPropertyFlagHideProperty ))
           {
               mEditProperty.Property = lProperty;
           }
       }
@endcode

     
    """
    def FBEditProperty(self):
        """
        Constructor.

        """
        pass

    LargeInc=property(doc="<b>Read Write Property:</b> Indicate the large increment applied when click-draging on the property value (usually left-click-dragging)         ")
    Precision=property(doc="<b>Read Write Property:</b> Used to specify the width and precision of the value shown. A value of 7.2 indicates to show at minimum 7 numbers, with 2 decimals.         ")
    Property=property(doc="<b>Read Write Property:</b> Property to edit. Set to NULL to disable.         ")
    SliderMax=property(doc="<b>Read Write Property:</b> Should the property be editable using a slider, set the maximum value atainable with the slider.         ")
    SliderMin=property(doc="<b>Read Write Property:</b> Should the property be editable using a slider, set the minimum value atainable with the slider.         ")
    SmallInc=property(doc="<b>Read Write Property:</b> Indicate the small increment applied when click-draging on the property value (usually right-click-dragging)         ")
    pass

class FBMaterial (FBBox):
    """
    Material class.     
        
    """
    def FBMaterial(self,pName):
        """
        Constructor.

        pName : Name of material. 
        """
        pass

    def Clone(self):
        """
        Clone the material.
        This will duplicated the current material.

        return : Newly created material. 
        """
        pass

    def OGLInit(self):
        """
        """
        pass

    Ambient=property(doc="<b>Read Write Property:</b> Ambient color.         ")
    Diffuse=property(doc="<b>Read Write Property:</b> Diffuse color.         ")
    Emissive=property(doc="<b>Read Write Property:</b> Emissive color.         ")
    Opacity=property(doc="<b>Read Write Property:</b> Opacity value.         ")
    Reflect=property(doc="<b>Read Write Property:</b> Reflection value.         ")
    Shininess=property(doc="<b>Read Write Property:</b> Shininess value.         ")
    Specular=property(doc="<b>Read Write Property:</b> Specular color.         ")
    pass

class FBBrowsingProperty (FBVisualComponent):
    """
    Property browsing.     
        
    """
    def FBBrowsingProperty(self):
        """
        Constructor.

        """
        pass

    def AddObject(self,pObject):
        """
        Add an object whose properties will be displayed.

        pObject : Object whose properties will be displayed in the property brwoser. 
        """
        pass

    def ObjectGet(self,pIndex):
        """
        Return the object at the specified index.

        pIndex : Index of the object to get. 
        return : Object at the index specified currently displayed in the property browser. 
        """
        pass

    def ObjectGetCount(self):
        """
        Get the number of object displayed in the property browser.

        return : Object currently displayed in the property browser. 
        """
        pass

    def RemoveObject(self,pObject):
        """
        Remove an object from the property browser.

        pObject : Object to remove. 
        """
        pass

    pass

class FBPropertyConnectionEditor (FBVisualComponent):
    """
    Property Connection Editor.     
        
    """
    def FBPropertyConnectionEditor(self):
        """
        Constructor.

        """
        pass

    def PopupList(self):
        """
        Launch a list of connected objects.

        """
        pass

    def PopupTree(self):
        """
        Launch a tree of object connections.

        """
        pass

    Property=property(doc="<b>Read Write Property:</b> Property to edit connections. Set to NULL to disable.         ")
    pass

class FBAssetFolder (FBAssetItem):
    """
    Class representing a folder stored in a version control database.     
        
    """
    def FBAssetFolder(self,pName):
        """
        Constructor.

        pName : Name of Command. 
        """
        pass

    def AddFile(self,pLocalPath,pComment,pCheckOut,pSilent):
        """
        Add a specified file into the database.
        It will be added in this folder.

        pLocalPath : The full path to the file on the local disk. 
        pComment : Comment to be applied for the operation. 
        pCheckOut : Whether the file should be checked out or not. 
        pSilent : If pSilent is set to true, no dialog will be displayed by this method. 
        return : An HFBAssetfile object representing the newly added file. 
        """
        pass

    def AddFolder(self,pName,pComment,pSilent):
        """
        Add a folder in the database.
        It will be added in this folder.

        pName : Name of the folder to be created. 
        pComment : Comment to be applied for the operation. 
        pSilent : If pSilent is set to true, no dialog will be displayed by this method. 
        return : An HFBAssetFolder object representing the newly added folder. 
        """
        pass

    def FBCreate(self):
        """
        Open Reality Creation function.

        return : Outcome of creation (true/false). 
        """
        pass

    def GetChild(self,pIndex):
        """
        Get the child at index <b>pIndex</b>.

        pIndex : int
        return : The child at <b>pIndex</b>, or NULL if the index was out of range. 
        """
        pass

    def GetChildCount(self):
        """
        Get the number of items in this folder.

        return : The number of items in this folder. 
        """
        pass

    def GetFile(self,pName):
        """
        Get a file present in this folder by using it's name.

        pName : str
        return : The file with the given name, or NULL if it was not found. 
        """
        pass

    def GetFolder(self,pName):
        """
        Get a folder present in this folder by using it's name.

        pName : str
        return : The folder with the given name, or NULL if it was not found. 
        """
        pass

    pass

class FBConstraint (FBBox):
    """
    Constraint class.     
        
    """
    def FBConstraint(self,pName):
        """
        Constructor.

        pName : Name of constraint. 
        """
        pass

    def AnimationNodeInCreate(self,pUserId,pModel,pAttribute):
        """
        Animation Node Creations (IN/OUT).
        Used to create the connectors (in or out) on an animation node. This function will return a newly created animation node, connected to the model specified by <b>pModel</b>.

        pUserId : User specified reference number. 
        pModel : Model to associate with animation node. 
        pAttribute : Attribute of model to animate (i.e. Translation, Lcl Translation, etc.) 
        return : Newly created IN/OUT animation node. 
        """
        pass

    def AnimationNodeInCreate(self,pUserId,pProperty):
        """
        Animation Node Creations (IN).
        Used to create the In connectors on an animation node. This function will return a newly created animation node, connected to the model specified by <b>pProperty</b>.

        pUserId : User specified reference number. 
        pProperty : Property of model to animate (must be animatable) 
        return : Newly created IN animation node. 
        """
        pass

    def AnimationNodeNotify(self,pAnimationNode,pEvaluateInfo,pConstraintInfo):
        """
        Notification callback for connectors.

        pAnimationNode : Animation node being notified. 
        pEvaluateInfo : Information for evaluation. 
        pConstraintInfo : Information for constraint. 
        return : <b>true</b> if successful. 
        """
        pass

    def AnimationNodeOutCreate(self,pUserId,pModel,pAttribute):
        """
        Animation Node Creations (IN/OUT).
        Used to create the connectors (in or out) on an animation node. This function will return a newly created animation node, connected to the model specified by <b>pModel</b>.

        pUserId : User specified reference number. 
        pModel : Model to associate with animation node. 
        pAttribute : Attribute of model to animate (i.e. Translation, Lcl Translation, etc.) 
        return : Newly created IN/OUT animation node. 
        """
        pass

    def Clone(self):
        """
        Clone the constraint.
        This will create a new constraint. If pCloneModels is specified as 'true' a copy of all the models will be made for the new constraint.

        return : Newly created (and copied) constraint. 
        """
        pass

    def DeformerBind(self,pModel):
        """
        Bind/Unbind <b>pModel</b> to deformation constraint.
        These functions are used for adding/removing a deformation binding to/from <b>pModel</b> if the constraint is a deformation constraint.

        pModel : Model to bind/unbind. 
        return : <b>true</b> if successful. 
        """
        pass

    def DeformerNotify(self,pModel,pSrcVertex,pSrcNormal,pCount,pDstVertex,pDstNormal):
        """
        Deformation notification function.

        pModel : Model to deform. 
        pSrcVertex : Source vertex array (i.e. vertex to deform). 
        pSrcNormal : Normals at source vertex array. 
        pCount : Number of vertices in source/destination arrays 
        pDstVertex : Destination vertex array (i.e. where source vertex gets deformed to) 
        pDstNormal : Normals at destination vertex array. 
        return : <b>true</b> if successful. 
        """
        pass

    def DeformerUnBind(self,pModel):
        """
        Bind/Unbind <b>pModel</b> to deformation constraint.
        These functions are used for adding/removing a deformation binding to/from <b>pModel</b> if the constraint is a deformation constraint.

        pModel : Model to bind/unbind. 
        return : <b>true</b> if successful. 
        """
        pass

    def Disable(self,pModel):
        """
        Disable constraint on <b>pModel</b>.

        pModel : Model on which constraint should be disabled. 
        return : <b>true</b> if successful. 
        """
        pass

    def FreezeSRT(self,pModel,pS,pR,pT):
        """
        Freeze current model state.

        pModel : Model to freeze constraint on. 
        pS : Scaling freeze? 
        pR : Rotation freeze? 
        pT : Translation freeze? 
        """
        pass

    def FreezeSuggested(self):
        """
        Suggest 'freeze'.

        """
        pass

    def ReferenceAdd(self,pGroupIndex,pModel):
        """
        Add a reference to a specified group.

        pGroupIndex : Group to add reference to. 
        pModel : Model to place at new reference. 
        return : <b>true</b> if successful. 
        """
        pass

    def ReferenceAddNotify(self,pGroupIndex,pModel):
        """
        Notification callbacks for when a reference is added or removed.

        pGroupIndex : Index of group where reference was affected. 
        pModel : Model to which reference was associated. 
        return : <b>true</b> if successful. 
        """
        pass

    def ReferenceGet(self,pGroupIndex,pItemIndex):
        """
        Get a reference.

        pGroupIndex : Index of reference group containing desired reference. 
        pItemIndex : Index of reference in group to get (default is 0). 
        return : Model at specified reference. 
        """
        pass

    def ReferenceGetCount(self,pGroupIndex):
        """
        Get number of references in a specified group.

        pGroupIndex : Index of group to query the number of references. 
        return : Number of references in specified group. 
        """
        pass

    def ReferenceGroupAdd(self,pGroupName,pMaxItemCount):
        """
        Add a group of references.

        pGroupName : Name of reference group to add. 
        pMaxItemCount : Maximum number of items in <b>pGroupName</b>. 
        return : Index of new reference group. 
        """
        pass

    def ReferenceGroupGetCount(self):
        """
        Return the number of reference groups.

        return : Number of reference groups. 
        """
        pass

    def ReferenceGroupGetMaxCount(self,pGroupIndex):
        """
        Get the maximum number of items that can exist in the reference group in question.

        pGroupIndex : Index of reference group. 
        return : Maximum number of items that can be added to the reference group. 
        """
        pass

    def ReferenceGroupGetName(self,pGroupIndex):
        """
        Get the name of the reference group.

        pGroupIndex : Index of the reference group to get the name for. 
        return : The name of the reference group <b>pGroupIndex</b>. 
        """
        pass

    def ReferenceRemove(self,pGroupIndex,pModel):
        """
        Remove a reference to <b>pModel</b> from the group at <b>pGroupIndex</b>.

        pGroupIndex : Index to remove reference from. 
        pModel : Model to remove reference from. 
        return : <b>true</b> if successful. 
        """
        pass

    def ReferenceRemoveNotify(self,pGroupIndex,pModel):
        """
        Notification callbacks for when a reference is added or removed.

        pGroupIndex : Index of group where reference was affected. 
        pModel : Model to which reference was associated. 
        return : <b>true</b> if successful. 
        """
        pass

    def RemoveAllAnimationNodes(self):
        """
        Remove animation nodes.

        """
        pass

    def RestoreModelState(self,pModel):
        """
        Restore the saved model state onto <b>pModel</b>.

        pModel : Model to affect with previous state. 
        """
        pass

    def SaveModelState(self,pModel,pS,pR,pT):
        """
        Save current state of <b>pModel</b>.

        pModel : Model to save. 
        pS : Scaling information? 
        pR : Rotation information? 
        pT : Translation information? 
        """
        pass

    def SetupAllAnimationNodes(self):
        """
        Setup animation nodes.

        """
        pass

    def SnapSuggested(self):
        """
        Suggest 'snap'.

        """
        pass

    Active=property(doc="<b>Read Write Property:</b> Active state.         ")
    Deformer=property(doc="<b>Read Write Property:</b> Is a deformer constraint?         ")
    Description=property(doc="<b>Read Write Property:</b> Long description of constraint.         ")
    HasLayout=property(doc="<b>Read Write Property:</b> Does the constraint have a layout?         ")
    Lock=property(doc="<b>Read Write Property:</b> Lock state.         ")
    Snap=property(doc="<b>Function Property:</b> Snap constraint.         ")
    Weight=property(doc="<b>Read Write Property:</b> Weight of constraint.         ")
    pass

class FBCharacterPose (FBPose):
    """
    FBCharacterPose class.     
    This class exposes the object used to store the pose of objects.     
    """
    def FBCharacterPose(self,pName):
        """
        Public constructor.
        This constructor is used to create a new object.

        pName : Object name. 
        """
        pass

    def ApplyPoseCandidate(self):
        """
        After setting the candidate on the skeleton node, calling this function will allow subsequent call to get the TRS value of a skeleton node to return the candidate value.

        """
        pass

    def ClearCharacterExtensionsPose(self):
        """
        Clear only the pose of the character extensions (omit the character).

        """
        pass

    def ClearCharacterPose(self):
        """
        Clear only the pose of the character (omit the extensions).

        """
        pass

    def ClearPose(self):
        """
        Clear all the data of the pose.

        """
        pass

    def CopyFrom(self,pFromPose):
        """
        Copy everything from a given object.

        pFromPose : Pose from which to copy. 
        """
        pass

    def CopyPose(self,pCharacter):
        """
        Copy the pose of a character and its extensions.

        pCharacter : Character to copy the pose from. 
        """
        pass

    def CopyPoseCharacter(self,pCharacter):
        """
        Copy the pose of only the character (omit the extensions).

        pCharacter : Character to copy the pose from. 
        """
        pass

    def CopyPoseCharacterExtension(self,pCharacterExtension):
        """
        Copy the pose of a single character extension.

        pCharacterExtension : Character extension to copy the pose from. 
        """
        pass

    def CopyPoseCharacterExtensions(self,pCharacter):
        """
        Copy the pose of only the character extensions (omit the character).

        pCharacter : Character to copy the pose of the extensions from. 
        """
        pass

    def CopyPoseCharacterExtensionsFrom(self,pFromPose):
        """
        Copy the pose data of only the character extensions from a given pose.

        pFromPose : Pose from which to copy the data. 
        """
        pass

    def CopyPoseCharacterFrom(self,pFromPose):
        """
        Copy the pose data of only the character from a given pose.

        pFromPose : Pose from which to copy the data. 
        """
        pass

    def CopyPoseDataFrom(self,pFromPose):
        """
        Copy all the pose data from a given pose.

        pFromPose : Pose from which to copy the data. 
        """
        pass

    def GetCharacterExtensionNameFromPose(self,pCharacterExtensionPose):
        """
        Get the name of the character extension for the specified pose.

        pCharacterExtensionPose : Pose of a character extension to check its name. 
        return : The name of the character extension (It is the label name of the character extension). 
        """
        pass

    def GetCharacterExtensionPose(self,pCharacterExtensionName):
        """
        Get the pose of a character extension.

        pCharacterExtensionName : Name of the character extension pose to get (It is the label name of the character extension). 
        return : The pose of the character extension, NULL if not found. 
        """
        pass

    def GetCharacterExtensionPoseAt(self,pIndex):
        """
        Get the pose of a character extension.

        pIndex : Index of the character extension pose to get. 
        return : The pose of the character extension. 
        """
        pass

    def GetCharacterExtensionPoseCount(self):
        """
        Get the number of character extension stored in the pose.

        return : Number of character extension stored in the pose. 
        """
        pass

    def GetExtraBoneParentRotationOffset(self,pR,pIndex):
        """
        Get the extra bone transformation offset.

        pR : A vector that will contains the parent rotation offset value on return. 
        pIndex : Index of the extra bone to get. 
        """
        pass

    def GetExtraBoneTransform(self,pT,pR,pS,pIndex):
        """
        Get the extra bone transformation.

        pT : A vector that will contains the translation value on return. 
        pR : A vector that will contains the rotation value on return. 
        pS : A vector that will contains the scale value on return. 
        pIndex : Index of the extra bone to get. 
        """
        pass

    def GetExtraBoneTransformOffset(self,pT,pR,pS,pIndex):
        """
        Get the extra bone transformation offset.

        pT : A vector that will contains the translation offset value on return. 
        pR : A vector that will contains the rotation offset value on return. 
        pS : A vector that will contains the scale offset value on return. 
        pIndex : Index of the extra bone to get. 
        """
        pass

    def GetMirrorPlaneEquation(self,pMirrorPlaneEquation,pCharacter,pCharacterPoseOptions):
        """
        Get the mirror plane equation that would be used to mirror according to the CharacterPoseOptions.

        pMirrorPlaneEquation : Out: Mirror plane equation. 
        pCharacter : Character to receive the pose. 
        pCharacterPoseOptions : Options used to paste the pose. 
        """
        pass

    def GetMirrorPlaneEquation(self,pMirrorPlaneEquation,pCharacter,pCharacterPoseOptions):
        """
        Get the mirror plane equation that would be used to mirror according to the CharacterPoseOptions.

        pMirrorPlaneEquation : Out: Mirror plane equation. 
        pCharacter : Character to receive the pose. 
        pCharacterPoseOptions : Options used to paste the pose. 
        """
        pass

    def GetOrCreateCharacterExtensionPose(self,pCharacterExtensionName):
        """
        Get the pose of a character extension and create it if necessary.

        pCharacterExtensionName : Name of the character extension pose to get (It is the label name of the character extension). 
        return : The pose of the character extension. 
        """
        pass

    def IsCharacterExtensionPoseStored(self,pCharacterExtensionName):
        """
        Is the pose of the character extension stored in the pose?

        pCharacterExtensionName : Name of the character extension. 
        return : <b>true</b> if the pose of the character extension stored in the pose. 
        """
        pass

    def IsCharacterPoseStored(self):
        """
        Is the pose of the character stored in the pose?

        return : <b>true</b> if the pose of the character stored in the pose. 
        """
        pass

    def PastePose(self,pCharacter,pCharacterPoseOptions):
        """
        Paste the pose of a character and its extensions.

        pCharacter : Character to paste the pose to. 
        pCharacterPoseOptions : Options used to specify how to paste. 
        """
        pass

    def PastePoseCharacter(self,pCharacter,pCharacterPoseOptions):
        """
        Paste the pose of only the character (omit the extensions).

        pCharacter : Character to paste the pose to. 
        pCharacterPoseOptions : Options used to specify how to paste. 
        """
        pass

    def PastePoseCharacterExtension(self,pCharacterExtension,pCharacterPoseOptions):
        """
        Paste the pose of a single character extension.

        pCharacterExtension : Character extension to paste the pose to. 
        pCharacterPoseOptions : Options used to specify how to paste. 
        """
        pass

    def PastePoseCharacterExtensions(self,pCharacter,pCharacterPoseOptions):
        """
        Paste the pose of only the character extensions (omit the character).

        pCharacter : Character to paste the pose of the extensions to. 
        pCharacterPoseOptions : Options used to specify how to paste. 
        """
        pass

    def RemoveCharacterExtensionPose(self,pCharacterExtensionName):
        """
        Remove the pose of a character extension.

        pCharacterExtensionName : Name of the character extension pose to remove (It is the label name of the character extension). 
        """
        pass

    def RemoveCharacterExtensionPoseAt(self,pIndex):
        """
        Remove the pose of a character extension.

        pIndex : Index of the character extension pose to remove. 
        """
        pass

    pass

class FBTimeCode (FBVisualComponent):
    """
        
        
    """
    def FBTimeCode(self):
        """
        Constructor.

        """
        pass

    OnChange=property(doc="<b>Event:</b> Timecode changed.         ")
    Value=property(doc="<b>Read Write Property:</b> Current timecode value.         ")
    pass

class FBEditNumber (FBVisualComponent):
    """
    Number edit box.     
        
    """
    def FBEditNumber(self):
        """
        Constructor.

        """
        pass

    LargeStep=property(doc="<b>Read Write Property:</b> Large step value.         ")
    Max=property(doc="<b>Read Write Property:</b> Maximum value.         ")
    Min=property(doc="<b>Read Write Property:</b> Minimum value.         ")
    OnChange=property(doc="<b>Event:</b> Number changed.         ")
    Precision=property(doc="<b>Read Write Property:</b> Precision of value.         ")
    SmallStep=property(doc="<b>Read Write Property:</b> Small step value.         ")
    Value=property(doc="<b>Read Write Property:</b> Current value.         ")
    pass

class FBMesh (FBGeometry):
    """
    Mesh class.     
        
    """
    def FBMesh(self,pModel):
        """
        Constructor.

        pModel : Model to which mesh belongs. 
        """
        pass

    def PolygonBegin(self):
        """
        Begin Polygon definition.

        return : Number of existing polygons in Mesh 
        """
        pass

    def PolygonCount(self):
        """
        Get number of polygons in mesh.

        return : Number of polygons in mesh. 
        """
        pass

    def PolygonEnd(self):
        """
        End Polygon definition.
        Clean up and associate vertices internally.

        return : Current number of polygons. 
        """
        pass

    def PolygonMaterialIdGet(self,pIndex):
        """
        Get a Material ID.

        pIndex : Vertex to get material ID at(default=-1). 
        return : ID of material of vertex at <b>pIndex</b>. 
        """
        pass

    def PolygonMaterialIdSet(self,pMaterialId,pIndex):
        """
        Set a material ID.

        pMaterialId : Material ID to set with. 
        pIndex : Vertex to set material ID at(default=-1). 
        return : <b>true</b> if successful. 
        """
        pass

    def PolygonSurfaceIdGet(self,pIndex):
        """
        Get a Surface ID.

        pIndex : Vertex to get Surface ID at(default=-1). 
        return : ID of Surface of vertex at <b>pIndex</b>. 
        """
        pass

    def PolygonSurfaceIdSet(self,pSurfaceId,pIndex):
        """
        Set a surface ID.

        pSurfaceId : Surface ID to set with. 
        pIndex : Vertex to set surface ID at(default=-1). 
        return : <b>true</b> if successful. 
        """
        pass

    def PolygonTextureIdGet(self,pIndex):
        """
        Get a Texture ID.

        pIndex : Vertex to get Texture ID at(default=-1). 
        return : ID of Texture at vertex <b>pIndex</b>. 
        """
        pass

    def PolygonTextureIdSet(self,pTextureId,pIndex):
        """
        Set a texture ID.

        pTextureId : Texture ID to set with. 
        pIndex : Vertex to set texture ID at(default=-1). 
        return : <b>true</b> if successful. 
        """
        pass

    def PolygonVertexAdd(self,pVertex):
        """
        Add a vertex.

        pVertex : Index in mesh of vertex to add to polygon 
        return : <b>true</b> if successful. 
        """
        pass

    def PolygonVertexCount(self,pPolygonIndex):
        """
        Get Polygon vertext count.

        pPolygonIndex : Index of polygon to get vertex count from. 
        return : Number of vertices in polygon at <b>pPolygonIndex</b>. 
        """
        pass

    def PolygonVertexIndex(self,pPolygonIndex,pVertexPolygonIndex):
        """
        Get global (for the mesh) index of a vertex from a polygon.

        pPolygonIndex : Index of polygon in question. 
        pVertexPolygonIndex : Polygon vertex index. 
        return : Index in mesh of vertex. 
        """
        pass

    pass

class FBVideo (FBBox):
    """
    Video media class.     
    Similar to the FBModel class, the FBVideo class serves as a general media class for images, video clips and video memory, as well as the possiblity of custom formats and custom live cards.To have a valid FBVideo object, it must be constructed with a string pointing to a valid media file. After the creation, the method 'IsValid()' should be used to confirm the object's status. An invalid object cannot be used or interact with any other application object. The only property that can be read and modified is its 'Filename'. To make convert an invalid FBVideo object into a vali one, simply change its Filename property to point to a supported media file.     
    """
    def FBVideo(self,pName):
        """
        Constructor.

        pName : Name of video media. 
        """
        pass

    pass

class FBEditPropertyModern (FBVisualComponent):
    """
    Property editor widget.     
    This is a more modern version of the widget FBEditProperty which is used in the property editor tool of the application.See class FBEditProperty for more details.     
    """
    def FBEditPropertyModern(self):
        """
        Constructor.

        """
        pass

    def SetBackgroundColorIndex(self,pIndex):
        """
        Set the background color index.
        Use the system-defined color palette to set the backgound color. By default the color used is kFBColorIndexStdListBg1

        pIndex : FBColorIndex
        """
        pass

    LargeInc=property(doc="<b>Read Write Property:</b> Indicate the large increment applied when click-draging on the property value (usually left-click-dragging)         ")
    Precision=property(doc="<b>Read Write Property:</b> Used to specify the width and precision of the value shown. A value of 7.2 indicates to show at minimum 7 numbers, with 2 decimals.         ")
    Property=property(doc="<b>Read Write Property:</b> Property to edit. Set to NULL to disable.         ")
    SliderMax=property(doc="<b>Read Write Property:</b> Should the property be editable using a slider, set the maximum value atainable with the slider.         ")
    SliderMin=property(doc="<b>Read Write Property:</b> Should the property be editable using a slider, set the minimum value atainable with the slider.         ")
    SmallInc=property(doc="<b>Read Write Property:</b> Indicate the small increment applied when click-draging on the property value (usually right-click-dragging)         ")
    pass

class FBPropertyAnimatableColor (FBPropertyAnimatable):
    """
        
        
    """
    Data=property(doc="<b>Read Write Property:</b> The property data value. Type of this depends on the subclass of FBPropertyAnimatable (ex: in a FBPropertyAnimatableInt, Data is of type int).         ")
    pass

class FBSpreadCell (FBSpreadPart):
    """
    Spreadsheet cell.     
        
    """
    def FBSpreadCell(self,pParent,pRow,pCol):
        """
        Constructor.

        pParent : Parent spreadsheet. 
        pRow : Row to which cell belongs. 
        pCol : Column to which cell belongs. 
        """
        pass

    pass

class FBImageContainer (FBVisualComponent):
    """
    Image.     
        
    """
    def FBImageContainer(self):
        """
        Constructor.

        """
        pass

    Filename=property(doc="<b>Read Write Property:</b> Filename for image.         ")
    Height=property(doc="<b>Read Write Property:</b> Image height.         ")
    OnDragAndDrop=property(doc="<b>Event:</b> Drag and drop.         ")
    Width=property(doc="<b>Read Write Property:</b> Image width.         ")
    pass

class FBContainer (FBVisualComponent):
    """
    Container.     
        
    """
    def FBContainer(self):
        """
        Constructor.

        """
        pass

    def GetSelection(self):
        """
        Get the selected item.

        return : Index of current selection. 
        """
        pass

    def ItemIconSet(self,pRef,pImage,pUseACopyOfTheImage):
        """
        Set an item's icon.

        pRef : Reference to item in container. 
        pImage : Handle to image to use. 
        pUseACopyOfTheImage : Create a copy of the image?(default=true) 
        return : Operation was successful (<b>true</b> or <b>false</b>). 
        """
        pass

    def ItemIconSet(self,pRef,pFilename):
        """
        Set an item's icon.

        pRef : Reference to item in container. 
        pFilename : Name of file where image is located. 
        return : Operation was successful (<b>true</b> or <b>false</b>). 
        """
        pass

    def ItemNameEdit(self,pRef):
        """
        Edit a container item.

        pRef : Reference of container to edit. 
        return : Operation was successful (<b>true</b> or <b>false</b>). 
        """
        pass

    IconPosition=property(doc="<b>Read Write Property:</b> Where the icon is positioned for the items.         ")
    ItemHeight=property(doc="<b>Read Write Property:</b> Item height.         ")
    ItemIndex=property(doc="<b>Read Write Property:</b> Current item selected.         ")
    ItemWidth=property(doc="<b>Read Write Property:</b> Item width.         ")
    ItemWrap=property(doc="<b>Read Write Property:</b> Are items wrapped when enough space is available?         ")
    Items=property(doc="<b>List:</b> Names of items in container.         ")
    OnChange=property(doc="<b>Event:</b> Container contents changed.         ")
    OnDblClick=property(doc="<b>Event:</b> Double click.         ")
    OnDragAndDrop=property(doc="<b>Event:</b> Drag and Drop event.         ")
    Orientation=property(doc="<b>Read Write Property:</b> Orientation of container.         ")
    pass

class FBThermometer (FBVisualComponent):
    """
    Thermometer.     
        
    """
    def FBThermometer(self):
        """
        Constructor.

        """
        pass

    def Clear(self):
        """
        Reset bounds and value.

        """
        pass

    Max=property(doc="<b>Read Write Property:</b> Maximum value.         ")
    Min=property(doc="<b>Read Write Property:</b> Minimum value.         ")
    Value=property(doc="<b>Read Write Property:</b> Current value.         ")
    pass

class FBHandle (FBBox):
    """
    FBHandle class.     
    This class exposes the Handle object of the application. This is a terminal class and should not be used as a base for a new class.     
    """
    def FBHandle(self,pName):
        """
        Public constructor.
        This constructor is used to create a new object.

        pName : Object name. 
        """
        pass

    def Select(self):
        """
        Meta selection.
        With this method, the handle itself is selected as well as all the models that are manipulated by the handle.

        """
        pass

    Follow=property(doc="<b>List:</b> Object to be followed by the handle. Should have a cardinality of 1.         ")
    Image=property(doc="<b>List:</b> Image to be used in the handle display. Only the image at position 0 is used.         ")
    Manipulate=property(doc="<b>List:</b> Objects manipulated by the handle.         ")
    ManipulateRotation=property(doc="<b>List:</b> Objects manipulated by the handle. Only their rotation is affected.         ")
    ManipulateScaling=property(doc="<b>List:</b> Objects manipulated by the handle. Only their scaling is affected.         ")
    ManipulateTranslation=property(doc="<b>List:</b> Objects manipulated by the handle. Only their translation is affected.         ")
    pass

class FBPropertyAnimatableDouble (FBPropertyAnimatable):
    """
        
        
    """
    Data=property(doc="<b>Read Write Property:</b> The property data value. Type of this depends on the subclass of FBPropertyAnimatable (ex: in a FBPropertyAnimatableInt, Data is of type int).         ")
    pass

class FBSpreadColumn (FBSpreadPart):
    """
    Spreadsheet column.     
        
    """
    def FBSpreadColumn(self,pParent,pCol):
        """
        Constructor.

        pParent : Parent spreadsheet. 
        pCol : Column number. 
        """
        pass

    Caption=property(doc="<b>Read Write Property:</b> Caption of the column.         ")
    Justify=property(doc="<b>Read Write Property:</b> Text justification.         ")
    Width=property(doc="<b>Read Write Property:</b> Column width.         ")
    pass

class FBEdit (FBVisualComponent):
    """
    Text edit box.     
        
    """
    def FBEdit(self):
        """
        Constructor.

        """
        pass

    OnChange=property(doc="<b>Event:</b> Text changed.         ")
    PasswordMode=property(doc="<b>Read Write Property:</b> Set password mode for this edit box.         ")
    Text=property(doc="<b>Read Write Property:</b> Text displayed.         ")
    pass

class FBNote (FBBox):
    """
    Note class.     
        
    """
    def FBNote(self,pName):
        """
        Constructor.

        pName : Name of note. 
        """
        pass

    def Attach(self,pComp):
        """
        Attach the note to a component.
        Will attach the note to the component. If <b>pComp</b> is NULL, the note will only be added to the scene.

        pComp : Component on which to attach note. 
        return : A boolean indicating if the operation was successful or not. 
        """
        pass

    def Detach(self,pComp):
        """
        Detach the note from a component.
        Will detach the note from the component. If <b>pComp</b> is NULL, the note will be removed from the scene and detached from all components.

        pComp : Component from which to detach note. 
        return : A boolean indicating if the operation was successful or not. 
        """
        pass

    StaticComment=property(doc="<b>Read Write Property:</b> Comment associated to this note.         ")
    pass

class FBPropertyAnimatableBool (FBPropertyAnimatable):
    """
        
        
    """
    Data=property(doc="<b>Read Write Property:</b> The property data value. Type of this depends on the subclass of FBPropertyAnimatable (ex: in a FBPropertyAnimatableInt, Data is of type int).         ")
    pass

class FBGlobalLight (FBBox):
    """
    Global light class.     
        
    """
    def FBGlobalLight(self):
        """
        Constructor.

        """
        pass

    AmbientColor=property(doc="<b>Read Write Property:</b> Ambient light color.         ")
    FogBegin=property(doc="<b>Read Write Property:</b> Begin fog distance.         ")
    FogColor=property(doc="<b>Read Write Property:</b> Fog color.         ")
    FogDensity=property(doc="<b>Read Write Property:</b> Fog density.         ")
    FogEnable=property(doc="<b>Read Write Property:</b> Enable fog?         ")
    FogEnd=property(doc="<b>Read Write Property:</b> End fog distance.         ")
    FogMode=property(doc="<b>Read Write Property:</b> Fog falloff mode.         ")
    pass

class FBPropertyAnimatableVector2d (FBPropertyAnimatable):
    """
        
        
    """
    Data=property(doc="<b>Read Write Property:</b> The property data value. Type of this depends on the subclass of FBPropertyAnimatable (ex: in a FBPropertyAnimatableInt, Data is of type int).         ")
    pass

class FBEditColor (FBVisualComponent):
    """
    Color edit widget.     
        
    """
    def FBEditColor(self):
        """
        Constructor.

        """
        pass

    ColorMode=property(doc="<b>Read Write Property:</b> 3 for RGB, 4 for RGBA (Default = 3)         ")
    OnChange=property(doc="<b>Event:</b> Color changed.         ")
    Value=property(doc="<b>Read Write Property:</b> Current value of color.         ")
    pass

class FBFCurveEditor (FBVisualComponent):
    """
    FCurve editor.     
        
    """
    def FBFCurveEditor(self):
        """
        Constructor.

        """
        pass

    def AddAnimationNode(self,pNode):
        """
        Add an animation node to the editor.

        pNode : Animation node to show in the editor. 
        """
        pass

    def Clear(self):
        """
        Clear the editor.

        """
        pass

    def RemoveAnimationNode(self,pNode):
        """
        Remove an animation node from the editor.

        pNode : Animation node to hide from editor. 
        """
        pass

    pass

class FBPropertyAnimatableEnum (FBPropertyAnimatable):
    """
        
        
    """
    def EnumList(self,pIdx):
        """
        pIdx : int
        """
        pass

    Data=property(doc="Return the string associated with the index. Will return None when no value is associated.         ")
    pass

class FBSurface (FBGeometry):
    """
    Surface class.     
        
    """
    def FBSurface(self,pModel):
        """
        Constructor.

        pModel : Model to which Nurbs belongs. 
        """
        pass

    def AddToArrayAndGoNext(self,pValue,pArray,pRemainArraySize,pArrayCount):
        """
        pValue : int
        pArray : int
        pRemainArraySize : int
        pArrayCount : int
        """
        pass

    def ControlPointsBegin(self):
        """
        """
        pass

    def ControlPointsEnd(self):
        """
        """
        pass

    def GetControlPoint(self,pIndex,pX,pY,pZ,pW):
        """
        pIndex : int
        pX : float
        pY : float
        pZ : float
        pW : float
        """
        pass

    def GetPatchStripCount(self):
        """
        """
        pass

    def GetPatchStripVertexIndexCount(self):
        """
        """
        pass

    def GetStripFromPatch(self,pStripIndexCountArray,pStripIndexCountArraySize,pStripVertexIndexArray,pStripVertexIndexArraySize):
        """
        pStripIndexCountArray : int
        pStripIndexCountArraySize : int
        pStripVertexIndexArray : int
        pStripVertexIndexArraySize : int
        """
        pass

    def GetSurfaceCapped(self,pUorV,pDirection):
        """
        pUorV : int
        pDirection : int
        """
        pass

    def GetTessellatedPointMaterialID(self):
        """
        """
        pass

    def GetTessellatedPointsCount(self):
        """
        """
        pass

    def GetTessellatedTriangleCount(self):
        """
        """
        pass

    def GetTessellatedTrianglePoints(self,pTriangleID,pTrianglePoints,pTriangleQuadUVIndex):
        """
        pTriangleID : int
        pTrianglePoints : int
        pTriangleQuadUVIndex : int
        """
        pass

    def GetVertexCount(self,pUorVorGlobal):
        """
        pUorVorGlobal : int
        """
        pass

    def SetControlPoint(self,pIndex,pX,pY,pZ,pW):
        """
        pIndex : int
        pX : float
        pY : float
        pZ : float
        pW : float
        """
        pass

    def SurfaceBegin(self):
        """
        """
        pass

    def SurfaceEditBegin(self):
        """
        """
        pass

    def SurfaceEditEnd(self):
        """
        """
        pass

    def SurfaceEnd(self):
        """
        """
        pass

    def VertexGetSelected(self,pU,pV):
        """
        Get the selected state of a vertex.

        pU : The u index of the vertex. 
        pV : The v index of the vertex. 
        return : true if the vertex is selected, false if not. 
        """
        pass

    def VertexGetTransformable(self,pU,pV):
        """
        Get the Transformable state of a vertex.

        pU : The u index of the vertex. 
        pV : The v index of the vertex. 
        return : true if the vertex is Transformable, false if not. 
        """
        pass

    def VertexGetVisible(self,pU,pV):
        """
        Get the visible state of a vertex.

        pU : The u index of the vertex. 
        pV : The v index of the vertex. 
        return : true if the vertex is visible, false if not. 
        """
        pass

    def VertexSetSelected(self,pU,pV,pState):
        """
        Set the selected state of a vertex.

        pU : The u index of the vertex. 
        pV : The v index of the vertex. 
        pState : Set the select state. 
        return : true if the vertex is selected, false if not. 
        """
        pass

    def VertexSetVisible(self,pU,pV,pState):
        """
        Set the visible state of a vertex.

        pU : The u index of the vertex. 
        pV : The v index of the vertex. 
        pState : Set the visible state. 
        return : true if the vertex is visible, false if not. 
        """
        pass

    ReductionFactor=property(doc="<b>Read Write Property:</b> Reduction factor.         ")
    SurfaceMode=property(doc="<b>Read Write Property:</b> Surface mode.         ")
    pass

class FBPropertyAnimatableAction (FBPropertyAnimatable):
    """
        
        
    """
    Data=property(doc="<b>Read Write Property:</b> The property data value. Type of this depends on the subclass of FBPropertyAnimatable (ex: in a FBPropertyAnimatableInt, Data is of type int).         ")
    pass

class FBSlider (FBVisualComponent):
    """
    Slider.     
        
    """
    def FBSlider(self):
        """
        Constructor.

        """
        pass

    Max=property(doc="<b>Read Write Property:</b> Maximum value.         ")
    Min=property(doc="<b>Read Write Property:</b> Minimum value.         ")
    OnChange=property(doc="<b>Event:</b> Slider value changed.         ")
    OnTransaction=property(doc="<b>Event:</b> Translation begin/end.         ")
    Orientation=property(doc="<b>Read Write Property:</b> Slider orientation.         ")
    Value=property(doc="<b>Read Write Property:</b> Current value.         ")
    pass

class FBList (FBVisualComponent):
    """
    List of items.     
        
    """
    def FBList(self):
        """
        Constructor.

        """
        pass

    def IsSelected(self,pIndex):
        """
        Returns whether or not the item <b>pIndex</b> is currently selected.

        pIndex : Index to see if select or not. 
        return : <b>true</b> if item at <b>pIndex</b> is selected. 
        """
        pass

    def Selected(self,pIndex,pSelected):
        """
        Set the current selected state of item at <b>pIndex</b> to <b>pSelected</b>.

        pIndex : Index to affect item at. 
        pSelected : State to set item at <b>pIndex</b> to. 
        """
        pass

    ExtendedSelect=property(doc="<b>Read Write Property:</b> Extended selection state?         ")
    ItemIndex=property(doc="<b>Read Write Property:</b> Current item index.         ")
    Items=property(doc="<b>List:</b> Names of items in list.         ")
    MultiSelect=property(doc="<b>Read Write Property:</b> Can multiple items be selected?         ")
    OnChange=property(doc="<b>Event:</b> List changed.         ")
    OnDragAndDrop=property(doc="<b>Event:</b> Drag and drop event.         ")
    Style=property(doc="<b>Read Write Property:</b> Style or direction of list.         ")
    pass

class FBFilePopup (FBVisualComponent):
    """
    File Popup (for open/save).     
        
    """
    def FBFilePopup(self):
        """
        Constructor.

        """
        pass

    def Execute(self):
        """
        Execute file popup.

        return : <b>true</b> if <b>OK</b> is clicked by user. 
        """
        pass

    Caption=property(doc="<b>Read Write Property:</b> Caption to put in popup window.         ")
    FileName=property(doc="<b>Read Write Property:</b> File selected.         ")
    Filter=property(doc="<b>Read Write Property:</b> Filter to use for popup window file selection.         ")
    FullFilename=property(doc="<b>Read Only Property:</b> Full filename (path and file).         ")
    Path=property(doc="<b>Read Write Property:</b> Path of file selected.         ")
    Style=property(doc="<b>Read Write Property:</b> Style of file popup.         ")
    pass

class FBButton (FBVisualComponent):
    """
    Button.     
        
    """
    def FBButton(self):
        """
        Constructor.

        """
        pass

    def GetStateColor(self,pState):
        """
        Queries the color associated with a button state.
        This method is only useful for buttons of style kFB2States.

        pState : The state to be queried. 
        return : The color vector. 
        """
        pass

    def SetImageFileNames(self,pUpImage,pDownImage,pThirdImage):
        """
        Sets the image used to generate a kFBBitmap2States.

        pUpImage : The image used when button is unpushed 
        pDownImage : The image used when button is pushed 
        pThirdImage : str
        """
        pass

    def SetStateColor(self,pState,pColor):
        """
        Returns whether or not the item <b>pIndex</b> is currently selected.

        pState : The state to be set. 
        pColor : The desired color vector. 
        """
        pass

    Justify=property(doc="<b>Read Write Property:</b> Current state of button.         ")
    Look=property(doc="<b>Read Write Property:</b> Current state of button.         ")
    OnClick=property(doc="<b>Event:</b> Button clicked.         ")
    State=property(doc="<b>Read Write Property:</b> Current state of button.         ")
    Style=property(doc="<b>Read Write Property:</b> Button style.         ")
    pass

class FBLabel (FBVisualComponent):
    """
    Text label.     
        
    """
    def FBLabel(self):
        """
        Constructor.

        """
        pass

    Justify=property(doc="<b>Read Write Property:</b> Text justification for label.         ")
    Style=property(doc="<b>Read Write Property:</b> Text style appearance.         ")
    WordWrap=property(doc="<b>Read Write Property:</b> Enable wordwrap on text drawing.         ")
    pass

class FBDevice (FBBox):
    """
    Base Device class.     
        
    """
    def FBDevice(self,pName):
        """
        Constructor.

        pName : Name of device. 
        """
        pass

    def AckOneBadSampleReceived(self):
        """
        Acknowlege that one <b>bad</b> sample was received (for statistical purposes).

        """
        pass

    def AckOneSampleReceived(self):
        """
        Acknowlege that one sample was received (for statistical purposes).

        """
        pass

    def AckOneSampleSent(self):
        """
        Acknowlege that one sample was sent (for statistical purposes).

        """
        pass

    def AnimationNodeNotify(self,pAnimationNode,pEvaluateInfo):
        """
        Notification function for animation thread.
        This function is called by the real-time engine in order to process animation information.

        pAnimationNode : Node containing the modified information. 
        pEvaluateInfo : Information concerning the evaluation of the animation (time, etc.) 
        return : <b>true</b> if animation node notification is successful. 
        """
        pass

    def FBCreate(self):
        """
        Open Reality Creation function.

        return : Outcome of creation (true/false). 
        """
        pass

    def FBDestroy(self):
        """
        Open Reality Destruction function.

        """
        pass

    def RecordingDoneAnimation(self,pAnimationNode):
        """
        When recording, finish animation.

        pAnimationNode : Animation node to write information to. 
        """
        pass

    def RecordingInitAnimation(self,pAnimationNode):
        """
        When recording, initialize animation.

        pAnimationNode : Animation node to read information from. 
        """
        pass

    CommType=property(doc="<b>Read Write Property:</b> Type of communications.         ")
    HardwareVersionInfo=property(doc="<b>Read Write Property:</b> Device information: Hardware Version.         ")
    IconFilename=property(doc="<b>Read Write Property:</b> Icon filename.         ")
    Information=property(doc="<b>Read Write Property:</b> Device information: Information.         ")
    ModelTemplate=property(doc="<b>Component:</b> Root of model template structure.         ")
    Online=property(doc="<b>Read Write Property:</b> Is online?         ")
    RecordingStartTime=property(doc="<b>Read Only Property:</b> The time at which the recording started.         ")
    RecordingStopTime=property(doc="<b>Read Only Property:</b> The time at which the recording stopped.         ")
    SamplingMode=property(doc="<b>Read Write Property:</b> Mode to use to record device.         ")
    SamplingPeriod=property(doc="<b>Read Write Property:</b> Sampling period for device.         ")
    Status=property(doc="<b>Read Write Property:</b> Device information: Status.         ")
    pass

class FBAssetFile (FBAssetItem):
    """
    Class representing a file stored in a version control database.     
        
    """
    def FBAssetFile(self,pName):
        """
        Constructor.

        pName : Name of Command. 
        """
        pass

    def FBCreate(self):
        """
        Open Reality Creation function.

        return : Outcome of creation (true/false). 
        """
        pass

    def GetCheckedOutBy(self):
        """
        Returns the name of the user who currently has this file checked out.

        return : The user name if the file is checked out, or an empty string if it is not. 
        """
        pass

    def IsCheckedOut(self):
        """
        Returns a boolean value indicating if this file is checked out by any user.

        return : A boolean value indicating if this node is checked out. 
        """
        pass

    def IsCheckedOutByMe(self):
        """
        Returns a boolean value indicating if this file is checked out by the current user.

        return : A boolean value indicating if this node is checked out by the current user. 
        """
        pass

    pass

class FBBoxPlaceHolder (FBBox):
    """
    Wrapper around a specific instance of a FBBox object.     
    This class is mainly used with a constraint relation to have multiple boxes that are a representation of the same underlying box. The underlying box will usually be a device. Instantiation of FBBoxPlaceHolder should be left to the the system.     
    """
    def FBBoxPlaceHolder(self):
        """
        Constructor.

        """
        pass

    Box=property(doc="<b>Read Only Property:</b> Underlying box object.         ")
    pass

class FBPropertyAnimatableColorAndAlpha (FBPropertyAnimatable):
    """
        
        
    """
    Data=property(doc="<b>Read Write Property:</b> The property data value. Type of this depends on the subclass of FBPropertyAnimatable (ex: in a FBPropertyAnimatableInt, Data is of type int).         ")
    pass

class FBPropertyAnimatableTime (FBPropertyAnimatable):
    """
        
        
    """
    Data=property(doc="<b>Read Write Property:</b> The property data value. Type of this depends on the subclass of FBPropertyAnimatable (ex: in a FBPropertyAnimatableInt, Data is of type int).         ")
    pass

class FBTabPanel (FBVisualComponent):
    """
    Tab panel.     
        
    """
    def FBTabPanel(self):
        """
        Constructor.

        """
        pass

    ItemIndex=property(doc="<b>Read Write Property:</b> Current tab panel.         ")
    Items=property(doc="<b>List:</b> Names for tab panels.         ")
    Layout=property(doc="<b>Read Write Property:</b> Layout for current tab panel.         ")
    OnChange=property(doc="<b>Event:</b> Tab panel change.         ")
    TabStyle=property(doc="<b>Read Write Property:</b> Style of the tab panel.         ")
    pass

class FBLayoutRegion (FBVisualComponent):
    """
    Layout region.     
        
    """
    def FBLayoutRegion(self):
        """
        Constructor.

        """
        pass

    pass

class FBFolderPopup (FBVisualComponent):
    """
    Folder Popup (for selecting a directory).     
        
    """
    def FBFolderPopup(self):
        """
        Constructor.

        """
        pass

    def Execute(self):
        """
        Execute folder popup.

        return : <b>true</b> if <b>OK</b> is clicked by user. 
        """
        pass

    Caption=property(doc="<b>Read Write Property:</b> Caption to put in popup window.         ")
    Path=property(doc="<b>Read Write Property:</b> Path of folder selected.         ")
    pass

class FBPropertyAnimatableInt (FBPropertyAnimatable):
    """
        
        
    """
    Data=property(doc="<b>Read Write Property:</b> The property data value. Type of this depends on the subclass of FBPropertyAnimatable (ex: in a FBPropertyAnimatableInt, Data is of type int).         ")
    pass

class FBPropertyAnimatableVector3d (FBPropertyAnimatable):
    """
        
        
    """
    Data=property(doc="<b>Read Write Property:</b> The property data value. Type of this depends on the subclass of FBPropertyAnimatable (ex: in a FBPropertyAnimatableInt, Data is of type int).         ")
    pass

class FBCharacterExtension (FBKeyingGroup):
    """
    Objects Grouping class.     
    This class is an interface to manipulate object's grouping in the scene.     
    """
    def FBCharacterExtension(self,pName):
        """
        Constructor.

        pName : Group name. 
        """
        pass

    def AddObjectProperties(self,pObj):
        """
        Return the attached Character.

        pObj : FBComponent
        """
        pass

    def FBDelete(self):
        """
        Virtual FBDelete function.

        """
        pass

    def GetCharacter(self):
        """
        return the character extension determined by MirrorLabel

        """
        pass

    def GetMirrorExtension(self):
        """
        Reset object position to the stance.

        """
        pass

    def GoToStancePose(self):
        """
        Update the stance pose to the current position of the character extension element.

        """
        pass

    def IsElementSelected(self):
        """
        Remove TR Properties from Object.

        """
        pass

    def IsPropertyIncluded(self,pProp):
        """
        return true if one object in object dependency list is selected.

        pProp : FBProperty
        """
        pass

    def RemoveObjectAndProperties(self,pObj):
        """
        Add TR Properties from Object.

        pObj : FBComponent
        """
        pass

    def UpdateStancePose(self):
        """
        """
        pass

    IncludePartInFullBody=property(doc="<b>Read Write Property:</b> Include or not this extension when fullBody is active.         ")
    Label=property(doc="<b>Read Write Property:</b> The logical name of the extension, use for mirroring.         ")
    MirrorLabel=property(doc="<b>Read Write Property:</b> Enum that indicate which extension is used as mirror, 0 is none, 1 is self, 2-n represent the (ith - 2)character extension in the attached character excluding self.         ")
    PlotAllowed=property(doc="<b>Read Write Property:</b> Controls if objects in the set are transformable.         ")
    ReferenceModel=property(doc="<b>Read Write Property:</b> Controls the referential of the extension.         ")
    pass

class FBView (FBVisualComponent):
    """
    Generic view.     
        
    """
    def FBView(self):
        """
        Constructor.

        """
        pass

    def DrawString(self,pText,pX,pY,pEnable):
        """
        Draw a string in the view.

        pText : Text to draw. 
        pX : X position of string. 
        pY : Y position of string. 
        pEnable : Is string enabled? (default =-1) 
        """
        pass

    def IsView(self):
        """
        Checks if object is a view.

        return : Is object a view? (<b>true</b> or <b>false</b>) 
        """
        pass

    def Refresh(self,pNow):
        """
        Refresh view.

        pNow : If <b>true</b>, refresh immediately (default = <b>false</b>). 
        """
        pass

    def SetViewport(self,pX,pY,pW,pH):
        """
        Set view's viewport.

        pX : Viewport X value. 
        pY : Viewport Y value. 
        pW : Viewport W (width) value. 
        pH : Viewport H (height) value. 
        return : Operation was successful (<b>true</b> or <b>false</b>). 
        """
        pass

    DoubleBuffer=property(doc="<b>Read Only Property:</b> Indicates if the view is double buffered.         ")
    GraphicOGL=property(doc="<b>Read Only Property:</b> Indicates if the view is OpenGL.         ")
    pass

class FBPhysicalProperties (FBBox):
    """
    Base class for physical properties attach to a model.     
        
    """
    def FBPhysicalProperties(self,pName):
        """
        pName : str
        """
        pass

    pass

class FBPropertyAnimatableVector4d (FBPropertyAnimatable):
    """
        
        
    """
    Data=property(doc="<b>Read Write Property:</b> The property data value. Type of this depends on the subclass of FBPropertyAnimatable (ex: in a FBPropertyAnimatableInt, Data is of type int).         ")
    pass

class FBTree (FBVisualComponent):
    """
    Tree list view.     
        
    """
    def FBTree(self):
        """
        Constructor.

        """
        pass

    def Clear(self):
        """
        Clear the tree (remove all nodes).

        """
        pass

    def GetRoot(self):
        """
        Get the root node.

        return : the root node of the tree. 
        """
        pass

    def InsertLast(self,pNode,pName):
        """
        Insert node at the end.

        pNode : Node under which the new node will appear. 
        pName : Text to display for this node. 
        return : the newly created node. 
        """
        pass

    AllowCollapse=property(doc="<b>Read Write Property:</b> When OnCollapsing occurs, set this to true to allow collapse.         ")
    AllowExpansion=property(doc="<b>Read Write Property:</b> When OnExpanding occurs, set this to true to allow expansion.         ")
    AutoExpandOnDblClick=property(doc="<b>Read Write Property:</b> Allow automatic expand on double click, default is false.         ")
    AutoExpandOnDragOver=property(doc="<b>Read Write Property:</b> Allow automatic expand on drag over, default is false.         ")
    AutoScroll=property(doc="<b>Read Write Property:</b> If AutoScroll property is True then the tree window will be automatically scrolled when the user drags item(s) over the boundaries of the tree.         ")
    AutoScrollOnExpand=property(doc="<b>Read Write Property:</b> Allow automatic scroll on expand, default is true.         ")
    CheckBoxes=property(doc="<b>Read Write Property:</b> Draw check boxe for each node.         ")
    DeselectOnCollapse=property(doc="<b>Read Write Property:</b> Tells whether node are deselected if parent node is collapsed.         ")
    EditNodeOn2Select=property(doc="<b>Read Write Property:</b> Set to true, to allow automatic node editing on second select.         ")
    HighlightOnRightClick=property(doc="<b>Read Write Property:</b> Hightlight node on right click.         ")
    Indent=property(doc="<b>Read Write Property:</b> Use Indent to determine how far child nodes are indented from their parent nodes when the parent is expanded.         ")
    ItemHeight=property(doc="<b>Read Write Property:</b> Height of an item.         ")
    MultiDrag=property(doc="<b>Read Write Property:</b> Tells whether multiple drag/drop is allowed or not.         ")
    MultiSelect=property(doc="<b>Read Write Property:</b> Tells whether multiple selection is allowed or not.         ")
    NoSelectOnDrag=property(doc="<b>Read Write Property:</b> Tells whether node are selected if drag is start and node is not already selected.         ")
    NoSelectOnRightClick=property(doc="<b>Read Write Property:</b> Tells whether node are selected if right click on node.         ")
    OnChange=property(doc="<b>Event:</b> Change of the selection.         ")
    OnClick=property(doc="<b>Event:</b> Click on a node of the tree.         ")
    OnCollapsed=property(doc="<b>Event:</b> Click on the '-' sign before a non-leaf node.         ")
    OnCollapsing=property(doc="<b>Event:</b> Fired before the node collapse. To refuse collapsing, set AllowCollapse to false.         ")
    OnDblClick=property(doc="<b>Event:</b> Double-Click on a node of the tree.         ")
    OnDragAndDrop=property(doc="<b>Event:</b> Drag and drop of an element.         ")
    OnExpanded=property(doc="<b>Event:</b> Click on the '+' sign before a non-leaf node         ")
    OnExpanding=property(doc="<b>Event:</b> Is fired before the node expand. To refuse expanding set AllowExpansion to false.         ")
    OnSelect=property(doc="<b>Event:</b> A node was selected.         ")
    SelectedCount=property(doc="<b>Read Only Property:</b> Count of selected items.         ")
    SelectionActive=property(doc="<b>Read Write Property:</b> Tells whether selection is allowed or not.         ")
    ShowLines=property(doc="<b>Read Write Property:</b> On node selection, will draw entire line selected         ")
    TreeHeight=property(doc="<b>Read Only Property:</b> Height of the tree.         ")
    TreeWidth=property(doc="<b>Read Only Property:</b> Width of the tree.         ")
    VisibleItemCount=property(doc="<b>Read Only Property:</b> Count of visible items.         ")
    pass

class FBArrowButton (FBVisualComponent):
    """
    Arrow Button.     
    This create a button, which when pushed, 'open' a layout to display content (another control or a layout). A small arrow, left to the button title, shows when the 'content' is showed (arrow points down) or hidden (arrow points to button title).     
    """
    def FBArrowButton(self):
        """
        Constructor.

        """
        pass

    def SetContent(self,pTitle,pContent,pContentWidth,pContentHeight):
        """
        Sets the content to be hidden/shown by button.
        The FBArrowButton MUST already be added to a layout BEFORE calling this method.

        pTitle : Title of the content manage by the FBArrowButton 
        pContent : Content that the FBArrowButton will display or hide 
        pContentWidth : Width of the content 
        pContentHeight : Height of the content 
        """
        pass

    pass

class FBSpreadRow (FBSpreadPart):
    """
    Spreadsheet row.     
        
    """
    def FBSpreadRow(self,pParent,pRow):
        """
        Constructor.

        pParent : Parent spreadsheet. 
        pRow : User-defined reference to assign to row. 
        """
        pass

    def EditCaption(self):
        """
        Edit the row caption.
        This will initiate the UI edit of a row caption.

        return : Operation was successful (<b>true</b> or <b>false</b>). 
        """
        pass

    def Remove(self):
        """
        Remove (destroy) row.

        """
        pass

    Caption=property(doc="<b>Read Write Property:</b> Caption to display with row.         ")
    Parent=property(doc="<b>Read Write Property:</b> Parent of row (reference).         ")
    Selected=property(doc="<b>Read Write Property:</b> Is row selected?         ")
    pass

class FBScrollBox (FBVisualComponent):
    """
    Scroll Box.     
    This class provide a layout that will be automatically managed with scrollbar according to the specified width and height. This provide an easy way to add big dynamic UI control.     
    """
    def FBScrollBox(self):
        """
        Constructor.

        """
        pass

    Content=property(doc="<b>Read Property:</b> an empty layout in which you can add scrollable content.         ")
    pass

class FBProgress (FBVisualComponent):
    """
    Progress bar.     
        
    """
    def FBProgress(self):
        """
        Constructor.

        """
        pass

    Caption=property(doc="<b>Read Write Property:</b> Caption to be displayed for progress bar.         ")
    Percent=property(doc="<b>Read Write Property:</b> Percent completed for the operation.         ")
    Text=property(doc="<b>Read Write Property:</b> Text to display on progress bar.         ")
    pass

class FBCharacterSolver (FBConstraint):
    """
    Constraint class.     
        
    """
    def FBCharacterSolver(self,pName):
        """
        Constructor.

        pName : Name of constraint. 
        """
        pass

    def GetParentRotationOffset(self,pR,pIndex):
        """
        Get the Parent Rotation Offset of the Given Extra Bone Index.
        The rotation Offset if extracted at Characterisation (in Stance Pose). You don't need this value if the parent of the bone is characterized too.

        pR : Offset Rotation between the Bone and is parent at Stance Pose. 
        pIndex : Index of extra Bone to get. 
        """
        pass

    def SetParentRotationOffset(self,pR,pIndex):
        """
        Set the Parent Rotation Offset of the Given Extra Bone Index.
        The rotation Offset if extracted at Characterisation (in Stance Pose). You don't need this value if the parent of the bone is characterized too.

        pR : Offset Rotation between the Bone and is parent at Stance Pose. 
        pIndex : Index of extra Bone to get. 
        """
        pass

    ExtraFK=property(doc="<b>Read Property:</b> List of Extra FK in character         ")
    ExtraBones=property(doc="<b>Read Property:</b> List of Extra Bones in character         ")
    Source=property(doc="<b>Read Write Property:</b> Source character when doing a character retarget.         ")
    pass

class FBShaderShadowLive (FBShader):
    """
    Shader Shadow Live class.     
    Use the Live Shadow shader to apply real-time shadows to models. You can specify shadow intensity as well as the lights and objects that cast shadows in a scene.There are two methods to create a FBShaderShadowLive object: using the FBShaderManager, or simply by instantiating a class object explicitely.Please consult the application documentation for more infos on shader properties and their effects.This class should not serve as a base class for another class.Sample C++ code: 
@code
    // Create a shadow shader.
    HFBShaderShadowLive lShader = new FBShaderShadowLive( 'New Shader' );

    // Add a cube in its list of affected objects.
    HFBModel lModel = FBFindModelByName( 'Cube' )
    if( lModel )
    {
        lShaderShadowLive.Add( lCube );
    }
@endcode

Sample Python code: 
@code
    from pyfbsdk import *

    # Create shader.
    lShader = FBShaderShadowLive( 'New Python Shader' )

    # Find a cube to put in our list of affected objects.
    lModel = FBFindModelByName( 'Cube' )
    if lModel:
        lShader.ShadowCasterProperty.append( lModel )
@endcode

     
    """
    def FBShaderShadowLive(self,pName):
        """
        Constructor.

        pName : Name of shader. 
        """
        pass

    Lights=property(doc="<b>List:</b> List of light object which will produce shadows.         ")
    LocalShadow=property(doc="<b>Read Write Property:</b> Creates an accurate projection of a shadow for each object.         ")
    Models=property(doc="<b>List:</b> List of object which when lighted will cast a shadow.         ")
    ShadowFrameType=property(doc="<b>Read Write Property:</b> Used to select the shadow calculation method.         ")
    ShadowIntensity=property(doc="<b>Read Write Property:</b> Controls the darkness of shadows cast by a selected object.         ")
    ShadowType=property(doc="<b>Read Write Property:</b> Indicate which shadow type is desired.         ")
    ShadowZOffset=property(doc="<b>Read Write Property:</b> Specifies the offset of the Live Shadow shader's plane from the original selected plane.         ")
    UseGobo=property(doc="<b>Read Write Property:</b> Includes the gobo in the shadow map calculation.         ")
    pass

class FBActor (FBConstraint):
    """
    Actor class.     
    <b>These classes are under development and may change dramatically between versions.</b>To obtain the list of actors present in a scene, you need to create an instance of class FBSystem, to obtain the current scene. The FBScene object holds the list of actors in the property Actors. 
@code
       FBSystem lSystem;
       HFBScene lScene = lSystem.Scene;
       for( int lIdx = 0; lIdx < lScene->Actors.GetCount(); ++lIdx )
       {
           FBTrace( 'Actor[%d]: '%s'\n', lIdx, (char*)lScene->Actors[lIdx] );
       }
@endcode

The current actor selected in the Character tool can be obtained via the FBApplication object. 
@code
       FBApplication lApplication;
       HFBActor lActor = lApplication.CurrentActor;
       if( lActor )
       {
           FBTrace( 'Current actor is: '%s'\n', (char*)lActor->Name );
       }
       else
       {
           FBTrace( 'No actor currently selected\n' );
       }
@endcode

     
    """
    def FBActor(self,pName):
        """
        Constructor.

        pName : Name of new actor. 
        """
        pass

    def FBDelete(self):
        """
        Actual Actor destructor.
        This method is used to delete the actual actor object represented by an instance of FBActor.

        """
        pass

    def GetCurrentSkeletonState(self):
        """
        Return the Current Skeleton State.

        return : Current Skeleton State 
        """
        pass

    def GetDefaultSkeletonState(self):
        """
        Return the Default Skeleton State.

        return : Default Skeleton State 
        """
        pass

    def GetDefinitionScaleVector(self,pSkeletonId,pScaleVector):
        """
        Get Actor Scaling Definition.

        pSkeletonId : Skeleton Node Id 
        pScaleVector : Actor Scaling Definition for the given ID 
        """
        pass

    def SetActorTranslation(self,pTranslationVector):
        """
        Translate Actor, similar to moving the hips of the Actor in the UI.

        pTranslationVector : Will move the entire Actor to pTranslationVector coordinate 
        """
        pass

    def SetDefinitionRotationVector(self,pSkeletonId,pRotationVector):
        """
        Set Actor Rotation Definition.

        pSkeletonId : Skeleton Node Id 
        pRotationVector : Actor Rotation value for the given ID 
        """
        pass

    def SetDefinitionScaleVector(self,pSkeletonId,pScaleVector):
        """
        Set Actor Scaling Definition.

        pSkeletonId : Skeleton Node Id 
        pScaleVector : Actor Scaling value for the given ID 
        """
        pass

    def Snap(self,pRecalcOffset):
        """
        Snap the marker set of the actor.

        pRecalcOffset : FBRecalcMarkerSetOffset
        return : True if the operation completed successfully. 
        """
        pass

    def UpdateValues(self,pEvalInfo):
        """
        Update Internal Values to be corresponding to the Given Evaluate Information.

        pEvalInfo : Evaluate Info of the Values 
        """
        pass

    Active=property(doc="<b>Read Write Property:</b> Is actor snap active?.         ")
    BodyColor=property(doc="<b>Read Write Property:</b> The color of the body of the actor.         ")
    ChestPosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.         ")
    FKFingerMultiplier=property(doc="<b>Read Write Property:</b> Used to augment the amount of FK propagation for unmarkered intermediate finger phalanges.         ")
    FKFingerTipMultiplier=property(doc="<b>Read Write Property:</b> Used to augment the amount of FK propagation for unmarkered finger tip phalanges.         ")
    FKThumbTipMultiplier=property(doc="<b>Read Write Property:</b> Used to augment the amount of FK propagation for unmarkered thumb tip phalanges.         ")
    HeadPosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.         ")
    HipsPosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.         ")
    HumanFingerLimits=property(doc="<b>Read Write Property:</b> Enables/Disables human finger limits during actor solve.         ")
    LeftAnklePosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.         ")
    LeftCollarPosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.         ")
    LeftElbowPosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.         ")
    LeftFootPosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.         ")
    LeftHandIndexIndex=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.         ")
    LeftHandIndexMiddle=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.         ")
    LeftHandIndexPinky=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.         ")
    LeftHandIndexRing=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.         ")
    LeftHandMiddleIndex=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.         ")
    LeftHandMiddleMiddle=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.         ")
    LeftHandMiddlePinky=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.         ")
    LeftHandMiddleRing=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.         ")
    LeftHandPinkyIndex=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.         ")
    LeftHandPinkyMiddle=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.         ")
    LeftHandPinkyPinky=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.         ")
    LeftHandPinkyRing=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.         ")
    LeftHandRingIndex=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.         ")
    LeftHandRingMiddle=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.         ")
    LeftHandRingPinky=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.         ")
    LeftHandRingRing=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.         ")
    LeftHipPosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.         ")
    LeftKneePosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.         ")
    LeftShoulderPosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.         ")
    LeftWristPosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.         ")
    Locked=property(doc="<b>Read Write Property:</b> Is actor locked?.         ")
    MarkerSet=property(doc="<b>Read Write Property:</b> Associated marker set.         ")
    MarkerSetSize=property(doc="<b>Read Write Property:</b> The size of the markers of the actor.         ")
    NeckPosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.         ")
    OutputMarkerSet=property(doc="<b>Read Write Property:</b> Associated output marker set.         ")
    PivotColor=property(doc="<b>Read Write Property:</b> The color of the pivot points of the actor.         ")
    PivotSize=property(doc="<b>Read Write Property:</b> The size of the pivot points of the actor.         ")
    RightAnklePosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.         ")
    RightCollarPosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.         ")
    RightElbowPosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.         ")
    RightFootPosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.         ")
    RightHandIndexIndex=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.         ")
    RightHandIndexMiddle=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.         ")
    RightHandIndexPinky=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.         ")
    RightHandIndexRing=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.         ")
    RightHandMiddleIndex=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.         ")
    RightHandMiddleMiddle=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.         ")
    RightHandMiddlePinky=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.         ")
    RightHandMiddleRing=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.         ")
    RightHandPinkyIndex=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.         ")
    RightHandPinkyMiddle=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.         ")
    RightHandPinkyPinky=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.         ")
    RightHandPinkyRing=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.         ")
    RightHandRingIndex=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.         ")
    RightHandRingMiddle=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.         ")
    RightHandRingPinky=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.         ")
    RightHandRingRing=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.         ")
    RightHipPosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.         ")
    RightKneePosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.         ")
    RightShoulderPosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.         ")
    RightWristPosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.         ")
    SkeletonColor=property(doc="<b>Read Write Property:</b> The color of the skeleton of the actor.         ")
    WaistPosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.         ")
    pass

class FBVideoOut (FBVideo):
    """
    Video media class.     
        
    """
    def FBVideoOut(self):
        """
        Constructor.

        """
        pass

    pass

class FBModelCube (FBModel):
    """
    Cube model class.     
        
    """
    def FBModelCube(self,pName):
        """
        Constructor.

        pName : Name of cube. 
        """
        pass

    pass

class FBVideoClip (FBVideo):
    """
        
        
    """
    def FBVideoClip(self,pName):
        """
        Constructor.

        pName : Name of video media. 
        """
        pass

    def DrawImage(self,pX,pY,pW,pH,pFrame):
        """
        Draw a frame of the image to the current view.

        pX : X position of image (default=0). 
        pY : Y position of image (default=0). 
        pW : Width of image (default=-1). 
        pH : Height of image (default=-1). 
        pFrame : Frame to draw (default=-1). 
        """
        pass

    def FBDelete(self):
        """
        Open Reality Deletion function.

        """
        pass

    def GetTextureID(self):
        """
        Get the texture ID.

        return : ID of the texture 
        """
        pass

    def IsValid(self):
        """
        Verifies the validity of the FBVideo object.

        return : <b>true</b> if data is valid. 
        """
        pass

    CurrentFrame=property(doc="<b>Read Write Property:</b> Current frame.         ")
    CurrentFrameTime=property(doc="<b>Read Write Property:</b> Current time in clip.         ")
    FPS=property(doc="<b>Read Only Property:</b> Frame rate.         ")
    Filename=property(doc="<b>Read Write Property:</b> Filename of media.         ")
    Format=property(doc="<b>Read Only Property:</b> Video format.         ")
    FrameTime=property(doc="<b>Read Only Property:</b> Inverse of FPS, time per frame         ")
    FreeRunning=property(doc="<b>Read Write Property:</b> Is free Running on?         ")
    Height=property(doc="<b>Read Only Property:</b> Height of image.         ")
    InterlaceMode=property(doc="<b>Read Write Property:</b> Interlace mode.         ")
    LastFrame=property(doc="<b>Read Only Property:</b> Last frame in clip.         ")
    LastFrameTime=property(doc="<b>Read Only Property:</b> Time of last frame         ")
    Loop=property(doc="<b>Read Write Property:</b> Loop video clip?         ")
    PlaySpeed=property(doc="<b>Read Write Property:</b> Playback speed.         ")
    PowerOfTwoHeight=property(doc="<b>Read Only Property:</b> Closest power of two walue superior to height of image.         ")
    PowerOfTwoWidth=property(doc="<b>Read Only Property:</b> Closest power of two walue superior to width of image.         ")
    ProxyMode=property(doc="<b>Read Write Property:</b> Proxy mode.         ")
    StartFrame=property(doc="<b>Read Write Property:</b> Frame to begin video playback from.         ")
    StopFrame=property(doc="<b>Read Write Property:</b> Frame to end video playback at.         ")
    StorageMode=property(doc="<b>Read Write Property:</b> Storage mode.         ")
    TimeOffset=property(doc="<b>Read Write Property:</b> Temporal offset for beginning of video.         ")
    Width=property(doc="<b>Read Only Property:</b> Width of image.         ")
    pass

class FBModelSkeleton (FBModel):
    """
    Root object class.     
        
    """
    def FBModelSkeleton(self,pName):
        """
        Constructor.

        pName : Name of skeleton. 
        """
        pass

    Color=property(doc="<b>Read Write Property:</b> Color of skeleton node.         ")
    Size=property(doc="<b>Read Write Property:</b> Size (not related to scaling).         ")
    pass

class FBModelPlaceHolder (FBBoxPlaceHolder):
    """
    Wrapper around a specific instance of a FBModel object.     
    This class is mainly used with a constraint relation to have multiple boxes that are a representation of the same underlying model. Instantiation of FBModelPlaceHolder should be left to the the system.     
    """
    def FBModelPlaceHolder(self):
        """
        Constructor.

        """
        pass

    Model=property(doc="<b>Read Only Property:</b> Underlying model object.         ")
    UseGlobalTransforms=property(doc="<b>Read Write Property:</b> Indicate if the translations are expressed in local or global mode.         ")
    pass

class FBModelPlane (FBModel):
    """
    Plane model class.     
        
    """
    def FBModelPlane(self,pName):
        """
        Constructor.

        pName : Name of Plane. 
        """
        pass

    pass

class FBCameraSwitcher (FBModel):
    """
    Camera switcher.     
    This class is a wrapper around the system's camera switcher object. There can only be one switcher in a given scene. Any attempts at creating a new instance will return the existing one.     
    """
    def FBCameraSwitcher(self):
        """
        Constructor.

        """
        pass

    CurrentCamera=property(doc="<b>Read Write Property:</b> Camera currently being used by the switcher.         ")
    CurrentCameraIndex=property(doc="<b>Read Write Property:</b> Camera index currently being used by the switcher.         ")
    pass

class FBPatch (FBSurface):
    """
    Patch class.     
        
    """
    def FBPatch(self,pModel):
        """
        Constructor.

        pModel : Model to which Patch belongs. 
        """
        pass

    def ControlPointsBegin(self):
        """
        Begin control points edition.

        """
        pass

    def ControlPointsEnd(self):
        """
        End control points edition.

        """
        pass

    def SurfaceBegin(self):
        """
        Begin Patch definition.

        """
        pass

    def SurfaceEditBegin(self):
        """
        Begin patch surface edit.

        """
        pass

    def SurfaceEditEnd(self):
        """
        End patch surface edit.

        """
        pass

    def SurfaceEnd(self):
        """
        End Patch definition.

        """
        pass

    pass

class FBLight (FBModel):
    """
    Light class.     
        
    """
    def FBLight(self,pName):
        """
        Constructor.

        pName : Name of light. 
        """
        pass

    AttenuationType=property(doc="<b>Read Write Property:</b> Type of attenuation for the light.         ")
    CastLightOnObject=property(doc="<b>Read Write Property:</b> Cast light on object?         ")
    ConeAngle=property(doc="<b>Read Write Property:</b> Cone angle for light.         ")
    DiffuseColor=property(doc="<b>Read Write Property:</b> Color: Diffuse color.         ")
    DrawFrontFacingVolumetric=property(doc="<b>Read Write Property:</b> Draw front facing volumetric light?         ")
    DrawGroundProjection=property(doc="<b>Read Write Property:</b> Draw ground projection of gobo?         ")
    DrawVolumetricLight=property(doc="<b>Read Write Property:</b> Draw volumetric light with gobo?         ")
    FogIntensity=property(doc="<b>Read Write Property:</b> Intensity of the fog (spot light).         ")
    GoboMedia=property(doc="<b>Read Write Property:</b> Media to use as a Gobo with the light.         ")
    Intensity=property(doc="<b>Read Write Property:</b> Light intensity.         ")
    LightType=property(doc="<b>Read Write Property:</b> Type of light.         ")
    pass

class FBModelNull (FBModel):
    """
    Null object class.     
        
    """
    def FBModelNull(self,pName):
        """
        Constructor.

        pName : Name of null. 
        """
        pass

    Size=property(doc="<b>Read Write Property:</b> Size (not related to scaling).         ")
    pass

class FBPopup (FBLayout):
    """
    Popup window.     
    This class lets a window (inheriting from FBLayout) be created for another interface.     
    """
    def FBPopup(self):
        """
        Constructor.

        """
        pass

    def Close(self,pOk):
        """
        Close popup.

        pOk : Equivalent of <b>OK</b> button clicked if <b>true</b> (default = <b>false</b>). 
        """
        pass

    def Show(self,pParent):
        """
        Show popup.

        pParent : Parent object for popup 
        return : Operation was successful (<b>true</b> or <b>false</b>). 
        """
        pass

    Caption=property(doc="<b>Read Write Property:</b> Caption to display in popup.         ")
    Modal=property(doc="<b>Read Write Property:</b> Modal?         ")
    pass

class FBShaderLighted (FBShader):
    """
    Lighted shader class.     
    This type of shader is the default type used by the application. It allows users to control luminosity, contrast and specularity as well as how the transparency is computed, should it be used.There are two methods to create a FBShaderLighted object: using the FBShaderManager, or simply by instantiating a class object explicitely.Please consult the application documentation for more infos on shader properties and their effects.This class should not serve as a base class for another class.Sample C++ code: 
@code
    // Creation of a lighted shader, and setting it to use
    // the constrast and specularity.
    HFBShaderLighted lShader = new FBShaderLighted( 'New Shader' );

    lShader->UseContrast  = true;
    lShader->UseSpecular  = true;
    lShader->Specular     = 35.0;
    lShader->Transparency = kFBAlphaSourceTransluscentAlpha;

    // Use the shader.
    HFBModel lModel = FBFindModelByName( 'Cube' );
    if( lModel )
    {
        lShader->ReplaceAll( lModel );
    }

    // Do some more things...

    // And then delete it when no longer necessary;
    lShader->FBDelete();
@endcode

The following sample code does the same task, but in Python.Sample Python code: 
@code
    from pyfbsdk import *

    # Creating the shader.
    lShader = FBShaderLighted( 'New Python Shader' )

    lShader.UseContrast  = True
    lShader.UseSpecular  = True
    lShader.Specular     = 35.0
    lShader.Transparency = FBAlphaSource.kFBAlphaSourceTransluscentAlpha

    lModel = FBFindModelByName( 'Cube' )
    if lModel:
        lShader.ReplaceAll( lModel )
@endcode

     
    """
    def FBShaderLighted(self,pName):
        """
        Constructor.

        pName : Name of shader. 
        """
        pass

    Alpha=property(doc="<b>Read Write Property:</b> Controls the actual effect of the shader on the object. At 0.0 it does nothing, and at 1.0 it fully affects the object.         ")
    Contrast=property(doc="<b>Read Write Property:</b> Changes the contrast of the object when it reflects light.         ")
    Luminosity=property(doc="<b>Read Write Property:</b> Changes the brightness of the object when reflecting light.         ")
    Specular=property(doc="<b>Read Write Property:</b> Changes an object's level of shininess when it reflects light by affecting the specular highlight.         ")
    Transparency=property(doc="<b>Read Write Property:</b> Indicates the computation method of the transparency.         ")
    UseContrast=property(doc="<b>Read Write Property:</b> Activate the Contrast option.         ")
    UseLuminosity=property(doc="<b>Read Write Property:</b> Activate the Luminosity option.         ")
    UseSpecular=property(doc="<b>Read Write Property:</b> Activate the Specularity option.         ")
    pass

class FBMemo (FBEdit):
    """
    Multi-line text input.     
        
    """
    def FBMemo(self):
        """
        Constructor.

        """
        pass

    def GetStrings(self,pLines):
        """
        Get the content of the memo.

        pLines : Content of the memo will be copied to it. 
        """
        pass

    def SetStrings(self,pLines):
        """
        Set the content of the memo.

        pLines : Content of the memo from will be set to it. 
        """
        pass

    pass

class FBTool (FBLayout):
    """
    Tool class.     
        
    """
    def FBTool(self,pName):
        """
        Constructor.

        pName : Name of tool. 
        """
        pass

    def FBTool(self,pName,pRegisterTool):
        """
        Constructor used when creating tools not in the Tools menu of Motion Builder.

        pName : Name of tool, must be an unique name. 
        pRegisterTool : Tells if we should register the tool on the toolmanager. You can later call Showtool to pop it. 
        """
        pass

    StartSizeX=property(doc="<b>Read Property:</b> Starting Size. This is the initial size in X when the tool is opened. Default = 800         ")
    StartSizeY=property(doc="<b>Read Property:</b> Starting Size. This is the initial size in Y when the tool is opened. Default = 400         ")
    MaxSizeX=property(doc="<b>Read Property:</b> Maximum Size in X (Disabled in this version). A value of -1 means no maximum size.         ")
    MaxSizeY=property(doc="Maximum Size in Y (Disabled in this version). A value of -1 means no maximum size.         ")
    MinSizeX=property(doc="<b>Read Property:</b> Minimum Size in X. A value of -1 means no minimum value.         ")
    MinSizeY=property(doc="<b>Read Property:</b> Minimum Size in Y. A value of -1 means no minimum value.         ")
    StartPosX=property(doc="<b>Read Property:</b> Starting Position in X. This is the initial position when the tool is opened. Default = 450         ")
    StartPosY=property(doc="<b>Read Property:</b> Starting Position in Y. This is the initial position when the tool is opened. Default = 450         ")
    ToolName=property(doc="<b>Read Property:</b> Tool Name         ")
    pass

class FBModelPath3D (FBModel):
    """
    Path 3D model class.     
        
    """
    def FBModelPath3D(self,pName):
        """
        Constructor.
        Python sample code: 
@code
        Script Sample.
        from pyfbsdk import *

        path = FBModelPath3D('Test')
        path.Show = True
        der = temp.Total_LocalPathEvaluateDerivative(1)
        tgMode = path.GetLeftTangeantMode(0)
        temp.PathKeySetLeftTangeant(1,FBVector4d(25,25,25,25),True)
        ## Ajouter un Vertex
        temp.PathKeyStartAdd(FBVector4d(0,0,100,0))
        temp.PathKeyEndAdd(FBVector4d(100,0,0,0))
        ## Creer Vertex
        temp.Segment_PathKeyAdd(75.0,FBVector4d(25,25,25,25))
        temp.Segment_PathKeyAdd(25.0,FBVector4d(25,0,25,25))
@endcode

        pName : Name of Path 3D. 
        """
        pass

    def ConvertSegmentPercentToTotalPercent(self,pPercent):
        """
        pPercent : float
        """
        pass

    def ConvertToSegmentPercentFactor(self):
        """
        """
        pass

    def ConvertToTotalPercentFactor(self):
        """
        """
        pass

    def ConvertTotalPercentToSegmentPercent(self,pPercent):
        """
        pPercent : float
        """
        pass

    def GetLeftTangeantMode(self,pKeyIndex):
        """
        pKeyIndex : int
        """
        pass

    def GetRightTangeantMode(self,pKeyIndex):
        """
        pKeyIndex : int
        """
        pass

    def GetSelectedPathKeyCount(self):
        """
        """
        pass

    def InsertNewEndKey(self):
        """
        """
        pass

    def InsertNewStartKey(self):
        """
        """
        pass

    def PatKeyGetLeftTangeantLength(self,pKeyIndex):
        """
        pKeyIndex : int
        """
        pass

    def PatKeyGetRightTangeantLength(self,pKeyIndex):
        """
        pKeyIndex : int
        """
        pass

    def PathKeyClear(self):
        """
        """
        pass

    def PathKeyEndAdd(self,pTLocal):
        """
        pTLocal : FBVector4d
        """
        pass

    def PathKeyGet(self,pKeyIndex):
        """
        pKeyIndex : int
        """
        pass

    def PathKeyGetCount(self):
        """
        """
        pass

    def PathKeyGetLeftTangeant(self,pKeyIndex):
        """
        pKeyIndex : int
        """
        pass

    def PathKeyGetRightTangeant(self,pKeyIndex):
        """
        pKeyIndex : int
        """
        pass

    def PathKeyGetXYZDerivative(self,pKeyIndex):
        """
        pKeyIndex : int
        """
        pass

    def PathKeyRemove(self,pKeyIndex):
        """
        pKeyIndex : int
        """
        pass

    def PathKeyRemoveSelected(self):
        """
        """
        pass

    def PathKeySet(self,pKeyIndex,pTLocal,pUpdate):
        """
        pKeyIndex : int
        pTLocal : FBVector4d
        pUpdate : bool
        """
        pass

    def PathKeySetLeftTangeant(self,pKeyIndex,pTLocal,pUpdate):
        """
        pKeyIndex : int
        pTLocal : FBVector4d
        pUpdate : bool
        """
        pass

    def PathKeySetRightTangeant(self,pKeyIndex,pTLocal,pUpdate):
        """
        pKeyIndex : int
        pTLocal : FBVector4d
        pUpdate : bool
        """
        pass

    def PathKeySetXDerivative(self,pKeyIndex,pDerivative,pUpdate):
        """
        pKeyIndex : int
        pDerivative : float
        pUpdate : bool
        """
        pass

    def PathKeySetXYZDerivative(self,pKeyIndex,pDerivative,pUpdate):
        """
        pKeyIndex : int
        pDerivative : FBVector4d
        pUpdate : bool
        """
        pass

    def PathKeySetYDerivative(self,pKeyIndex,pDerivative,pUpdate):
        """
        pKeyIndex : int
        pDerivative : float
        pUpdate : bool
        """
        pass

    def PathKeySetZDerivative(self,pKeyIndex,pDerivative,pUpdate):
        """
        pKeyIndex : int
        pDerivative : float
        pUpdate : bool
        """
        pass

    def PathKeyStartAdd(self,pTLocal):
        """
        pTLocal : FBVector4d
        """
        pass

    def Segment_GlobalPathEvaluate(self,pSegmentPercent):
        """
        pSegmentPercent : float
        """
        pass

    def Segment_GlobalPathEvaluateDerivative(self,pSegmentPercent):
        """
        pSegmentPercent : float
        """
        pass

    def Segment_IsPathKey(self,pSegmentPercent):
        """
        pSegmentPercent : float
        """
        pass

    def Segment_LocalPathEvaluate(self,pSegmentPercent):
        """
        pSegmentPercent : float
        """
        pass

    def Segment_LocalPathEvaluateDerivative(self,pSegmentPercent):
        """
        pSegmentPercent : float
        """
        pass

    def Segment_PathKeyAdd(self,pSegmentPercent,pTLocal):
        """
        pSegmentPercent : float
        pTLocal : FBVector4d
        """
        pass

    def SetLeftTangeantMode(self,pKeyIndex,pTangeantMode):
        """
        pKeyIndex : int
        pTangeantMode : FBPathTangeantMode
        """
        pass

    def SetRightTangeantMode(self,pKeyIndex,pTangeantMode):
        """
        pKeyIndex : int
        pTangeantMode : FBPathTangeantMode
        """
        pass

    def ShowCurveControls(self,pShow):
        """
        pShow : bool
        """
        pass

    def ShowCurvePoints(self,pShow):
        """
        pShow : bool
        """
        pass

    def Total_GlobalPathEvaluate(self,pTotalPercent):
        """
        pTotalPercent : float
        """
        pass

    def Total_GlobalPathEvaluateDerivative(self,pTotalPercent):
        """
        pTotalPercent : float
        """
        pass

    def Total_IsPathKey(self,pTotalPercent):
        """
        pTotalPercent : float
        """
        pass

    def Total_LocalPathEvaluate(self,pTotalPercent):
        """
        pTotalPercent : float
        """
        pass

    def Total_LocalPathEvaluateDerivative(self,pTotalPercent):
        """
        pTotalPercent : float
        """
        pass

    def Total_PathKeyAdd(self,pTotalPercent,pTLocal):
        """
        pTotalPercent : float
        pTLocal : FBVector4d
        """
        pass

    pass

class FBVideoIn (FBVideo):
    """
    Video media class.     
        
    """
    def FBVideoIn(self):
        """
        Constructor.

        """
        pass

    pass

class FBCharacterFace (FBConstraint):
    """
    Character class.     
    <b>These classes are under development and may change dramatically between versions.</b>     
    """
    def FBCharacterFace(self,pName):
        """
        Constructor.

        pName : Name of new character. 
        """
        pass

    def ClusterGroupAdd(self,pList,pName):
        """
        Add a cluster group to the character face.

        pList : List of clusters to add to this group. 
        pName : Optional name to assign to this cluster group. 
        return : <b>Index</b> of the new cluster group <b>-1</b> if the operation failed to complete. 
        """
        pass

    def ClusterGroupFindByName(self,pName):
        """
        Find a cluster group by name.

        pName : Name to search for on the face. 
        return : <b>Index</b> of the matching cluster group. <b>-1</b> if not found. 
        """
        pass

    def ClusterGroupGetCount(self):
        """
        Retrieve the total number of cluster groups.

        return : Number of cluster groups on the face. 
        """
        pass

    def ClusterGroupGetName(self,pClusterGrpId):
        """
        Retrieve the name of a cluster group.

        pClusterGrpId : Index of the cluster group to query. 
        return : Name of the specified cluster group. 
        """
        pass

    def ClusterGroupRemove(self,pClusterGrpId):
        """
        Remove a cluster group from the character face.

        pClusterGrpId : Index of the cluster group to remove. 
        return : True if the operation completed successfully. 
        """
        pass

    def ClusterGroupSetName(self,pClusterGrpId,pName):
        """
        Set the name of a cluster group.

        pClusterGrpId : Index of the cluster group to modify. 
        pName : New name for the cluster group. 
        return : True of the operation completed successfully. 
        """
        pass

    def ClusterGroupSnapRest(self,pClusterGrpId):
        """
        Set a cluster group's rest pose to the current pose.

        pClusterGrpId : Index of the cluster group to modify. 
        return : True if the operation completed succesfully. 
        """
        pass

    def ClusterShapeAdd(self,pClusterGrpId,pName):
        """
        Add a cluster shape to a cluster group.

        pClusterGrpId : Index of the cluster group to modify. 
        pName : Optional name to assign to the shape. 
        return : <b>Index</b> of the new shape. <b>-1</b> if the operation failed to complete. 
        """
        pass

    def ClusterShapeFindByName(self,pClusterGrpId,pName):
        """
        Find a cluster shape in a cluster group by name.

        pClusterGrpId : Index of the cluster group to search. 
        pName : Name to search for in the cluster group. 
        return : <b>Index</b> of the matching shape. <b>-1</b> if not found. 
        """
        pass

    def ClusterShapeGetCount(self,pClusterGrpId):
        """
        Retrieve the total number of shapes in a cluster group.

        pClusterGrpId : Index of the cluster group to query. 
        return : Number of shapes in the specified cluster group. 
        """
        pass

    def ClusterShapeGetName(self,pClusterGrpId,pClusterShapeId):
        """
        Retrieve the name of a shape in a cluster group.

        pClusterGrpId : Index of the cluster group to query. 
        pClusterShapeId : Index of the cluster shape to query. 
        return : Name of the specified shape. 
        """
        pass

    def ClusterShapeRemove(self,pClusterGrpId,pClusterShapeId):
        """
        Remove a cluster shape from a cluster group.

        pClusterGrpId : Index of the cluster group to modify. 
        pClusterShapeId : Index of the shape in the cluster group to remove. 
        return : True of the operation completed succesfully. 
        """
        pass

    def ClusterShapeSetName(self,pClusterGrpId,pClusterShapeId,pName):
        """
        Set the name of a shape in a cluster group.

        pClusterGrpId : Index of the cluster group to modify. 
        pClusterShapeId : Index of the cluster shape to modify. 
        pName : Name to assign to the cluster shape. 
        return : True if the operation completed successfully. 
        """
        pass

    def ClusterShapeSnap(self,pClusterGrpId,pClusterShapeId):
        """
        Record the current pose of the cluster group to a cluster shape.

        pClusterGrpId : Index of the cluster group to record. 
        pClusterShapeId : Index of the cluster shape to record the pose. 
        return : True if the operation completed successfully. 
        """
        pass

    def ExpressionAdd(self,pName):
        """
        Add an expression to the face.

        pName : Optional name to assign to the new expression. 
        return : <b>Index</b> of the new expression. <b>-1</b> if the operation failed to complete. 
        """
        pass

    def ExpressionFindByName(self,pName):
        """
        Find an expression on the face by name.

        pName : Name of the expression to search for. 
        return : <b>Index</b> of the matching expression. <b>-1</b> if not found. 
        """
        pass

    def ExpressionGetCount(self):
        """
        Retrieve the total number of expressions on the face.

        return : Number of expressions on the face. 
        """
        pass

    def ExpressionGetName(self,pExpressionId):
        """
        Retrieve the name of an expression.

        pExpressionId : Index of the expression to query. 
        return : Name of the specified expression. 
        """
        pass

    def ExpressionRemove(self,pExpressionId):
        """
        Remove an expression from the face.

        pExpressionId : Index of the expression to remove. 
        return : True if the operation completed successfully. 
        """
        pass

    def ExpressionSetName(self,pExpressionId,pName):
        """
        Set the name of an expression.

        pExpressionId : Index of the expression to modify. 
        pName : Name to assign to the expression. 
        return : True if the operation completed successfully. 
        """
        pass

    def ExpressionSetShapeWeight(self,pExpressionId,pGrpId,pShapeId,pValue):
        """
        Assign the weight of a shape to an expression.

        pExpressionId : Index of the expression to modify. 
        pGrpId : Index of the blendshape or cluster group containing the shape of interest. 
        pShapeId : Index of the blendshape or cluster shape to weight. 
        pValue : Weight of the shape to assign to this expression. Valid range of [0.0, 1.0]. 
        return : True if the operation completed successfully. 
        """
        pass

    def FBDelete(self):
        """
        Actual Character Face destructor.
        This method is used to delete the actual character face object represented by an instance of FBCharacterFace.

        """
        pass

    def GotoRest(self):
        """
        Set the character face back to its rest shape.

        """
        pass

    def PlotAnimation(self):
        """
        Plot the animation of the character face.

        return : True if the operation completed successfully. 
        """
        pass

    def ShapeFindByName(self,pShapeGrpId,pName):
        """
        Find a shape in a blendshape group by name.

        pShapeGrpId : Index of the blendshape group to search. 
        pName : Name to search for. 
        return : <b>Index</b> of the shape, <b>-1</b> if not found. 
        """
        pass

    def ShapeGetCount(self,pShapeGrpId):
        """
        Retrieve the total number of shapes in a blendshape group.

        pShapeGrpId : Index of the blendshape group to query. 
        return : Number of shapes in the specified blendshape group. 
        """
        pass

    def ShapeGetName(self,pShapeGrpId,pShapeId):
        """
        Retrieve the name of the shape in a blendshape group.

        pShapeGrpId : Index of the blendshape group to query. 
        pShapeId : Index of the shape in the blendshape group to query. 
        return : Name of the specified shape. 
        """
        pass

    def ShapeGroupAdd(self,pList,pName):
        """
        Add a blendshape model group containing models.

        pList : List of models to be associated with this blendshape group. 
        pName : Optional name for this model group. 
        return : True if the operation completed successfully. 
        """
        pass

    def ShapeGroupFindByName(self,pName):
        """
        Find a blendshape group by name.

        pName : Name to search for. 
        return : <b>Index</b> of the blendshape group, <b>-1</b> if not found. 
        """
        pass

    def ShapeGroupGetCount(self):
        """
        Retrieve the total number of blendshape groups on this character face.

        return : Number of blendshape groups on this character face. 
        """
        pass

    def ShapeGroupGetName(self,pShapeGrpId):
        """
        Retrieve the name of a blendshape group.

        pShapeGrpId : Index of the blendshape group to query. 
        return : Name of the blendshape group. 
        """
        pass

    def ShapeGroupRemove(self,pShapeGrpId):
        """
        Remove a blendshape model group.

        pShapeGrpId : Index of the blendshape group to remove. 
        return : True if the operation completed successfully. 
        """
        pass

    def ShapeGroupSetName(self,pShapeGrpId,pName):
        """
        Set the name of a blendshape group.

        pShapeGrpId : Index of the blendshape group to modify. 
        pName : Name to set on the blendshape group. 
        return : True if the operation completed successfully. 
        """
        pass

    def ShapeSetName(self,pShapeGrpId,pShapeId,pName):
        """
        Set the name of the shape in a blendshape group.

        pShapeGrpId : Index of the blendshape group to query. 
        pShapeId : Index of the shape in the blendshape group to set. 
        pName : Name to set on the shape. 
        return : True if the operation completed successfully. 
        """
        pass

    ActiveInput=property(doc="<b>Read Write Property:</b> Is the character input active?         ")
    InputActorFace=property(doc="<b>Read Write Property:</b> The index of the actor used for the input.         ")
    pass

class FBCharacter (FBConstraint):
    """
    Character class.     
    <b>These classes are under development and may change dramatically between versions.</b> This class exposes part of the functionality associated with a Character. A character can possess a number of potential sources at the same time, such as an actor and another character, but with only one active at any given time. Before setting the InputType to the desired value, one must make sure to have previously set either the InputCharacter or the InputActor.To obtain the list of characters present in a scene, you need to create an instance of class FBSystem, to obtain the current scene. The FBScene object holds the list of characters in the property Characters. 
@code
       FBSystem lSystem;
       HFBScene lScene = lSystem.Scene;
       for( int lIdx = 0; lIdx < lScene->Characters.GetCount(); ++lIdx )
       {
           FBTrace( 'Character[%d]: '%s'\n', lIdx, (char*)lScene->Characters[lIdx] );
       }
@endcode

The current character selected in the Character tool can be obtained via the FBApplication object. 
@code
       FBApplication lApplication;
       HFBCharacter lCharacter = lApplication.CurrentCharacter;
       if( lCharacter )
       {
           FBTrace( 'Current character is: '%s'\n', (char*)lCharacter->Name );
       }
       else
       {
           FBTrace( 'No character currently selected\n' );
       }
@endcode

     
    """
    def FBCharacter(self,pName):
        """
        Constructor.

        pName : Name of new character. 
        """
        pass

    def AddCharacterExtension(self,pExt):
        """
        AddCharacterExtension.

        pExt : extension to be added to the character. 
        """
        pass

    def Clone(self):
        """
        Clone the character.

        """
        pass

    def CopyAnimation(self):
        """
        Copy the animation from the input character to us.

        """
        pass

    def CreateControlRig(self,pSetFKIK):
        """
        Create the Control-Rig.

        pSetFKIK : true to use FK/IK or false to use IK only. 
        return : current state of the flag after the operation (true if it did succeed). 
        """
        pass

    def FBDelete(self):
        """
        Actual Character destructor.
        This method is used to delete the actual character object represented by an instance of FBCharacter.

        """
        pass

    def GetActiveBodyPart(self,pActivePart):
        """
        Get the active body part array.

        pActivePart : A pointer to an array of bool. On return, the index with a "true" value are active part. 
        """
        pass

    def GetCharacterize(self):
        """
        Get Characterize flag.

        return : Current state of the Characterize flag. 
        """
        pass

    def GetCharacterizeError(self):
        """
        Get error message for the previous SetCharacterizeOn operation.

        return : The string containing all errors and warnings. 
        """
        pass

    def GetCtrlRigModel(self,pBodyNodeId):
        """
        Get the model associated with each body part in the Control Rig of the character.

        pBodyNodeId : FBBodyNodeId
        return : The model in the Control Rig corresponding to the specified body part. 
        """
        pass

    def GetCurrentControlSet(self,pForce):
        """
        Obtain Input ControlSet.

        pForce : If True, will return the current ControlSet even if the character is not in ControlSet Input. 
        return : Return current Active ControlSet, NULL if none. 
        """
        pass

    def GetEffectorModel(self,pEffectorId,pEffectorSetID):
        """
        Get the model associated with each effector in the Control Rig of the character.

        pEffectorId : The effector ID. 
        pEffectorSetID : Id of the ControlSet to obtain, if not specified the current one is taken. 
        return : The model in the Control Rig corresponding to the specified Effector. 
        """
        pass

    def GetExternalSolver(self):
        """
        Get a pointer to the external solver of a character, or NULL is no external solver is used on the character.

        return : The pointer of the current External Solver, NULL if it's the internal solver. 
        """
        pass

    def GetFloorContactModel(self,pMemberIndex):
        """
        Get the model associated with the floor contact ID.

        pMemberIndex : Id of the floor contact 
        return : The model associated with the floor contact ID 
        """
        pass

    def GetIndexByModel(self,pModel):
        """
        Get the index associated with Given Model.

        pModel : FBModel
        return : The model linked to the specified body part. 
        """
        pass

    def GetModel(self,pBodyNodeId):
        """
        Get the model associated with each body part of the character.

        pBodyNodeId : FBBodyNodeId
        return : The model linked to the specified body part. 
        """
        pass

    def GetParentROffset(self,pBodyNodeId,pRVector):
        """
        pBodyNodeId : FBBodyNodeId
        pRVector : FBRVector
        """
        pass

    def GetROffset(self,pBodyNodeId,pRVector):
        """
        pBodyNodeId : FBBodyNodeId
        pRVector : FBRVector
        """
        pass

    def GetSOffset(self,pBodyNodeId,pSVector):
        """
        pBodyNodeId : FBBodyNodeId
        pSVector : FBSVector
        """
        pass

    def GetTOffset(self,pBodyNodeId,pTVector):
        """
        pBodyNodeId : FBBodyNodeId
        pTVector : FBTVector
        """
        pass

    def GetTransformOffset(self,pBodyNodeId,pOffsetMatrix):
        """
        pBodyNodeId : FBBodyNodeId
        pOffsetMatrix : FBMatrix
        """
        pass

    def GoToStancePose(self,pPushUndo,pIncludeCharacterExtensions):
        """
        Set the character in stance pose.

        pPushUndo : Should we push an undo transaction on the undo stack? Don't push undo in non UI thread. 
        pIncludeCharacterExtensions : Should the character extensions go to stance pose too? 
        """
        pass

    def IsParentNodeOffset(self,pNodeId):
        """
        Check if there is an offset on Parent.

        pNodeId : Node Id to Check. 
        return : True if there is an offset on Parent. 
        """
        pass

    def IsRotationPin(self,pEffectorIndex):
        """
        Return true if the object is Pinned in Rotation (Manipulation).

        pEffectorIndex : Given Index to obtain Model 
        return : True if the effector is pinned in Rotation 
        """
        pass

    def IsTranslationPin(self,pEffectorIndex):
        """
        Return true if the object is Pinned in Translation (Manipulation).

        pEffectorIndex : Given Index to obtain Model 
        return : True if the effector is pinned in Translation 
        """
        pass

    def PlotAnimation(self,pPlotWhere,pPlotOptions):
        """
        Plot the animation of the character.

        pPlotWhere : FBCharacterPlotWhere
        pPlotOptions : FBPlotOptions
        return : True if the operation completed successfully. 
        """
        pass

    def ReadyForRetarget(self):
        """
        Test if character is ready for the Retarget operation (basically, is it in character input ?).

        return : True if the character is ready. 
        """
        pass

    def RemoveCharacterExtension(self,pExt):
        """
        Get the model associated with each body part of the character.

        pExt : extension to be removed to the character. 
        """
        pass

    def ResetProperties(self,pType):
        """
        Reset the properties of the character.

        pType : Speficy which properties will be reset. 
        """
        pass

    def Retarget(self,pOnBaseLayer):
        """
        Retarget the animation from the input character to us.

        pOnBaseLayer : if true, keys corrections will be made on base layer; else they will be made on another layer. 
        """
        pass

    def SelectModels(self,pSelect,pApplyToCharacter,pApplyToRig,pApplyToExtensions):
        """
        Select the objects that make a character.

        pSelect : True to select, false to deselect. 
        pApplyToCharacter : TSould the character contraint be selected ? 
        pApplyToRig : should The rig (and its children) be selected ? 
        pApplyToExtensions : Should the character extensions (and their children) be selected ? 
        """
        pass

    def SetCharacterizeOff(self):
        """
        Set Characterize flag off.

        """
        pass

    def SetCharacterizeOn(self,pSetAsBiped):
        """
        Set the Characterize flag on.

        pSetAsBiped : true to use biped characterization or false to use quadruped. 
        return : current state of the flag after the operation (true if it did succeed). 
        """
        pass

    def SetExternalSolver(self,pIndex):
        """
        Set character external solver.

        pIndex : Index of external solver. 
        """
        pass

    def SetExternalSolver(self,pSolver):
        """
        Set character solver.

        pSolver : Character solver that will be used by the character. 
        """
        pass

    ActiveInput=property(doc="<b>Read Write Property:</b> Is the character input active?         ")
    CharacterExtensions=property(doc="<b>List:</b> Character Extensions in the character.         ")
    ContactBehaviour=property(doc="<b>Read Write Property:</b> Contact Behavior selection.         ")
    HipsTranslationMode=property(doc="<b>Read Write Property:</b> Hips Translation Mode.         ")
    InputActor=property(doc="<b>Read Write Property:</b> The index of the actor used for the input.         ")
    InputCharacter=property(doc="<b>Read Write Property:</b> The index of the character used for the input.         ")
    InputType=property(doc="<b>Read Write Property:</b> The input type for the character (ex: Actor).         ")
    InverseLeftElbow=property(doc="<b>Read Write Property:</b> Is left elbow inverted.         ")
    InverseLeftKnee=property(doc="<b>Read Write Property:</b> Is left knee inverted.         ")
    InverseRightElbow=property(doc="<b>Read Write Property:</b> Is right elbow inverted.         ")
    InverseRightKnee=property(doc="<b>Read Write Property:</b> Is right knee inverted.         ")
    KeyingMode=property(doc="<b>Read Write Property:</b> The current keying mode.         ")
    LeftElbowKillPitch=property(doc="<b>Read Write Property:</b> is Pitch used for Left elbow.         ")
    LeftKneeKillPitch=property(doc="<b>Read Write Property:</b> is Pitch used for Left knee.         ")
    MirrorMode=property(doc="<b>Read Write Property:</b> is in mirror mode.         ")
    RightElbowKillPitch=property(doc="<b>Read Write Property:</b> is Pitch used for Right elbow.         ")
    RightKneeKillPitch=property(doc="<b>Read Write Property:</b> is Pitch used for Right knee.         ")
    RollSolver=property(doc="<b>Read Write Property:</b> Roll Solver selection.         ")
    ShoulderCorrection=property(doc="<b>Read Write Property:</b> shoulder correction values.         ")
    SyncMode=property(doc="<b>Read Write Property:</b> is character in sync mode.         ")
    WriteReference=property(doc="<b>Read Write Property:</b> are we writing back on reference.         ")
    pass

class FBModelRoot (FBModel):
    """
    Root object class.     
        
    """
    def FBModelRoot(self,pName):
        """
        Constructor.

        pName : Name of root. 
        """
        pass

    Size=property(doc="<b>Read Write Property:</b> Size (not related to scaling).         ")
    pass

class FBConstraintRelation (FBConstraint):
    """
    ConstraintRelation class.     
    This class exposes the relation constraint and allows addition of new boxes and removal of existing ones.     
    """
    def FBConstraintRelation(self,pName):
        """
        Constructor.

        pName : Name of constraint. 
        """
        pass

    def GetBoxPosition(self):
        """
        Get a box position in the GUI.
        Get the position of a box within the constraint layout view.

        return : A tuple containing: the result of operation (bool), X value (int), and Y value(int) 
        """
        pass

    def ConstrainObject(self,pConstrainedObject):
        """
        Create a receiver box.
        Use an existing FBBox object to create a receiver in the relation.

        pConstrainedObject : Destination box to insert in the constraint. 
        return : A place holder box for the object. 
        """
        pass

    def CreateFunctionBox(self,pGroup,pName):
        """
        Create a function box.
        Ask the constraint to create new function box.

        pGroup : Name of the group under which the function is located in the Constraint Relation GUI (case-sensitive!). 
        pName : Name of the function, as seen in the GUI (case-sensitive!). 
        return : The newly created function box, or NULL if the name/group combination was invalid. 
        """
        pass

    def SetAsSource(self,pSource):
        """
        Create a sender box.
        Use an existing FBBox object to create a sender in the relation.

        pSource : Source box to insert in the constraint. 
        return : A place holder box for the object. 
        """
        pass

    def SetBoxPosition(self,pBox,pX,pY):
        """
        Set a box position in the GUI.
        Set the position of a box within the constraint layout view.

        pBox : Box which needs to be moved. 
        pX : New X position. 
        pY : New Y position. 
        return : A boolean value indicating success (True) or failure (False). 
        """
        pass

    Boxes=property(doc="<b>List:</b> Boxes used in this constraint.         ")
    pass

class FBConstraintSolver (FBConstraint):
    """
    Base class for constraint solver.     
        
    """
    def FBConstraintSolver(self,pName):
        """
        pName : str
        """
        pass

    pass

class FBModelMarker (FBModel):
    """
    Model marker class.     
        
    """
    def FBModelMarker(self,pName):
        """
        Constructor.

        pName : Name of model marker. If pObject is not NULL, pName will be ignored. 
        """
        pass

    Color=property(doc="<b>Read Write Property:</b> Color of model marker.         ")
    IKPivot=property(doc="<b>Read Write Property:</b> marker Pivot Offset.         ")
    Length=property(doc="<b>Read Write Property:</b> Length for capsule (not related to scaling).         ")
    Look=property(doc="<b>Read Write Property:</b> Look of model marker.         ")
    ResLevel=property(doc="<b>Read Write Property:</b> Resolution level of model marker.         ")
    Size=property(doc="<b>Read Write Property:</b> Size (not related to scaling).         ")
    Type=property(doc="<b>Read Write Property:</b> Type of model marker.         ")
    pass

class FBNurbs (FBSurface):
    """
    Nurbs class.     
        
    """
    def FBNurbs(self,pModel):
        """
        Constructor.

        pModel : Model to which Nurbs belongs. 
        """
        pass

    def ControlPointsBegin(self):
        """
        Begin NURBS control points edition.

        """
        pass

    def ControlPointsEnd(self):
        """
        End NURBS control points edition.

        """
        pass

    def GetControlKnotValue(self,pUorV,pIndex):
        """
        Get knot vector value of control point.

        pUorV : <b>1</b> if V knot vector, <b>0</b> if U knot vector. 
        pIndex : Index of control point to set knot value for. 
        """
        pass

    def GetControlMultiplicity(self,pUorV,pIndex):
        """
        Get multiplicity (number of 'instances') of control point.

        pUorV : <b>1</b> if V multiplicity, <b>0</b> if U multlipicity. 
        pIndex : Index of control point to get multiplicity for. 
        """
        pass

    def GetControlWeight(self,pIndex):
        """
        Get weight of control point.

        pIndex : Index of control point to get weight from. 
        return : Weight of control point at index <b>pIndex</b>. 
        """
        pass

    def GetKnotCount(self,pUorV):
        """
        Number of knot vectors.

        pUorV : <b>1</b> if V knot vector, <b>0</b> if U knot vector. 
        return : Number of knot vectors on NURBS surface 
        """
        pass

    def SetControlKnotValue(self,pUorV,pIndex,pKnotValue):
        """
        Set knot vector value of control point.

        pUorV : <b>1</b> if V knot vector, <b>0</b> if U knot vector. 
        pIndex : Index of control point to set knot value for. 
        pKnotValue : Knot value for control point at <b>pIndex</b>. 
        """
        pass

    def SetControlMultiplicity(self,pUorV,pIndex,pMultiplicity):
        """
        Set multiplicity (number of 'instances') of control point.

        pUorV : <b>1</b> if V multiplicity, <b>0</b> if U multlipicity. 
        pIndex : Index of control point to set multiplicity for. 
        pMultiplicity : Multiplicity value for control point at <b>pIndex</b>. 
        """
        pass

    def SetControlWeight(self,pIndex,pWeight):
        """
        Set weight of control point.

        pIndex : Index of control point to set weight at. 
        pWeight : Weight of control point. 
        """
        pass

    def SurfaceBegin(self):
        """
        Begin NURBS definition.

        """
        pass

    def SurfaceEditBegin(self):
        """
        Begin NURBS surface edition.

        """
        pass

    def SurfaceEditEnd(self):
        """
        End NURBS surface edition.

        """
        pass

    def SurfaceEnd(self):
        """
        End NURBS definition.

        """
        pass

    pass

class FBModelOptical (FBModel):
    """
    Optical model class.     
        
    """
    def FBModelOptical(self,pName):
        """
        Constructor.

        pName : Name of optical model. 
        """
        pass

    def ClearSegments(self,pUnUsedOnly):
        """
        Clear the segments (by default only the unused).

        pUnUsedOnly : Clear only the unused segments if <b>true</b>(default=true). 
        """
        pass

    def ExportSetup(self):
        """
        Setup exportation from optical model.

        return : <b>true</b> if successful. 
        """
        pass

    def ImportSetup(self):
        """
        Setup importation for optical model.

        return : <b>true</b> if successful. 
        """
        pass

    MarkerSize=property(doc="<b>Read Write Property:</b> Size of markers.         ")
    SamplingPeriod=property(doc="<b>Read Write Property:</b>Sampling period.         ")
    SamplingStart=property(doc="<b>Read Write Property:</b> Sampling start time.         ")
    SamplingStop=property(doc="<b>Read Write Property:</b>Sampling stop time.         ")
    pass

class FBCamera (FBModel):
    """
    Camera class.     
    Cameras do come in two versions: system cameras, and user cameras. System cameras are created by the application and cannot be destroyed.     
    """
    def FBCamera(self,pName):
        """
        Constructor.

        pName : Name of camera. 
        """
        pass

    Active=property(doc="<b>Read Write Property:</b> Is camera registered in application?         ")
    AntiAliasingIntensity=property(doc="<b>Read Write Property:</b> Anti-aliasing intensity.         ")
    AntiAliasingMethod=property(doc="<b>Read Write Property:</b> Anti-aliasing method.         ")
    ApertureMode=property(doc="<b>Read Write Property:</b> Aperture mode.         ")
    BackGroundColor=property(doc="<b>Read Write Property:</b> Background color for camera.         ")
    BackGroundImageCenter=property(doc="<b>Read Write Property:</b> Center the background image         ")
    BackGroundImageCrop=property(doc="<b>Read Write Property:</b> Crop the background image         ")
    BackGroundImageFit=property(doc="<b>Read Write Property:</b> Fit the background image         ")
    BackGroundImageKeepRatio=property(doc="<b>Read Write Property:</b> Keep the background image's ratio         ")
    BackGroundMedia=property(doc="<b>Read Write Property:</b> BackGround Image         ")
    BackGroundPlaneDistance=property(doc="<b>Read Write Property:</b> Set the distance for the background plane.         ")
    BackGroundPlaneDistanceMode=property(doc="<b>Read Write Property:</b> Select mode for the background plane's distance.         ")
    Display2DMagnifierFrame=property(doc="<b>Read Write Property:</b> Enable/Disable the drawing of the 2D Magnifier frame box.         ")
    DisplayTurnTableIcon=property(doc="<b>Read Write Property:</b> Enable/Disable the drawing of the Turn Table icon.         ")
    FarPlaneDistance=property(doc="<b>Read Write Property:</b> Far plane distance.         ")
    FieldOfView=property(doc="<b>Read Write Property:</b> Field of View (used when in horizontal or vertical aperture modes).         ")
    FieldOfViewX=property(doc="<b>Read Write Property:</b> Field of View X angle (used in horizontal and vertical aperture mode).         ")
    FieldOfViewY=property(doc="<b>Read Write Property:</b> Field of View Y angle (used in horizontal and vertical aperture mode).         ")
    FilmAspectRatio=property(doc="<b>Read Write Property:</b> Film aspect ratio.         ")
    FilmBackType=property(doc="<b>Read Write Property:</b> Film back standard type.         ")
    FilmSizeHeight=property(doc="<b>Read Write Property:</b> Height of the film.         ")
    FilmSizeWidth=property(doc="<b>Read Write Property:</b> Width of the film.         ")
    FocalLength=property(doc="<b>Read Write Property:</b> Focal Length.         ")
    FocusAngle=property(doc="<b>Read Write Property:</b> Focus Angle (rendering dof).         ")
    FocusDistanceSource=property(doc="<b>Read Write Property:</b> Select source for focusing.         ")
    FocusSpecificDistance=property(doc="<b>Read Write Property:</b> Specfic distance for focusing.         ")
    ForeGroundAlpha=property(doc="<b>Read Write Property:</b> Opacity of foreground.         ")
    ForeGroundImageCenter=property(doc="<b>Read Write Property:</b> Center the foreground image         ")
    ForeGroundImageCrop=property(doc="<b>Read Write Property:</b> Crop the foreground image         ")
    ForeGroundImageFit=property(doc="<b>Read Write Property:</b> Fit the foreground image         ")
    ForeGroundImageKeepRatio=property(doc="<b>Read Write Property:</b> Keep the foreground image's ratio?         ")
    ForeGroundMaterialThreshold=property(doc="<b>Read Write Property:</b> Material threshold for a transparent foreground.         ")
    ForeGroundMedia=property(doc="<b>Read Write Property:</b> ForeGround Image         ")
    ForeGroundPlaneDistance=property(doc="<b>Read Write Property:</b> Set the distance for the foreground plane.         ")
    ForeGroundPlaneDistanceMode=property(doc="<b>Read Write Property:</b> Select mode for the foreground plane's distance.         ")
    ForeGroundTransparent=property(doc="<b>Read Write Property:</b> Is the foreground transparent?         ")
    FrameColor=property(doc="<b>Read Write Property:</b> Frame color for camera.         ")
    FrameSizeMode=property(doc="<b>Read Write Property:</b> Frame size standard mode.         ")
    InteractiveMode=property(doc="<b>Read Write Property:</b> Interactive mode?         ")
    Interest=property(doc="<b>Read Write Property:</b> Direct camera's interest.         ")
    MagnifierPosX=property(doc="<b>Read Write Property:</b> 2D Magnifier X Position.         ")
    MagnifierPosY=property(doc="<b>Read Write Property:</b> 2D Magnifier Y Position.         ")
    MagnifierZoom=property(doc="<b>Read Write Property:</b> 2D Magnifier Zoom value.         ")
    MouseLockCamera=property(doc="<b>Read Write Property:</b> Mouse lock for camera?         ")
    NearPlaneDistance=property(doc="<b>Read Write Property:</b> Near plane distance.         ")
    NumberOfSamples=property(doc="<b>Read Write Property:</b> Number of samples to oversample with.         ")
    OpticalCenterX=property(doc="<b>Read Write Property:</b> Optical Center X (mm).         ")
    OpticalCenterY=property(doc="<b>Read Write Property:</b> Optical Center Y (mm).         ")
    OrthogonalVerticalSize=property(doc="<b>Read Write Property:</b> Near plane distance.         ")
    PixelAspectRatio=property(doc="<b>Read Write Property:</b> Pixel aspect ratio.         ")
    ResolutionHeight=property(doc="<b>Read Write Property:</b> Resolution height.         ")
    ResolutionMode=property(doc="<b>Read Write Property:</b> Resolution standard mode.         ")
    ResolutionWidth=property(doc="<b>Read Write Property:</b> Resolution width.         ")
    Roll=property(doc="<b>Read Write Property:</b> Camera's roll on it's Z axis.         ")
    SafeAreaMode=property(doc="<b>Read Write Property:</b> Select mode for safe area.         ")
    SamplingType=property(doc="<b>Read Write Property:</b> Type of over sampling.         ")
    SqueezeRatio=property(doc="<b>Read Write Property:</b> Squeeze ratio.         ")
    SystemCamera=property(doc="<b>Read Only Property:</b> Indicate if this a default camera or a user-created camera.         ")
    TurnTable=property(doc="<b>Read Write Property:</b> Camera's rotation around its interest.         ")
    Type=property(doc="<b>Read Write Property:</b> Type of camera         ")
    Use2DMagnifier=property(doc="<b>Read Write Property:</b> Enable/Disable the 2D Magnifier.         ")
    UseAccumulationBuffer=property(doc="<b>Read Write Property:</b> Use accumulation buffer?         ")
    UseAntiAliasing=property(doc="<b>Read Write Property:</b> Use anti-aliasing?         ")
    UseDepthOfField=property(doc="<b>Read Write Property:</b> Use depth of field calculations?         ")
    UseFrameColor=property(doc="<b>Read Write Property:</b> Use frame color?         ")
    ViewBackGroundPlaneMode=property(doc="<b>Read Write Property:</b> Background plane view mode         ")
    ViewCameraInterest=property(doc="<b>Read Write Property:</b> Show the camera interest?         ")
    ViewDisplaySafeArea=property(doc="<b>Read Write Property:</b> Display safe area?         ")
    ViewForeGroundPlaneMode=property(doc="<b>Read Write Property:</b> Foreground plane view mode         ")
    ViewNearFarPlane=property(doc="<b>Read Write Property:</b> Show near/far planes?         ")
    ViewOpticalCenter=property(doc="<b>Read Write Property:</b> View optical center?         ")
    ViewShowAxis=property(doc="<b>Read Write Property:</b> Show axis?         ")
    ViewShowGrid=property(doc="<b>Read Write Property:</b> Show grid?         ")
    ViewShowTimeCode=property(doc="<b>Read Write Property:</b> Show time code?         ")
    WindowHeight=property(doc="<b>Read Only Property:</b> Window height.         ")
    pass

