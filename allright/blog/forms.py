from django import forms
from .models import CadastroHomePage

class CadastroHomePageForm(forms.ModelForm):
    descricao = forms.CharField(label=
        'Diga-nos um pouco mais sobre seu negócio',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Qual serviço procura? Quantos funcionários tem sua empresa?'
            }
        )
    )
    class Meta:
        model = CadastroHomePage
        fields = "__all__"