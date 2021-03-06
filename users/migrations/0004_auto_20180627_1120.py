# Generated by Django 2.0.6 on 2018-06-27 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_bd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='security_answer',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='security_question',
        ),
        migrations.AddField(
            model_name='customuser',
            name='sa',
            field=models.CharField(default=False, max_length=10, verbose_name='Security Answer'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='sq',
            field=models.TextField(choices=[('1', 'Best friends name'), ('2', 'Favourite food'), ('3', "Pet's name")], default=False, max_length=20, verbose_name='Security Question'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='bd',
            field=models.DateField(verbose_name='Birth Date'),
        ),
    ]
