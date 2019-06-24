from django.conf import settings
from django.db.models import (
    Model,
    CharField,
    ImageField,
    DateField,
    ForeignKey,
    OneToOneField,
    ManyToManyField,
    BooleanField,
    PositiveIntegerField,
    EmailField,
    TextField,
    SET_NULL,
)
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from multiselectfield import MultiSelectField
from places.fields import PlacesField

from kosha.useful.validators import phone_regex
from kosha.users.models import User

GENDER_CHOICES = (("M", "Male"), ("F", "Female"), ("O", "Others"))

NATIONALITY_CHOICES = (("IN", "India"),)

OCCUPATION_CHOICES = (("IT", "Information Technology"),)

MARITAL_STATUS_CHOICES = (
    ("SGL", "Single"),
    ("ENG", "Engaged"),
    ("SKG", "Seeking"),
    ("MRD", "Married"),
    ("SEP", "Separated"),
    ("DIV", "Divorced"),
    ("WID", "Widow"),
)

CARE_LEVEL_CHOICES = (
    ("A", "Aspiring"),
    ("Z", "Shelter"),
    ("D1", "Harinam"),
    ("D2", "Brahmin"),
    ("S", "Siksha"),
    ("BTG", "Back to Godhead"),
)

RELATION_WITH_GM_CHOICES = (("SS", "Spiritual son"), ("SD", "Spiritual daughter"))

OUTSIDE_INITIATION_BY_CHOICES = (
    ("VG", "Vaishnava Guru"),
    ("NVG", "Non Vaishnava Guru"),
)

TEMPLE_ROLE_CHOICES = (("FT", "Full time"), ("NM", "Namhatta"))

CONTACT_MODE_CHOICES = (("CP", "Congregational Preaching"),)

COMMUNICATION_CHANNEL_CHOICES = (("JPSFB", "JPS Facebook"),)

SUBSCRIPTION_TOPIC_CHOICES = (("JPSB", "JPS Books"),)

EMAIL_TOPIC_CHOICES = (("NM", "Namhatta"), ("BV", "Bhakti Vriksha"))


class GuruRole(Model):
    name = CharField(max_length=50)

    class Meta:
        db_table = "guru_role"


class Guru(Model):
    name = CharField(max_length=255, help_text=_("Name"))
    legal_name = CharField(max_length=255, blank=True, help_text=_("Legal name"))
    user = OneToOneField(
        User, null=True, blank=True, on_delete=SET_NULL, help_text=_("User")
    )
    roles = ManyToManyField(GuruRole, blank=True)

    class Meta:
        db_table = "guru"


