from django.contrib import admin

from kosha.people.models import Person, Guru, GuruRole, Temple, Meeting

# Register your models here.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Guru)
class GuruAdmin(admin.ModelAdmin):
    pass


@admin.register(GuruRole)
class GuruRoleAdmin(admin.ModelAdmin):
    pass


@admin.register(Temple)
class TempleAdmin(admin.ModelAdmin):
    pass


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    pass
