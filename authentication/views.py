from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from authentication.forms import LoginForm, SignUpForm
from custom_user.models import BugUser
from django.contrib.admin.views.decorators import staff_member_required

def loginview(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data["username"],
                password=data["password"]
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("homepage"))
                )
    form = LoginForm()
    return render(request, "generic_form.html", {"form": form})

def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse("loginpage"))

# @staff_member_required
def signupview(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = BugUser.objects.create_user(
                username = data["username"],
                password = data["password"],
                display_name = data["display_name"]
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("loginpage"))
    form = SignUpForm()
    return render(request, "generic_form.html", {"form": form})
