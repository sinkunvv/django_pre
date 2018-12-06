from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=20, unique=True)
    passwd = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name
