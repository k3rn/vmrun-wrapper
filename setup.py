try:
    from setuptools import setup, find_packages
except ImportError:
    print 'Please install setuptools.'
    sys.exit(1)

setup(
    name='vmrun_wrapper',
    version='0.0.1',
    author='Matues Kern',
    author_email='kern@mateuskern.com',
    license='LICENSE.txt',
    packages=find_packages(),
    test_suite='vmrun_wrapper.tests'
)
