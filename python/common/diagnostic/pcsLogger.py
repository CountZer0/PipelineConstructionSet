"""
Makes logger

*Examples:* ::

    >>> import common.diagnostic.pcsLogger
    >>> maya_logger = common.diagnostic.pcsLogger.logger
    >>> mobu_logger = common.diagnostic.pcsLogger.moBuLogger

*Author:*
    * Jason.Parks, jason@continuityai.com, 1/8/14 5:04 PM
"""

from common.core import globalVariables as gv
import exceptions
import getpass
import logging.handlers
import os
import sys
# Remember, cannot import MayaCore because it imports this module

MAILHOST = 'mail.myCompany.com'
FROMADDRESS = '@myCompany.com'

# email addresses
gameArtPipelineEmail = 'logger@gameartpipeline.com'
teamATechArtistEmail = 'techArtistA@myCompany.com'
teamBTechArtistEmail = 'techArtistB@myCompany.com'
toAddresses = [gameArtPipelineEmail]

#artTeam = parser_pcs.ParseSomething().userGet('myCompanyActiveTeam')
artTeam = 'GreatGameA'
if artTeam == gv.teamA:
    toAddresses = [gameArtPipelineEmail, teamATechArtistEmail]
if artTeam == gv.teamB:
    toAddresses = [gameArtPipelineEmail, teamBTechArtistEmail]

CRITICAL = 50
FATAL = CRITICAL

# ours
ERRORDIALOG = 45

ERROR = 40
WARNING = 30
WARN = WARNING

# ours
INFODIALOG = 25

INFO = 20

# ours
DEBUGDIALOG = 15

DEBUG = 10
NOTSET = 0


