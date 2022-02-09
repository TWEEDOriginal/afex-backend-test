from django.contrib import admin

from .models import Client, ClientWallet

# Register your models here.
admin.site.register(Client)
admin.site.register(ClientWallet)
