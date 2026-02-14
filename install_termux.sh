#!/bin/bash

# Script to install the Thanatos framework on Termux

# Update packages
pkg update -y
pkg upgrade -y

# Install required packages
pkg install git -y
pkg install python -y
pkg install pip -y

# Clone the Thanatos repository
git clone https://github.com/Vaenomynous/Thanatos.git

# Navigate to the Thanatos directory
cd Thanatos

# Install required Python packages
pip install -r requirements.txt

echo "Thanatos framework installed successfully!"