"""Utilities for make the code run both on Python2 and Python3.
"""
import sys

PY2 = sys.version_info[0] == 2

# urllib renames
if PY2:
    from urlparse import urljoin
    from urllib import splitquery, urlencode, unquote, quote
else:
    from urllib.parse import urljoin, splitquery, urlencode, unquote, quote as urlquote

# Dictionary iteration
if PY2:
    iterkeys = lambda d: d.iterkeys()
    itervalues = lambda d: d.itervalues()
    iteritems = lambda d: d.iteritems()
else:
    iterkeys = lambda d: iter(d.keys())
    itervalues = lambda d: iter(d.values())
    iteritems = lambda d: iter(d.items())

# Iter iteration
def iternext(iter):
    if PY2:
        return iter.next()
    else:
        return iter.__next__()

# string and text types
if PY2:
    text_type = unicode
    string_types = (str, unicode)
else:
    text_type = str
    string_types = (str,)

# imap
if PY2:
	from itertools import imap
else:
	imap = map
