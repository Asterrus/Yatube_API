# Generated by Django 3.2.16 on 2023-01-01 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='Проверка подписки на сомого себя',
        ),
    ]
