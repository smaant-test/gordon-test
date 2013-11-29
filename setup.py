from setuptools import setup

setup(name='gordon-test',
      version='1.0',
      description='Blaa',
      author='Gordon Syme',
      py_modules=['hello'],
      tests_require=['nose'],
      test_suite = 'nose.collector'
     )
