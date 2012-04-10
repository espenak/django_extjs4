from django.views.generic import View
from django.shortcuts import render


class Extjs4AppView(View):
    template_name = "extjs4/apptemplate.django.html"
    title = 'ExtJS app'
    css_staticpath = 'extjs4/resources/css/ext-all.css'
    appname = None

    def get(self, request, **kwargs):
        if not self.appname:
            raise ValueError('appname is required')
        data = {'title': self.title,
                'css_staticpath': self.css_staticpath,
                'appall_staticpath': '{appname}/app-all.js'.format(appname=self.appname),
                'app_staticpath': '{appname}/app.js'.format(appname=self.appname),
                'params': kwargs}
        return render(request, self.template_name, data)
