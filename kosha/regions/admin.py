from django.contrib import admin

from kosha.regions.models import Country, Language


@admin.register(Country)
class Country(admin.ModelAdmin):
    pass


@admin.register(Language)
class NationalityAdmin(admin.ModelAdmin):
    pass
