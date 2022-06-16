from .base import *

try:
    from ecommerce2.settings.local import *
except Exception:
    pass

DEBUG = False
ALLOWED_HOSTS = [
    'test.com',
    'www.test.com',
]