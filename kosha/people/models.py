import datetime
import json

from iso3166 import countries

from django.conf import settings
from django.db.models import (
    Model,
    CharField,
    ImageField,
    DateField,
    DateTimeField,
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
from django.utils.encoding import smart_text
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from places.fields import PlacesField as _PlacesField

from kosha.useful.validators import phone_regex
from kosha.useful.models import BaseModel
from kosha.users.models import User

GENDER_CHOICES = (("M", "Male"), ("F", "Female"), ("O", "Others"))

DOB_TYPE_CHOICES = (("A", "Actual"), ("C", "Calculated"))

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
    ("RTK", "Ritvik"),
    ("GB/S", "God brother or sister"),
    ("Ex-D", "Ex Disciple"),
    ("G", "Guidance"),
    ("H", "Help"),
    ("I", "Interest"),
    ("PB", "Prayers and blessings"),
    ("M", "Mission"),
    ("U", "Unofficial siksha"),
    ("C", "Special care"),
    ("W", "Write questions"),
    ("P", "Prayers"),
    ("SN", "Spiritual nephew/niece"),
)

RELATION_WITH_GM_CHOICES = (
    ("SS", "Spiritual son"),
    ("SD", "Spiritual daughter"),
    ("SNE", "Spiritual nephew"),
    ("SNI", "Spiritual niece"),
    ("SSB", "Spiritual son bhakta"),
    ("SDB", "Spiritual daughter bhaktin"),
    ("SKD", "Siksha disciple"),
    ("BTA", "Bhakta"),
    ("BTI", "Bhaktin"),
    ("WW", "Well wisher"),
)

OUTSIDE_INITIATION_BY_CHOICES = (
    ("VG", "Vaishnava Guru"),
    ("NVG", "Non Vaishnava Guru"),
)

TEMPLE_ROLE_CHOICES = (("FT", "Full time"), ("NM", "Namhatta"))

LIFE_STATUS_CHOICES = (
    ("AC", "Active"),
    ("IN", "Inactive"),
    ("LO", "Lost"),
    ("PA", "Passed away"),
)

DATA_SOURCE_CHOICES = (
    ("IF", _("Initiation form")),
    ("SF", _("Shelter form")),
    ("AF", _("Aspiring form")),
    ("INB", _("INB")),
)


class PlacesField(_PlacesField):
    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return smart_text(value)


class GuruRole(BaseModel):
    name = CharField(max_length=50, unique=True, db_index=True)

    class Meta:
        db_table = "guru_role"

    def __str__(self):
        return self.name.title()


class Guru(BaseModel):
    name = CharField(max_length=255, unique=True, db_index=True, help_text=_("Name"))
    code = CharField(max_length=5, unique=True, null=True, db_index=True)
    legal_name = CharField(
        max_length=255, blank=True, null=True, help_text=_("Legal name")
    )

    user = OneToOneField(
        User,
        null=True,
        blank=True,
        on_delete=SET_NULL,
        db_index=True,
        help_text=_("User"),
    )
    roles = ManyToManyField(GuruRole, blank=True)

    class Meta:
        db_table = "guru"

    def __str__(self):
        return self.code


