# Generated by Django 4.1.7 on 2023-03-26 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Users', '0004_alter_avatar_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avatar',
            old_name='imagen',
            new_name='imagen_avatar',
        ),
    ]
