from django.contrib import admin
from django.urls import path, include
from accounts import views

app_name = 'accounts'

urlpatterns = [
    # path('accounts/', include('django.contrib.auth.urls')),
    path('login', views.loginUser, name="login_user"),
    path('signup', views.registerUser,  name="register_user"),
    path('logout', views.logoutUser, name='logout_user'),

    path('review', views.review, name='review')

   ]