from django.urls import path
from cachorro.views import cadastro

urlpatterns = [
    path('cadastro/', cadastro),
]