from django.urls import path
from . import views

urlpatterns = [
	path('', views.AppUserOverview, name='home'),
    path('create/', views.add_items, name='create'),
    path('list/', views.view_items, name='list'),
    path('update/<int:pk>/', views.update_items, name='update'),
    path('delete/<int:pk>/', views.delete_items, name='delete'),
]
