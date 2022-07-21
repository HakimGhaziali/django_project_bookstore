from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm , CustpmUdserChangeForm


class CustomUserAdmin(UserAdmin):

    add_form= CustomUserCreationForm
    form = CustpmUdserChangeForm
    model = CustomUser
    list_display = ['username','email','age']
    fieldsets= UserAdmin.fieldsets + (

        (None , {'fields':('age',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets  + (

        (None , {'fields':('age',)}),
    )



admin.site.register(CustomUser,CustomUserAdmin)

