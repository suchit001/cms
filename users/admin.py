from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Documents

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'name', 'gender', 'sq', 'sa', 'bd','fname', 'phoneno', 'lname','profpic', 'address' ]
    list_editable = [ 'username', 'name', 'gender', 'sq', 'sa', 'bd','fname', 'phoneno', 'lname','profpic']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Documents)
