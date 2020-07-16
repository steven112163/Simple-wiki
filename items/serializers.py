from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'image', 'stackable', 'renewable', 'durability', 'material', 'type', 'attack_damage',
                  'attack_speed', 'defense_points', 'update']
