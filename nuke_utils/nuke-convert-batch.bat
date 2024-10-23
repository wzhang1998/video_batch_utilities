@echo off
setlocal enabledelayedexpansion

:: Set exact Nuke path
set "NUKE_PATH=C:\Program Files\Nuke15.1v3"
set "NUKE_EXE=Nuke15.1.exe"

:: Check if Nuke exists
if not exist "%NUKE_PATH%\%NUKE_EXE%" (
    echo Error: Could not find Nuke 15.1 installation
    echo Expected path: %NUKE_PATH%\%NUKE_EXE%
    pause
    exit /b 1
)

:: Create a simple batch file named 'nuke.bat' in Windows system directory
set "ALIAS_PATH=%SystemRoot%\System32\nuke.bat"
(
    echo @echo off
    echo "%NUKE_PATH%\%NUKE_EXE%" %%*
) > "%ALIAS_PATH%"

:: Set NUKE_PATH
setx NUKE_PATH "%USERPROFILE%\.nuke"

:: Create .nuke directory if it doesn't exist
if not exist "%USERPROFILE%\.nuke" mkdir "%USERPROFILE%\.nuke"

echo Nuke 15.1 environment setup complete:
echo.

:: Check if script exists in .nuke folder
set "SCRIPT_PATH=%USERPROFILE%\.nuke\nuke-exr-to-png.py"
if not exist "%SCRIPT_PATH%" (
    echo Error: Could not find nuke-exr-to-png.py in %USERPROFILE%\.nuke
    echo Please make sure the script is installed correctly
    pause
    exit /b 1
)

:: If no arguments provided, show usage
if "%~1"=="" (
    echo Usage: convert_exr.bat path\to\sequence.####.exr
    echo Example: convert_exr.bat D:\renders\shot_001\beauty.####.exr
    pause
    exit /b 1
)

echo Using Nuke: %NUKE_PATH%\%NUKE_EXE%
echo Converting sequence: %1
echo.

"%NUKE_PATH%\%NUKE_EXE%" -t "%SCRIPT_PATH%" "%~1"

if errorlevel 1 (
    echo.
    echo Conversion failed
    pause
    exit /b 1
) else (
    echo.
    echo Conversion completed successfully
    pause
)
