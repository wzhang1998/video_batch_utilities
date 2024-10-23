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
    echo "C:\Program Files\Nuke15.1v3\Nuke15.1.exe" %%*
) > "%ALIAS_PATH%"

:: Set NUKE_PATH
setx NUKE_PATH "%USERPROFILE%\.nuke"

:: Create .nuke directory if it doesn't exist
if not exist "%USERPROFILE%\.nuke" mkdir "%USERPROFILE%\.nuke"

echo Nuke 15.1 environment setup complete:
echo.
echo Installation: %NUKE_PATH%\%NUKE_EXE%
echo Created alias: typing 'nuke' will now run Nuke 15.1
echo NUKE_PATH set to: %USERPROFILE%\.nuke
echo.
echo Please restart your command prompt for changes to take effect.
pause