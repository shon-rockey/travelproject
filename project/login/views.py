from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "invalid user")
            return redirect("login_page")
    return render(request, "login.html")


def lgn(request):
    if request.method == "POST":
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["password1"]
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username is already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email is already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                email=email,
                                                password=password)
                user.save();
                print("user created")
                return redirect("login_page")
        else:
            print("password is not matching")
            return redirect('register')
        return redirect('/')
    return render(request, "Register.html")


def logout(request):
    auth.logout(request)
    return redirect("/")
