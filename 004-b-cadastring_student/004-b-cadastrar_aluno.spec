# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['004-b-cadastrar_aluno.py'],
             pathex=['C:\\Users\\diego\\OneDrive\\Desktop\\DESKTOP\\DATA_SCIENCE\\PYTHON\\BOT_CENSO_2021\\004-b-cadastring_student'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='004-b-cadastrar_aluno',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='004-b-cadastrar_aluno')