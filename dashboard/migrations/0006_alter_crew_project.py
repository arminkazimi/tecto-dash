# Generated by Django 4.2.15 on 2024-10-01 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0005_alter_crew_project"),
    ]

    operations = [
        migrations.AlterField(
            model_name="crew",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="crews",
                to="dashboard.project",
            ),
        ),
    ]