class Person(BaseModel):

    # Basic fields
    reference_number = CharField(
        max_length=15,
        unique=True,
        db_index=True,
        help_text=_("Unique reference number for the devotee"),
    )
    name = CharField(max_length=100, db_index=True, help_text=_("Name"))
    initiated_name = CharField(
        max_length=100,
        blank=True,
        default="",
        db_index=True,
        help_text=_("Initiated name"),
    )
    photo = ImageField(max_length=100, blank=True, null=True, help_text=_("Photo"))
    gender = CharField(
        max_length=1, choices=GENDER_CHOICES, db_index=True, help_text=_("Gender")
    )
    dob = DateField(verbose_name=_("Date of birth"), blank=True, null=True)
    dob_type = CharField(
        max_length=1,
        choices=DOB_TYPE_CHOICES,
        null=True,
        default="A",
        db_index=True,
        verbose_name=_("Date of birth type"),
    )
    dod = DateField(blank=True, null=True, verbose_name=_("Date of death"))
    life_status = CharField(
        max_length=2,
        choices=LIFE_STATUS_CHOICES,
        blank=True,
        null=True,
        db_index=True,
        help_text=_("Life status"),
    )
    #  age
    nationality = ForeignKey(
        "regions.Nationality",
        blank=True,
        null=True,
        to_field="nationality",
        related_name="nationals",
        on_delete=SET_NULL,
        db_index=True,
        help_text=_("Nationality"),
    )
    occupation = ForeignKey(
        "Occupation",
        blank=True,
        null=True,
        on_delete=SET_NULL,
        db_index=True,
        help_text=_("Occupation"),
    )

    # Contact details
    # -------------------------------------------------------------------------
    mobile = CharField(
        validators=[phone_regex],
        max_length=17,
        blank=True,
        null=True,
        db_index=True,
        help_text=_("Mobile number"),
    )
    phone = CharField(
        validators=[phone_regex],
        max_length=17,
        blank=True,
        null=True,
        db_index=True,
        help_text=_("Phone number"),
    )
    email = EmailField(blank=True, null=True, db_index=True, help_text=_("Email "))

    # Present address
    address_line_1 = CharField(
        max_length=100, blank=True, null=True, help_text=_("Address line 1")
    )
    address_line_2 = CharField(
        max_length=100, blank=True, null=True, help_text=_("Address line 2")
    )
    zipcode = CharField(
        max_length=10, blank=True, null=True, db_index=True, help_text=_("Zipcode")
    )
    locality = CharField(
        max_length=100,
        blank=True,
        null=True,
        db_index=True,
        help_text=_("Locality (City, town or village)"),
    )
    district = CharField(max_length=100, blank=True, null=True, db_index=True)
    state = CharField(
        max_length=255, blank=True, null=True, db_index=True, help_text=_("State")
    )
    country = ForeignKey(
        "regions.Country",
        null=True,
        related_name="present_persons",
        on_delete=SET_NULL,
        db_index=True,
        help_text=_("Country"),
    )

    # Permanent address
    permanent_address_same_as_current = BooleanField(default=True)
    permanent_address_line_1 = CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=_("Permanent address line 1"),
    )
    permanent_address_line_2 = CharField(
        max_length=100,
        blank=True,
        null=True,
        default="",
        verbose_name=_("Permanent address line 2"),
    )
    permanent_zipcode = CharField(
        max_length=10, blank=True, null=True, verbose_name=_("Permanent zipcode")
    )
    permanent_locality = CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=_("Permanent locality"),
        help_text=_("Permanent Locality (City, town or village)"),
    )
    permanent_district = CharField(max_length=100, blank=True, null=True)
    permanent_state = CharField(
        max_length=255, blank=True, null=True, verbose_name=_("Permanent state")
    )
    permanent_country = ForeignKey(
        "regions.Country",
        blank=True,
        null=True,
        related_name="permanent_persons",
        on_delete=SET_NULL,
        help_text=_("Permanent country"),
    )

    zone = ForeignKey(
        "organizations.Zone",
        blank=True,
        null=True,
        on_delete=SET_NULL,
        db_index=True,
        help_text=_("Zone"),
    )

    # Family details
    # -------------------------------------------------------------------------

    marital_status = CharField(
        max_length=3,
        choices=MARITAL_STATUS_CHOICES,
        db_index=True,
        help_text=_("Marital status"),
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
        max_length=5,
        choices=CARE_LEVEL_CHOICES,
        db_index=True,
        help_text=_("Care level"),
    )
    relation_with_gm = CharField(
        max_length=3,
        verbose_name=_("Relation with Guru Maharaj"),
        choices=RELATION_WITH_GM_CHOICES,
        db_index=True,
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
    shelter_place = PlacesField(
        blank=True, null=True, db_index=True, help_text=_("Shelter place")
    )
    shelter_date = DateField(
        blank=True, null=True, db_index=True, help_text=_("Shelter date")
    )
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
        blank=True, null=True, db_index=True, help_text=_("First initiation place")
    )
    first_initiation_date = DateField(
        blank=True, null=True, db_index=True, help_text=_("First initiation date")
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
        blank=True, null=True, db_index=True, help_text=_("Second initiation place")
    )
    second_initiation_date = DateField(
        blank=True, null=True, db_index=True, help_text=_("Second initiation date")
    )
    second_initiation_recommendation = CharField(
        max_length=200,
        blank=True,
        default="",
        help_text=_("Recommended for second initiation by"),
    )

    # Aspiring details
    aspiring_date = DateField(
        blank=True, null=True, db_index=True, help_text=_("Aspiring date")
    )
    aspiring_place = PlacesField(
        blank=True, null=True, db_index=True, help_text=_("Aspiring place")
    )

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

    is_gm_siksha_guru = BooleanField(
        blank=True,
        null=True,
        db_index=True,
        verbose_name=_("Is Guru Maharaj Siksha Guru"),
    )

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
        "organizations.Temple",
        blank=True,
        null=True,
        on_delete=SET_NULL,
        related_name="people",
        db_index=True,
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

    intensive_care = BooleanField(
        blank=True, null=True, help_text=_("Is intensive care needed?")
    )

    # Communication preferences
    # -------------------------------------------------------------------------
    contact_modes = ManyToManyField(
        "ContactMode", blank=True, help_text=_("Modes for contact")
    )
    communication_channels = ManyToManyField(
        "CommunicationChannel", blank=True, help_text=_("Channels for communuication")
    )
    subscription_topics = ManyToManyField(
        "SubscriptionTopic", blank=True, help_text=_("Topics subscribed to")
    )
    email_topics = ManyToManyField(
        "EmailTopic", blank=True, help_text=_("Topics subscribed via email")
    )

    # Office
    # -------------------------------------------------------------------------
    # office_notes = ManyToManyField('note.Note')
    # gm_notes = ManyToManyField('note.Note', verbose_name='Guru Maharaj notes')
    life_history = TextField(
        max_length=2048,
        blank=True,
        default="",
        help_text=_("Life history of the person"),
    )
    data_source = CharField(
        max_length=3, choices=DATA_SOURCE_CHOICES, blank=True, null=True
    )

    updated_by = ForeignKey(
        "users.User",
        blank=True,
        null=True,
        editable=False,
        related_name="+",
        on_delete=SET_NULL,
        help_text="Updated by user",
    )
    approved = BooleanField(blank=True, null=True)
    approved_by = ForeignKey(
        "users.User",
        blank=True,
        null=True,
        editable=False,
        related_name="+",
        on_delete=SET_NULL,
        help_text="Approved by user",
    )
    approved_at = DateTimeField(blank=True, null=True, editable=False)

    class Meta:
        db_table = "person"

    def __str__(self):
        return self.name

    @property
    def age(self):
        if self.dob:
            return int((datetime.datetime.now() - self.dob).days / 365.25)


