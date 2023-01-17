from django.db import models


class Pokemon(models.Model):
    name=models.CharField(max_length=50)
    dex=models.PositiveIntegerField(unique=True)
    
    def __str__(self):
        return self.name