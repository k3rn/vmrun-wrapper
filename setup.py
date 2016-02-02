try:
    from setuptools import setup, find_packages
except ImportError:
    print 'Please install setuptools.'
    sys.exit(1)

setup(
    name='vmrun_wrapper',
    description='a wrapper for the VMWare Fusion\'s vmrun utility.',
    version='1.0',
    author='Mateus Kern',
    author_email='kern@mateuskern.com',
    url='https://github.com/k3rn/vmrun-wrapper',
    license='MIT',
    test_suite='vmrun_wrapper.tests',
    packages=find_packages(exclude='tests'),
)
