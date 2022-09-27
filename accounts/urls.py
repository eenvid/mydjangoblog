from . import views
from django.urls import path


app_name = 'accounts'
urlpatterns = [
    path('signup', views.signup_view, name = 'signup'),
    path('login', views.login_view, name = 'login')
]