#!/bin/bash

echo " Creating virtual environment..."
python3 -m venv venv

echo " Activating environment and installing dependencies..."
source venv/bin/activate
pip install --upgrade pip
pip install pygame

echo " Dependencies installed."
echo " Starting the simulation..."
python python_sim/main.py
