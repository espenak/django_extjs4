Django Extjs4
=============

ExtJS version
=============

The current version of ExtJS distributed with this app is **4.0.7**.


Requirements
------------

`Django <https://www.djangoproject.com/>`_ 1.3 or later


Installation
------------

::

    $ pip install django_extjs4


Setup
-----

Just add ``'django.contrib.staticfiles'`` and ``'django_extjs4'`` to
INSTALLED_APPS in your settings.py::

    INSTALLED_APPS = (
        # ...

        'django.contrib.staticfiles',
        'django_extjs4',

        # ...
    )

Refer to Django `static files <https://docs.djangoproject.com/en/dev/howto/static-files/>`_
documentation to configure and deploy static files.


What parts of ExtJS is included?
--------------------------------

The ExtJS sources, except for the ``examples/`` and ``docs/`` directories.


Usage
-----

You can refer to extjs4 in your template with::

    {% static "/extjs4/ext-all-dev.js %}
