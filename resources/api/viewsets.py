from rest_framework.viewsets import ModelViewSet
from resources.models import Resource
from .serializers import ResourceSerializer


class ResourceViewSet(ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    filterset_fields = ["name", "description"]
