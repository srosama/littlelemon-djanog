# Generated by Django 4.2.1 on 2023-07-03 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menumodel',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
