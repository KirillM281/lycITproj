# Generated by Django 3.0.6 on 2020-10-18 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Diary', '0003_auto_20201018_0800'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reverse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, null=True)),
                ('oldmail', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]