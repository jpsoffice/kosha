from django.db.models import Model, CharField
from django.utils.translation import ugettext_lazy as _


class Zone(Model):
    name = CharField(max_length=100, unique=True, help_text=_("Name"))

    class Meta:
        db_table = "zone"

    def __str__(self):
        return self.name


class Temple(Model):
    name = CharField(max_length=255)

    class Meta:
        db_table = "temple"

    def __str__(self):
        return self.name
