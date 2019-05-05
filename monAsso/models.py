from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class Benevole(models.Model):
    idBenevole = models.AutoField(primary_key=True)
    #user model
    userResponsable = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Benevole"
        ordering = ['idBenevole']

    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard dans l'administration
        """
        return self.userResponsable.first_name

class Asso(models.Model):
    idAsso=models.AutoField(primary_key=True)
    userResponsable=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nomAsso=models.CharField(max_length=100)
    typeAsso=models.CharField(max_length=40)
    description= models.TextField(null=True)
    dateCreation=models.DateTimeField(default=timezone.now,
                                verbose_name="Date de creation")

    class Meta:
        verbose_name = "association"
        ordering = ['idAsso']

    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard dans l'administration
        """
        return self.nomAsso

class Event(models.Model):
    idEvent=models.AutoField(primary_key=True)
    nomEvent=models.CharField(max_length=30)
    lieu=models.CharField(max_length=30)
    dateDebut=models.DateTimeField()
    dateFin = models.DateTimeField()
    description=models.TextField(null=True)
    nbBenevole=models.IntegerField(null=True)

    class Meta:
        verbose_name = "evenement"
        ordering = ['idEvent']

    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard dans l'administration
        """
        return self.nomEvent