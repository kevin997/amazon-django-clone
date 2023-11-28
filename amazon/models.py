 
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
   


class User(TimeStampedModel, ActivatorModel):
    username = models.CharField(verbose_name="username", max_length=250)
    user_id = models.CharField(verbose_name="user_id", max_length=100)
    password = models.CharField(verbose_name="password", max_length=100)

    def __str__(self):
        return self.username



class Cathegorie(TimeStampedModel, ActivatorModel):
    nom = models.CharField(verbose_name = "nom", max_length=100)
    description = models.TextField(verbose_name="description", null=True)
    photo =models.TextField(null=True)
    
    def __str__(self):
        return self.nom



class Article(TimeStampedModel, ActivatorModel):

    class Meta:
        verbose_name_plural = "Articles"

    designation = models.CharField(verbose_name = 'designation', max_length=100)
    prix = models.IntegerField(verbose_name= 'prix')
    description = models.TextField(verbose_name="description")
    photo_article = models.TextField(verbose_name="photo_article", null=True)
    cathegorie = models.ForeignKey(Cathegorie, related_name="article", on_delete=models.CASCADE)
    qte_en_stock = models.IntegerField(verbose_name="quantité en en stock")
    #quante_en_stock = models.ForeignKey(StockGlobal, related_name=article)

    def __str__(self):
        return self.designation
    


class Adresse(TimeStampedModel,ActivatorModel):
    nom = models.CharField(verbose_name = "nom", max_length=200, null=True)
    prenom = models.CharField(verbose_name ="prenom", max_length=200,null=True)
    pays = models.CharField(verbose_name = "pays", max_length=100, null=True)
    ville = models.CharField(verbose_name = "ville", max_length=100, null=True)
    rue = models.CharField(verbose_name ="rue", max_length=200, null=True)
    code_postal = models.CharField(verbose_name ="code_postal", max_length=50, null=True)
    telephone = models.IntegerField(verbose_name ="telephone", null=True)

    def __str__(self):
        return self.nom
    





 
