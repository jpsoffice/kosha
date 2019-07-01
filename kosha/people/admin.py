from django.contrib import admin

from kosha.people.models import Person, Guru, GuruRole, Meeting, Address


class PresentAddressInline(admin.TabularInline):
    model = Address


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    # inlines = [PresentAddressInline,]
    fieldsets = (
        (
            "Basic details",
            {
                "fields": (
                    ("reference_number", "photo"),
                    ("name", "initiated_name", "gender"),
                    ("dob", "is_dob_ambiguous"),
                    ("dod", "life_status"),
                    ("nationality", "occupation"),
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
                    ("country"),
                    (
                        "permanent_address_line_1",
                        "permanent_address_line_2",
                        "permanent_locality",
                    ),
                    ("permanent_zipcode", "permanent_state"),
                    ("permanent_country"),
                    ("zone"),
                )
            },
        ),
        (
            "Family details",
            {"fields": (("marital_status",), ("spouse",), ("children_names",))},
        ),
        (
            "Spiritual details",
            {
                "fields": (
                    ("care_level", "relation_with_gm"),
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
            {"fields": (("life_history",), ("data_source",), ("approved",))},
        ),
    )


@admin.register(Guru)
class GuruAdmin(admin.ModelAdmin):
    pass


@admin.register(GuruRole)
class GuruRoleAdmin(admin.ModelAdmin):
    pass


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    pass
