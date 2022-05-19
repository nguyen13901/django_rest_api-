from rest_framework import routers

from api_basic.views import AccountViewSet
from api_basic.views.article import ArticleViewSet
from api_basic.views.author import AuthorViewSet


app_name = 'api_basic'

router = routers.SimpleRouter(trailing_slash=True)

router.register(r'article', ArticleViewSet, basename='article')
router.register(r'author', AuthorViewSet, basename='article')
router.register(r'account', AccountViewSet, basename='account')

urlpatterns = router.urls
