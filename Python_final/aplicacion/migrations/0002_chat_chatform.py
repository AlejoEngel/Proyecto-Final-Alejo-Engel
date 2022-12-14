# Generated by Django 4.0.6 on 2022-09-28 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario_to', models.CharField(max_length=20)),
                ('usuario_from', models.CharField(max_length=20)),
                ('mensaje', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='chatform',
            fields=[
                ('chat_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aplicacion.chat')),
            ],
            bases=('aplicacion.chat',),
        ),
    ]
