from django.urls import path

from . import views


urlpatterns = [
    path('' , views.indexPage , name='index_page'),
    path('about/' , views.aboutPage , name='about_page'),
]