# vario_gui.py
#
# written by: Oliver Cordes 2016-09-26
# changed by: Oliver Cordes 2016-09-26

import sys, os
import logging

from ginga import AstroImage
from ginga.misc import log
from ginga.qtw.QtHelp import QtGui, QtCore
from ginga.qtw.ImageViewCanvasQt import ImageViewCanvas

from helper import *

class Vario_GUI( MainWindow ):

    def __init__( self, logger ):
        super( Vario_GUI, self).__init__()
        self.logger = logger

        self.fileMenu = self.menuBar().addMenu( "&File" )

        fileNewAction  = self.createAction( '&New...', self.fileNew,
                            QtGui.QKeySequence.New, 'filenew', 'Create a new project' )
        fileQuitAction = self.createAction( '&Quit', self.close,
                            'Ctrl-Q', 'filequit', 'Close the program' )


        #self.fileMenuActions = ( fileNewAction, fileOpenAction,
        #    fileSaveAction, fileSaveAsAction, None, fileQuitAction )

        self.fileMenuActions = ( fileNewAction, fileQuitAction )
        self.addActions( self.fileMenu, self.fileMenuActions )
        self.connect( self.fileMenu, QtCore.SIGNAL( 'aboutToShow()' ), self.updateFileMenu )

    def load_file( self, filename ):
        print( 'Load file')

    def fileNew( self ):
        print( 'File new')
