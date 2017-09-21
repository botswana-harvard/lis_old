from django.contrib import admin
from ..models import SpecimenCondition


@admin.register(SpecimenCondition)
class SpecimenConditionAdmin(admin.ModelAdmin):

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
