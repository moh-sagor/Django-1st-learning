
from django.contrib import admin
from django.urls import path
from first_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index,name='index'),
    path('contact/', views.contact,name='contact'),
    path('',views.index,name='index'),
]
