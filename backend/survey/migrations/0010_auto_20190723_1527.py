# Generated by Django 2.2.2 on 2019-07-23 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0009_response_kommunikation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='answer',
            new_name='the_answer',
        ),
    ]
