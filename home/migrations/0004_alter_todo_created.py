# Generated by Django 4.2 on 2023-04-13 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_todo_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created',
            field=models.DateTimeField(),
        ),
    ]
