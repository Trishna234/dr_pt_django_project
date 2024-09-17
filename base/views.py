from django.contrib import messages
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
            user = authenticate(request, user=user.username, password=password)
            if user is not None:
                login(request, user)
                return redirect('create')
            else:
                messages.error(request, message='Invalid password')
        except User.DoesnotExit:
            messages.error(request, message='User doesnot exit')
    context = {page: page}
    return render(request, template_name='login_register.html', context=context)
