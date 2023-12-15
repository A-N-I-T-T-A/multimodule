from django.shortcuts import render,redirect
from threemodapp.models import CustomUser,Usermember
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
import os
# Create your views here.
def index(request):
    return render(request,'index.html')
def patientreg(request):
    return render(request,'patientreg.html')
def doctorreg(request):
    return render(request,'doreg.html')
@login_required(login_url='loginpage')
def ahome(request):
    users=Usermember.objects.all()
    return render(request,'ahome.html',{'users':users})
@login_required(login_url='loginpage')
def pdet(request):
    users=Usermember.objects.all()
    return render(request,'patientd.html',{'users':users})
@login_required(login_url='loginpage')
def dodet(request):
    users=Usermember.objects.all()
    return render(request,'doctord.html',{'users':users})
@login_required(login_url='loginpage')
def dhome(request):
    current=request.user.id 
    user=Usermember.objects.get(user_id=current) 
    return render(request,'dhome.html',{'user':user})
@login_required(login_url='loginpage')
def phome(request):
    current=request.user.id 
    user=Usermember.objects.get(user_id=current) 
    return render(request,'phome.html',{'user':user})
def loginpage(request):
    return render(request,'login.html')
def preg(request):
    if request.method == 'POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        user=request.POST['username']
        email=request.POST['email']
        pwd=request.POST['password']
        cpwd=request.POST['cpassword']
        age=request.POST['age']
        phone=request.POST['contact']
        image=request.FILES.get('profile')
        user_type=request.POST['text']
        if pwd==cpwd:
            if CustomUser.objects.filter(username=user).exists():
                messages.info(request,'This username already exists!!')
                return redirect('patientreg')
            else:
                usr=CustomUser.objects.create_user(first_name=fname,last_name=lname,username=user,email=email,password=pwd,user_type=user_type)
                usr.save()

                det=Usermember(phone=phone,Image=image,age=age,user=usr)
                det.save()
                subject='Your Hopital Login username and password'
                message2= 'Username:'+user+'\n'+'Password:'+pwd
                send_mail(subject,message2,settings.EMAIL_HOST_USER,[email])
                return redirect('loginpage')
        else:
            messages.info(request,'Password doesn"t match!!')
            return redirect('patientreg')
    return render(request,'patientreg.html')
def dreg(request):
    if request.method == 'POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        user=request.POST['username']
        email=request.POST['email']
        pwd=request.POST['password']
        cpwd=request.POST['cpassword']
        age=request.POST['age']
        phone=request.POST['contact']
        image=request.FILES.get('profile')
        user_type=request.POST['text']
        if pwd==cpwd:
            if CustomUser.objects.filter(username=user).exists():
                messages.info(request,'This username already exists!!')
                return redirect('doctorreg')
            else:
                usr=CustomUser.objects.create_user(first_name=fname,last_name=lname,username=user,email=email,password=pwd,user_type=user_type)
                usr.save()

                det=Usermember(phone=phone,Image=image,age=age,user=usr)
                det.save()
                subject='Your Hopital Login username and password'
                message2= 'Username:'+user+'\n'+'Password:'+pwd
                send_mail(subject,message2,settings.EMAIL_HOST_USER,[email])
                return redirect('loginpage')
        else:
            messages.info(request,'Password doesn"t match!!')
            return redirect('doctorreg')
    return render(request,'doctorreg.html')
def loginuser(request):
    if request.method == 'POST':
        user=request.POST['username']
        pwd=request.POST['password']
        usr1=auth.authenticate(username=user, password=pwd)
        if usr1 is not None:
            if usr1.user_type == '1':
                login(request,usr1)
                return redirect('ahome')
            elif usr1.user_type == '2':
                auth.login(request,usr1)
                return redirect('dhome')
            else:
                auth.login(request,usr1)
                return redirect('phome')
        else:
            messages.info(request,'Invalid Username or Password!. Try again')
            return redirect('loginpage')
    else:
        return redirect('loginpage')
@login_required(login_url='loginpage')
def logout_admin(request):
    auth.logout(request)
    return redirect('index')
@login_required(login_url='loginpage')
def logout_user(request):
    auth.logout(request)
    return redirect('index')
    
