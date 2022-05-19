from django.contrib.auth.hashers import make_password, check_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api_basic.models import Account


class ListAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['id', 'username']


class CreateAccountSerializer(serializers.ModelSerializer):

    def validate_password(self, data):
        if len(data) >= 8 and len(data) <= 20:
            return make_password(data)
        raise ValidationError("password must >= 8 and <= 20")

    class Meta:
        model = Account
        fields = '__all__'
