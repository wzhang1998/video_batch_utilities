@echo off
setlocal

REM Check if ffmpeg is in PATH
where ffmpeg >nul 2>&1
if %errorlevel% neq 0 (
    echo FFmpeg is not installed or not found in PATH.
    pause
    exit /b
)

REM Check if files were dragged and dropped
if "%~1"=="" (
    echo Please drag and drop one or more video files onto this script to convert them to Hap Q format.
    pause
    exit /b
)

REM Loop through all dragged files
:loop
if "%~1"=="" goto endloop

REM Get the input file path
set "inputFile=%~1"
echo Debug: inputFile=%inputFile%

REM Set the output file path
set "outputFile=%~dp1%~n1_hapq.mov"
echo Debug: outputFile=%outputFile%

REM Convert the file using FFmpeg with resizing and Hap Q format
echo Debug: Running ffmpeg -i "%inputFile%" -vf "scale='min(3840,iw)':'min(2160,ih)':force_original_aspect_ratio=decrease" -c:v hap -format hap_q "%outputFile%"
ffmpeg -i "%inputFile%" -vf "scale='min(3840,iw)':'min(2160,ih)':force_original_aspect_ratio=decrease" -c:v hap -format hap_q "%outputFile%"

REM Shift to the next file
shift
goto loop

:endloop
echo Conversion complete for all files.
pause