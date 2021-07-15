from rest_framework import viewsets
from .serializers import *
from .models import *

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ['username', 'email']
    search_fields = ['username', 'email']


class CategorieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    filterset_fields = ['nom']
    search_fields = ['nom']


class ProduitViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer
    filterset_fields = ['nom','categorie']
    search_fields = ['nom', 'categorie']


class LivraisonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Livraison.objects.all()
    serializer_class = LivraisonSerializer
    filterset_fields = ['user', 'produits']


class seFaireLivrerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = SeFaireLivrer.objects.all()
    serializer_class = SeFaireLivrerSerializer
