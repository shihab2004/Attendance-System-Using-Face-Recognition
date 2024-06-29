# Generated by Django 4.1.1 on 2022-09-21 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import recognition.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Attendence",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "Faculty_Name",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("Student_ID", models.CharField(blank=True, max_length=200, null=True)),
                ("date", models.DateField(auto_now_add=True, null=True)),
                ("time", models.TimeField(auto_now_add=True, null=True)),
                ("branch", models.CharField(max_length=200, null=True)),
                ("year", models.CharField(max_length=200, null=True)),
                ("section", models.CharField(max_length=200, null=True)),
                ("period", models.CharField(max_length=200, null=True)),
                (
                    "status",
                    models.CharField(default="Absent", max_length=200, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("firstname", models.CharField(blank=True, max_length=200, null=True)),
                ("lastname", models.CharField(blank=True, max_length=200, null=True)),
                ("registration_id", models.CharField(max_length=200, null=True)),
                (
                    "branch",
                    models.CharField(
                        choices=[
                            ("CSE", "CSE"),
                            ("BBA", "BBA"),
                            ("THM", "TMH"),
                            ("MAS", "MAS"),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "year",
                    models.CharField(
                        choices=[("1", "1"), ("2", "2"), ("3", "3"), ("4", "4")],
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "section",
                    models.CharField(
                        choices=[("A", "A"), ("B", "B"), ("C", "C")],
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "profile_pic",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=recognition.models.student_directory_path,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Faculty",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("firstname", models.CharField(blank=True, max_length=200, null=True)),
                ("lastname", models.CharField(blank=True, max_length=200, null=True)),
                ("phone", models.CharField(max_length=200, null=True)),
                ("email", models.CharField(max_length=200, null=True)),
                (
                    "profile_pic",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=recognition.models.user_directory_path,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
