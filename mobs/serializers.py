from rest_framework import serializers
from .models import Mob


class MobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mob
        fields = ['id', 'name', 'image', 'height', 'width', 'behavior', 'attack_strength', 'spawn', 'update']
