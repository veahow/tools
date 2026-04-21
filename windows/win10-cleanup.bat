@echo off
title Windows 10 System Cleanup Tool
color 0A

echo ========================================
echo     Windows 10 System Cleanup Tool
echo ========================================
echo.
echo Cleaning system junk files, please wait...
echo.

:: Clean user temp folder
echo [1/8] Cleaning user temp files...
del /f /s /q "%TEMP%\*.*" >nul 2>&1
rd /s /q "%TEMP%" >nul 2>&1

echo [2/8] Cleaning system temp files...
del /f /s /q "%SystemRoot%\Temp\*.*" >nul 2>&1
rd /s /q "%SystemRoot%\Temp" >nul 2>&1
md "%SystemRoot%\Temp" >nul 2>&1

:: Clean prefetch files
echo [3/8] Cleaning prefetch files...
del /f /s /q "%SystemRoot%\Prefetch\*.*" >nul 2>&1

:: Clean recent documents (preserve pinned items in AutomaticDestinations and CustomDestinations)
echo [4/8] Cleaning recent documents...
del /f /q "%APPDATA%\Microsoft\Windows\Recent\*.lnk" >nul 2>&1

:: Clean recycle bin
echo [5/8] Cleaning recycle bin...
PowerShell -Command "Clear-RecycleBin -Force -ErrorAction SilentlyContinue"

:: Clean Windows update cache
echo [6/8] Cleaning Windows update cache...
del /f /s /q "%SystemRoot%\SoftwareDistribution\Download\*.*" >nul 2>&1

:: Clean log files
echo [7/8] Cleaning system log files...
del /f /s /q "%SystemRoot%\Logs\*.*" >nul 2>&1

:: Clean thumbnail cache (only thumbcache, preserve iconcache for taskbar)
echo [8/8] Cleaning thumbnail cache...
del /f /q "%LOCALAPPDATA%\Microsoft\Windows\Explorer\thumbcache_*.db" >nul 2>&1

echo.
echo ========================================
echo     Cleanup Complete!
echo ========================================
echo.
pause
