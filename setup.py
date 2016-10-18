from distutils.core import setup
from distutils.core import Extension
MOD = "ext"
module = Extension(MOD, sources =["hello_ext.cpp"])
setup(name = MOD, ext_modules = [module])