######################################
Extjs4 sources bundled as a Django app
######################################

ExtJS version
=============

The current version of ExtJS distributed with this app is **4.0.7**.

Issues/contribute
=================

Report any issues at the `github project page <django_extjs4>`_, and feel free
to add your own guides/experiences to the wiki, and to contribute changes using
pull requests.


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


Template context
================

The ``extjs4.context_processors.extjs4`` template context adds exports the
``EXTJS4_DEBUG`` attribute from ``settings.py`` to your Django templates.  This
is useful if you want to be able to test your production ExtJS app on the
Django test server, since setting ``DEBUG`` to ``True`` disables
``staticfiles``. If you add the template context, but do not set
``EXTJS4_DEBUG`` in ``settings.py``, it defaults to ``False``.


A generic view
==============

See ``generic_extjs4_app`` in `django_extjs4_examples`_ for how-to use ``extjs4.views.Extjs4AppView``.


What parts of ExtJS is included?
================================

The ExtJS sources, except for the ``examples/`` and ``docs/`` directories is
included in ``extjs4/static/extjs4/``.


Usage
=====

See `django_extjs4_examples`_.


.. _`django_extjs4_examples`: https://github.com/espenak/django_extjs4_examples
.. _`django_extjs4`: https://github.com/espenak/django_extjs4
