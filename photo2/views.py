from django.shortcuts import render,HttpResponse
from photo2.models import bird,insects,reptile,nature,travels
# Create your views here.
def home(request):
    return render(request,'index.html')
def bir(request):
    content = {"message": bird.objects.all()}
    return render(request,"bird.html",content)
def rept(request):
    content = {"message": reptile.objects.all()}
    return render(request,"reptile.html",content)
def ins(request):
    content = {"message": insects.objects.all()}
    return render(request,"insects.html",content)
def tra(request):
    content = {"message": travels.objects.all()}
    return render(request,"travels.html",content)
def nat(request):
    content = {"message": nature.objects.all()}
    return render(request,"nature.html",content)