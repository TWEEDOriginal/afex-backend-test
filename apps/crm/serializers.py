from django.contrib.auth.models import User
from .models import Client, ClientWallet
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["pk", "username", "email"]


class ClientWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientWallet
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    created_by_ = UserSerializer(source="created_by")
    client_wallet_ = ClientWalletSerializer(source="client_wallet")

    class Meta:
        model = Client
        fields = "__all__"
