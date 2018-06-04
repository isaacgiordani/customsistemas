# -*- coding: utf-8 -*-

from .models import Entity, PhoneBook

def entities(request):
    return {
    'entities': Entity.objects.all()
    }