# Create your models here.
class Person(Model):

    # Basic fields
    reference_number = CharField(
        max_length=10,
        unique=True,
        help_text=_("Unique reference number for the devotee"),
    )
    name = CharField(max_length=100, help_text=_("Name"))
    initiated_name = CharField(
        max_length=100, blank=True, default="", help_text=_("Initiated name")
    )
    photo = ImageField(max_length=100, blank=True, null=True, help_text=_("Photo"))
    gender = CharField(max_length=1, choices=GENDER_CHOICES, help_text=_("Gender"))
    dob = DateField(blank=True, null=True, help_text=_("Date of birth"))
    is_dob_ambiguous = BooleanField(
        default=False, help_text=_("Is date of birth ambiguous?")
    )
    #  age
    nationality = CharField(
        max_length=3, choices=NATIONALITY_CHOICES, help_text=_("Nationality")
    )
    occupation = CharField(
        max_length=3, choices=OCCUPATION_CHOICES, help_text=_("Occupation")
    )

    # Contact details

    # Present address

    # Permanent address

    marital_status = CharField(
        max_length=3, choices=MARITAL_STATUS_CHOICES, help_text=_("Marital status")
    )
    spouse = CharField(
        max_length=100, blank=True, default="", help_text=_("Spouse name")
    )
    children_names = CharField(
        max_length=500, blank=True, default="", help_text=_("Names of children")
    )

    # Spiritual details
    # -------------------------------------------------------------------------

    care_level = CharField(
        max_length=3, choices=CARE_LEVEL_CHOICES, help_text=_("Care level")
    )
    relation_with_gm = CharField(
        max_length=3,
        choices=RELATION_WITH_GM_CHOICES,
        help_text=_("Relation with Guru Maharaj"),
    )

    # shelter details
    shelter_guru = ForeignKey(
        Guru,
        blank=True,
        null=True,
        on_delete=SET_NULL,
        related_name="sheltered_disciples",
        help_text=_("Shelter Guru"),
    )
    shelter_place = PlacesField(blank=True, null=True, help_text=_("Shelter place"))
    shelter_date = DateField(blank=True, null=True, help_text=_("Shelter date"))
    shelter_recommendation = CharField(
        max_length=200,
        blank=True,
        default="",
        help_text=_("Recommended for shelter by"),
    )

    # First initiation details
    first_initiation_guru = ForeignKey(
        Guru,
        blank=True,
        null=True,
        on_delete=SET_NULL,
        related_name="first_initiation_disciples",
        help_text=_("First initiation Guru"),
    )
    first_initiation_place = PlacesField(
        blank=True, null=True, help_text=_("First initiation place")
    )
    first_initiation_date = DateField(
        blank=True, null=True, help_text=_("First initiation date")
    )
    first_initiation_recommendation = CharField(
        max_length=200,
        blank=True,
        default="",
        help_text=_("Recommended for first initiation by"),
    )

    # Second initiation details
    second_initiation_guru = ForeignKey(
        Guru,
        blank=True,
        null=True,
        on_delete=SET_NULL,
        related_name="second_initiation_disciples",
        help_text=_("Second initiation Guru"),
    )
    second_initiation_place = PlacesField(
        blank=True, null=True, help_text=_("Second initiation place")
    )
    second_initiation_date = DateField(
        blank=True, null=True, help_text=_("Second initiation date")
    )
    second_initiation_recommendation = CharField(
        max_length=200,
        blank=True,
        default="",
        help_text=_("Recommended for second initiation by"),
    )

    # Aspiring details
    aspiring_date = DateField(blank=True, null=True, help_text=_("Aspiring date"))
    aspiring_place = PlacesField(blank=True, null=True, help_text=_("Aspiring place"))

    # Outside initiation
    outside_initiation_by = CharField(
        choices=OUTSIDE_INITIATION_BY_CHOICES,
        max_length=3,
        blank=True,
        default="",
        help_text=_("Initiation by outside gurus"),
    )
    outside_initiation_community = CharField(
        max_length=255,
        blank=True,
        default="",
        help_text=_(
            "Name of the Sampradaya/Math/Guru/Group/Religious organization/Ritvik Guru of initiation"
        ),
    )

    is_gm_siksha_guru = BooleanField(help_text=_("Is Guru Maharaj siksha guru?"))

    # Sisksha gurus
    siksha_gurus = ManyToManyField(Guru, blank=True, help_text=_("Siksha gurus"))

    # Devotional details
    # -------------------------------------------------------------------------
    # devotional_services = ManyToManyField(DevotionalService, blank=True, null=True, help_text=_("Devotional services"))
    kc_start_date = DateField(
        blank=True, null=True, help_text=_("Start date for Krishna Consciousness")
    )
    is_following_four_regs = BooleanField(
        blank=True, null=True, help_text=_("Is following 4 regulative principles?")
    )
    following_four_regs_since = DateField(
        blank=True, null=True, help_text=_("Following 4 regulative principles since")
    )
    chanting_rounds_number = PositiveIntegerField(
        blank=True, null=True, help_text=_("Number of rounds chanting")
    )
    chanting_sixteen_rounds_since = DateField(
        blank=True, null=True, help_text=_("Chanting 16 rounds since")
    )

    # Temple details
    # -------------------------------------------------------------------------
    temple = ForeignKey(
        "Temple",
        blank=True,
        null=True,
        on_delete=SET_NULL,
        related_name="people",
        help_text=_("Temple connected with"),
    )
    temple_role = CharField(
        max_length=3,
        choices=TEMPLE_ROLE_CHOICES,
        blank=True,
        default="",
        help_text=_("Temple connection mode"),
    )

    # meetings back referenced from Meeting model

    # Other details
    # -------------------------------------------------------------------------

    # Counselor details
    counselor_name = CharField(
        max_length=255, blank=True, default="", help_text=_("Name of counselor")
    )
    counselor_mobile = CharField(
        validators=[phone_regex],
        max_length=17,
        blank=True,
        null=True,
        help_text=_("Mobile number of counselor"),
    )
    counselor_email = EmailField(
        blank=True, null=True, help_text=_("Email of counselor")
    )

    # Local care coordinator details
    local_care_coordinator_name = CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text=_("Name of local care coordinator"),
    )
    local_care_coordinator_mobile = CharField(
        validators=[phone_regex],
        max_length=17,
        blank=True,
        null=True,
        help_text=_("Mobile number of local care coordinator"),
    )
    local_care_coordinator_email = EmailField(
        blank=True, null=True, help_text=_("Email of local care coordinator")
    )

    # National care coordinator details
    national_care_coordinator_name = CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text=_("Name of national care coordinator"),
    )
    national_care_coordinator_mobile = CharField(
        validators=[phone_regex],
        max_length=17,
        blank=True,
        null=True,
        help_text=_("Mobile number of national care coordinator"),
    )
    national_care_coordinator_email = EmailField(
        blank=True, null=True, help_text=_("Email of national care coordinator")
    )

    # Communication preferences
    # -------------------------------------------------------------------------
    contact_modes = MultiSelectField(
        choices=CONTACT_MODE_CHOICES,
        blank=True,
        null=True,
        help_text=_("Modes for contact"),
    )
    communication_channels = MultiSelectField(
        choices=COMMUNICATION_CHANNEL_CHOICES,
        blank=True,
        null=True,
        help_text=_("Channels for communuication"),
    )
    subscription_topics = MultiSelectField(
        choices=SUBSCRIPTION_TOPIC_CHOICES,
        blank=True,
        null=True,
        help_text=_("Topics subscribed to"),
    )
    email_topics = MultiSelectField(
        choices=EMAIL_TOPIC_CHOICES,
        blank=True,
        null=True,
        help_text=_("Topics subscribed via email"),
    )

    class Meta:
        db_table = "person"


class Meeting(Model):
    date = DateField()
    place = PlacesField()
    summary = TextField(max_length=1024, default="", help_text=_("Meeting summary"))
    guru = ForeignKey(
        Guru,
        null=True,
        on_delete=SET_NULL,
        related_name="people_meetings",
        default=settings.GURU_MAHARAJ_ID,
    )
    person = ForeignKey(Person, null=True, related_name="meetings", on_delete=SET_NULL)

    class Meta:
        db_table = "meeting"


class Temple(Model):
    name = CharField(max_length=255)

    class Meta:
        db_table = "temple"
