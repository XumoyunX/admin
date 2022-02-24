from django.db import models

# Create your models here.


class Team(models.Model):
    images = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=250)
    text = models.CharField(max_length=250)
    telegram = models.CharField(max_length=250)
    instagram = models.CharField(max_length=250)
    fecebook = models.CharField(max_length=250)
    linkedin = models.CharField(max_length=250)



class Edu(models.Model):
    images = models.ImageField(upload_to="images/")
    name = models.CharField(max_length=250)
    text = models.TextField()




class Portfolio(models.Model):
    images = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=250)
    clinet = models.CharField(max_length=250)
    project = models.CharField(max_length=250)
    project_url = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    text = models.TextField()


class Blog(models.Model):
    images = models.ImageField(upload_to="images/")
    name = models.TextField()
    text = models.TextField()
    images1 = models.ImageField(upload_to="images/")
    name1 = models.TextField()
    text1 = models.TextField()