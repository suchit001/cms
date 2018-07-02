# Generated by Django 2.0.6 on 2018-07-02 05:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20180630_1815'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(default='', upload_to='documents%Y%m%d')),
                ('birth_certificate', models.FileField(default='', upload_to='documents%Y%m%d')),
                ('marksheet', models.FileField(default='', upload_to='documents%Y%m%d')),
            ],
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profpic',
            field=models.FileField(default='', upload_to='documents%Y%m%d'),
        ),
        migrations.AddField(
            model_name='documents',
            name='customuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]