from rest_framework.viewsets import ModelViewSet

from api_basic.models import Author
from api_basic.serializers import AuthorSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
