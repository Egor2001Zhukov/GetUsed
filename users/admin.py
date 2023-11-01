from django.contrib import admin

from users import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email',)
