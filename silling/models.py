from django.db import models
from colorfield.fields import ColorField
from django.contrib.auth.models import User
from silling.widgets import ColorPickerWidget
from django.forms import widgets


class Siz(models.Model):
    Siz= models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.Siz

class Type(models.Model):
    Type = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.Type


class Write(models.Model):
    Write = models.CharField(max_length=15, blank=True, null=True)
    #file= models.FileField(upload_to='media')

    def __str__(self):
        return self.Write
class Photographers(models.Model):
    Fname = models.CharField(max_length=15, blank=True, null=True)
    Lname = models.CharField(max_length=15)
    Address = models.CharField(max_length=15, blank=True, null=True)
    Phone = models.CharField(max_length=15)

    def __str__(self):
        return self.Fname
class Albums(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Size = models.CharField(max_length=15, blank=True, null=True)
    Type = models.CharField(max_length=15, blank=True, null=True)
    Color = ColorField(default='#FF0000')
    Colorw=models.CharField(max_length=15,blank=True,null=True)
    Write = models.CharField(max_length=15, blank=True, null=True)
    Hasbands = models.CharField(max_length=30, blank=True, null=True)
    file= models.FileField(upload_to='media',blank=True, null=True)
    state=models.IntegerField(max_length=2,default=0)
    many=models.BooleanField(default=False)
    fold=models.BooleanField(default=False)
    mag=models.BooleanField(default=False)
    board=models.BooleanField(default=False)
    photoshop=models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    Countp=models.IntegerField(default=10)
    def __str__(self):
        return self.Size


# Create your model her
class Color(models.Model):
    Color = ColorField(default='#FF0000')

    def __str__(self):
        return self.Color
class ColorField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        super(ColorField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = ColorPickerWidget
        return super(ColorField, self).formfield(**kwargs)