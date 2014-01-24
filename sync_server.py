#!/usr/bin/python
# 
# sync_server.py
# 
# This script runs on the web server. This script is triggered by sync.py. 
# Remember that sync.py is run on your laptop (development machine).
# 
# In order to work with the example sync.py, this file must be located here:
# /usr/local/www/mysite/sync_server.py
# 
# NOTE: You will need to add '/etc/init.d/apache2 reload' to the sudoers file.

import subprocess
import datetime
import shutil

SITE_DIR = '/usr/local/www/mysite/'

STATIC_DIR = '/usr/local/www/documents/static'


# Pull the latest version from Subversion:

subprocess.call(['svn', 'update', '.'], cwd=SITE_DIR)


# Copy the 'static' dir into place:

# Aside: Why are we copying the static directory from one place to another?
# I like to keep the static files inside version control, and I use version 
# control to sync the static files. However, I like to have the static files 
# in a different directory on the actual web server. Sometimes, the static 
# files may be on a totally different server, such as Amazon.

shutil.rmtree(STATIC_DIR)
print "Deleted old static dir, %s." % STATIC_DIR

shutil.copytree(SITE_DIR + 'static', STATIC_DIR)
print "Copied in new static dir."


# Reload Apache:

subprocess.call(['sudo', '/etc/init.d/apache2', 'reload'])
