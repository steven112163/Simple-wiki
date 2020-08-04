from rest_framework import serializers
from .models import Mob, Behavior


class BehaviorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Behavior
        fields = ['id', 'name']


class MobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mob
        fields = ['id', 'name', 'image', 'health_points', 'height', 'width', 'behavior', 'attack_strength', 'spawn', 'update']
