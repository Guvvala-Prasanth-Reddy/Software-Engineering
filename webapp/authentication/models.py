from django.db import models

# Create your models here.
class speical_user_access(models.Model):
    user_name = models.CharField(max_length = 150)
