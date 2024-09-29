from django import forms
from django.contrib import admin
from .models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"
        widgets = {
            "first_name": forms.TextInput(attrs={"autocomplete": "off"}),
            "last_name": forms.TextInput(attrs={"autocomplete": "off"}),
        }


class PersonAdmin(admin.ModelAdmin):
    form = PersonForm

    list_display = ["id", "first_name", "last_name", "age", "deleted"]
    list_filter = ["deleted"]
    list_per_page = 5
    search_fields = ["first_name", "last_name"]
    ordering = ["-id"]
    exclude = ["deleted"]
    readonly_fields = ["deleted"]
    fields = ["first_name", "last_name", "age"]


admin.site.register(Person, PersonAdmin)
