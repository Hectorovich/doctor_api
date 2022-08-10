from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Specialization, Doctor, User


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    list_filter = ["name", "slug"]
    search_fields = ["name"]


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = [
        "name",
        "slug",
        "birth_date",
        "experience",
        "user"
    ]
    list_filter = [
        "name",
        "slug",
        "birth_date",
        "experience",
        "user"
    ]


@admin.register(User)
class UserAdmin(UserAdmin):
    pass
