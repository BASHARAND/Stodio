"""stodiom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from django.urls import path
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from silling.views import RegisterOrder,Albums,Albums_cus,home,upload,done,download,recive
from django.contrib.auth.views import  LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('start/', RegisterOrder),

    path('Albums', Albums),
    path('myalbums/', Albums_cus,name='myalbums'),
    path('upload/<id>', upload,name='upload'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('done/<id>/', done, name='done'),
    url(r'^download/(?P<path>.*)$', download,{'document_root':settings.MEDIA_ROOT}),
    path('rec/<id>/', recive, name='rec'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)