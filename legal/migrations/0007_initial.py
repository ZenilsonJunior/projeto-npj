# Generated by Django 4.1.2 on 2022-11-11 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('legal', '0006_delete_usermaster'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.IntegerField(primary_key=True, serialize=False)),
                ('senha', models.CharField(max_length=10)),
            ],
        ),
    ]