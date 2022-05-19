from rest_framework.viewsets import ModelViewSet

from api_basic.models import Article
from api_basic.serializers import ArticleSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
