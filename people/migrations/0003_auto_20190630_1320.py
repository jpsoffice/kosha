# Generated by Django 2.2.2 on 2019-06-30 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("people", "0002_auto_20190630_1221")]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="dob",
            field=models.DateField(blank=True, null=True, verbose_name="Date of birth"),
        ),
        migrations.AlterField(
            model_name="person",
            name="dod",
            field=models.DateField(blank=True, null=True, verbose_name="Date of death"),
        ),
        migrations.AlterField(
            model_name="person",
            name="is_dob_ambiguous",
            field=models.BooleanField(
                blank=True, null=True, verbose_name="Is date of birth ambiguous?"
            ),
        ),
        migrations.RemoveField(model_name="person", name="permanent_address"),
        migrations.AddField(
            model_name="person",
            name="permanent_address",
            field=models.ManyToManyField(
                help_text="Permanent address",
                related_name="person_permanent",
                to="people.Address",
            ),
        ),
        migrations.RemoveField(model_name="person", name="present_address"),
        migrations.AddField(
            model_name="person",
            name="present_address",
            field=models.ManyToManyField(
                help_text="Present address",
                related_name="person_present",
                to="people.Address",
            ),
        ),
        migrations.AlterField(
            model_name="person",
            name="relation_with_gm",
            field=models.CharField(
                choices=[("SS", "Spiritual son"), ("SD", "Spiritual daughter")],
                help_text="Relation with Guru Maharaj",
                max_length=3,
                verbose_name="Relation with Guru Maharaj",
            ),
        ),
    ]
