# Generated by Django 2.2.2 on 2019-07-04 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("regions", "0003_remove_country_iso_code")]

    operations = [
        migrations.CreateModel(
            name="Nationality",
            fields=[],
            options={"proxy": True, "indexes": [], "constraints": []},
            bases=("regions.country",),
        )
    ]