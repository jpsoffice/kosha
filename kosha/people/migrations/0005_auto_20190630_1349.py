# Generated by Django 2.2.2 on 2019-06-30 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("people", "0004_auto_20190630_1344")]

    operations = [
        migrations.RenameField(
            model_name="person", old_name="addess_line_1", new_name="address_line_1"
        )
    ]
