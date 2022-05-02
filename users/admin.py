import csv
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

admin.site.unregister(Group)

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


@admin.action(description='Make csv from queryset')
def make_csv(modeladmin, request, queryset):
    with open('users_list.csv', 'w') as f:
        writer = csv.writer(f)
        for user in queryset:
            writer.writerow([user.email, user.name, user.phone, user.date_of_birth])



@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'name', 'phone', 'date_of_birth')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal data', {'fields': ('name', 'phone', 'date_of_birth')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')})
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}),
    )
    search_fields = ('email', )
    ordering = ('email', )
    actions = [make_csv]
