from setuptools import setup

setup(
  name='LocalHarvest',
  version='0.0.1',
  author='gabriel meringolo',
  author_email='gabriel.meringolo@gmail.com',
  packages=['local_harvest', 'local_harvest.test'],
  scripts=['bin/script1','bin/script2'],
  url='',
  license='LICENSE.txt',
  description='local harvest',
  long_description=open('README.txt').read(),
  install_requires=[
      "zipcode", "pytest", "requests",
  ],
)

