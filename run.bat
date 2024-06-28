@echo off

REM Check if .firstrun file exists
if not exist .firstrun (
    echo First time setup: Installing dependencies...

    REM Install Python dependencies
    pip install -r requirements.txt

    REM Install Playwright with Chromium
    playwright install --with-deps chromium

    REM Create .firstrun file to mark setup completion
    type nul > .firstrun

    REM Run tests using pytest
    pytest -s app.py
    
) else (
    echo Running tests...

    REM Run tests using pytest
    pytest -s app.py
)