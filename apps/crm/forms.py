from django import forms
from .models import Client, ClientWallet


# creating a form
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"
        exclude = ("created_by",)


class ClientWalletForm(forms.ModelForm):
    class Meta:
        model = ClientWallet
        fields = "__all__"
        exclude = ("client",)
