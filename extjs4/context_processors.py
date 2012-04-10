from django.conf import settings


def extjs4(request):
    return {'EXTJS4_DEBUG': getattr(settings, 'EXTJS4_DEBUG', False)}
