# Generated by Django 4.1.3 on 2022-11-05 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0007_alter_questions_value_alter_staff_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('complete', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='Evaluations',
        ),
        migrations.AddField(
            model_name='questions',
            name='evaluations',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Login.evaluation'),
        ),
    ]
