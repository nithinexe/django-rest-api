from rest_framework import viewsets

from .serializers import mobileSerializer
from .models import mobile


class mobileViewSet(viewsets.ModelViewSet):
    queryset = mobile.objects.all().order_by('name')
    serializer_class = mobileSerializer
