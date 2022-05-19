from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api_basic.models import Account
from api_basic.serializers import ListAccountSerializer, CreateAccountSerializer


class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    # serializer_class = AccountSerializer
    serializer_map = {
        "list": ListAccountSerializer,
        "create": CreateAccountSerializer
    }

    def get_serializer_class(self):
        return self.serializer_map.get(self.action, self.serializer_class)

    def create(self, request, *args, **kwargs):
        serializer: CreateAccountSerializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
