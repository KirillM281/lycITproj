# Generated by Django 3.0.6 on 2020-11-05 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Diary', '0010_auto_20201105_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventnote',
            name='eventimage',
            field=models.ImageField(null=True, upload_to='image/'),
        ),
    ]
