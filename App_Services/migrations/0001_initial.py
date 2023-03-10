# Generated by Django 4.1.7 on 2023-03-09 20:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('servicio', models.CharField(choices=[('impresion3D', 'Impresion3D'), ('escaneo3D', 'Escaneo3D'), ('software', 'Software'), ('otro', 'Otro')], default='impresion3D', max_length=15)),
                ('marca', models.CharField(max_length=40)),
                ('modelo', models.CharField(max_length=40)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('anio', models.IntegerField()),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('telefono_contacto', models.IntegerField()),
                ('email_contacto', models.EmailField(max_length=254)),
                ('imagen_servicio', models.ImageField(blank=True, null=True, upload_to='imagenes/')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['usuario', '-fecha_publicacion'],
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('mensaje', models.TextField(blank=True, null=True)),
                ('fecha_comentario', models.DateTimeField(auto_now_add=True)),
                ('comentario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='App_Services.servicio')),
            ],
            options={
                'ordering': ['-fecha_comentario'],
            },
        ),
    ]
