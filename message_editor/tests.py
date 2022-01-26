from django.test import TestCase
from .models import Message
from django.urls import reverse, resolve
from message_editor import  views
from message_editor.views import show_all_messages

class  UserTest(TestCase):
    def setUp(self):
        message = Message(id=200,
                          userId=200,
                          title='Ahoj',
                          body='skuska')
        message.save()

    def test_user_exists(self):
        user_count = Message.objects.all().count()
        self.assertEqual(user_count, 1)



    def url_is_resolved(self):

        self.assertEqual(resolve(reverse('messages')).func,show_all_messages)

