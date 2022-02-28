import os.path
from django.conf import settings

from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
#from django.views.generic import CreateView,ListView
#from django.urls import reverse_lazy
#from datetime import datetime,timedelta

from django.http import HttpResponse
#from django.urls import reverse
#from django.views.generic import TemplateView
from . import models
from django.contrib.auth.decorators import login_required
from .forms import PostForm,uploadf,Chois
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
#from django.http import StreamingHttpResponse
#from WSGIREF.UTIL import filewrapper
#import mimetypes
@login_required
def home(request):
    form = Chois(request.POST or None, request.FILES or None)
    user = request.user
    a = user.id
    if request.method == 'GET':
        context = {
            'form': form,'a':a

        }
        return render(request, 'home.html', context)

    else:

         form = Chois(request.POST or None, request.FILES or None)
         if form.is_valid():

           s = form.cleaned_data['المصورة']
           A = models.User.objects.get(username=s)
           m=A.id
           All_albums=models.Albums.objects.filter(user=m)

           context = {'orders': All_albums}

           return render(request, 'All_Albums1.html', context)
# Create your views here.
@login_required
def RegisterOrder(request):

    prod = PostForm(request.POST or None, request.FILES or None)


    if request.method=='GET':
        return render(request, 'Addalbums.html', {'form': prod})
    else:
        user = request.user
        a = user.id
        if prod.is_valid():


            table = models.Albums()
            table.user_id= a
            table.Type = prod.cleaned_data['الخامة']
            table.Size = prod.cleaned_data['المقاس']
            table.Write = prod.cleaned_data['النقش']
            table.Color= prod.cleaned_data['اللون']
            table.Colorw=prod.cleaned_data['كاللون']
            table.Countp=prod.cleaned_data['الصفحات']
            table.file= prod.cleaned_data['تحميل']
            table.fold= prod.cleaned_data['مطوية']
            table.mag= prod.cleaned_data['مجلة']
            table.board= prod.cleaned_data['لوحة']
            table.many= prod.cleaned_data['ميني']
            table.photoshop= prod.cleaned_data['معالجة']

            table.Hasbands = prod.cleaned_data['العرسان']



            table.save()
            return redirect('/')


def Albums(request):
    All_albums = models.Albums.objects.filter(state=0).select_related()


    context = { 'orders':All_albums}

    return render(request, 'All_Albums.html', context)

def Albums_cus(request):
    user = request.user
    s = user.id
    if s==1 :
      All_albums = models.Albums.objects.all()
    else:
       All_albums = models.Albums.objects.filter(user_id=s).select_related()

    context = { 'orders':All_albums}

    return render(request, 'cus_Albums.html', context)
def upload(request,id):
      user = request.user
      s = user.id
    # return All
      All =models.Albums.objects.get(user_id=s, id=id)
      d=All.file
      if d =='':


        form = uploadf(instance=All)
        if request.method == 'POST':
            form = uploadf(request.POST,request.FILES ,instance=All)
            if form.is_valid():
                 form.save()

        context = {
            'form': form,

        }
        return render(request, 'upload.html', context)
      else:
          return redirect('')

def done(request,id):
    post1 = models.Albums.objects.filter(id=id)
    post1.delete()
    return redirect('/')
def download(request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response=HttpResponse(fh.read(),content_type="application/file")
            response['content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response
        raise Http404
def recive(request,id):

    post1 = models.Albums.objects.filter(id=id).update(state=1)
    return redirect('/')