@echo off
setlocal

REM Prompt for source and target directories with more detailed explanations
set /p source="Enter the source directory (the directory containing the files you want to copy): "
set /p target="Enter the target directory (the directory where you want the files to be copied to): "

REM Get the latest modified file in the source directory
forfiles /p "%source%" /s /m *.* /c "cmd /c if @isdir==FALSE echo @fdate @ftime @path" /d -1 /o:d /c "cmd /c echo @path" > latest_source.txt
set /p latest_source=<latest_source.txt

REM Get the latest modified file in the target directory
forfiles /p "%target%" /s /m *.* /c "cmd /c if @isdir==FALSE echo @fdate @ftime @path" /d -1 /o:d /c "cmd /c echo @path" > latest_target.txt
set /p latest_target=<latest_target.txt

REM Get the last modified dates of the latest files
for %%I in ("%latest_source%") do set source_date=%%~tI
for %%I in ("%latest_target%") do set target_date=%%~tI

REM Compare the dates
if "%source_date%" GTR "%target_date%" (
    echo Source is newer. Performing robocopy...
    robocopy "%source%" "%target%" /MIR /Z /R:5 /W:5
    if %errorlevel% leq 1 (
        echo Robocopy completed successfully.
    ) else (
        echo Robocopy encountered errors. Exit code: %errorlevel%
    )
) else (
    echo Target is up to date or newer.
    set /p proceed="Do you still want to copy the files? (y/n): "
    if /i "%proceed%"=="y" (
        robocopy "%source%" "%target%" /MIR /Z /R:5 /W:5
        if %errorlevel% leq 1 (
            echo Robocopy completed successfully.
        ) else (
            echo Robocopy encountered errors. Exit code: %errorlevel%
        )
    ) else (
        echo Copy operation aborted by user.
    )
)

endlocal
pause

