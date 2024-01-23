from django.db import models


# Create your models here.


class School(models.Model):
    name=models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    description=models.TextField()




    def __str__(self):
        return self.name



