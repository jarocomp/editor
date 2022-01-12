from django.urls import path
from . import views

urlpatterns = [
    #path("", views.index, name="message_list"),
   path("/", views.show_data, name="messages"),
   path("create_message/", views.CreateMessage.as_view(), name="new_message"),
   path('show_message/<id>', views.show_message, name='show-message'),
   path("search_message/", views.search_message, name="search-message"),
   path('update_message/<id>', views.update_message, name='update-message'),
]