# Generated by Django 4.2.10 on 2024-02-20 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mmorpg', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='text',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='content',
        ),
    ]
