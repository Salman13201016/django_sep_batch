from django.shortcuts import render
from django.shortcuts import redirect

from .models import Categories

# Create your views here.

def index(request):
    return render(request,'admin/category.html')

def insert(request):
    cat_name = request.POST.get('cat_name')
    cat_code = request.POST.get('cat_code')
    cat_obj= Categories()
    cat_obj.cat_name = cat_name
    cat_obj.cat_code = cat_code

    cat_obj.save()
    return redirect('cat_index')

