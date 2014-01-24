# sync.py
# 
# Run this script on your laptop and it will push changes to the web server.
# Immediately prior to running this script, you must do a Git/Subversion 
# commit and (in the case of Git) a push to the remote repository.

import subprocess

subprocess.call([
    'ssh',
    'my.domain.com',
    'python', 
    '/usr/local/www/mysite/sync_server.py'])
