from django.shortcuts import render

# Create your views here.
from .models import People


def people(request):
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get('fullname') and request.POST.get('phone') and request.POST.get('hall'):
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
            return render(request, 'people.html')
    else:
        return render(request, "people.html")
