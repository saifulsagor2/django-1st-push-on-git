from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the task manager")


def contact(request):
    return HttpResponse("Welcome to the contact page")


def show_task(request):
    return HttpResponse("This is our show-Task page")