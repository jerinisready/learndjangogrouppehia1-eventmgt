from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import redirect


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def signin(request):
    errors = ""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if len(username) == 0:
            errors = "Username is required!"
        elif len(password) == 0:
            errors = "Password is required!"
        if not errors:
            users = User.objects.all().filter(username=username)
            if len(users) == 0:
                errors = "There is no user with this username!"
            else:
                user = users[0]
                is_password_correct = user.check_password(password)
                if is_password_correct is False:
                    errors = "There is no user with this username and password!"
                else:
                    login(request, user)
                    return redirect('/')
    return render(request, 'signin.html', {'error': errors})


def signin2(request):
    errors = ""
    if request.method == "POST":
        user = authenticate(**request.POST)
        if not user:
            errors = "There is no user with this username and password"
        else:
            login(request, user)
            return redirect('/')
    return render(request, 'signin.html', {'error': errors})


def signout(request):
    logout(request)
    return redirect('/')
