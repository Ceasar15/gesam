# Create your views here.

from django.shortcuts import render
from django.contrib import messages
from django.template import RequestContext
from django.http import HttpRequest, HttpResponseRedirect
from .models import Contact

# Create your views here.


def events(request):
    assert isinstance(request, HttpRequest)
    return render(render, 'event.html')


def index(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'home.html')


def contact(request):
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get('fullname') and request.POST.get('email') and request.POST.get('phone') and request.POST.get('message'):
            contact = Contact()
            contact.fullname = request.POST.get('fullname')
            contact.email = request.POST.get('email')
            contact.phone = request.POST.get('phone')
            contact.message = request.POST.get('message')
            contact.save()
            print(contact)

        return render(request, "contact.html")
    else:
        return render(request, "contact.html")


def beliefs(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'beliefs.html')


def sermons(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'sermons.html')
