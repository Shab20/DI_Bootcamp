from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import SignupForm, LoginForm
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


def home(request):
    return render(request, 'home.html')

@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_REDIRECT_URL)
            
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect(settings.LOGIN_REDIRECT_URL)
