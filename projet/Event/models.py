from django.db import models
from django.utils import timezone

class Event(models.Model):
    nomEvent = models.CharField(max_length=100)
    idAsso = models.IntegerField()
    lieu =  models.CharField(max_length=100)
    nbBenevole= models.IntegerField()
    description = models.TextField(null=True)
    dateDebut = models.DateTimeField("Date de début")
    dateFin = models.DateTimeField("Date de fin")

    class Meta:
        verbose_name = "evenement"
        ordering = ['id']