from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        # Grab the data from the HTML form
        u = request.POST.get('username')
        p = request.POST.get('password')
        
        # Check against the database
        user = authenticate(request, username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('/projects/')  # Redirect to dashboard on success
        else:
            messages.error(request, 'Invalid Username or Password')

    # If it's a GET request, just show the login page
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('/accounts/login/')
