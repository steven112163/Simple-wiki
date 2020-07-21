from rest_framework import serializers
from .models import Block, Texture


class TextureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Texture
        fields = ['id', 'name']


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ['id', 'name', 'image', 'stackable', 'flammable', 'transparent', 'luminant', 'tool', 'texture',
                  'update']
