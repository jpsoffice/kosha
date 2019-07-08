# Generated by Django 2.2.2 on 2019-07-05 14:54

from django.db import migrations
import kosha.people.models


class Migration(migrations.Migration):

    dependencies = [("people", "0019_auto_20190705_1414")]

    operations = [
        migrations.AlterField(
            model_name="meeting",
            name="place",
            field=kosha.people.models.PlacesField(max_length=255),
        ),
        migrations.AlterField(
            model_name="person",
            name="aspiring_place",
            field=kosha.people.models.PlacesField(
                blank=True,
                db_index=True,
                help_text="Aspiring place",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="person",
            name="first_initiation_place",
            field=kosha.people.models.PlacesField(
                blank=True,
                db_index=True,
                help_text="First initiation place",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="person",
            name="second_initiation_place",
            field=kosha.people.models.PlacesField(
                blank=True,
                db_index=True,
                help_text="Second initiation place",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="person",
            name="shelter_place",
            field=kosha.people.models.PlacesField(
                blank=True,
                db_index=True,
                help_text="Shelter place",
                max_length=255,
                null=True,
            ),
        ),
    ]
