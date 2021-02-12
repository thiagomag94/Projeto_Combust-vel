from cx_Freeze import setup, Executable
    
base = None    

executables = [Executable("primeiro_teste.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "sPyce Travel",
    options = options,
    version = '1.0',
    description = 'Qualquer coisa',
    executables = executables
)