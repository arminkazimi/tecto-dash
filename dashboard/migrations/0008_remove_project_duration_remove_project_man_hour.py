# Generated by Django 4.2.15 on 2024-11-06 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0007_alter_crew_crew_count"),
    ]

    operations = [
        migrations.RemoveField(model_name="project", name="duration",),
        migrations.RemoveField(model_name="project", name="man_hour",),
    ]
