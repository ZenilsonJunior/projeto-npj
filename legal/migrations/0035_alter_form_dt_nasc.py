# Generated by Django 4.1.2 on 2022-11-17 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legal', '0034_alter_form_dt_nasc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='dt_nasc',
            field=models.CharField(max_length=15),
        ),
    ]
