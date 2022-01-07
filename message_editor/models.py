from django.db import models

class Message(models.Model):


    id = models.PositiveIntegerField(primary_key=True)
    userId = models.IntegerField()
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)

    def __str__(self):
        return "id of artist: {0} | userId: {1} | title: {2} | body: {3}".format(self.id, self.userId, self.title, self.body)
