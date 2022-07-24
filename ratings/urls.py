from django.urls import path
from . import views

urlpatterns = [
	path('', views.RatingOverview, name='home'),
    path('create/', views.add_items, name='create'),
    path('list/', views.view_items, name='list'),
    path('fetch/<int:user_id>/<int:song_id>/', views.get_item, name='get'),
    path('update/<int:pk>/', views.update_items, name='update'),
    path('delete/<int:pk>/', views.delete_items, name='delete'),
]
