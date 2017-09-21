from django.contrib import admin
from ..models import SpecimenType


@admin.register(SpecimenType)
class SpecimenTypeAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'short_name',
        'created')

    search_fields = (
        'name',
        'short_name')

    list_filter = (
        'created',
    )
