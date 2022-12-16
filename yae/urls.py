from django.urls import path
from . import views

app_name = 'yae'

urlpatterns = [
    path('', views.home, name='home'),
    path('docs/',views.docs, name='docs'),
    path('dash/',views.dash, name='dash'),
    path('signup/',views.signup, name='register'),
]
