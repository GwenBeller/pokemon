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
    pv = models.PositiveIntegerField()
    base_attaque = models.PositiveIntegerField()
    base_defense = models.PositiveIntegerField()
    base_attaque_spe = models.PositiveIntegerField()
    base_defense_spe = models.PositiveIntegerField()
    base_vitesse = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Move(models.Model):
    name = models.CharField(max_length=100, unique=True)
    identifier = models.PositiveIntegerField(unique=True)
    damage_class = models.CharField(max_length=20)
    base_damage = models.PositiveIntegerField()
