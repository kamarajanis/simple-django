from django.urls import path
from hello_world import views
from django.conf.urls import include

urlpatterns = [path('', views.hello_world, name='hello_world'),]