# Generated by Django 2.1.5 on 2019-04-30 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0005_auto_20190430_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='task',
            field=models.CharField(max_length=75),
        ),
    ]