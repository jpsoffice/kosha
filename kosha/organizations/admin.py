from django.contrib import admin

from kosha.organizations.models import Temple, Zone


@admin.register(Temple)
class TempleAdmin(admin.ModelAdmin):
    pass


@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    pass
