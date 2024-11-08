from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


# Create your models here
class Project(models.Model):
    class Levels(models.TextChoices):
        ONE = "1", _("level 1")
        TWO = "2", _("level 2")
        THREE = "3", _("level 3")
        FOUR = "4", _("level 4")

    class Status(models.TextChoices):
        PENDING = 'P', 'Pending'
        CONFIRMED = 'C', 'Confirmed'
        RESUBMISSION = 'SR', 'Schedule Resubmission'

    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.PENDING,
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=250)
    level = models.CharField(
        max_length=1,
        choices=Levels.choices,
        default=Levels.ONE,
    )
    # image = models.ImageField(upload_to='dashboard/project-image/', blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("project-detail", kwargs={"pk": self.pk})

    def get_duration(self):
        pass

    def get_man_hour(self):
        pass

    def get_total_workers(self):
        total_workers = self.crews.all().aggregate(Sum('crew_count'))['crew_count__sum']
        return total_workers


class Crew(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='crews')
    title = models.CharField(max_length=100)
    crew_count = models.PositiveIntegerField(default=0)
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Notification(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=250)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
