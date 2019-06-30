# Generated by Django 2.2.2 on 2019-06-30 11:46

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import places.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("organizations", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("regions", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "addess_line_1",
                    models.CharField(help_text="Address line 1", max_length=100),
                ),
                (
                    "address_line_2",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="Address line 2",
                        max_length=100,
                    ),
                ),
                ("zipcode", models.CharField(help_text="Zipcode", max_length=10)),
                (
                    "locality",
                    models.CharField(
                        help_text="Locality (City, town or village)", max_length=100
                    ),
                ),
                ("state", models.CharField(help_text="State", max_length=255)),
                (
                    "country",
                    models.ForeignKey(
                        help_text="Country",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="regions.Country",
                    ),
                ),
            ],
            options={
                "verbose_name": "Address",
                "verbose_name_plural": "Addresses",
                "db_table": "address",
            },
        ),
        migrations.CreateModel(
            name="CommunicationChannel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "name",
                    models.CharField(
                        help_text="Name of communication channel", max_length=100
                    ),
                ),
            ],
            options={"db_table": "communication_channel"},
        ),
        migrations.CreateModel(
            name="ContactMode",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "name",
                    models.CharField(help_text="Name of contact mode", max_length=100),
                ),
            ],
            options={"db_table": "contact_mode"},
        ),
        migrations.CreateModel(
            name="EmailTopic",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "name",
                    models.CharField(help_text="Name of email topic", max_length=100),
                ),
            ],
            options={"db_table": "email_topic"},
        ),
        migrations.CreateModel(
            name="Guru",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(help_text="Name", max_length=255)),
                (
                    "legal_name",
                    models.CharField(
                        blank=True, help_text="Legal name", max_length=255
                    ),
                ),
            ],
            options={"db_table": "guru"},
        ),
        migrations.CreateModel(
            name="GuruRole",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=50)),
            ],
            options={"db_table": "guru_role"},
        ),
        migrations.CreateModel(
            name="Occupation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "name",
                    models.CharField(
                        db_index=True, help_text="Name", max_length=100, unique=True
                    ),
                ),
            ],
            options={"db_table": "occupation"},
        ),
        migrations.CreateModel(
            name="SubscriptionTopic",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "name",
                    models.CharField(
                        help_text="Name of subscription topic", max_length=100
                    ),
                ),
            ],
            options={"db_table": "subscription_topic"},
        ),
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "reference_number",
                    models.CharField(
                        help_text="Unique reference number for the devotee",
                        max_length=10,
                        unique=True,
                    ),
                ),
                ("name", models.CharField(help_text="Name", max_length=100)),
                (
                    "initiated_name",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="Initiated name",
                        max_length=100,
                    ),
                ),
                (
                    "photo",
                    models.ImageField(
                        blank=True, help_text="Photo", null=True, upload_to=""
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female"), ("O", "Others")],
                        help_text="Gender",
                        max_length=1,
                    ),
                ),
                (
                    "dob",
                    models.DateField(blank=True, help_text="Date of birth", null=True),
                ),
                (
                    "is_dob_ambiguous",
                    models.BooleanField(
                        blank=True, help_text="Is date of birth ambiguous?", null=True
                    ),
                ),
                (
                    "dod",
                    models.DateField(blank=True, help_text="Date of death", null=True),
                ),
                (
                    "life_status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("AC", "Active"),
                            ("IN", "Inactive"),
                            ("LO", "Lost"),
                            ("PA", "Passed away"),
                        ],
                        help_text="Life status",
                        max_length=2,
                        null=True,
                    ),
                ),
                (
                    "mobile",
                    models.CharField(
                        blank=True,
                        help_text="Mobile number",
                        max_length=17,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
                                regex="^\\+?1?\\d{9,15}$",
                            )
                        ],
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True,
                        help_text="Phone number",
                        max_length=17,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
                                regex="^\\+?1?\\d{9,15}$",
                            )
                        ],
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, help_text="Email ", max_length=254, null=True
                    ),
                ),
                (
                    "marital_status",
                    models.CharField(
                        choices=[
                            ("SGL", "Single"),
                            ("ENG", "Engaged"),
                            ("SKG", "Seeking"),
                            ("MRD", "Married"),
                            ("SEP", "Separated"),
                            ("DIV", "Divorced"),
                            ("WID", "Widow"),
                        ],
                        help_text="Marital status",
                        max_length=3,
                    ),
                ),
                (
                    "spouse",
                    models.CharField(
                        blank=True, default="", help_text="Spouse name", max_length=100
                    ),
                ),
                (
                    "children_names",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="Names of children",
                        max_length=500,
                    ),
                ),
                (
                    "care_level",
                    models.CharField(
                        choices=[
                            ("A", "Aspiring"),
                            ("Z", "Shelter"),
                            ("D1", "Harinam"),
                            ("D2", "Brahmin"),
                            ("S", "Siksha"),
                            ("BTG", "Back to Godhead"),
                        ],
                        help_text="Care level",
                        max_length=3,
                    ),
                ),
                (
                    "relation_with_gm",
                    models.CharField(
                        choices=[("SS", "Spiritual son"), ("SD", "Spiritual daughter")],
                        help_text="Relation with Guru Maharaj",
                        max_length=3,
                    ),
                ),
                (
                    "shelter_place",
                    places.fields.PlacesField(
                        blank=True, help_text="Shelter place", max_length=255, null=True
                    ),
                ),
                (
                    "shelter_date",
                    models.DateField(blank=True, help_text="Shelter date", null=True),
                ),
                (
                    "shelter_recommendation",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="Recommended for shelter by",
                        max_length=200,
                    ),
                ),
                (
                    "first_initiation_place",
                    places.fields.PlacesField(
                        blank=True,
                        help_text="First initiation place",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "first_initiation_date",
                    models.DateField(
                        blank=True, help_text="First initiation date", null=True
                    ),
                ),
                (
                    "first_initiation_recommendation",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="Recommended for first initiation by",
                        max_length=200,
                    ),
                ),
                (
                    "second_initiation_place",
                    places.fields.PlacesField(
                        blank=True,
                        help_text="Second initiation place",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "second_initiation_date",
                    models.DateField(
                        blank=True, help_text="Second initiation date", null=True
                    ),
                ),
                (
                    "second_initiation_recommendation",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="Recommended for second initiation by",
                        max_length=200,
                    ),
                ),
                (
                    "aspiring_date",
                    models.DateField(blank=True, help_text="Aspiring date", null=True),
                ),
                (
                    "aspiring_place",
                    places.fields.PlacesField(
                        blank=True,
                        help_text="Aspiring place",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "outside_initiation_by",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("VG", "Vaishnava Guru"),
                            ("NVG", "Non Vaishnava Guru"),
                        ],
                        default="",
                        help_text="Initiation by outside gurus",
                        max_length=3,
                    ),
                ),
                (
                    "outside_initiation_community",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="Name of the Sampradaya/Math/Guru/Group/Religious organization/Ritvik Guru of initiation",
                        max_length=255,
                    ),
                ),
                (
                    "is_gm_siksha_guru",
                    models.BooleanField(help_text="Is Guru Maharaj siksha guru?"),
                ),
                (
                    "kc_start_date",
                    models.DateField(
                        blank=True,
                        help_text="Start date for Krishna Consciousness",
                        null=True,
                    ),
                ),
                (
                    "is_following_four_regs",
                    models.BooleanField(
                        blank=True,
                        help_text="Is following 4 regulative principles?",
                        null=True,
                    ),
                ),
                (
                    "following_four_regs_since",
                    models.DateField(
                        blank=True,
                        help_text="Following 4 regulative principles since",
                        null=True,
                    ),
                ),
                (
                    "chanting_rounds_number",
                    models.PositiveIntegerField(
                        blank=True, help_text="Number of rounds chanting", null=True
                    ),
                ),
                (
                    "chanting_sixteen_rounds_since",
                    models.DateField(
                        blank=True, help_text="Chanting 16 rounds since", null=True
                    ),
                ),
                (
                    "temple_role",
                    models.CharField(
                        blank=True,
                        choices=[("FT", "Full time"), ("NM", "Namhatta")],
                        default="",
                        help_text="Temple connection mode",
                        max_length=3,
                    ),
                ),
                (
                    "counselor_name",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="Name of counselor",
                        max_length=255,
                    ),
                ),
                (
                    "counselor_mobile",
                    models.CharField(
                        blank=True,
                        help_text="Mobile number of counselor",
                        max_length=17,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
                                regex="^\\+?1?\\d{9,15}$",
                            )
                        ],
                    ),
                ),
                (
                    "counselor_email",
                    models.EmailField(
                        blank=True,
                        help_text="Email of counselor",
                        max_length=254,
                        null=True,
                    ),
                ),
                (
                    "local_care_coordinator_name",
                    models.CharField(
                        blank=True,
                        help_text="Name of local care coordinator",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "local_care_coordinator_mobile",
                    models.CharField(
                        blank=True,
                        help_text="Mobile number of local care coordinator",
                        max_length=17,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
                                regex="^\\+?1?\\d{9,15}$",
                            )
                        ],
                    ),
                ),
                (
                    "local_care_coordinator_email",
                    models.EmailField(
                        blank=True,
                        help_text="Email of local care coordinator",
                        max_length=254,
                        null=True,
                    ),
                ),
                (
                    "national_care_coordinator_name",
                    models.CharField(
                        blank=True,
                        help_text="Name of national care coordinator",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "national_care_coordinator_mobile",
                    models.CharField(
                        blank=True,
                        help_text="Mobile number of national care coordinator",
                        max_length=17,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
                                regex="^\\+?1?\\d{9,15}$",
                            )
                        ],
                    ),
                ),
                (
                    "national_care_coordinator_email",
                    models.EmailField(
                        blank=True,
                        help_text="Email of national care coordinator",
                        max_length=254,
                        null=True,
                    ),
                ),
                (
                    "communication_channels",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Channels for communuication",
                        to="people.CommunicationChannel",
                    ),
                ),
                (
                    "contact_modes",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Modes for contact",
                        to="people.ContactMode",
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        help_text="Country, auto generated from present address",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="persons",
                        to="regions.Country",
                    ),
                ),
                (
                    "email_topics",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Topics subscribed via email",
                        to="people.EmailTopic",
                    ),
                ),
                (
                    "first_initiation_guru",
                    models.ForeignKey(
                        blank=True,
                        help_text="First initiation Guru",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="first_initiation_disciples",
                        to="people.Guru",
                    ),
                ),
                (
                    "nationality",
                    models.ForeignKey(
                        blank=True,
                        help_text="Nationality",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="nationals",
                        to="regions.Country",
                        to_field="nationality",
                    ),
                ),
                (
                    "occupation",
                    models.ForeignKey(
                        blank=True,
                        help_text="Occupation",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="people.Occupation",
                    ),
                ),
                (
                    "permanent_address",
                    models.ForeignKey(
                        blank=True,
                        help_text="Permanent address",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="people.Address",
                    ),
                ),
                (
                    "present_address",
                    models.ForeignKey(
                        blank=True,
                        help_text="Present address",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="people.Address",
                    ),
                ),
                (
                    "second_initiation_guru",
                    models.ForeignKey(
                        blank=True,
                        help_text="Second initiation Guru",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="second_initiation_disciples",
                        to="people.Guru",
                    ),
                ),
                (
                    "shelter_guru",
                    models.ForeignKey(
                        blank=True,
                        help_text="Shelter Guru",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="sheltered_disciples",
                        to="people.Guru",
                    ),
                ),
                (
                    "siksha_gurus",
                    models.ManyToManyField(
                        blank=True, help_text="Siksha gurus", to="people.Guru"
                    ),
                ),
                (
                    "subscription_topics",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Topics subscribed to",
                        to="people.SubscriptionTopic",
                    ),
                ),
                (
                    "temple",
                    models.ForeignKey(
                        blank=True,
                        help_text="Temple connected with",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="people",
                        to="organizations.Temple",
                    ),
                ),
                (
                    "zone",
                    models.ForeignKey(
                        blank=True,
                        help_text="Zone",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="organizations.Zone",
                    ),
                ),
            ],
            options={"db_table": "person"},
        ),
        migrations.CreateModel(
            name="Meeting",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("date", models.DateField()),
                ("place", places.fields.PlacesField(max_length=255)),
                (
                    "summary",
                    models.TextField(
                        default="", help_text="Meeting summary", max_length=1024
                    ),
                ),
                (
                    "guru",
                    models.ForeignKey(
                        default=0,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="people_meetings",
                        to="people.Guru",
                    ),
                ),
                (
                    "person",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="meetings",
                        to="people.Person",
                    ),
                ),
            ],
            options={"db_table": "meeting"},
        ),
        migrations.AddField(
            model_name="guru",
            name="roles",
            field=models.ManyToManyField(blank=True, to="people.GuruRole"),
        ),
        migrations.AddField(
            model_name="guru",
            name="user",
            field=models.OneToOneField(
                blank=True,
                help_text="User",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]