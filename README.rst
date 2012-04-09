#############
Django Extjs4
#############

ExtJS version
=============

The current version of ExtJS distributed with this app is **4.0.7**.


Requirements
============

`Django <https://www.djangoproject.com/>`_ 1.3 or later


Installation
============

::

    $ pip install django_extjs4


Setup
=====

Just add ``'django.contrib.staticfiles'`` and ``'django_extjs4'`` to
INSTALLED_APPS in your settings.py::

    INSTALLED_APPS = (
        # ...

        'django.contrib.staticfiles',
        'extjs4',

        # ...
    )

Refer to Django `static files <https://docs.djangoproject.com/en/dev/howto/static-files/>`_
documentation to configure and deploy static files.


What parts of ExtJS is included?
================================

The ExtJS sources, except for the ``examples/`` and ``docs/`` directories is
included in ``extjs4/static/extjs4/``.


Usage
=====

See `django_extjs4_examples`_.


.. _`django_extjs4_examples`: https://github.com/espenak/django_extjs4_examples
