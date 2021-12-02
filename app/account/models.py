from django.contrib.auth.models import AbstractUser
from django.db import models


class Role(models.Model):
    """
    Роли пользователей
    """

    MONITOR = 1
    CURATOR = 2
    ADMIN = 9
    ROLE_CHOICES = (
        (MONITOR, 'Специалист мониторинга'),
        (CURATOR, 'Руководитель'),
        (ADMIN, 'Администратор системы'),
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True, verbose_name='Роли пользователя')

    def __str__(self):
        return self.get_id_display()


class Account(AbstractUser):
    """
    Custom model for User
    """
    roles = models.ManyToManyField(Role)