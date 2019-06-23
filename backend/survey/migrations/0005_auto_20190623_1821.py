# Generated by Django 2.2.2 on 2019-06-23 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_auto_20190623_1818'),
    ]

    operations = [
        migrations.RenameField(
            model_name='survey',
            old_name='surveyid',
            new_name='survey_Id',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_Max_Points',
        ),
        migrations.AlterField(
            model_name='question',
            name='question_Answer',
            field=models.CharField(blank=True, help_text='Important that this is exact', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_Type',
            field=models.CharField(choices=[('text', 'short_text'), ('text', 'long_text'), ('text', 'dropdown'), ('choice.label', 'multiple_choice (single option)'), ('choice.labels', 'multiple_choice (multiple options)'), ('choice.label', 'picture_choice (single option)'), ('choice.labels', 'picture_choice (multiple options)'), ('email', 'email'), ('url', 'website'), ('file_url', 'file_upload'), ('boolean', 'legal'), ('boolan', 'yes_no'), ('number', 'rating'), ('number', 'opinion_scale'), ('number', 'number'), ('date', 'date')], help_text='Important that this is right', max_length=20),
        ),
        migrations.AlterField(
            model_name='question',
            name='survey',
            field=models.ForeignKey(blank=True, help_text='Choose to what Survey this question belongs to', null=True, on_delete=django.db.models.deletion.CASCADE, to='survey.Survey'),
        ),
    ]
