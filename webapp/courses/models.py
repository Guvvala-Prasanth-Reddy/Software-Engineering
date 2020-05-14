from django.db import models

# Create your models here.
class course(models.Model):
    course_code = models.CharField(max_length = 10)
    course_name = models.CharField(max_length = 50)
    Description = models.TextField()
    semester    = models.IntegerField()
    Branch      = models.CharField(max_length = 4)
    

class content(models.Model): 
    course_name = models.CharField(max_length = 50)
    semester    = models.IntegerField()
    content     = models.FileField(upload_to = 'files')
    QP          = models.BooleanField(default = False)
    course_code = models.CharField(max_length = 10)
    rating      = models.IntegerField()
    Notes       = models.BooleanField(default = False)
    Textbook    =  models.BooleanField(default = False)
