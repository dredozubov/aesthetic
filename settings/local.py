#flake8: NOQA
try:
    from base import *
except ImportError, e:
    print 'Unable to load base.py:', e
