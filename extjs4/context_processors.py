from django.conf import settings


def extjs4(request):
    return {'EXTJS4_DEBUG': getattr(settings, 'EXTJS4_DEBUG', False),
            'EXTJS4_DEBUGFILE': getattr(settings, 'EXTJS4_DEBUGFILE', 'extjs4/ext-all-dev.js'),
            'EXTJS4_PRODFILE': getattr(settings, 'EXTJS4_PRODFILE', 'extjs4/ext.js')
            }
