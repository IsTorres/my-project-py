from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    alowed = models.BooleanField()