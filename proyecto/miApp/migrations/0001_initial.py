# Generated by Django 2.2.10 on 2020-08-30 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MiLista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articulo', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField()),
            ],
        ),
    ]