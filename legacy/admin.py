from django.contrib import admin

from .models import Clientes, Os


class ClientesAdmin(admin.ModelAdmin):
    using = "legacy_db"

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'other' database.
        return super().get_queryset(request).using(self.using)

    list_display = (
    "cli_codigo", "cli_nomefantasia_nomecomercial", "full_fone")


class OsAdmin(admin.ModelAdmin):
    using = "legacy_db"

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    list_display = ("os_codigo", "cli_codigo", "os_dataabertura", "os_status")


admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Os, OsAdmin)
