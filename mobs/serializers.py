from rest_framework import serializers
from .models import Mob


class MobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mob
        fields = ['id', 'name', 'image', 'height', 'width', 'behavior', 'attack_strength', 'spawn', 'update']
