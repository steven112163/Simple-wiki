from rest_framework import serializers
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
    class Meta:
        model = Item
        fields = ['id', 'name', 'image', 'stackable', 'renewable', 'durability', 'material', 'type', 'attack_damage',
                  'attack_speed', 'defense_points', 'update']

    def create(self, validated_data):
        material = validated_data['material']
        if material is not None:
            materials = Material.objects.filter(name=material)
            if len(materials) > 0:
                material = materials[0]
            else:
                material = None

        item_type = validated_data['type']
        if item_type is not None:
            types = Type.objects.filter(name=item_type)
            if len(types) > 0:
                item_type = types[0]
            else:
                item_type = None

        # Create new item
        item = Item.objects.create(
            name=validated_data['name'],
            image=validated_data['image'],
            stackable=validated_data['stackable'],
            renewable=validated_data['renewable'],
            durability=validated_data['durability'],
            material=material,
            type=item_type,
            attack_damage=validated_data['attack_damage'],
            attack_speed=validated_data['attack_speed'],
            defense_points=validated_data['defense_points']
        )
        item.save()
        return item
