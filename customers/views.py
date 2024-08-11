from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from . models import Customer
from django.contrib import messages

# Create your views here.
def sign_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')
def show_account(request):
    context={}
    if request.POST and 'register' in request.POST:
        context['register'] = True
        try:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            address = request.POST.get('address')
            phone = request.POST.get('phone')

            # create user accouts
            user = User.objects.create(username=username, email=email)
            user.set_password(password)
            user.save()

            # creates customer accounts
            customer = Customer.objects.create(user=user, address=address, phone=phone)
            success_message = "User registered successfully"
            messages.success(request, success_message)
        except Exception as e:
            error_message = "Duplicate username or Invalid credentials"
            messages.error(request, error_message)

    if request.POST and 'login' in request.POST:
        context['register'] = False
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Invalid username or password"
            messages.error(request, error_message)
            
    return render(request, 'account.html', context)