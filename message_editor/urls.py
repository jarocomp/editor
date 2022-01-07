from django.urls import path
from . import views

urlpatterns = [
    #path("", views.index, name="message_list"),
   path("", views.download_data, name="users"),
]