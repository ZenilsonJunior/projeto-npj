# Generated by Django 4.1.2 on 2022-11-11 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legal', '0004_rename_usermaster_carla'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMaster',
            fields=[
                ('username', models.IntegerField(primary_key=True, serialize=False)),
                ('senha', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='carla',
        ),
    ]
