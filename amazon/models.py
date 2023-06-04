
from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import (
    TimeStampedModel,
    ActivatorModel
)

class UserProfile (TimeStampedModel,
    ActivatorModel
    ):
    
    class Meta:
        verbose_name_plural = "UserProfiles"
    
    user = models.OneToOneField(
    User, on_delete=models.CASCADE, null=False, blank=False   
    )
    adresse = models.CharField(verbose_name="adresse", max_length=255)
    date_naissance = models.DateTimeField(verbose_name='date_naissance', null=True, max_length=100)
    lieu_naissance = models.CharField(verbose_name="lieu_naissance", null=True, max_length=100)
    pays_residence = models.CharField(verbose_name="pays_residence", null=True, max_length=100)
    photo = models.TextField(verbose_name="photo", null=True)
    type_piece_identite = models.CharField(verbose_name="type_piece_identite", null=True, max_length=255)
    numero_piece_identite = models.CharField(verbose_name="numero_piece_identite", null=True, max_length=255)
    date_expiration_piece_identite = models.CharField(verbose_name="numero_piece_identite", null=True, max_length=255)
   
    def __str__(self):
        return f'{self.user.username}'
   