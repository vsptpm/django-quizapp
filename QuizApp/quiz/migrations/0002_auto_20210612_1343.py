# Generated by Django 3.2.4 on 2021-06-12 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='option3',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='option4',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]