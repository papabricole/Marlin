from os import makedirs
from os.path import isdir, join
Import('env')

# bugfix for Weak symbols (https://github.com/platformio/platformio-core/issues/2070)
# Surround the library archives with linker --whole-archive/--no-whole-archive pair
libString = env.subst("$_LIBFLAGS") # something like "-Wl,--start-group .pioenvs/foo/libFrameworkArduinoVariant.a .pioenvs/foo/libFrameworkArduino.a -larm_cortexM7l_math -lc -lm -lgcc -lstdc++ -lc -Wl,--end-group"
tokens = libString.lstrip(' ').rstrip(' ').split()
archives = [t for t in tokens if t.endswith(".a")]		# find the archives
tokens = [t for t in tokens if t not in archives]			# remove the archives from the orignal set
#rebuild a new string with --whole-archive option pair surrounding the archives
newLibString = ' '.join([tokens[0] , "-Wl,--whole-archive"] + archives + ["-Wl,--no-whole-archive"] +tokens[1:])
env.Replace(
  _LIBFLAGS=newLibString,
  LINKCOM='$LINK -o $TARGET $LINKFLAGS $__RPATH $SOURCES $_LIBDIRFLAGS $_LIBFLAGS'
)