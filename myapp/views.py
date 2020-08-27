from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from django.contrib import messages
from .models import Contact, People
from django.conf import settings
from pypaystack import Transaction

# Create your views here.


def index(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'home.html')


def people(request):
    if request.method == "POST":
        print(request.POST)
        if request.POST.get('fullname') and request.POST.get('phone') and request.POST.get('hall') and request.POST.get("program"):
            people = People()
            people.fullname = request.POST.get('fullname')
            people.phone = request.POST.get('phone')
            people.hall = request.POST.get('hall')
            people.roomNumber = request.POST.get('roomNumber')
            people.program = request.POST.get("program")
            people.birthday = request.POST.get("birthday")
            people.gender = request.POST.get("gender")
            people.level = request.POST.get("level")
            people.save()
            messages.success(request, 'Submitted Successfully')
            return render(request, "people.html")
    else:
        return render(request, "people.html")


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
            return render(request, 'contact.html')
    else:
        return render(request, "contact.html")


def beliefs(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'beliefs.html')


def sermons(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'sermons.html')


def donations(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'donations.html')


def verify(request, reference):
    transaction = Transaction(settings.PAYSTACK_SECRET_KEY)
    response = transaction.verify(reference)
    if response[3]['status'] == 'success':
        return render(request, 'donations.html')
    else:
        return HttpResponse('failed')
