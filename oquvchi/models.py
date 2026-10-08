from django.db import models

# Create your models here.
class Oquvchi(models.Model):
    ism = models.CharField(max_length=99)
    familiya = models.CharField(max_length=99)
    yosh = models.IntegerField()

    def __str__(self):
        return f"O'quvchi ismi- {self.ism}"