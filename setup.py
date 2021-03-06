from distutils.core import setup

setup(
    name='GroupMeScoreTracker',
    version='0.1b',
    url='#',
    author='Matthew Doto',
    author_email='matt@mattdoto.com',
    packages=['scoretracker'],
    license='LICENSE.txt',
    description='A score tracker for GroupMe, allowing competition between friends',
    long_description=open('README.rst').read(),
    install_requires=open('requirements.txt').readlines()
)
