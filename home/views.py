from django.shortcuts import render, redirect
from .models import Blog
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

CATEGORIES = [
    "Entertainment",
    "Business",
    "Technology",
    "Food",
    "Games",
    "Adventure",
    "Travel",
]

# Create your views here.
def login_page(request):
    try:
        if request.method == "POST":
            data = request.POST
            username = data.get("lUsername")
            password = data.get("lPassword")

            if username and password:
                user = User.objects.get(username =username)
                if user:
                    isCorrect = authenticate(username = username, password = password)
                    
                    if not isCorrect:
                        raise ValueError("Invalid Credentials.")
                    
                    login(request, user)
                    return redirect('/')
            else:
                raise ValueError("Please enter all the details to log in to your account.")
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, "login.html")
    except ValueError as e:
        return render(request, "login.html",context={"exception":e})
    except Exception as e:
        return render(request, "login.html",context={"exception":e})


def signup_page(request):
    try:
        if request.method == "POST":
            data = request.POST
            username = data.get("sUsername")
            email = data.get("sEmail")
            password = data.get("sPassword")

            if username and email and password:
                is_existing_user = User.objects.filter(username = username).exists()
                if is_existing_user:
                    raise ValueError(f"User with username = {username} already exists.")
                user = User.objects.create(
                    username=username, email=email
                )
                user.set_password(password)
                user.save()
                return redirect('/login/')
            else:
                raise ValueError("Please enter all the details to sign up.")
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, "signup.html")
    except ValueError as e:
        return render(request, "signup.html",context={"exception":e})
    except Exception as e:
        return render(request, "signup.html",context={"exception":e})

def logout_page(request):
    try:
        logout(request)
        return redirect('/login/')
    except Exception as e:
        print(e)

# Create your views here.
def home_page(request):
    search = request.GET.get('search')
    if search:
        blogs = Blog.objects.filter(title__icontains = search)
    else:
        blogs = Blog.objects.all()
    return render(request, "index.html", context={"blogs": blogs})

def category_blogs(request, category):
    
    if category in CATEGORIES:
        search = request.GET.get('search')
        if search:
            blogs = Blog.objects.filter(category=category, title__icontains=search)
        else:
            blogs = Blog.objects.filter(category=category)
        return render(request, "index.html", context={"blogs": blogs})
    return redirect('/')

def add_blog(request):
    try:
        if not request.user.is_authenticated:
            return redirect("/login/")

        if request.method == "POST":
            data = request.POST

            title = data.get("title")
            description = data.get("description")
            category = data.get("category")
            img_url = data.get("img_url")

            if title and description and (category in CATEGORIES) and img_url:
                Blog.objects.create(
                    title=title,
                    description=description,
                    category=category,
                    img_url=img_url,
                    user=request.user,
                )
                return redirect("/")
            else:
                raise ValueError(
                    "Please fill up all the fields before creating a new blog."
                )
        return render(request, "addBlog.html")
    except ValueError as e:

        return render(request, "addBlog.html", context={"exception": e})
    except Exception as e:

        return render(request, "addBlog.html", context={"exception": e})


def acc_info(request):
    if not request.user.is_authenticated:
            return redirect("/login/")

    blogs = Blog.objects.filter(user = request.user)
    return render(request, "accInfo.html", context={"blogs": blogs})


def edit_blog(request, id):
    try:
        if not request.user.is_authenticated:
            return redirect("/login/")


        blog = Blog.objects.get(id=id)
        if request.method == "GET" and blog:
            return render(request, "editBlog.html", context={"blog": blog})
        if request.method == "POST":
            data = request.POST

            title = data.get("title")
            description = data.get("description")
            category = data.get("category")
            img_url = data.get("img_url")

            if title and description and (category in CATEGORIES) and img_url:
                blog.title = title
                blog.description = description
                blog.category = category
                blog.img_url = img_url

                blog.save()
                return redirect("/accInfo")
            else:
                raise ValueError("Please fill up all the fields to Edit the blog.")
    except ValueError as e:

        return render(request, "editBlog.html", context={'blog':blog,"exception": e})
    except Exception as e:

        return render(request, "editBlog.html", context={'blog':blog,"exception": e})


def delete_blog(request, id):
    try:
        if not request.user.is_authenticated:
            return redirect("/login/")

        blog = Blog.objects.get(id=id, user = request.user)
        if blog:
            blog.delete()
        return redirect("/accInfo")
    except Exception as e:
        return redirect("/accInfo")


def view_blog(request, id):
    try:
        blog= Blog.objects.get(id = id)
        return render(request, 'viewBlog.html', context={"blog":blog})
    except Exception as e:
        return redirect("/accInfo")
