# Generated by Django 2.2.2 on 2019-06-08 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveys',
            name='titlel',
            field=models.CharField(default='Something defult titel', max_length=500),
        ),
    ]
