# -*- mode: python -*-
a = Analysis(['Main.py'],
             pathex=['d:\\python\\Fixity Project'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Main.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True , icon='assets\\icon.ico')