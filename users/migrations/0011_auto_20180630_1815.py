# Generated by Django 2.0.6 on 2018-06-30 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20180630_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profpic',
            field=models.ImageField(default='', upload_to='documents%Y%m%d'),
        ),
    ]
