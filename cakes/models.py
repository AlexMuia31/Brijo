from django.db import models

# Create your models here.


class Cakes(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=256)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
