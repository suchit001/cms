# Generated by Django 2.0.6 on 2018-06-29 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20180627_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='post',
            field=models.FileField(default=False, upload_to=''),
        ),
    ]
