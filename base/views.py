from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('create')
    if request.method == "POST":
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, user = user.username, password=password)
            if user is not None:
                login(request,user)



# Create your views here.
