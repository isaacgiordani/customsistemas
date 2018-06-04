# -*- coding: utf-8 -*-

from django.shortcuts import render

from .models import PhoneBook, Entity

def phone_list(request):
    context = {
        'phone_list': PhoneBook.objects.all()
    }
    return render(request, 'listatelefonica/phones.html', context)

def entity(request, slug):
    entity = Entity.objects.get(slug=slug)
    context = {
        'current_entity': entity,
        'phone_list': PhoneBook.objects.filter(entity=entity),
    }
    return render(request, 'listatelefonica/entity.html', context)

def phone(request, slug):
    phone = PhoneBook.objects.get(slug=slug)
    context = {
        'phone': phone
    }
    return render(request, 'listatelefonica/phone.html', context)
