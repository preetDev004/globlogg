from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY_CHICES = {
    "ENTERTAINMENT": "Entertainment",
    "BUSINESS": "Business",
    "TECHNOLOGY": "Technology",
    "FOOD": "Food",
    "GAMES": "Games",
    "ADVENTURE": "Adventure",
    "TRAVEL":'Travel'
}

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField()
    description = models.TextField()
    category = models.CharField(
        max_length=15, default="Entertainment"
    )
    img_url = models.URLField()
    created_at = models.DateField(auto_now_add=True)
    
