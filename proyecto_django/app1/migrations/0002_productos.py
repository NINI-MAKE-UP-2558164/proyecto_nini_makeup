# Generated by Django 4.2.2 on 2023-11-29 01:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Productos",
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
                ("nombres", models.CharField(blank=True, max_length=45, null=True)),
                ("catidad", models.CharField(blank=True, max_length=450, null=True)),
                ("precio", models.CharField(blank=True, max_length=45, null=True)),
                ("created_at", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "db_table": "productos",
                "managed": False,
            },
        ),
    ]
