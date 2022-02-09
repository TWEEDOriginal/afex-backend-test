from django.shortcuts import render, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from rest_framework import generics
from .models import Client, ClientWallet
from .forms import ClientForm, ClientWalletForm
from .serializers import ClientSerializer


class ClientApiList(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientApiDetail(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class IndexView(ListView):
    model = Client
    queryset = Client.objects.all().order_by("-updated")
    template_name = "crm/client_list.html"
    context_object_name = "client_list"


class ClientDetail(DetailView):
    model = Client
    template_name = "crm/client_detail.html"
    context_object_name = "client"


class CreateClient(CreateView):
    model = Client
    form_class = ClientForm
    template_name = "crm/create_client.html"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("client_detail", args=(self.object.pk,))


class EditClient(UpdateView):
    model = Client
    form_class = ClientForm
    pk_url_kwarg = "pk"
    template_name = "crm/edit_client.html"

    def get_success_url(self):
        return reverse("client_detail", kwargs={"pk": self.kwargs["pk"]})


class DeleteClient(DeleteView):
    model = Client
    pk_url_kwarg = "pk"
    template_name = "crm/delete_client.html"
    success_url = "/"


class EditWallet(UpdateView):
    model = ClientWallet
    form_class = ClientWalletForm
    pk_url_kwarg = "pk"
    template_name = "crm/edit_wallet.html"
    context_object_name = "wallet"

    def get_success_url(self):

        return reverse("client_detail", kwargs={"pk": self.object.client.pk})


def create_wallet(request, pk):
    client = Client.objects.get(pk=pk)
    try:
        client.client_wallet
        return redirect("client_detail", pk)
    except:
        if request.method == "POST":
            form = ClientWalletForm(request.POST)
            form.instance.client = client
            if form.is_valid():
                form.save()

                messages.success(request, f"Wallet created successfully")
                return redirect("client_detail", pk)
        else:
            form = ClientWalletForm()

        context = {"form": form, "client": client}
        return render(request, "crm/create_wallet.html", context)


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(
                request, f"Your account has been created. You can log in now!"
            )
            return redirect("login")
    else:
        form = UserCreationForm()

    context = {"form": form}
    return render(request, "auth/register.html", context)
