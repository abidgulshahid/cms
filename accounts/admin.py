from django.contrib import admin
from django.contrib.auth import get_user_model
from .forms import *
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(BS)
admin.site.register(announcments)



class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username','email','password']

admin.site.register(CustomUser, CustomUserAdmin)
