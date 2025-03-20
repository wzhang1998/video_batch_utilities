@echo off
setlocal EnableDelayedExpansion

REM Check if ffmpeg is in PATH
where ffmpeg >nul 2>&1
if %errorlevel% neq 0 (
    echo FFmpeg is not installed or not found in PATH.
    pause
    exit /b
)

REM Check if files were dragged and dropped
if "%~1"=="" (
    echo Please drag and drop one or more video files onto this script to convert them.
    pause
    exit /b
)

REM Ask user for conversion type
set /p conversionType="Enter conversion type (1 for Any Video to Hap Q, 2 for Any Video to MP4): "

REM Loop through all dragged files
:loop
if "%~1"=="" goto endloop

REM Get the input file path and components
set "inputFile=%~1"
set "inputDir=%~dp1"
set "inputName=%~n1"
set "inputExt=%~x1"

echo Processing: "!inputFile!"

if "%conversionType%"=="1" (
    REM Set the output file path for conversion to Hap Q
    set "outputFile=!inputDir!!inputName!_hapq.mov"
    echo Output will be saved to: "!outputFile!"
    
    REM Convert the file using FFmpeg with proper timescale for QuickTime
    ffmpeg -i "!inputFile!" -vf "scale=iw-mod(iw\,4):ih-mod(ih\,4)" -c:v hap -format hap_alpha -video_track_timescale 60000 -f mov "!outputFile!"
    
    if !errorlevel! neq 0 (
        echo Error during conversion.
        pause
    )
) else if "%conversionType%"=="2" (
    REM Set the output file path for MP4
    set "outputFile=!inputDir!!inputName!.mp4"
    echo Output will be saved to: "!outputFile!"
    
    REM Convert any video format to MP4 (H.264)
    ffmpeg -i "!inputFile!" -vf "scale=iw-mod(iw\,4):ih-mod(ih\,4)" -c:v libx264 -preset medium -crf 23 -pix_fmt yuv420p "!outputFile!"
    
    if !errorlevel! neq 0 (
        echo Error during conversion.
        pause
    )
) else (
    echo Invalid conversion type.
    pause
    exit /b
)

shift
goto loop

:endloop
echo Conversion complete for all files.
pause