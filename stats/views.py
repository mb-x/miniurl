from django.shortcuts import render, redirect, reverse
from stats.forms import ConnexionForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_view(request):
    form = ConnexionForm(request.POST or None)
    error = False
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            else:
                error=True
    return render(request, 'connection.html', {"form": form, "error": error})

def logout_view(request):
    logout(request)
    return redirect(reverse(login_view))

@login_required
def secured_view(request):
    pass