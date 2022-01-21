from django.conf.urls import url
from django.urls import path, include
from .views import SignUpView
from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', views.profile, name='profile'),
    path('update/', views.update_profile, name='update_profile'),
]
