from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from users.forms import RegisterForm, LoginForm, ForgotForm

# Create your views here.
def register(request):
    return render(request, 'users/register.html')
    # redirect the user to the login page.

def testRegister(request):
    if request.method == 'POST':
        form = RegisterForm()
        if form.is_valid():
            name = form.cleaned_data['name']   
            email = form.cleaned_data['email']
            print(name, email)

    form = RegisterForm()
    return render(request, 'users/testRegister.html', {'form': form})

def testLogin(request):
    if request.method == 'POST':
        form = LoginForm()
        if form.is_valid:
            userName = form.cleaned_data['userName']
            password = form.cleaned_data['password']
            print(userName, password)
    form = LoginForm()
    return render(request, 'users/testLogin.html', {'form': form} )

def testForgot(request):
    if request.method == 'POST':
        form = ForgotForm()
        if form.is_valid:
            email = form.cleaned_data['email']
            print(email)
    form = ForgotForm()
    return render(request, 'users/testForgot.html', {'form': form} )

def login(request):
    # if request.method == 'POST':
    #     form = UserName(request.POST)
    #     if form.is_valid():
    #         return HttpResponseRedirect('/thanks/')
    # else:
    #     form = UserName()
    # if request.method == 'POST':
    #     form = password(request.POST)
    #     if form.is_valid():
    #         return HttpResponseRedirect('/thanks/')
    # else:
    #     form = password()
        

    return render(request, 'users/login.html')
    
def forgot(request):
    #if request.method == 'POST':
    return render(request, 'users/forgot.html')

