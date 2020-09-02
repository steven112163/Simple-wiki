from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from .models import Item, Material, Type


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['id', 'name']


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name']


class ItemSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = Item
        fields = ['id', 'name', 'image', 'stackable', 'renewable', 'durability', 'material', 'type', 'attack_damage',
                  'attack_speed', 'defense_points', 'update']
