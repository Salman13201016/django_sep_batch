
from django.shortcuts import render,redirect
from .models import About,Facts

from django.http import HttpResponse

from datetime import date,datetime
def about_index(request):
    all_data = About.objects.all()
    if(len(all_data)>0):
        size = True
    else:
        size = False


    data = {'d':all_data,'size':size}
    
    return render(request,'admin/about.html',data)

def facts(request):

    

    return render(request,'admin/facts.html')

def f_insert(request):
    description = request.POST.get('desc')
    no_of_clients = request.POST.get('no_client')
    no_of_projects = request.POST.get('no_of_projects')
    no_of_hours = request.POST.get('no_of_hours')
    no_of_hardworkers = request.POST.get('no_of_hardworker')
    facts_obj = Facts()

    facts_obj.description = description
    facts_obj.no_of_client = no_of_clients
    facts_obj.no_of_project = no_of_projects
    facts_obj.no_of_hours = no_of_hours
    facts_obj.no_of_hardworkers = no_of_hardworkers

    facts_obj.save()
    return redirect("facts")


def about_delete(request,u_id):
    about_obj = About.objects.get(id=u_id)
    about_obj.delete()
    return redirect('about')

def about_edit(request,u_id):
    about_obj = About.objects.get(id=u_id)
    about_data = {'data':about_obj}
    return render(request,'admin/edit.html',about_data)


def index1(request):
    all_data = About.objects.get(id=5)
    all_facts = Facts.objects.get(id=1)

    dob = all_data.dob
    dob = datetime.strptime(dob, "%Y-%m-%d").date()
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    data = {'d':all_data,'age':age,'facts':all_facts}
    return render(request,'index.html',data)

# def about_insert(request):
#     name = request.POST.get('name')
#     email = request.POST.get('email')
#     return HttpResponse("this is a about insert")

def about_edit_f(request):
    id = request.POST.get('id')
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

    about_obj = About.objects.get(id=id)



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


