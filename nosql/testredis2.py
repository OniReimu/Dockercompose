#!/usr/bin/python

import os
from django.conf import settings
from django.core.cache import cache

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

#read cache user id
cache.get('get_user_id_bugall');

#write cache user id
cache.set('get_user_id_bugall',123,settings.NEVER_REDIS_TIMEOUT)


##On redis server

#redis-cli keys ¡®*¡¯ #Check all current avaliable keys
