# Generated by Django 2.2.2 on 2019-07-04 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("people", "0014_auto_20190704_2025")]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="dob_type",
            field=models.CharField(
                choices=[("A", "Actual"), ("C", "Calculated")],
                default="A",
                max_length=1,
                null=True,
                verbose_name="Date of birth type",
            ),
        )
    ]
