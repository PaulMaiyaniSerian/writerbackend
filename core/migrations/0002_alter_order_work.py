# Generated by Django 5.0.3 on 2024-03-21 17:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="work",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
