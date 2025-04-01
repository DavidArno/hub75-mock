from distutils.core import setup

setup(
    name='hub75_mock',
    version='0.4.0',
    packages = [ 'mocking_support' ],
    py_modules = [ 'hub75' ],
    install_requires = [ 'pypng' ]
)