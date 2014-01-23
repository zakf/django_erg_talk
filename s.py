# File: s.py
# 
# The filename 's' is short for 'setup'. The filename is extra short because it 
# must frequently be typed by hand.
# 
# This file belongs in the same directory as manage.py, in a Django project.
# 
# This file should be used every time you use 'manage.py shell', and it should 
# be used in the following way:
# 
# sh> python manage.py shell
# 
# py> execfile('s.py')
# 
# Done.

import datetime
import decimal
D = decimal.Decimal
# What else do you commonly use? re? sys?

import format_text as ft

from mysite.myapp.models import *
from mysite.myapp.views import *
from mysite.otherapp.models import *
from mysite.otherapp.views import *

print "Imported format_text as ft"
print "Imported decimal.Decimal as D"
print "Imported other stuff"
print "Done with s.py, the environment is set up."
