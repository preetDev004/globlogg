from django.db import models
from django.contrib.auth.models import User

# Blog model
class Blog(models.Model):
    # using django's inbuilt User model
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField()
    description = models.TextField()
    category = models.CharField(
        max_length=15, default="Entertainment"
    )
    img_url = models.URLField()
    created_at = models.DateField(auto_now_add=True)
    
