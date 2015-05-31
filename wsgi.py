# coding: utf-8
"""
WSGI config for avoscloud_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os
import leancloud
from wsgiref import simple_server
from django.core.wsgi import get_wsgi_application

APP_ID = os.environ['LC_APP_ID']
MASTER_KEY = os.environ['LC_APP_MASTER_KEY']
PORT = int(os.environ['LC_APP_PORT'])

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "avoscloud_django.settings")

leancloud.init(APP_ID, master_key=MASTER_KEY)
application = get_wsgi_application()

if __name__ == '__main__':
    # 只在本地开发环境执行的代码
    server = simple_server.make_server('0.0.0.0', PORT, application)
    server.serve_forever()