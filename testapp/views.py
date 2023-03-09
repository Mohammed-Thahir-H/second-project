from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def one(request):
    return HttpResponse('<h2>This is One</h2>')

def two(request):
    return HttpResponse('<h2>this is two</h2>')

def three(request):
    return HttpResponse('<h2>this is Three</h2>')

def four(request):
    return HttpResponse('<h2>this is Four</h2>')

def five(request):
    return HttpResponse('<h2>this will be Five</h2>')
def six(request):
    return HttpResponse('<h1>This is six</h1>')
