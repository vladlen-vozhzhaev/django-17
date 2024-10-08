"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from myapp.views import *
urlpatterns = [
    path("", index, name="home"),
    path("article/<int:id>", article),
    path("register/", registration),
    path("login/", login_handler),
    path("add_comment/", add_comment),
    path("products/", products),
    path("product/<int:index>", product),
    path("about/", about),
    path("contact/", contact),
    path('admin/', admin.site.urls),
    path('game/', game, name="game"),
    path('pages/page1/', get_phrase1, name="get_phrase1"),
    path('pages/page2/', get_phrase2, name="get_phrase2"),
    path('handler-contact/', handlerContact),
]
