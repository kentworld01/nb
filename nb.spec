# -*- mode: python -*-
hiddenimports = ["sip", "PySide.QtCore", "PySide.QtGui", "PySide.QtNetwork", "PySide.QtWebKit", "PySide._qt"]

a = Analysis([os.path.join(HOMEPATH,'support\\_mountzlib.py'), os.path.join(HOMEPATH,'support\\useUnicode.py'), 'd:\\pro\\net_study\\net_bag\\nb.pyw'],
             pathex=['D:\\pro\\python\\pyinstaller'])
pyz = PYZ(a.pure)
exe = EXE( pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'nb.exe'),
          debug=False,
          strip=False,
          upx=True,
          console=False )
