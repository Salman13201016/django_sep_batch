from django.shortcuts import render
from category.models import Categories

# Create your views here.

def index(request):
    all_cat = Categories.objects.all()
    all_data = {'data':all_cat}
    return render(request,'home.html',all_data)