class Meeting(BaseModel):
    date = DateField()
    place = PlacesField()
    summary = TextField(max_length=1024, default="", help_text=_("Meeting summary"))
    guru = ForeignKey(
        Guru, null=True, on_delete=SET_NULL, related_name="people_meetings"
    )
    person = ForeignKey(
        Person, null=True, related_name="meetings", db_index=True, on_delete=SET_NULL
    )

    class Meta:
        db_table = "meeting"

    def __str__(self):
        return "{} {}".format(self.person.name, self.date)


class ContactMode(BaseModel):
    name = CharField(max_length=100, help_text=_("Name of contact mode"))

    class Meta:
        db_table = "contact_mode"

    def __str__(self):
        return self.name


class CommunicationChannel(BaseModel):
    name = CharField(max_length=100, help_text=_("Name of communication channel"))

    class Meta:
        db_table = "communication_channel"

    def __str__(self):
        return self.name


class SubscriptionTopic(BaseModel):
    name = CharField(max_length=100, help_text=_("Name of subscription topic"))

    class Meta:
        db_table = "subscription_topic"

    def __str__(self):
        return self.name


class EmailTopic(BaseModel):
    name = CharField(max_length=100, help_text=_("Name of email topic"))

    class Meta:
        db_table = "email_topic"

    def __str__(self):
        return self.name


class Address(BaseModel):
    addess_line_1 = CharField(max_length=100, help_text=_("Address line 1"))
    address_line_2 = CharField(
        max_length=100, blank=True, default="", help_text=_("Address line 2")
    )
    zipcode = CharField(max_length=10, help_text=_("Zipcode"))
    locality = CharField(
        max_length=100, help_text=_("Locality (City, town or village)")
    )
    state = CharField(max_length=255, help_text=_("State"))
    country = ForeignKey(
        "regions.Country", null=True, on_delete=SET_NULL, help_text=_("Country")
    )

    class Meta:
        db_table = "address"
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return "{} {} {} {}".format(
            self.country, self.state, self.locality, self.zipcode
        )


class Occupation(BaseModel):
    name = CharField(max_length=100, unique=True, db_index=True, help_text=_("Name"))

    class Meta:
        db_table = "occupation"

    def __str__(self):
        return self.name
