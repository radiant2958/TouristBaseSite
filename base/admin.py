from django.contrib import admin

from .models import Booking, Client, News

admin.site.register(Client)
admin.site.register(Booking)
admin.site.register(News)
