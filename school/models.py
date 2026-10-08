from django.db import models

# Create your models here.
class sinf_royhati(models.Model):
    sinf = models.CharField(max_length=100)
    oquvchilar_soni = models.IntegerField()
    def __str__(self):
        return self.sinf
    
