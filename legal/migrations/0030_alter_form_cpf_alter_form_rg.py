# Generated by Django 4.1.2 on 2022-11-16 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legal', '0029_form_delete_formu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='cpf',
            field=models.IntegerField(max_length=14),
        ),
        migrations.AlterField(
            model_name='form',
            name='rg',
            field=models.IntegerField(max_length=12),
        ),
    ]
