# Generated by Django 4.1.5 on 2024-03-14 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_remove_countytocbsa_cbsa_remove_countytocbsa_county_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="CoreBasedStatisticalArea",
            new_name="CoreBaseStatisticalArea",
        ),
    ]