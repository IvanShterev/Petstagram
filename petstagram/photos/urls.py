from django.urls import path, include
from petstagram.photos import views


urlpatterns = [
    path('add/', views.photo_add_page, name='add-photo'),
    path('<int:pk>/', include([
        path('', views.show_photo_details, name='photo-details'),
        path('edit/', views.photo_edit_page, name='edit-photo'),
        path('delete/', views.photo_delete, name='photo-delete'),
    ]))
]