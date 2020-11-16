from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('searchposts/', views.searchposts, name='searchposts'),
    path('detail/<str:slug>/', views.post_detail, name='detail'),
    path('category/<str:slug>/', views.cat_detail, name='category'),

]