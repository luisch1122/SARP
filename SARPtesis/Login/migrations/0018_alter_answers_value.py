# Generated by Django 4.1.3 on 2022-11-22 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0017_remove_answers_questions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='value',
            field=models.IntegerField(null=True),
        ),
    ]
