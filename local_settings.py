# File: local_settings.py
# 
# This file should be imported by settings.py.

# This file will check what machine it is running on, then it will choose 
# the corresponding settings.

# Always use a trailing slash, both on OS directory paths and on URLs. This 
# is just a convention so that I can remember whether I need one.

# If I want a string to end with a \ character, I MUST use TWO \'s as the 
# end. To be consistent, I have chosen to NOT use raw strings 
# (e.g. r'\path\to\somewhere\\', which is correct and is interpreted as 
# having just one \ at the end) because using \ everywhere except the end, 
# where I must use \\, is weird. So I use non-raw strings, and use \\ 
# everywhere that I mean \.
# 
# To recap, if I want to say this:
#	\Users\zakf\medica_latest\
# These are my options:
#	r'\Users\zakf\medica_latest\\'		# Correct, oddly
#	r'\Users\zakf\medica_latest\'		# Incorrect, syntax error
#	r'\\Users\\zakf\\medica_latest\\'	# Incorrect, extra \'s
#	'\Users\zakf\medica_latest\'		# Incorrect, syntax error
#	'\\Users\\zakf\\medica_latest\\'	# Correct, USE THIS STYLE

from uuid import getnode

gotnode = getnode()

use_default = True

if gotnode == 207508019175032:
    # This is MBP 2013
    
    # No webserver
    # Mac OS X 10.9 Mavericks
    # Django 1.4.0 final
    # Python 2.7.5
        
    print "SETTINGS: gotnode matched %s" % gotnode
    print "SETTINGS: Using MBP 2013 local_settings.py"
    
    use_default = False
    
    root_dir = '/Users/zakf/progs/pts/'
    
    mysite_dir = root_dir + 'mysite/'
    
    database_name = root_dir + 'database/MBP_2011_amps.sqlite'
    database_engine = 'django.db.backends.sqlite3'
    database_user = ''
    database_password = ''
    database_host = ''  # Set to empty string for localhost.
    database_port = ''  # Set to empty string for default.
    
    template_dirs_pts = root_dir + 'mysite/pts/templates/'
    template_dirs_biseps = root_dir + 'mysite/biseps/templates/'
    template_dirs_templates = root_dir + 'templates/'
    
    staticfiles_dir = root_dir + 'static/'
    
    printer_installed = False
    
    ibutton_installed = False
    
    login_required = False
    
    backup_dir = '/Users/zakf/progs/pts_backups/'

#==============================================================================#

if gotnode == 26439108562915:
    # This is Dev185
    
    # No webserver
    # Windows 7 x64
    # Django 1.4.0 final
    # Python 2.7.2 32-bit
    
    print "SETTINGS: gotnode matched %s" % gotnode
    print "SETTINGS: Using Dev185 local_settings.py"
    
    use_default = False
    
    root_dir = 'C:\\Users\\zfallows\\pts\\'
    root_dj_dir = 'C:/Users/zfallows/pts/'
    
    mysite_dir = root_dir + 'mysite\\'
    mysite_dj_dir = root_dj_dir + 'mysite/'
    
    database_name = 'amps_database'
    database_engine = 'django.db.backends.mysql'
    database_user = 'database_user'
    database_password = 'secretsecretsecret'
    database_host = '192.168.5.210'
    database_port = '2000'
    
    # These need _dj_dirs with /, not _dirs with \\:
    template_dirs_pts = root_dj_dir + 'mysite/pts/templates/'
    template_dirs_biseps = root_dir + 'mysite/biseps/templates/'
    template_dirs_templates = root_dj_dir + 'templates/'
    
    staticfiles_dir = root_dj_dir + 'static/'
    
    printer_installed = True
    
    ibutton_installed = True
    
    login_required = False
    
    backup_dir = 'C:\\Users\\zfallows\\progs\\pts_backups\\'

#==============================================================================#

if use_default:
    # Put default settings here.
    pass
