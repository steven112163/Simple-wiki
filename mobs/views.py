from rest_framework import viewsets
from .serializers import MobSerializer, BehaviorSerializer
from .models import Mob, Behavior


# Create your views here.
class BehaviorViewSet(viewsets.ModelViewSet):
    serializer_class = BehaviorSerializer
    queryset = Behavior.objects.all()


class MobViewSet(viewsets.ModelViewSet):
    serializer_class = MobSerializer
    queryset = Mob.objects.all()
