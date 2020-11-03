# Generated by Django 3.1.2 on 2020-11-03 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcms', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='blog_details',
            new_name='blog_details_one',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='blog_headline',
            new_name='blog_headline_one',
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_details_two',
            field=models.CharField(blank=True, max_length=1500),
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_headline_two',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_images_two',
            field=models.ImageField(default=1, upload_to='blog'),
            preserve_default=False,
        ),
    ]