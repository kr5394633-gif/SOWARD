# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['launcher.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('dashboard/build', 'dashboard/build'),
        ('.env', '.'),
    ],
    hiddenimports=[
        'discord',
        'discord.ext',
        'discord.ext.commands',
        'discord.http',
        'fastapi',
        'uvicorn',
        'asyncpg',
        'wavelink',
        'chat_exporter',
        'cogs',
        'core',
        'databases',
        'connections',
        'services',
        'functions',
        'modules',
        'api',
    ],
    hookspath=['pyinstaller_hooks'],
    runtime_hooks=[],
    excludedimports=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='SowardBot',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
