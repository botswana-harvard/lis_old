from django.contrib import admin

from ..models import Client


class ClientAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "ip",
        "label_printer",
    )

admin.site.register(Client, ClientAdmin)


class ClientInline(admin.TabularInline):

    model = Client
    extras = 3
