from django.urls import path
from . import views


urlpatterns = [
    path('register/' , views.registerPage , name='register_page'),
    path('login/' , views.loginPage , name='login_page'),
    path('logout/' , views.logoutPage , name='logout_page'),
    path('user/<str:pk>/' , views.userPage , name='user_page'),
]