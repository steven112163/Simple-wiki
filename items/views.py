from rest_framework import viewsets
from .serializers import ItemSerializer
from .models import Item


# Create your views here.
class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
