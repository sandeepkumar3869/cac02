from django.shortcuts import render, redirect
from .models import *
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

# bottomlevel = []

# Create your views here.
# def index(request):
#     if request.method == 'POST':
#         new_task = request.POST['task']
#         bottomlevel.append(new_task.strip())
#         return redirect('index')
#     return render( request, 'bottomlevel/index.html', context={'task':bottomlevel})

@login_required(login_url='login')
def index(request):
    if request.method == 'POST':
        new_task = request.POST['task'].strip()
        description1 =request.POST['description']

        bottomlevel1 = bottomlevel(task_title=new_task , task_description=description1)
      
        bottomlevel1.save()
        
        return redirect('index')
    bottomlevel1 = bottomlevel.objects.all()
    
    return render(request, 'bottomlevel/index.html', context={'task':bottomlevel1})

def deletetask(request,id):
    task = bottomlevel.objects.get(taskid=id)
    task.delete()
    return redirect('index')


def edittask(request,id):
    task = bottomlevel.objects.get(taskid=id)
    if request.POST:
        new_task = request.POST['task'].strip()
        description1 =request.POST['description']
        task.task_title = new_task
        task.task_description = description1
        task.save()
        return redirect('index') 

    return render(request,'bottomlevel/edit.html',context={'task': task})
def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        message = request.POST.get("message")
        contact =  contactus(name = name , phone = phone, email= email ,message = message, date = datetime.today())
        contact.save()
    return render(request,'bottomlevel/contactus.html')


def login_view(request):
    print("skasf")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("ok")
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        print("4595")
        if user is not None:
            # This block will be executed if user is not None
            print("ok1")
            # Login the user
            login(request,user)
            print("success")
            messages.success(request, 'Login successful.')
            return redirect('index')  # Replace 'home' with the name of your home URL or the URL you want to redirect to
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'bottomlevel/login.html')
def registration(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        print("asdfghj")

        if not User.objects.filter(email=email).exists():
            if password == password1:

                myuser = User.objects.create_user(username=email,email=email,password=password)
                myuser.save()
                print("authuser")
                new_user = Usertbl(email=email, password=password, name=name, last_name=last_name)
                new_user.save()
                print("new_user")
                print(new_user)
                return redirect('login')
            else:
                return render(request,"bottomlevel/contactus.html")
        else:
            return render(request,"bottomlevel/aboutus.html")

    return render(request, 'bottomlevel/reg.html')

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')