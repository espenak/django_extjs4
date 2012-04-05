Django Extjs4
=============


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


Usage
-----

You can refer to extjs4 in your template with::

    {% static "/extjs4/ext-all-dev.js %}
