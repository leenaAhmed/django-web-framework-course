# Generated by Django 5.1.3 on 2024-12-09 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_contact_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Full_name',
            new_name='full_name',
        ),
    ]
