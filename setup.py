from distutils.core import setup

setup(name='gordon-test',
      version='1.0',
      description='Blaa',
      author='Gordon Syme',
      py_modules=['hello.py'],
      test_suite = 'nose.collector'
     )
