from .models import *
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']


class CategorieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categorie
        fields = ['id', 'nom', 'description']


class ProduitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Produit
        fields = ['id', 'nom','prix', 'image',"categorie"]


class LivraisonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Livraison
        fields = ['id', 'date', 'prix', "ville",
                  "quartier", "description", "user", "produits"]


class SeFaireLivrerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SeFaireLivrer
        fields = ['id', 'produit', 'livraison', "quantite"]
