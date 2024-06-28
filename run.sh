#!/bin/bash

# Check if .firstrun file exists
if [ ! -f .firstrun ]; then
    echo "First time setup: Installing dependencies..."

    # Install Python dependencies
    pip install -r requirements.txt

    # Install Playwright with Chromium
    playwright install --with-deps chromium

    # Create .firstrun file to mark setup completion
    touch .firstrun

    # Run tests using pytest
    pytest -s app.py
else
    echo "Running tests..."

    # Run tests using pytest
    pytest -s app.py
fi