from django.urls import path, include
from petstagram.pets import views


urlpatterns = [
    path('add/', views.pet_add_page, name='add-pet'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', views.show_pet_details, name='pet-details'),
        path('edit/', views.pet_edit_page, name='pet-edit'),
        path('delete/', views.pet_delete_page, name='pet-delete'),
    ])),
]