#!/bin/bash
# 
# File: serve.sh
# 
# This file is helpful if you have multiple Django sites on the same machine.
# This file delivers two benefits:
# 
#   1. Run multiple sites at the same time.
# 
#   2. Firefox / Chrome / LastPass will CORRECTLY remember different passwords 
#      for each site this way. Otherwise all sites have the same URL.

echo ""
echo "PORT: 8003"
echo ""

python manage.py runserver 8003
