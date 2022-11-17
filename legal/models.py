

from django.db import models

# Create your models here.


class User(models.Model):
    username = models.IntegerField(primary_key=True)
    email = models.EmailField
    senha = models.CharField(max_length=10)


GENERO_CHOICES = (
    ('m', 'Masculino'),
    ('f', 'Feminino'),
    ('lgbt', 'Prefiro não opinar'),
)

UF_CHOICES = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paramá'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
    ('DF', 'Distrito Federal'),
)

AREA_CHOICES = (
    ('civil', 'civil'),
    ('familia', 'familia'),
    ('penal', 'penal'),
    ('trabalhista', 'trabalhista'),
)


class form(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=150)
    dt_nasc = models.DateField()
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=12)
    genero = models.CharField(max_length=4, choices=GENERO_CHOICES)
    estado_civil = models.CharField(max_length=12, unique=True)
    orgao_emissor = models.CharField(max_length=12)
    renda_mensal = models.CharField(max_length=10)
    email = models.EmailField(blank=True, null=True)
    tel = models.CharField(max_length=12)
    tel2 = models.CharField(max_length=12)
    endereco = models.CharField(max_length=50)
    numero = models.CharField(max_length=6)
    complemento = models.CharField(max_length=10)
    cidade = models.CharField(max_length=50)
    cep = models.CharField(max_length=9)
    bairro = models.CharField(max_length=50)
    uf = models.CharField(max_length=2, choices=UF_CHOICES)
    area = models.CharField(max_length=11, choices=AREA_CHOICES)
    obs = models.CharField(max_length=500)


def __str__(self):
    return self.nome
