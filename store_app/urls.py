from . import views
from django.urls import path

urlpatterns = [

    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('commerce/', views.commerce, name='commerce'),
    path('chemistry/', views.chemistry, name='chemistry'),

    path('phy/', views.phy, name='phy'),

    path('eco/', views.eco, name='eco'),

    path('eng/', views.eng, name='eng'),
    path('computer/', views.computer, name='computer'),
    path('Detail/', views.Detail, name="Detail"),
    path('index/', views.index, name='index'),

]