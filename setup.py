import sys

from os.path import join
from setuptools import setup, Command


class PyTest(Command):
    """
    A command to convince setuptools to run pytests.
    """
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import pytest
        pytest.main("test.py")


dependencies = open('requirements.txt').read().split()

setup(
    name='weibowarc',
    version='0.1.1',
    url='https://github.com/gwu-libraries/weibowarc',
    author='Vict Tan',
    author_email='tanych5233@gmail.com',
    description="Archiving Weibo friendship timeline",
    platforms=['POSIX'],
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    py_modules=['weibowarc','weibowarchtml'],
    install_requires=dependencies,
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2.7',
        'Development Status :: 4 - Beta',
    ],
)
