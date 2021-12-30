from django.db import models


class mobile(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField(max_length=60)

    def __str__(self):
        return self.name
