# Generated by Django 4.2.7 on 2023-11-05 23:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("API", "0003_group"),
    ]

    operations = [
        migrations.AddField(
            model_name="group",
            name="name",
            field=models.CharField(default="Default", max_length=100),
        ),
    ]
