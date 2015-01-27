#A file for testing the python apt module

import apt
import sys

pkg_name = "firefx"

cache = apt.cache.Cache()
#cache.update()

if pkg_name in cache:
	pkg = cache[pkg_name]
	print pkg.versions[0].description
else:
	print "Package %s not found"%pkg_name
