from . import views
from django.urls import path

app_name='school_app'
urlpatterns = [

    path('',views.index,name='index'),






]
