from rest_framework.viewsets import ModelViewSet

from data.models import Category
from v1.serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
