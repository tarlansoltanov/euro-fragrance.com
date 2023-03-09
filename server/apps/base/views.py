from django.shortcuts import render
from .models import BaseSetting


def home(request, template_name='base/index.html', context={}):
    context['title'] = 'Home'

    context['settings'] = BaseSetting.objects.first()

    return render(request, template_name, context)

def about(request, template_name='base/about.html', context={}):
    context['title'] = 'About'

    context['settings'] = BaseSetting.objects.first()

    return render(request, template_name, context)

def contact(request, template_name='base/contact.html', context={}):
    context['title'] = 'Contact'

    context['settings'] = BaseSetting.objects.first()

    return render(request, template_name, context)