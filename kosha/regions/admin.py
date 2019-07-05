from django.contrib import admin

from reversion.admin import VersionAdmin

from kosha.regions.models import Country, Language


@admin.register(Country)
class Country(VersionAdmin):
    pass


@admin.register(Language)
class NationalityAdmin(VersionAdmin):
    pass
