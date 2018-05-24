#coding=utf-8

from .models import Entity

def entidades(request):
    return {
    'entidades': Entity.objects.all()
    }
