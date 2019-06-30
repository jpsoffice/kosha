from django.db.models import Model, CharField, PositiveIntegerField
from django.utils.translation import ugettext_lazy as _


class Country(Model):
    name = CharField(max_length=255, unique=True, db_index=True, help_text=_("Name"))
    code = CharField(max_length=3, unique=True, db_index=True, help_text=_("Code"))
    iso_code = PositiveIntegerField(unique=True, db_index=True, help_text=_("ISO code"))
    nationality = CharField(
        max_length=255, unique=True, db_index=True, help_text=_("Nationality")
    )

    class Meta:
        db_table = "country"

    def __str__(self):
        return "{} ({})".format(self.name, self.code)


class Language(Model):
    name = CharField(max_length=255, unique=True, db_index=True, help_text=_("Name"))
    code = CharField(max_length=3, unique=True, db_index=True, help_text=_("Code"))

    class Meta:
        db_table = "language"

    def __str__(self):
        return "{} {}".format(self.name, self.code)