class PCSlogging(logging.Logger):
    """ subclass to wrap error method to return function to end script """

    def errorDialog(self, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'INFO'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.info("Houston, we have a %s", "thorny problem", exc_info=1)
        """
        print "Using PCSlogging subclass"

        if self.isEnabledFor(INFODIALOG):
            self._log(ERROR, msg, args, **kwargs)

            title = 'logger.errorDialog'
            if len(args) > 1:
                title = args[1]
            try:
                from maya import cmds

                result = cmds.confirmDialog(t=title, m=msg, b=['OK', 'Cancel'], db='OK', cb='Cancel', ds='Cancel')
                if result == "Cancel":
                    print "*** Canceled ***"
                    sys.exit()
            except RuntimeError:
                import pyfbsdk

                pyfbsdk.FBMessageBox(title, msg, "OK")
            finally:
                print "Not in Maya or MoBu?"

        raise exceptions.BaseException(msg)

    def error(self, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'ERROR'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.error("Houston, we have a %s", "major problem", exc_info=1)
        """
        print "Using PCSlogging subclass"

        if self.isEnabledFor(ERROR):
            self._log(ERROR, msg, args, **kwargs)

        raise exceptions.BaseException(msg)

    def infoDialog(self, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'INFO'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.info("Houston, we have a %s", "thorny problem", exc_info=1)
        """
        print "Using PCSlogging subclass"

        if self.isEnabledFor(INFODIALOG):
            self._log(INFO, msg, args, **kwargs)

            title = 'logger.infoDialog'
            if len(args) > 1:
                title = args[1]
            try:
                # noinspection PyUnresolvedReferences
                import maya.cmds

                result = maya.cmds.confirmDialog(t=title, m=msg, b=['OK', 'Cancel'], db='OK', cb='Cancel', ds='Cancel')
                if result == "Cancel":
                    print "*** Canceled ***"
                    sys.exit()
            except ImportError:
                import pyfbsdk

                pyfbsdk.FBMessageBox(title, msg, "OK")
            finally:
                print "Not in Maya or MoBu?"

    def debugDialog(self, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'DEBUG'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.debug("Houston, we have a %s", "thorny problem", exc_info=1)
        """
        print "Using PCSlogging subclass"

        if self.isEnabledFor(DEBUGDIALOG):
            self._log(DEBUG, msg, args, **kwargs)

            title = 'logger.debugDialog'
            if len(args) > 1:
                title = args[1]
            try:
                from maya import cmds

                result = cmds.confirmDialog(t=title, m=msg, b=['OK', 'Cancel'], db='OK', cb='Cancel', ds='Cancel')
                if result == "Cancel":
                    print "*** Canceled ***"
                    sys.exit()
            except RuntimeError:
                import pyfbsdk

                pyfbsdk.FBMessageBox(title, msg, "OK")
            finally:
                print "Not in Maya or MoBu?"


def pcs_logger(filePathName='%s/data/%s/%s.log' % (gv.logLocation, getpass.getuser(), getpass.getuser()), _logger='',
               name='pcsLogger', fresh=0):
    """
    SYNOPSIS: Creates nice logger. Will nuke FileHandler logger of similar
                type if filePathName is different from existing loggers

    INPUTS
     (string) 	filePathName:	path and file name of FileHandler stream
     (logging.Logger)	logger:	python or pymel logger object
     (string) 			name:	'handle' to logger object
     (bool) 			fresh:	1 = tries to delete old log file

    RETURNS: (logging.Logger) logger object
    """

    # create dir if doesn't exist
    filePathName = filePathName.replace('\\', '/')
    filePath = filePathName[:filePathName.rfind('/')]
    if not os.path.exists(filePath):
        os.makedirs(filePath)

    # delete file if already exists
    if fresh:
        try:
            if os.path.exists(filePathName):
                os.remove(filePathName)
        except RuntimeError:
            print ("'%s' still opened, skipping deletion" % filePathName)

    # use our logger	# Not needed w/ pymelLogger
    logging.setLoggerClass(PCSlogging)

    if not isinstance(_logger, logging.Logger):
        _logger = logging.getLogger(name)
    else:
        name = _logger.name

    # turn off Exceptions?
    logging.raiseExceptions = 1

    # create file format
    if sys.version_info[1] >= 5:
        # python 2.6 allows function name in logging
        formatter = logging.Formatter('%(asctime)s, %(module)s, %(funcName)s, %(lineno)d, %(levelname)s, %(message)s')
    else:
        formatter = logging.Formatter('%(asctime)s, %(lineno)d, %(levelname)s, %(message)s')

    # determine if handler has been made
    makeNewFileHandler = 1
    makeNewSMTPHandler = 1
    smtpHandlerFound = 0
    if len(_logger.handlers):
        for hndlr in map(lambda x: x, _logger.handlers):
            if hndlr.__class__ == logging.FileHandler:
                if not hndlr.stream.closed:
                    if hndlr.stream.name == filePathName:
                        makeNewFileHandler = 0
                    else:
                        deleteHandler(_logger.handlers, hndlr)
                else:
                    deleteHandler(_logger.handlers, hndlr)
            elif smtpHandlerFound and hndlr.__class__ == logging.handlers.SMTPHandler:
                deleteHandler(_logger.handlers, hndlr)
            else:
                smtpHandlerFound = 1
                makeNewSMTPHandler = 0

    # Make fileHandler and email handler
    if makeNewFileHandler:
        hdlr = logging.FileHandler(filePathName)
        #hdlr = logging.handlers.RotatingFileHandler(filePathName, 'a', 500, 2)
        hdlr.setFormatter(formatter)
        _logger.addHandler(hdlr)

    # Make email handler
    if makeNewSMTPHandler:
        userName = getpass.getuser()
        sHdlr = logging.handlers.SMTPHandler(MAILHOST, '%s%s' % (userName, FROMADDRESS), toAddresses,
                                             '%s: Critical from %s' % (name, userName))
        sHdlr.setLevel(logging.CRITICAL)
        _logger.addHandler(sHdlr)

    # set default level
    _logger.setLevel(logging.INFO)

    return _logger


def addMoBuHandler(_logger):
    hdlr = logging.StreamHandler()
    formatter = logging.Formatter('%(funcName)s, %(lineno)d, %(levelname)s, %(message)s')
    hdlr.setFormatter(formatter)
    _logger.addHandler(hdlr)

    return _logger


def deleteHandler(handlers, handler):
    """
    SYNOPSIS: removes handler from list of logger.handlers

    INPUTS
     (list) 			handlers:	list of handlers
     (logger.handler) 	handler:	handler to remove from list

    RETURNS: nothing
    """

    i = 0
    for hnd in handlers:
        if hnd == handler:
            del (handlers[i])
            return
        i += 1

# convenience instance
logger = pcs_logger()
moBuLogger = addMoBuHandler(pcs_logger(name='pcs_mobu_logger'))

if __name__ == '__main__':
    print 'run from Maya session'
else:
    print "common.diagnostic.pcsLogger imported"