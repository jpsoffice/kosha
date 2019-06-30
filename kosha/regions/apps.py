from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RegionsConfig(AppConfig):
    name = "kosha.regions"
    verbose_name = _("Regions")

    def ready(self):
        try:
            import kosha.organizations.signals  # noqa F401
        except ImportError:
            pass
