from os.path import join, dirname
from setuptools import setup, find_packages


try:
    f = open(join(dirname(__file__), 'README.rst'))
    long_description = f.read().strip()
    f.close()
except IOError:
    long_description = None

setup(name = 'django_extjs4',
      description = 'Packages extjs as a Django app.',
      licence='GPL',
      version = '1.0',
      url = 'http://github.com/espenak/django_extjs4',
      author = 'Espen Angell Kristiansen',
      long_description=long_description,
      packages=find_packages(exclude=['ez_setup']),
      install_requires = ['setuptools', 'Django'],
      classifiers=[
                   'Development Status :: 5 - Production/Stable',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: GPL',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python'
                  ],
      )
)
