from rest_framework import viewsets
from .serializers import MobSerializer
from .models import Mob


# Create your views here.
class MobViewSet(viewsets.ModelViewSet):
    serializer_class = MobSerializer
    queryset = Mob.objects.all()
