# Generated by Django 2.2.2 on 2019-07-04 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("regions", "0002_auto_20190704_0616")]

    operations = [migrations.RemoveField(model_name="country", name="iso_code")]