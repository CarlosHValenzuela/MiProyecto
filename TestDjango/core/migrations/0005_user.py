# Generated by Django 4.0.4 on 2022-07-04 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_suscripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=250, verbose_name='Nombre del usuario')),
                ('password', models.CharField(max_length=150, verbose_name='Contraseña del usuario')),
            ],
        ),
    ]
