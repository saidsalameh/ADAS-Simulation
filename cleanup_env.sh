#!/bin/bash

if [ -d "venv" ]; then
  echo " Removing virtual environment..."
  rm -rf venv
  echo " Virtual environment removed."
else
  echo " No virtual environment found."
fi
