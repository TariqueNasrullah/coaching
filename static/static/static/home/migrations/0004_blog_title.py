# Generated by Django 2.1.8 on 2019-05-22 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20190522_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(default='', max_length=1024),
        ),
    ]
