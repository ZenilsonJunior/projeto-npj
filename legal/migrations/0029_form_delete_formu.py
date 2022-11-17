# Generated by Django 4.1.2 on 2022-11-16 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legal', '0028_rename_form_formu'),
    ]

    operations = [
        migrations.CreateModel(
            name='form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=150)),
                ('dt_nasc', models.DateField(blank=True, null=True)),
                ('cpf', models.CharField(max_length=14)),
                ('rg', models.CharField(max_length=12)),
                ('genero', models.CharField(choices=[('m', 'Masculino'), ('f', 'Feminino'), ('lgbt', 'Prefiro não opinar')], max_length=4)),
                ('estado_civil', models.CharField(max_length=12, unique=True)),
                ('orgao_emissor', models.CharField(max_length=12)),
                ('renda_mensal', models.CharField(max_length=10)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('tel', models.CharField(max_length=12)),
                ('tel2', models.CharField(max_length=12)),
                ('endereco', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=6)),
                ('complemento', models.CharField(max_length=10)),
                ('cidade', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=9)),
                ('bairro', models.CharField(max_length=50)),
                ('uf', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paramá'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins'), ('DF', 'Distrito Federal')], max_length=2)),
                ('area', models.CharField(choices=[('civil', 'civil'), ('familia', 'familia'), ('penal', 'penal'), ('trabalhista', 'trabalhista')], max_length=11)),
                ('obs', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='formu',
        ),
    ]
