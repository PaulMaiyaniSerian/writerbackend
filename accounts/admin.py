from django.contrib import admin

# Register your models here.
from .models import User, UserWallet

admin.site.register(User)
admin.site.register(UserWallet)