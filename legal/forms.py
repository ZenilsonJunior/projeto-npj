from django import forms

from .models import form


class formularioCadastro(forms.ModelForm):
    class Meta:
        model = form
        fields = ('nome', 'sobrenome', 'dt_nasc', 'cpf', 'rg', 'genero', 'estado_civil', 'orgao_emissor', 'renda_mensal', 'email', 'tel', 'tel2', 'endereco', 'numero', 'complemento', 'cidade', 'cep', 'bairro', 'uf', 'area', 'obs')  # noqa
