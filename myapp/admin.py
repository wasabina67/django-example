from django.contrib import admin
from .models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "age", "deleted"]
    list_filter = ["deleted"]
    list_per_page = 5
    search_fields = ["first_name", "last_name"]


admin.site.register(Person, PersonAdmin)
