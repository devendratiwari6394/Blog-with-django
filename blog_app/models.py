from django.db import models
from django.conf import settings

# Create your models here.

class Blog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    blog_title = models.CharField(max_length=50)
    blog_content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,   # ← THIS IS KEY
        on_delete=models.CASCADE,
        related_name="blogs"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog_title