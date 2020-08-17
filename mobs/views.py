from rest_framework import viewsets, generics
from .serializers import MobSerializer, BehaviorSerializer, UserSerializer
from .models import Mob, Behavior
from django.contrib.auth.models import User


# Create your views here.
class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class BehaviorViewSet(viewsets.ModelViewSet):
    serializer_class = BehaviorSerializer
    queryset = Behavior.objects.all()


class MobViewSet(viewsets.ModelViewSet):
    serializer_class = MobSerializer
    queryset = Mob.objects.all()
