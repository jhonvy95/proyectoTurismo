# Generated by Django 3.2.8 on 2021-10-10 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('idReserva', models.AutoField(primary_key=True, serialize=False)),
                ('fechaReserva', models.DateField()),
                ('fechaIngreso', models.DateField()),
                ('fechaSalida', models.DateField()),
                ('costo', models.IntegerField()),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cliente')),
            ],
        ),
    ]
