from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
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
    image = Base64ImageField(required=False)

    class Meta:
        model = Mob
        fields = ['id', 'name', 'image', 'health_points', 'height', 'width', 'behavior', 'attack_strength', 'spawn',
                  'update']
