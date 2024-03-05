from django.shortcuts import render, redirect
from .models import Blog
from .authentication.auth import *  # Import all authentication functions
from .constants import CATEGORIES

# User authentication views
def login_page(request):
    """
    Redirects user to the login process to the `user_login` function
    defined in the authentication module.
    """
    return user_login(request)


def signup_page(request):
    """
    Redirects user to the sign up process to the `user_signup` function
    defined in the authentication module.
    """
    return user_signup(request)


def logout_page(request):
    """
    Initiates the user logout process by the `user_logout` function
    defined in the authentication module.
    """
    return user_logout(request)


# Main view and CRUD operations for blogs
def home_page(request):
    """
    Handles displaying all or filtered blogs based on user search query.
    - Retrieves all blogs if no search query is provided.
    - Filters blogs by title containing the search query if provided.
    - Sorts retrieved blogs by descending order of creation date (newest first).
    - Renders the "index.html" template with the list of blogs in context.
    """
    search = request.GET.get("search")
    if search:
        blogs = Blog.objects.filter(title__icontains=search).order_by("-id")
    else:
        blogs = Blog.objects.all().order_by("-id")
    return render(request, "index.html", context={"blogs": blogs})

def add_blog(request):
    """
    Handles creating new blog posts and form validation.
    - Checks if the user is authenticated before allowing blog creation.
    - Redirects to the login page if the user is not authenticated.
    - Handles POST requests for creating new blog posts.
    - Extracts blog post details (title, description, category, image URL) from the request data.
    - Performs validation to ensure all required fields are filled and the category is valid.
    - Creates a new blog post object in the database if validation passes.
    - Redirects the user to the home page upon successful blog creation.
    - Renders the "addBlog.html" template if the request is GET (to display the blog creation form).
    - Handles any exceptions that might occur during the process (e.g., validation errors, database errors).
    - Renders the "addBlog.html" template with an error message in the context if an exception occurs.
    """
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


def edit_blog(request, id):
    """
    Handles editing existing blog posts and form validation.
    - Checks if the user is authenticated before allowing blog editing.
    - Redirects to the login page if the user is not authenticated.
    - Attempts to retrieve the blog post with the given ID from the database.
    - Handles GET requests to pre-populate the edit form with the blog post details.
    - Renders the "editBlog.html" template with the blog post details in context if the blog is found and the request is GET.
    - Handles POST requests to update the blog post details.
    - Extracts updated blog post details (title, description, category, image URL) from the request data.
    - Performs validation to ensure all required fields are filled and the category is valid.
    - Updates the retrieved blog post object with the new details if validation passes.
    - Saves the updated blog post object to the database.
    - Redirects the user to their account information page upon successful blog update.
    - Handles any exceptions that might occur during the process (e.g., validation errors, database errors, blog not found).
    - Renders the "editBlog.html" template with the blog post details (if found) and an error message in the context if an exception occurs.
    """
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

        return render(request, "editBlog.html", context={"blog": blog, "exception": e})
    except Exception as e:

        return render(request, "editBlog.html", context={"blog": blog, "exception": e})


def delete_blog(request, id):
    """
    Handles deleting blog posts by the authenticated user.
    - Checks if the user is authenticated before allowing blog deletion.
    - Redirects to the login page if the user is not authenticated.
    - Attempts to retrieve the blog post with the given ID from the database and ensure it belongs to the authenticated user.
    - Deletes the retrieved blog post if found and it belongs to the user.
    - Redirects the user to their account information page upon successful blog deletion.
    - Handles any exceptions that might occur during the process (e.g., database errors, blog not found, blog does not belong to user).
    - Redirects the user to their account information page even if an exception occurs (to avoid displaying error messages publicly).
    """
    try:
        if not request.user.is_authenticated:
            return redirect("/login/")

        blog = Blog.objects.get(id=id, user=request.user)
        if blog:
            blog.delete()
        return redirect("/accInfo")
    except Exception as e:
        return redirect("/accInfo")


def view_blog(request, id):
    """
    Handles displaying an individual blog post.
    - Attempts to retrieve the blog post with the given ID from the database.
    - Renders the "viewBlog.html" template with the retrieved blog post details in context if found.
    - Handles any exceptions that might occur during the process (e.g., database errors, blog not found).
    - Redirects the user to their account information page even if an exception occurs (to avoid displaying error messages publicly).
    """
    try:
        blog = Blog.objects.get(id=id)
        return render(request, "viewBlog.html", context={"blog": blog})
    except Exception as e:
        return redirect("/accInfo")


def acc_info(request):
    """
    Displays all blogs created by the authenticated user.
    Renders the "accInfo.html" template or redirects to login page if not authenticated.
    """
    if not request.user.is_authenticated:
        return redirect("/login/")

    blogs = Blog.objects.filter(user=request.user).order_by("-id")
    return render(request, "accInfo.html", context={"blogs": blogs})


def category_blogs(request, category):
    """
    Handles displaying blogs belonging to a specific category or filtered blogs within that category based on search query.
    - Checks if the provided category is valid (exists in the CATEGORIES list).
    - Retrieves blogs belonging to the specified category if valid.
    - Filters retrieved blogs by title containing the search query if provided.
    - Sorts retrieved blogs by descending order of creation date (newest first).
    - Renders the "index.html" template with the list of blogs in context if category is valid.
    - Redirects to the home page if the provided category is invalid.
    """
    if category in CATEGORIES:
        search = request.GET.get("search")
        if search:
            blogs = Blog.objects.filter(
                category=category, title__icontains=search
            ).order_by("-id")
        else:
            blogs = Blog.objects.filter(category=category).order_by("-id")
        return render(request, "index.html", context={"blogs": blogs})
    return redirect("/")

