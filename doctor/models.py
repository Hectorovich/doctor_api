from django.contrib.auth.models import AbstractUser
from django.db import models


class Specialization(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    pass


class Doctor(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    specializations = models.ManyToManyField(
        "Specialization",
        related_name="doctors"
    )
    description = models.TextField()
    birth_date = models.DateField()
    experience = models.IntegerField()
    user = models.OneToOneField(
        User,
        related_name="doctors",
        on_delete=models.SET_NULL,
        null=True
    )

    class Meta:
        ordering = ["id", "name"]

    def __str__(self):
        return self.name
