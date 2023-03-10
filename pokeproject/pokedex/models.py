from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=30, unique=True)
    identifier = models.PositiveIntegerField(unique=True)
    # moves une clé étrangère many to many

    def __str__(self):
        return self.name


class Pokemon(models.Model):
    name = models.CharField(max_length=50, unique=True)
    identifier = models.PositiveIntegerField(unique=True)
    type = models.ManyToManyField(Type)

    def __str__(self):
        return self.name
