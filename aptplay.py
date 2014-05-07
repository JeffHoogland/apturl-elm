import apt
import sys

pkg_name = "firefox"

cache = apt.cache.Cache()
#cache.update()

pkg = cache[pkg_name]
print pkg.versions[0].description
