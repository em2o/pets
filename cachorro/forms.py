from django import forms

from cachorro.models import Cachorro


class CachorroForm(forms.ModelForm):
    class Meta:
        model = Cachorro
        fields = "__all__"