#
# Run tox via setup.py
#
from setuptools.command.test import test as TestCommand
from setuptools import setup
import sys
import os

class Tox(TestCommand):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]
    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)
        elif os.environ.get("TOX_ARGUMENTS"):
            args = shlex.split(os.environ.get("TOX_ARGUMENTS"))
        else:
            args = shlex.split('-e py27')
        errno = tox.cmdline(args=args)
        sys.exit(errno)


setup(
    #...,
    name='test-openshift',
    version='1.0',
    description='Simple package for testing openshift',
      author='Greg Ward',
    tests_require=['tox', 'nose'],
    cmdclass = {
        'test': Tox, 
        #'build': build
    },
    )

