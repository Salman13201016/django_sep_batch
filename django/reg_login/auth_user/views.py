from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages
import re
from datetime import datetime, timedelta
from django.core.signing import Signer, BadSignature
import random
from django.core.mail import send_mail
from  reg_login.models import User

from django.utils.html import format_html

def registration_done(request):


    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        con_pw = request.POST.get('con_pw')
        print(password)
        print(con_pw)
        phone = request.POST.get('phone')
        email_reg = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if(name=='' or email =='' or password=='' or con_pw=='' or phone==''):
            messages.error(request, 'your field can not be empty')
            return redirect('reg')
        else:
            if(len(name)<3):
                messages.error(request, 'The name length must be minimum 3')
                return redirect('reg')
            elif not re.match(email_reg,email):
                messages.error(request, 'Please Provide Approprate Email')
                return redirect('reg')
            elif(password!=con_pw):
                messages.error(request, 'Password Does Not Match')
                return redirect('reg')
            elif(len(phone)!=11):
                messages.error(request, 'Please Provide Appropriate Phone Number')
                return redirect('reg')
            else:
                time = datetime.now().strftime("%H:%M:%S")
                hour,m,s  = map(int,time.split(':'))
                print(hour,m,s)
                total_s = hour*60**2 + m*60 + s
                random_number = random.choices('123456790',k=4)
                print(random_number)
                random_number = ''.join(random_number)
                print(random_number)
                v_code = str(total_s) + random_number
                signer = Signer()
                encrypted_value = signer.sign(v_code).split(':')[1]
                print(encrypted_value)

                subject = 'Verify your account'
                link = f"<p>Congratulations Mr {name} ! For registering as a user in our system. To confirm the registration </p><a href='http://127.0.0.1:8000/auth/user/email_verification/"+encrypted_value+"' target='_blank'>please click this Activation link</a>"
                from_email = 'projectsocialmedias@gmail.com'
                format_link = format_html(link)
                recipient_list = ['projectsocialmedias@gmail.com',email]

                send_mail(subject, format_link, from_email, recipient_list,html_message=format_link)
                user_obj = User()
                user_obj.name = name
                user_obj.email = email
                user_obj.pw = password
                user_obj.phone = phone
                user_obj.v_code = encrypted_value
                user_obj.v_status = 0
                user_obj.save()
                
                return redirect('reg')

                 
    
    else:
        return HttpResponse("this is not a post request")
def reg(request):
    if 'user_id' in request.session:
         return redirect('home')
    else:

    
        return render(request,'register.html')
def verification(request,id):
    update = User.objects.get(v_code=id)
    update.v_status=1
    update.save()
    update = User.objects.get(v_code=id)
    status = update.v_status
    print(update.v_status)
    if(status=='1'):
        return HttpResponse("Successfully Registered")
    else:
        return HttpResponse("failed")
    
def home(request):
    if 'user_id' in request.session:

    
        return render(request,'home.html')
    elif 'social_auth_google-oauth2' in request.session:
        return render(request,'home.html')
    else:
        return redirect('login')

def login(request):
    if 'user_id' in request.session:

        return redirect('home')
    elif 'social_auth_google-oauth2' in request.session:
        return redirect('home')
    
    return render(request,'login.html')


def login_done(request):
    email = request.POST.get('email')
    pw = request.POST.get('password')
    check = User.objects.get(email=email)
    # print(list(check.id))
    if(check.v_status=='1' and check.pw==pw):
        request.session['user_id'] = check.id
        return redirect('home')
        
    else:
        return HttpResponse("Login Failed")
    
def logout(request):
    if 'user_id' in request.session:
        request.session.flush()
    elif 'social_auth_google-oauth2' in request.session:
        del request.session['social_auth_google-oauth2']
    return render(request,'login.html')
    
