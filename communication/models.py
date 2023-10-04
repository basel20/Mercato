from django.db import models
from django.contrib.auth.models import User

from item.models import Item

class Communication(models.Model):
    item = models.ForeignKey(Item, related_name='communications', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='communications')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    class Mate:
        ordering = ('-modified_at',)


class CommunicationMessage(models.Model):
    communication = models.ForeignKey(Communication, related_name='messages', on_delete=models.CASCADE) 
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)
