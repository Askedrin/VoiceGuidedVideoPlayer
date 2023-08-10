#!/bin/bash

# Add executable permissions to the script
chmod +x "$0"

# Install mpv package
sudo apt-get install mpv

# Install Python requirements from requirements.txt
pip install -r requirements.txt

