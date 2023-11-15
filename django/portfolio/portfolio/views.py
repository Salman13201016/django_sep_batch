from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import About

def about_index(request):
    all_data = About.objects.all()

    data = {'d':all_data}
    
    return render(request,'admin/about.html',data)

def index1(request):
    return render(request,'index.html')

def about_insert(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    dob = request.POST.get('dob')
    git = request.POST.get('git')
    fb = request.POST.get('fb')
    linkedin = request.POST.get('linkedin')
    pw = request.POST.get('pw')
    conpw = request.POST.get('conpw')
    gender = request.POST.get('gender')
    image = request.FILES.get('image')
    address = request.POST.get('address')
    desc = request.POST.get('desc')
    # return HttpResponse(desc)
    about_obj = About()
    about_obj.name = name
    about_obj.email = email
    about_obj.phone = phone
    about_obj.dob = dob
    about_obj.git = git
    about_obj.fb = fb
    about_obj.linkedin = linkedin
    about_obj.linkedin = linkedin
    about_obj.pw = pw
    about_obj.gender = gender
    about_obj.address = address
    about_obj.description = desc
    about_obj.save()
    return redirect("about")


    return HttpResponse(image)

