import os
import os.path
import subprocess
from distutils.core import setup

setup(
    name='gpmf',
    version='0.7.0',
    author='Eero "rambo" af Heurlin',
    author_email='rambo@iki.fi',
    packages=['gpmf', ],
    license='MIT',
    long_description=open('README.md').read(),
    description='GoPro Metadata Format parser',
    #install_requires=open(os.path.join(os.path.dirname(__file__), 'requirements.txt'), 'rt').readlines(),
    install_requires=['construct<3.0.0', 'python-dateutil<2.9.0', 'hachoir<4.0.0'],
    url='https://github.com/rambo/python-gpmf',
)
