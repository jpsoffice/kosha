from django.contrib import admin

from djangoql.admin import DjangoQLSearchMixin
from reversion.admin import VersionAdmin

from kosha.people.models import Person, Guru, GuruRole, Meeting, Address, Occupation


class MeetingInline(admin.StackedInline):
    model = Meeting
    extra = 1


@admin.register(Person)
class PersonAdmin(DjangoQLSearchMixin, VersionAdmin):
    list_display = (
        "name",
        "reference_number",
        "mobile",
        "email",
        "nationality",
        "zone",
        "care_level",
        "relation_with_gm",
        "marital_status",
        "temple",
    )
    list_select_related = ("nationality", "zone", "temple", "country")
    list_filter = (
        "zone",
        "nationality",
        "country",
        "care_level",
        "relation_with_gm",
        "temple",
    )
    search_fields = ("reference_number", "name", "mobile", "email")
    readonly_fields = (
        # "reference_number",
        "approved_by",
        "approved_at",
        "created_at",
        "updated_at",
        "updated_by",
    )
    inlines = (MeetingInline,)
    fieldsets = (
        (
            "Basic details",
            {
                "fields": (
                    ("reference_number", "photo"),
                    ("name", "initiated_name", "gender"),
                    ("dob", "dob_type"),
                    ("dod", "life_status"),
                    ("nationality", "occupation"),
                    ("country",),
                    ("zone"),
                    ("marital_status"),
                    ("care_level", "relation_with_gm"),
                )
            },
        ),
        (
            "Contact details",
            {
                "fields": (
                    ("mobile", "phone", "email"),
                    ("address_line_1", "address_line_2", "locality"),
                    ("zipcode", "state"),
                    ("permanent_address_same_as_current",),
                    (
                        "permanent_address_line_1",
                        "permanent_address_line_2",
                        "permanent_locality",
                    ),
                    ("permanent_zipcode", "permanent_state"),
                    ("permanent_country"),
                )
            },
        ),
        ("Family details", {"fields": (("spouse",), ("children_names",))}),
        (
            "Spiritual details",
            {
                "fields": (
                    ("shelter_guru",),
                    ("shelter_date", "shelter_recommendation"),
                    ("shelter_place",),
                    ("first_initiation_guru",),
                    ("first_initiation_date", "first_initiation_recommendation"),
                    ("first_initiation_place",),
                    ("second_initiation_guru",),
                    ("second_initiation_date", "second_initiation_recommendation"),
                    ("second_initiation_place",),
                    ("aspiring_date",),
                    ("aspiring_place",),
                    ("is_gm_siksha_guru",),
                    ("siksha_gurus",),
                )
            },
        ),
        (
            "Devotional details",
            {
                "fields": (
                    ("kc_start_date",),
                    ("is_following_four_regs", "following_four_regs_since"),
                    ("chanting_rounds_number", "chanting_sixteen_rounds_since"),
                    ("temple", "temple_role"),
                )
            },
        ),
        (
            "Other details",
            {
                "fields": (
                    ("counselor_name", "counselor_mobile", "counselor_email"),
                    (
                        "local_care_coordinator_name",
                        "local_care_coordinator_mobile",
                        "local_care_coordinator_email",
                    ),
                    (
                        "national_care_coordinator_name",
                        "national_care_coordinator_mobile",
                        "national_care_coordinator_email",
                    ),
                    ("intensive_care",),
                )
            },
        ),
        (
            "Communication preferences",
            {
                "fields": (
                    ("contact_modes",),
                    ("communication_channels",),
                    ("subscription_topics",),
                    ("email_topics",),
                )
            },
        ),
        (
            "Office details",
            {
                "fields": (
                    ("life_history",),
                    ("data_source",),
                    ("created_at", "updated_at", "updated_by"),
                    ("approved", "approved_by", "approved_at"),
                )
            },
        ),
    )


@admin.register(Guru)
class GuruAdmin(VersionAdmin):
    pass


@admin.register(GuruRole)
class GuruRoleAdmin(VersionAdmin):
    pass


@admin.register(Meeting)
class MeetingAdmin(VersionAdmin):
    pass


@admin.register(Occupation)
class OccupationAdmin(VersionAdmin):
    pass
