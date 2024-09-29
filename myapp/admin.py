from django.contrib import admin
from .models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "age", "deleted"]


admin.site.register(Person, PersonAdmin)
