# Generated by Django 3.1.2 on 2020-11-03 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webcms', '0005_auto_20201103_1915'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='author',
            new_name='author_name',
        ),
    ]
