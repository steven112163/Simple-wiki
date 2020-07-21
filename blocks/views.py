from rest_framework import viewsets
from .serializers import BlockSerializer, TextureSerializer
from .models import Block, Texture


# Create your views here.
class TextureViewSet(viewsets.ModelViewSet):
    serializer_class = TextureSerializer
    queryset = Texture.objects.all()


class BlockViewSet(viewsets.ModelViewSet):
    serializer_class = BlockSerializer
    queryset = Block.objects.all()
