from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def user_login(request):
    try:
        if request.method == "POST":
            data = request.POST
            username = data.get("lUsername")
            password = data.get("lPassword")

            if username and password:
                user = User.objects.get(username=username)
                if user:
                    isCorrect = authenticate(username=username, password=password)

                    if not isCorrect:
                        raise ValueError("Invalid Credentials.")

                    login(request, user)
                    return redirect("/")
            else:
                raise ValueError(
                    "Please enter all the details to log in to your account."
                )
        if request.user.is_authenticated:
            return redirect("/")
        return render(request, "login.html")
    except ValueError as e:
        return render(request, "login.html", context={"exception": e})
    except Exception as e:
        return render(request, "login.html", context={"exception": e})


def user_signup(request):
    try:
        if request.method == "POST":
            data = request.POST
            username = data.get("sUsername")
            email = data.get("sEmail")
            password = data.get("sPassword")

            if username and email and password:
                is_existing_user = User.objects.filter(username=username).exists()
                if is_existing_user:
                    raise ValueError(f"User with username = {username} already exists.")
                user = User.objects.create(username=username, email=email)
                user.set_password(password)
                user.save()
                return redirect("/login/")
            else:
                raise ValueError("Please enter all the details to sign up.")
        if request.user.is_authenticated:
            return redirect("/")
        return render(request, "signup.html")
    except ValueError as e:
        return render(request, "signup.html", context={"exception": e})
    except Exception as e:
        return render(request, "signup.html", context={"exception": e})


def user_logout(request):
    try:
        logout(request)
        return redirect("/login/")
    except Exception as e:
        print(e)
