# Generated by Django 4.1.7 on 2023-03-27 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Users', '0008_alter_avatar_imagen_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='imagen_avatar',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes'),
        ),
    ]