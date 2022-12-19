# Generated by Django 3.0 on 2022-12-18 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='institucion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='seminario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombreR', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('institucion', models.CharField(max_length=50)),
                ('fechareserva', models.DateTimeField(auto_now_add=True)),
                ('estado', models.IntegerField(choices=[(1, 'Reservado'), (2, 'Completada'), (3, 'Anulada'), (4, 'No Asisten')], default=1)),
                ('observacion', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
