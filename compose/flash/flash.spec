# -*- mode: python -*-
a = Analysis([os.path.join(HOMEPATH,'support\\_mountzlib.py'), os.path.join(HOMEPATH,'support\\useUnicode.py'), 'D:\\pro\\net_study\\net_bag\\compose\\flash\\flash.pyw'],
             pathex=['D:\\pro\\python\\pyinstaller'])
pyz = PYZ(a.pure)
exe = EXE( pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'flash.exe'),
          debug=False,
          strip=False,
          upx=True,
          console=True )
