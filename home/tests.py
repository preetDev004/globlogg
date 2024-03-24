from .views import *
from django.test import TestCase, Client
from django.urls import reverse
from .models import Blog
from django.test import RequestFactory
from django.contrib.auth.models import User

class HomePageTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('home_page')

    def test_home_page_no_search_query(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertQuerysetEqual(response.context['blogs'], Blog.objects.all().order_by('-id'), transform=lambda x: x)

    def test_home_page_with_search_query(self):
        response = self.client.get(self.url, {'search': '1M'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertQuerysetEqual(response.context['blogs'], Blog.objects.filter(title__icontains='1M').order_by('-id'), transform=lambda x: x)

    def test_home_page_invalid_search_query(self):
        response = self.client.get(self.url, {'search': 'invalid'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertQuerysetEqual(response.context['blogs'], Blog.objects.none(), transform=lambda x: x)

    def test_home_page_empty_search_query(self):
        response = self.client.get(self.url, {'search': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertQuerysetEqual(response.context['blogs'], Blog.objects.all().order_by('-id'), transform=lambda x: x)


class AddBlogTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_add_blog_authenticated(self):
        # Test adding a blog when the user is authenticated
        request = self.factory.post('/add-blog/', {
            'title': 'Test Blog',
            'description': 'This is a test blog',
            'category': 'Technology',
            'img_url': 'https://example.com/image.jpg'
        })
        request.user = User.objects.create_user(username='testuser', password='testpassword')
        response = add_blog(request)
        self.assertEqual(response.status_code, 302)  # Redirect to home page
        self.assertEqual(Blog.objects.count(), 1)  # Blog should be created

    def test_add_blog_not_authenticated(self):
        # Test adding a blog when the user is not authenticated
        request = self.factory.post('/add-blog/', {
            'title': 'Test Blog',
            'description': 'This is a test blog',
            'category': 'Technology',
            'img_url': 'https://example.com/image.jpg'
        })
        response = add_blog(request)
        self.assertEqual(Blog.objects.count(), 0)  # Blog should not be created

    def test_add_blog_missing_fields(self):
        # Test adding a blog with missing required fields
        request = self.factory.post('/add-blog/', {
            'title': 'Test Blog',
            'description': 'This is a test blog',
            'category': 'Technology'
        })
        request.user = User.objects.create_user(username='testuser', password='testpassword')
        response = add_blog(request)
        self.assertEqual(response.status_code, 200)  # Render addBlog.html template
        self.assertEqual(Blog.objects.count(), 0)  # Blog should not be created

    def test_add_blog_invalid_category(self):
        # Test adding a blog with an invalid category
        request = self.factory.post('/add-blog/', {
            'title': 'Test Blog',
            'description': 'This is a test blog',
            'category': 'Invalid Category',
            'img_url': 'https://example.com/image.jpg'
        })
        request.user = User.objects.create_user(username='testuser', password='testpassword')
        response = add_blog(request)
        self.assertEqual(response.status_code, 200)  # Render addBlog.html template
        self.assertEqual(Blog.objects.count(), 0)  # Blog should not be created
