# Generated by Django 3.0.5 on 2020-04-29 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0010_auto_20200429_0722'),
    ]

    operations = [
        migrations.AddField(
            model_name='filterphone',
            name='Predicted',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
