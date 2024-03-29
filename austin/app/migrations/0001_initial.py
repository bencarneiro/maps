# Generated by Django 4.1.5 on 2024-03-14 15:08

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ACSVariable",
            fields=[
                (
                    "id",
                    models.CharField(max_length=64, primary_key=True, serialize=False),
                ),
                ("label", models.CharField(max_length=1024)),
                ("concept", models.CharField(max_length=1024)),
                ("group", models.CharField(max_length=64)),
                ("required", models.BooleanField(default=False)),
                ("predicate_type", models.CharField(max_length=64)),
            ],
            options={
                "db_table": "acs_variable",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="County",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fips", models.IntegerField()),
                ("name", models.CharField(max_length=512)),
            ],
            options={
                "db_table": "county",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="State",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=512)),
            ],
            options={
                "db_table": "state",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Tract",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tract_id", models.IntegerField()),
                ("name", models.CharField(max_length=128)),
                ("name_lsad", models.CharField(max_length=512)),
                ("mtfcc", models.CharField(max_length=128)),
                ("funcstat", models.CharField(max_length=64)),
                ("aland", models.BigIntegerField(blank=True, null=True)),
                ("awater", models.BigIntegerField(blank=True, null=True)),
                ("intptlat", models.FloatField(blank=True, null=True)),
                ("intptlon", models.FloatField(blank=True, null=True)),
                (
                    "shape",
                    django.contrib.gis.db.models.fields.PolygonField(
                        geography=True, srid=4326
                    ),
                ),
                (
                    "county",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="app.county"
                    ),
                ),
                (
                    "state",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="app.state"
                    ),
                ),
            ],
            options={
                "db_table": "tract",
                "managed": True,
            },
        ),
        migrations.AddField(
            model_name="county",
            name="state",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="app.state"
            ),
        ),
        migrations.CreateModel(
            name="ACS5ValueByTract",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("year", models.IntegerField()),
                ("value", models.IntegerField(blank=True, default=0, null=True)),
                (
                    "acs_variable",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="app.acsvariable",
                    ),
                ),
                (
                    "tract",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="app.tract"
                    ),
                ),
            ],
            options={
                "db_table": "acs5_value_by_tract",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="ACS1ValueByTract",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("year", models.IntegerField()),
                ("value", models.IntegerField(blank=True, default=0, null=True)),
                (
                    "acs_variable",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="app.acsvariable",
                    ),
                ),
                (
                    "tract",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="app.tract"
                    ),
                ),
            ],
            options={
                "db_table": "acs1_value_by_tract",
                "managed": True,
            },
        ),
    ]
