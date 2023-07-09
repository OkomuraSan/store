from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from users.forms import UserLoginForm, UserRegForm, UserProfileForm
from django.urls import reverse
from users.models import User
@csrf_exempt
def login(request):

    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("index"))
    else:
            form = UserLoginForm()
    context = {
        "form": form

    }
    return render(request,  'users/login.html', context)

@csrf_exempt
def register(request):
        if request.method == "POST":
            form = UserRegForm(data=request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse("users:login"))
        else:
            form = UserRegForm()
        context = {"form" : form }
        return render(request, "users/register.html ", context)

@csrf_exempt
def profile(request):
    if request.method == "POST":
        form = UserProfileForm(instance=request.user, data = request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("users:profile"))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        "title":"Профиль",
        "form": form
    }
    return render(request, "users/profile.html", context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("index"))