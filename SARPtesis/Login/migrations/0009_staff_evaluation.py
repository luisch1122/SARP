# Generated by Django 4.1.3 on 2022-11-05 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0008_evaluation_delete_evaluations_questions_evaluations'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='evaluation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Login.evaluation'),
        ),
    ]
