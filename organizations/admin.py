from django.contrib import admin
from reversion.admin import VersionAdmin

from kosha.organizations.models import Temple, Zone


@admin.register(Temple)
class TempleAdmin(VersionAdmin):
    pass


@admin.register(Zone)
class ZoneAdmin(VersionAdmin):
    pass
