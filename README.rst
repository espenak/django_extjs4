######################################
Extjs4 sources bundled as a Django app
######################################

Versions
=============

- ``1.0.5``: ExtJS 4.0.7
- ``1.1.0_extjs4.1.1``: ExtJS 4.1.1 (from this version on, the extjs version is suffixed to all versions)

All versions are tagged in the GIT repo, and second-level versions (4.0.x,
4.1.x...) get their own branch when a new version is released.

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
``EXTJS4_DEBUG``, ``EXTJS4_DEBUGFILE`` and ``EXTJS4_PRODFILE`` attributes from
``settings.py`` to your Django templates.


``EXTJS4_DEBUG`` is useful if you want to be able to test your
production ExtJS app on the Django test server, since setting ``DEBUG`` to
``True`` disables ``staticfiles``, but setting ``EXTJS4_DEBUG`` only uses your
``app-all.js`` instead of ``app.js`` and dynamic loading. If you add the
template context, but do not set ``EXTJS4_DEBUG`` in ``settings.py``, it
defaults to ``False``.

``EXTJS4_DEBUGFILE`` can be used to configure the ExtJS bundle to load. It defaults
to ``extjs4/ext-all-dev.js``, which is fast. ``ext-all-dev.js`` does not
provide the best debugging experience, so you may want to use
``extjs4/ext-dev.js`` instead, at least when you have a hard time debugging something.

``EXTJS4_PRODFILE`` is just like ``EXTJS4_DEBUGFILE``, but for production. It
defaults to ``extjs4/ext.js``. This assumes that  you have built your app with
``EXTJS4_DEBUGFILE="extjs4/ext-dev.js"``.


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
