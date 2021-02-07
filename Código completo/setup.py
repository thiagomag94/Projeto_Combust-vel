from cx_Freeze import setup, Executable

setup(
    name="test_sqlite3",
    version="0.3",
    description="cx_Freeze script to test sqlite3",
    executables=[Executable("Sistema_combustível.py")],
    options={
        "build_exe": {
            "excludes": ["tkinter"],
            "replace_paths": [("*", "")],
            "zip_include_packages": ["*"],
            "zip_exclude_packages": [],
        }
    },
)
