# Generated by Django 5.1.2 on 2024-12-02 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_commentmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentmodel',
            old_name='commented_on',
            new_name='timestamp',
        ),
    ]
