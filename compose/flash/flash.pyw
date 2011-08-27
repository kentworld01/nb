#!/usr/bin/env python


import sip
import os
import sys
import signal

import ctypes
from ctypes import wintypes
import win32con

from PyQt4 import QtCore, QtGui
from PyQt4 import QAxContainer
from PyQt4.QAxContainer import QAxWidget



def sigint_handler(signum,frame):  
	print 'eeexxeexx'  
	#s.close()  
	print 'close'  
	sys.exit()  



try:
    from PyQt4.phonon import Phonon
except ImportError:
    app = QtGui.QApplication(sys.argv)
    QtGui.QMessageBox.critical(None, "Music Player",
            "Your Qt installation does not have Phonon support.",
            QtGui.QMessageBox.Ok | QtGui.QMessageBox.Default,
            QtGui.QMessageBox.NoButton)
    sys.exit(1)


class Flash( QAxWidget ):
    def translateKeyEvent( self, msg, key ):
        print "----------"
        print msg
        print key
        if( msg == 256 and key == 27 ):
            sys.exit(0)
        return True


if __name__ == '__main__':
    if len( sys.argv ) <= 1 :
        print "usage: flash.exe flash_file"
        exit(0)
    file = sys.argv[1]
    app = QtGui.QApplication(sys.argv)
    flash = Flash()
    flash.resize( 800,600 )
    flash.setControl( (u'{d27cdb6e-ae6d-11cf-96b8-444553540000}') );
    #file_name = os.getcwd() + "\look.swf"
    file_name = u'' + os.getcwd() + "\\" + file.decode( 'gbk' )
    #file_name = file
    print file_name
    flash.dynamicCall("LoadMovie(long,string)",0, file_name );
    #flash.dynamicCall("LoadMovie(long,string)",0, file_name.encode('unicode') );
    flash.showFullScreen();
    #flash.show();

    signal.signal(signal.SIGINT,sigint_handler) 
    sys.exit(app.exec_())








