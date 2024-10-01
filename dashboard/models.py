from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here
class Project(models.Model):
    class Levels(models.TextChoices):
        ONE = "1", _("level 1")
        TWO = "2", _("level 2")
        THREE = "3", _("level 3")
        FOUR = "4", _("level 4")

    class Status(models.TextChoices):
        PENDING = 'P', _('Pending')
        CONFIRMED = 'C', _('Confirmed')
        RESUBMISSION = 'SR', _('Schedule Resubmission')
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.PENDING,
    )
    name = models.CharField(max_length=250)
    level = models.CharField(
        max_length=1,
        choices=Levels.choices,
        default=Levels.ONE,
    )
    image = models.ImageField(upload_to='dashboard/project-image/', blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    duration = models.DurationField()
    man_hour = models.DurationField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Crew(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='crews')
    title = models.CharField(max_length=100)
    crew_count = models.PositiveIntegerField(default=1)
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Notification(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
