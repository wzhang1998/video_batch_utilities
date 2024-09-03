@echo off
setlocal enabledelayedexpansion

REM Get the current date in YYYYMMDD format
for /f "tokens=2 delims==" %%i in ('"wmic os get localdatetime /value"') do set datetime=%%i
set date=%datetime:~0,8%

:loop
REM Get the input file path
set "inputFile=%~1"
if "%inputFile%"=="" goto endloop
echo Processing file: "%inputFile%"

REM Set the output file path with date
set "outputFile=%date%_%~dp1%~n1_hapq.mov"
echo Output file will be: "%outputFile%"

REM Get the video width
for /f "tokens=5 delims==_" %%i in ('ffprobe -v error -of flat^=s^=_ -select_streams v:0 -show_entries stream^=width "%inputFile%"') do set width=%%i
echo Width: %width%

REM Get the video height
for /f "tokens=5 delims==_" %%i in ('ffprobe -v error -of flat^=s^=_ -select_streams v:0 -show_entries stream^=height "%inputFile%"') do set height=%%i
echo Height: %height%

echo Original dimensions: %width%x%height%

REM Check if dimensions are multiples of 4 and adjust if necessary
set /a remainderWidth=width %% 4
set /a remainderHeight=height %% 4

if %remainderWidth% neq 0 (
    set /a newWidth=width + 4 - remainderWidth
) else (
    set /a newWidth=width
)

if %remainderHeight% neq 0 (
    set /a newHeight=height + 4 - remainderHeight
) else (
    set /a newHeight=height
)

echo Adjusted dimensions: %newWidth%x%newHeight%

REM Check if newWidth and newHeight are set correctly
if "%newWidth%"=="0" (
    echo Error: newWidth is not set correctly.
    pause
    goto endloop
)
if "%newHeight%"=="0" (
    echo Error: newHeight is not set correctly.
    pause
    goto endloop
)

REM Convert the file using FFmpeg with debug log level
ffmpeg -loglevel debug -i "%inputFile%" -vf "scale=%newWidth%:%newHeight%" -c:v hap -format hap_q "%outputFile%"
if %errorlevel% neq 0 (
    echo An error occurred during the conversion of "%inputFile%".
    pause
)

shift
goto loop

:endloop
echo Conversion complete for all files.
pause