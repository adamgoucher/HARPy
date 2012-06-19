import os, sys
try:
    from setuptools import setup
except ImportError:
    from distribute_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

setup(
    name='HARPy',
    description='HARPy: a simple library for interrogating an HTTP Archive (HAR) file',
    version='0.1.0',
    url='https://github.com/adamgoucher/HARPy',
    license='LICENSE.txt',
    platforms=['unix', 'linux', 'osx', 'cygwin', 'win32'],
    author='Adam Goucher',
    author_email='adam@element34.ca',
    classifiers=['Development Status :: 4 - Beta',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: Apache Software License',
                 'Operating System :: POSIX',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: MacOS :: MacOS X',
                 'Topic :: Software Development :: Testing',
                 'Topic :: Software Development :: Libraries',
                 'Topic :: Utilities',
                 'Programming Language :: Python'],
    packages=['harpy'],
    py_modules=['harpy'],
    zip_safe=False,
)   