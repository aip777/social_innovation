# Generated by Django 3.1.2 on 2020-11-13 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webcms', '0008_navbar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='navbar',
            name='is_published',
        ),
    ]
