# admin.py
from django.contrib import admin
from .models import Product, ContactMessage
from .models import Feedback

admin.site.register(Product)
admin.site.register(ContactMessage)

admin.site.register(Feedback)