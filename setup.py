from setuptools import setup, find_packages
from extjs4 import version


setup(name = 'django_extjs4',
      description = 'Packages extjs as a Django app.',
      license='GPL',
      version = version,
      url = 'http://github.com/espenak/django_extjs4',
      author = 'Espen Angell Kristiansen',
      long_description=open('README.rst').read(),
      packages=find_packages(exclude=['ez_setup', 'fabfile']),
      install_requires = ['setuptools', 'Django'],
      include_package_data=True,
      zip_safe=False,
      classifiers=[
                   'Development Status :: 5 - Production/Stable',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python'
                  ]
     )
