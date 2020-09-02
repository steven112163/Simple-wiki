from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from .models import Block, Texture


class TextureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Texture
        fields = ['id', 'name']


class BlockSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = Block
        fields = ['id', 'name', 'image', 'stackable', 'flammable', 'transparent', 'luminant', 'tool', 'texture',
                  'update']
