# Generated by Django 4.1.2 on 2022-11-16 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legal', '0031_alter_form_cpf_alter_form_rg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='cep',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='form',
            name='numero',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='form',
            name='renda_mensal',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='form',
            name='tel',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='form',
            name='tel2',
            field=models.IntegerField(),
        ),
    ]