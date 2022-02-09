from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("client_details/<int:pk>", views.ClientDetail.as_view(), name="client_detail"),
    path("edit_client/<int:pk>", views.EditClient.as_view(), name="edit_client"),
    path("delete_client/<int:pk>", views.DeleteClient.as_view(), name="delete_client"),
    path("edit_wallet/<int:pk>", views.EditWallet.as_view(), name="edit_wallet"),
    path("create_wallet/<int:pk>", views.create_wallet, name="create_wallet"),
    path("create_client", views.CreateClient.as_view(), name="create_client"),
    path("register/", views.register, name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="auth/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="auth/logout.html"),
        name="logout",
    ),
    path(
        "api/client_list",
        views.ClientApiList.as_view(),
        name="client_list_api",
    ),
    path(
        "api/client_detail/<int:pk>",
        views.ClientApiDetail.as_view(),
        name="client_detail_api",
    ),
]
