# Generated by Django 3.0.6 on 2020-10-18 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Diary', '0002_bignote_littlenote'),
    ]

    operations = [
        migrations.AddField(
            model_name='bignote',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='littlenote',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
