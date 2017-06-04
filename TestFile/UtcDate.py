# -*- coding: utf-8 -*- 
__author__ = 'Peng'

from dateutil import tz
from dateutil.tz import tzlocal
from datetime import datetime

# get local time zone name
print datetime.now(tzlocal()).tzname()

# UTC Zone
from_zone = tz.gettz('UTC')
# China Zone
to_zone = tz.gettz('CST')

utc = datetime.utcnow()

# Tell the datetime object that it's in UTC time zone
utc = utc.replace(tzinfo=from_zone)

# Convert time zone
local = utc.astimezone(to_zone)
print datetime.strftime(local, "%Y-%m-%d %H:%M:%S")