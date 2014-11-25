try:
    from setuptools import setup
except ImportError:
    print 'Please install setuptools.'
    sys.exit(1)

setup(
    name='vmrun_wrapper',
    version='0.0.1',
    author='Matues Kern',
    author_email='kern@mateuskern.com',
    license='LICENSE.txt',
    packages=['vmrun_wrapper'],
    test_suite='vmrun_wrapper.tests'
)
