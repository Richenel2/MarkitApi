from django.db import models
from django.db.models.fields import IntegerField
from django.utils import timezone

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    def __str__(self) -> str:
        return self.username


class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(null=True)
    def __str__(self) -> str:
        return self.nom


class Produit(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.IntegerField()
    image = models.ImageField(upload_to="ProduitImage/")
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.nom


class Livraison(models.Model):
    date = models.DateTimeField(default=timezone.now)
    prix = models.IntegerField()    
    ville = models.CharField(max_length=20)
    quartier = models.CharField(max_length=20)
    description = models.TextField(null=True)
    user = models.ForeignKey('User', on_delete=models.PROTECT)
    produits= models.ManyToManyField(Produit, through="SeFaireLivrer")

    def __str__(self) -> str:
        return "Livraison de "+self.user.username


class SeFaireLivrer(models.Model):
    produit = models.ForeignKey('Produit', on_delete=models.PROTECT)
    livraison = models.ForeignKey('Livraison', on_delete=models.PROTECT)
    quantite = IntegerField()
