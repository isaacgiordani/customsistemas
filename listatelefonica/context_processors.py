# -*- coding: utf-8 -*-

from .models import Entity, PhoneBook

def entities(request):
    return {
    'entities': Entity.objects.all()
    }

def phones(request):
    return {
    'phones': PhoneBook.objects.all()
    }
