from django.db import models

# Create your models here.


class Temperature(models.Model):
    date = models.DateField(auto_now_add=True)
    value = models.IntegerField()

    def __str__(self):
        return self.value
    
    