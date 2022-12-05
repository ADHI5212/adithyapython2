
from django.shortcuts import render
from .models import place, founder


def home(request):
    obj=place.objects.all()
    rpm = founder.objects.all()
    return render(request, "index.html",{'result':obj,'result1':rpm})
