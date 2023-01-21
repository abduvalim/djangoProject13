
from django.contrib import admin
from django.templatetags.static import static
from django.urls import path, include

from app.views import index, user_details, update_user, create_user, delete_user
from root import settings

urlpatterns = [
    path('', index, name='index'),
    path('user-detail/<int:user_id>', user_details, name='user-detail'),
    path('update-product/<int:user_id>', update_user, name='update-user'),
    path('create-user/<int:user_id>', create_user, name='create-user'),
    path('delete-user/<int:user_id>', delete_user, name='delete-user')
]