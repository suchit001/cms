# Generated by Django 2.0.6 on 2018-06-29 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_customuser_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='post',
        ),
        migrations.AddField(
            model_name='customuser',
            name='profpic',
            field=models.FileField(default='', upload_to=''),
        ),
    ]