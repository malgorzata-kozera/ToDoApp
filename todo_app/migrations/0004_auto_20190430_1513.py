# Generated by Django 2.1.5 on 2019-04-30 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0003_auto_20190430_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='task',
            field=models.CharField(max_length=100),
        ),
    ]