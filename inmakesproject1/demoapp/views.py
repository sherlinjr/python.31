from django.http import HttpResponse
from django.shortcuts import render
from . models import world
# Create your views here.


def demo(request):
    obj=world.objects.all()
    return render(request,"index.html",{'final':obj})


# def contact(request):
#     return HttpResponse("contact number")
# def home(request):
#     return render(request,"demo1.html")
# def thankyou(request):
#     return HttpResponse("thankyou all")