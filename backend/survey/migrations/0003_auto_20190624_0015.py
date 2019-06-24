# Generated by Django 2.2.2 on 2019-06-23 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20190623_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='survey',
            field=models.ForeignKey(blank=True, help_text='Choose what Survey thos Category belogs to.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='catagory', to='survey.Survey'),
        ),
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.ForeignKey(blank=True, help_text='Choose to what Category this question belongs to', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question', to='survey.Category'),
        ),
    ]