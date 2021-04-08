from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Carousels,Products,Customer,Order

admin.site.register(Carousels)
admin.site.register(Products)
admin.site.register(Customer)
admin.site.register(Order )