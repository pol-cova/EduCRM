# Generated by Django 4.2.7 on 2023-11-05 22:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("API", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Student",
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
                ("name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("group", models.CharField(max_length=1)),
                ("question_1", models.BooleanField(default=False)),
                ("question_2", models.BooleanField(default=False)),
                ("question_3", models.BooleanField(default=False)),
                ("question_4", models.BooleanField(default=False)),
                ("question_5", models.BooleanField(default=False)),
                ("question_6", models.BooleanField(default=False)),
                ("question_7", models.BooleanField(default=False)),
                ("question_8", models.BooleanField(default=False)),
                ("question_9", models.BooleanField(default=False)),
                ("status", models.BooleanField(default=False)),
                ("punctuation", models.IntegerField(default=0)),
                (
                    "courses_enrolled",
                    models.ManyToManyField(related_name="students", to="API.course"),
                ),
            ],
        ),
    ]
