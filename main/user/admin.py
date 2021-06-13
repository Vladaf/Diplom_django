from django.contrib import admin
from user.models import User

class AdminUser(admin.ModelAdmin):
    list_display = ["username", "is_musician"]

admin.site.register(User, AdminUser)
