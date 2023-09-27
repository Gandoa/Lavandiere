from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


SERVICES_CHOICES = (
    ("1", "Express"),
    ("2", "Standard")
)
# declare a new model with a name "GeeksModel"
class CommandeModel(models.Model):
	# declare a new model with a name "GeeksModel"
        # fields of the model
    Nom = models.CharField(max_length = 200)
    Numéro_de_Téléphone = models.IntegerField()
    Date = models.DateTimeField(auto_now_add = True)
    Email = models.EmailField(max_length=200, blank=True, null=True)
    Services = models.CharField(max_length=20,choices=SERVICES_CHOICES, default="2")
    Code = models.IntegerField(blank=True, null=True)
    Commentaire = models.TextField(max_length=200)
    
        # renames the instances of the model
        # with their title name
    def __str__(self):
        return self.Nom

class ContactModel(models.Model):
    nom = models.CharField(max_length=100)
    numéro = models.IntegerField()
    Email = models.EmailField(max_length=100, blank=True, null=True)
    Message = models.TextField(max_length=200)

    def __str__(self):
        return self.Message

class Partner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    city = models.CharField(max_length=50)
    name_enterprise = models.CharField(max_length=50)
    domain = models.CharField(max_length=50)

    def __str__(self):
        return self.name_enterprise
