from django.shortcuts import render
from .models import BaseSetting


def home(request, template_name='base/index.html', context={}):
    context['title'] = 'Home'

    context['settings'] = BaseSetting.objects.first()

    return render(request, template_name, context)