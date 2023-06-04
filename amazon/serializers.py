from . import models
from rest_framework import serializers
from rest_framework.fields import CharField, EmailField, DateTimeField, TextField



## Create User Serializer



class UserProfileSerialiazer(serializers.ModelSerializer):

    adresse = CharField(required=True)
    date_naissance = DateTimeField(required=True)
    lieu_naissance = CharField(required=True)
    pays_residence = CharField(required=True)
    photo = TextField(required=True)
    type_piece_identite = CharField(required=True)
    numero_piece_identite = CharField(required=True)
    date_expiration_piece_identite = CharField(required=True)

    class Meta:
        model = models.UserProfile
        fields = (
            'addresse',
            'date_naissance',
            'lieu_naissance',
            'pays_residence',
            'photo',
            'type_piece_identite',
            'numero_piece_identite',
            'date_expiration_piece_identite'
        )


