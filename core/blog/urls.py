from django.urls import path
from blog import views

urlpatterns = [
    path('account/register', views.UserCreate.as_view()),
]
