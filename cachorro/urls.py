from django.urls import path
from cachorro.views import *

urlpatterns = [
    path('cadastro/', cadastro),
    path('atualizar/<int:id>', update),
]