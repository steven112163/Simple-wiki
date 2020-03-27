from rest_framework import serializers
from .models import Block


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ['id', 'name', 'image', 'stackable', 'flammable', 'transparent', 'luminant', 'tool', 'texture',
                  'update']
