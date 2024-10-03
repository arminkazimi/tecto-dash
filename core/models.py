from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager, ManagerManager, ContractorManager


class CustomUser(AbstractUser):
    class Types(models.TextChoices):
        SUPERUSER = 'SUPERUSER', 'Superuser'
        MANAGER = 'MANAGER', 'Manager'
        CONTRACTOR = 'CONTRACTOR', 'Contractor'

    username = None
    email = models.EmailField(_("email address"), unique=True)
    type = models.CharField(_('Type'), max_length=50, choices=Types.choices, default=Types.SUPERUSER)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def is_manager(self):
        return bool(self.type == CustomUser.Types.MANAGER)

    def is_contractor(self):
        return bool(self.type == CustomUser.Types.CONTRACTOR)

    def __str__(self):
        return self.email


class Manager(CustomUser):
    objects = ManagerManager()

    class Meta:
        proxy = True

        permissions = (
            ('is_manager', 'Can access the manager dashboard view'),
        )

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = CustomUser.Types.MANAGER
        return super().save(*args, **kwargs)


class Contractor(CustomUser):
    objects = ContractorManager()

    class Meta:
        proxy = True

        permissions = (
            ('is_contractor', 'Can access the contractor dashboard view'),
        )

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = CustomUser.Types.CONTRACTOR
        return super().save(*args, **kwargs)
