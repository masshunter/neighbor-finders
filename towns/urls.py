from django.urls import path
from . import views

urlpatterns = {
    path('', views.post_list, name='post_list'),
    path('towns/', views.town_list, name='town_list'),
}
