# Generated by Django 4.1.3 on 2022-11-06 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0011_evaluation_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='complete',
            field=models.BooleanField(null=True),
        ),
    ]
