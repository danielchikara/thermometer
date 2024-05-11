from django.db import models

# Create your models here.


class Temperature(models.Model):
    name = models.CharField(max_length=200)
    value = models.IntegerField()

    def __str__(self):
        return self.choice_text
    
    