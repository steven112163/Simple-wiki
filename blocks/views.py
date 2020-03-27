from rest_framework import viewsets
from .serializers import BlockSerializer
from .models import Block


# Create your views here.
class BlockViewSet(viewsets.ModelViewSet):
    serializer_class = BlockSerializer
    queryset = Block.objects.all()
