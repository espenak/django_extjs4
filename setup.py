from os.path import join, dirname
from setuptools import setup, find_packages
from os import walk, chdir, getcwd

this_dir = dirname(__file__)

try:
    f = open(join(this_dir, 'README.rst'))
    long_description = f.read().strip()
    f.close()
except IOError:
    long_description = None


def _find_all_files(root, subdir):
    all_filenames = []
    cwd = getcwd()
    chdir(root)
    for dirpath, dirnames, filenames in walk(subdir):
        for filename in filenames:
            all_filenames.append(join(dirpath, filename))
    chdir(cwd)
    return all_filenames

def find_all_files(root, *subdirs):
    all_filenames = []
    for subdir in subdirs:
        all_filenames += _find_all_files(root, subdir)
    return all_filenames




setup(name = 'django_extjs4',
      description = 'Packages extjs as a Django app.',
      license='GPL',
      version = '1.0',
      url = 'http://github.com/espenak/django_extjs4',
      author = 'Espen Angell Kristiansen',
      long_description=long_description,
      packages=find_packages(exclude=['ez_setup']),
      install_requires = ['setuptools', 'Django'],
      package_data = {'extjs4': find_all_files(join(this_dir, 'extjs4'), 'static')},
      zip_safe=False,
      classifiers=[
                   'Development Status :: 5 - Production/Stable',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python'
                  ],
     )
