from django.shortcuts import render
from django.http import HttpResponse
from Blog.models import Articles

# Create your views here.
def hello(request):
    return render(request, 'blog/hello.html', {'annee_academique':'2022-2023','nom':['ulrich','david']})


def about (request):
    return render(request,'blog/about.html')

def art(request):
    Art  = Articles.objects.all()
    return render(request,'blog/art.html',{'Art':Art})