from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages
import re
from datetime import datetime, timedelta
from django.core.signing import Signer, BadSignature
import random

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
                return HttpResponse(encrypted_value)

                 
    
    else:
        return HttpResponse("this is not a post request")
def reg(request):
    return render(request,'register.html')
