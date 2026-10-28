@echo off
setlocal
cd /d "%~dp0"
echo ========================================
echo   Smart Resume Matcher - Setup and Run
echo ========================================
echo.
where py >nul 2>nul
if %errorlevel%==0 (
  set "PY=py"
) else (
  set "PY=python"
)
echo Installing required packages...
%PY% -m pip install -r requirements.txt
if errorlevel 1 (
  echo.
  echo Package installation failed. Check your internet connection and Python installation.
  pause
  exit /b 1
)
echo.
echo Starting Smart Resume Matcher in your browser...
%PY% -m streamlit run app.py
if errorlevel 1 (
  echo.
  echo The app could not start. Copy the error above for troubleshooting.
  pause
  exit /b 1
)
endlocal
