# Generated by Django 3.1.2 on 2020-11-13 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webcms', '0013_auto_20201113_1935'),
    ]

    operations = [
        migrations.RenameField(
            model_name='footer',
            old_name='nav_link_about',
            new_name='about_link',
        ),
        migrations.RenameField(
            model_name='footer',
            old_name='nav_link_blog',
            new_name='blog_link',
        ),
        migrations.RenameField(
            model_name='footer',
            old_name='nav_link_contact',
            new_name='contact_link',
        ),
        migrations.RenameField(
            model_name='footer',
            old_name='nav_link_project',
            new_name='project_link',
        ),
        migrations.RenameField(
            model_name='footer',
            old_name='nav_link_services',
            new_name='services_link',
        ),
        migrations.RenameField(
            model_name='footer',
            old_name='nav_link_team',
            new_name='team_link',
        ),
    ]
