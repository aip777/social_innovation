# Generated by Django 3.1.2 on 2020-10-31 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcms', '0004_process_process_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='process',
            old_name='icon',
            new_name='icon_one',
        ),
        migrations.RenameField(
            model_name='process',
            old_name='process_title',
            new_name='icon_two',
        ),
        migrations.RenameField(
            model_name='process',
            old_name='process_details',
            new_name='process_details_two',
        ),
        migrations.AddField(
            model_name='process',
            name='process_title_one',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='process',
            name='process_title_two',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
