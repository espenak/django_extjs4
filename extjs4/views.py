from django.views.generic import View
from django.shortcuts import render


class Extjs4AppView(View):
    template_name = "extjs4/apptemplate.django.html"
    title = 'ExtJS app'
    css_staticpath = 'extjs4/resources/css/ext-all.css'

    def get(self, request, **kwargs):
        data = {'title': self.title,
                'css_staticpath': self.css_staticpath,
                'params': kwargs}
        return render(request, self.template_name, data)
