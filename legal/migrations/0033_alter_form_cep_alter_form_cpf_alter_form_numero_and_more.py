# Generated by Django 4.1.2 on 2022-11-16 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legal', '0032_alter_form_cep_alter_form_numero_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='cep',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='form',
            name='cpf',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='form',
            name='numero',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='form',
            name='renda_mensal',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='form',
            name='rg',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='form',
            name='tel',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='form',
            name='tel2',
            field=models.CharField(max_length=12),
        ),
    ]