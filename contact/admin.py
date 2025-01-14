# admin.py
from django.contrib import admin
from .models import Product, ContactMessage
from .models import Feedback, Farmer

admin.site.register(Product)
admin.site.register(ContactMessage)
admin.site.register(Farmer)
admin.site.register(Feedback)