from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return render(request, 'login/success.html')
        else:
            return render(request, 'login/login.html', {'error': "Invaild credentials"})
    return render(request, 'login/login.html')