from numpy.distutils.core import setup
from pathlib import Path

scripts = [str(x) for x in Path('Scripts').iterdir() if x.is_file()]

setup(
    name='template',
    version='0.0.1',
    description='Software to do something',
    author='Full name',
    author_email='email@address.com',
    install_requires=['obspy'],
    python_requires='>=3.6',
    packages=['template'],
    scripts=scripts)
