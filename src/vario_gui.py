# vario_gui.py
#
# written by: Oliver Cordes 2016-09-26
# changed by: Oliver Cordes 2016-10-05

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


        # statusbar
        self.statusbar = QtGui.QStatusBar( self )
        self.setStatusBar( self.statusbar )

        # window content
        self.centralwidget = QtGui.QWidget( self )
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        #hBoxlayout	= QtGui.QHBoxLayout( self.centralwidget )
        hBoxlayout	= QtGui.QHBoxLayout( self.centralwidget )


        self.treeview = QtGui.QTreeView()
        self.treeview.setMinimumSize(QtCore.QSize(200, 500))
        self.treeview.setMaximumSize(QtCore.QSize(200, 16777215))
        #self.treeview.resize( 600, 100 )

        self.notebook = QtGui.QTabWidget()
        #self.notebook.resize( 600, 400 )

        self.tab1, name = self.create_tab1()
        self.notebook.addTab( self.tab1, name )
        self.tab2, name = self.create_tab2()
        self.notebook.addTab( self.tab2, name )
        self.tab3, name = self.create_tab3()
        self.notebook.addTab( self.tab3, name )

        #hBoxlayout.addWidget( self.treeview )
        #hBoxlayout.addWidget( self.notebook )

        #self.centralwidget.setLayout( hBoxlayout )
        #self.centralwidget.resize( 600, 500 )

        self.splitter = QtGui.QSplitter( self.centralwidget )
        self.splitter.setOrientation( QtCore.Qt.Horizontal )
        self.splitter.addWidget( self.treeview )
        self.splitter.addWidget( self.notebook )
        hBoxlayout.addWidget(self.splitter)

        self.setCentralWidget( self.centralwidget )



    # create the 1st tab
    def create_tab1( self ):
        name = 'Properties'
        tab = QtGui.QWidget()

        return tab, name

    # create the 2nd tab
    def create_tab2( self ):
        name = 'Image'
        tab  =  QtGui.QWidget()

        return tab, name

    # create 3rd tab
    def create_tab3( self ):
        name = 'Stars'
        tab  =  QtGui.QWidget()

        return tab, name


    def load_file( self, filename ):
        print( 'Load file')

    def fileNew( self ):
        print( 'File new')
