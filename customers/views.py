from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from . models import Customer
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def signout(request):
    logout(request)
    return redirect('home')


def account(request):
    context={}  # for login/registration tab activation
    if request.POST and 'register' in request.POST:
        context['register']=True
        # print(request.POST)
        try:
            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            address=request.POST.get('address')
            phone=request.POST.get('phone')
            #create user obj
            user=User.objects.create_user(
                username=username,
                password=password,
                email=email,
            )
            #create customer obj
            customer=Customer.objects.create(
                user=user,
                phone=phone,
                address=address,
            )
            success_mesage='Registered successfully'
            messages.success(request,success_mesage)
        except Exception as e:
            error_message='Duplicate username or invalid inputs'
            messages.error(request,error_message)
    if request.POST and 'login' in request.POST:
        context['register']=False
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            print("success")
            login(request,user)
            return redirect('home')
        else:
            print("error")
            messages.error(request,'Invalid user credentials')

    return render(request,'account.html',context)