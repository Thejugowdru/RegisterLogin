from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        return redirect('login')
    return render(request, "register/register.html")