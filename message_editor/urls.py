from django.urls import path
from . import views

urlpatterns = [
    #path("", views.index, name="message_list"),
   path("", views.show_data, name="users"),
]