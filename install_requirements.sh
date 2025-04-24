#!/bin/bash

echo "🔧 Installing system dependencies..."
sudo apt update
sudo apt install -y build-essential ruby-full git iproute2

echo "💎 Installing Ceedling (Ruby-based test framework)..."
sudo gem install ceedling

echo "🌐 Setting up virtual CAN interface..."
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0
echo "✅ vcan0 ready for use"


echo "✅ All tools installed!"
