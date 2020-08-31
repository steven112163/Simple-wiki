from rest_framework import serializers
from .models import Mob, Behavior
from django.contrib.auth.models import User
import re


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value):
        """
        Check password is longer than 6 characters,
        containing at least one letter and at least one number
        :param value: password
        :return: password that passes validation
        """
        password = str(value)
        if len(password) < 6:
            raise serializers.ValidationError('Password has to be longer than 6 characters')
        if not bool(re.match('^(?=.*[a-zA-Z])(?=.*[0-9]).+$', password)):
            raise serializers.ValidationError('Password must contain at least one letter and at least one number')

        return value

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class BehaviorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Behavior
        fields = ['id', 'name']


class MobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mob
        fields = ['id', 'name', 'image', 'health_points', 'height', 'width', 'behavior', 'attack_strength', 'spawn',
                  'update']

    def create(self, validated_data):
        behavior = validated_data['behavior']
        if behavior is not None:
            behaviors = Behavior.objects.filter(name=behavior)
            if len(behaviors) > 0:
                behavior = behaviors[0]
            else:
                behavior = Behavior.objects.create(name=behavior)
                behavior.save()
        else:
            behavior = None
        mob = Mob.objects.create(
            name=validated_data['name'],
            image=validated_data['image'],
            health_points=validated_data['health_points'],
            height=validated_data['height'],
            width=validated_data['width'],
            behavior=behavior,
            attack_strength=validated_data['attack_strength'],
            spawn=validated_data['spawn']
        )
        mob.save()
        return mob
