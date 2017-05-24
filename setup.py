#setup.py
from cx_Freeze import setup, Executable
setup(
    name = "ISCA",
    version = "1.0.0",
    options = {"build_exe": {
        'packages': ["win32service","win32serviceutil","win32event","servicemanager"],
        'include_msvcr': True,
    }},
    #executables = [Executable("servicos.py",base="Win32GUI")]
    )
