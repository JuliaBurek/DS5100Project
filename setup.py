from setuptools import setup, find_packages

setup(
    name='MonteCarloPackage',
    version='1.0.0',
    url='https://github.com/JuliaBurek/DS5100Project',
    author='Julia Burek',
    author_email='jeb5pb@virginia.edu',
    description='Monte Carlo Simulator Package',
    packages=find_packages(),
    install_requires=['numpy >= 1.11.1', 'matplotlib >= 1.5.1'],
)