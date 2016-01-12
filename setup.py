from setuptools import setup

setup(
    name='weibowarc',
    version='0.1.0',
    url='https://github.com/gwu-libraries/weibowarc',
    author='Vict Tan',
    author_email='tanych5233@gmail.com',
    description="Archiving Weibo friendship timeline",
    platforms=['POSIX'],
    py_modules=['weibowarc','weibowarchtml'],
    install_requires=['weibo>=0.2.2', 'beautifulsoup4'],
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2.7',
        'Development Status :: 4 - Beta',
    ],
)