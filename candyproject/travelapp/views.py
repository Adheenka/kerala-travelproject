from django.http import HttpResponse
from django.shortcuts import render
from . models import place

# Create your views here.
def dummy(request):
    obj=place.objects.all()
    return render(request,"index.html",{'result':obj})