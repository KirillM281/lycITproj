# Generated by Django 3.0.6 on 2020-10-18 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Diary', '0005_auto_20201018_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='littlenote',
            name='notifydate',
            field=models.DateField(),
        ),
    ]
