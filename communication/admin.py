from django.contrib import admin

from .models import Communication, CommunicationMessage

admin.site.register(Communication)
admin.site.register(CommunicationMessage)

