# Generated by Django 2.2.2 on 2019-06-08 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Surveys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(default='Something defult item', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answers', models.TextField(default='Something defult ansewr', max_length=500)),
                ('surveys', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='survey.Surveys')),
            ],
        ),
    ]
