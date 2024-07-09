from django.shortcuts import render
from .models import People

# Create your views here.

def home(request):
    people = People.objects.all()
    return render(request, 'home.html', {'people' : people})