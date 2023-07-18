from django.contrib import admin
from .models import Destination, Spot, List # import the Artist model from models.py
# Register your models here.

admin.site.register(Destination) # this line will add the model to the admin panel
admin.site.register(Spot)
admin.site.register(List)
# admin.site.register(User)
# admin.site.register(Review)