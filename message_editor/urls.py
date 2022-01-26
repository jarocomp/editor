from django.urls import path
from . import views

urlpatterns = [
   path("", views.show_all_messages, name="messages"),
   path("home/", views.home, name="home"),
   path("create_message/", views.CreateMessage.as_view(), name="new-message"),
   path('show_message/<id>', views.show_message, name='show-message'),
   path("search_message/", views.search_message, name="search-message"),
   path('update_message/<id>', views.update_message, name='update-message'),
   path('delete_message/<id>', views.delete_message, name='delete-message'),
   path('test_data', views.test_data, name='test-data'),
   path('test_users', views.test_users, name='test-users'),
]