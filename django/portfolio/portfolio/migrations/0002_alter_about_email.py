# Generated by Django 4.1.7 on 2023-11-15 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='email',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]
