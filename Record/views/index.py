from django.shortcuts import render, HttpResponse , redirect
from Record.models import User


# Create your views here.

def index(request):
    return render(request, 'index.html')


def logout(request):
    request.session.clear()
    return redirect('index') #name of index url