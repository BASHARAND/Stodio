from .models import Albums,Siz,Type,Write,Color,ColorField,User
from django import forms
from django.core.files.storage import FileSystemStorage
from django.forms import widgets

from silling.widgets import ColorPickerWidget

from django.forms import ModelChoiceField
from django.http import HttpResponseRedirect
from colorfield.fields import ColorField
from colorfield.widgets import ColorWidget



class PostForm(forms.Form):

       
        المقاس = forms.ModelChoiceField(queryset=Siz.objects.filter())
        الخامة = forms.ModelChoiceField(queryset=Type.objects.filter())
        النقش = forms.ModelChoiceField(queryset=Write.objects.filter())
        العرسان = forms.CharField(max_length = 100)


        تحميل=forms.FileField(required=False)
        اللون= forms.CharField(label='اللون', max_length=7,
                                widget=forms.TextInput(attrs={'type': 'color'}))
        كاللون =forms.CharField(max_length=15)
        الصفحات =forms.IntegerField()

        ميني=forms.BooleanField(required=False)
        مطوية=forms.BooleanField(required=False)
        مجلة=forms.BooleanField(required=False)
        لوحة=forms.BooleanField(required=False)
        معالجة=forms.BooleanField(required=False)

class uploadf(forms.ModelForm):
        class Meta:
          model = Albums
          fields = ["file"]




#class PostForm(forms.ModelForm):
  #  class Meta:

    #
     #   fields =[

    #        "Size",
     #      "Type",
      #      "Write",
      #      "Color",
        #    "file",

      #  ]

class  Chois(forms.Form):
    المصورة = forms.ModelChoiceField(queryset=User.objects.filter(),label='Your name')


