from django.shortcuts import render

# Create your views here.
from .models import PhoneBook

def telefones(request):
    return render(request,'listatelefonica/telefones.html')
