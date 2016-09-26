# helper.py
#
# written by: Oliver Cordes 2016-09-26
# changed by: Oliver Cordes 2016-09-26


from ginga.qtw.QtHelp import QtGui, QtCore
from ginga.qtw.ImageViewCanvasQt import ImageViewCanvas


class MainWindow( QtGui.QMainWindow ):

    def __init__( self ):
        super( MainWindow, self).__init__()
        self.filename = None
        self.recentFiles = []

    def createAction( self, text, slot=None, shortcut=None, icon=None,
                    tip=None, checkable=False, signal='triggered()' ):
        action = QtGui.QAction( text, self )
        if icon is not None:
            action.setIcon( QtGui.QIcon( ':/%s.pngÄ' % icon ))
        if shortcut is not None:
            action.setShortcut( shortcut )
        if tip is not None:
            action.setToolTip( tip )
            action.setStatusTip( tip )
        if slot is not None:
            self.connect( action, QtCore.SIGNAL( signal ), slot )
        if checkable:
            action.setCheckable( True )

        return action


    def addActions( self, target, actions ):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction( action )

    def updateFileMenu( self ):
        self.fileMenu.clear()
        self.addActions( self.fileMenu, self.fileMenuActions[:-1] )
        current = QtCore.QString( self.filename ) \
                    if self.filename is not None else None
        recentFiles = []
        for fname in self.recentFiles:
            if fname != current and QtCore.QFile.exists( fname ):
                recentFiles.append( fname )
        if recentFiles:
            sef.fileMenu.addSeparator()
            for i, fname in enmerate( recentfiles ):
                action = QtGui.QAction( QIcon( ':/icon.png' ),
                           '&%d %s' % ( i +1, QtCore.QFileInfo( fname ).filename()), self)
                action.setData( QtGui.QVarian( fname ) )
                self.connect( action, QtCore.SIGNAL( 'triggered()' ), self.laodFile )
                self.fileMenu.addAction( action )
