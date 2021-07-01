# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['002-b-pesquisa_aluno_gemul.py'],
             pathex=['C:\\Users\\diego\\OneDrive\\Desktop\\DESKTOP\\DATA_SCIENCE\\PYTHON\\BOT_CENSO_2021\\002-b-pesquisa_aluno_gemul'],
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
          name='002-b-pesquisa_aluno_gemul',
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
               name='002-b-pesquisa_aluno_gemul')
