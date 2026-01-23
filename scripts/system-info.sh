#!/usr/bin/env bash
set -euo pipefail

echo "Host: $(hostname)"
echo "User: $(whoami)"
echo "Uptime: $(uptime -p)"
echo "Kernel: $(uname -r)"
echo "Disk:"
df -h /
echo "Memory:"
free -h
