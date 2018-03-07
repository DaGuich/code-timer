try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.md', 'r') as f:
    long_description = f.read()


setup(
    name='code-timer',
    version='1.0',
    description='measure elapsed time and count pass in code paths',
    long_description=long_description,
    author='', # Your name here
    author_email='', # Your e-mail address here
    url='https://github.com/gulaki/code-timer',
    packages=['code_timer']
)
