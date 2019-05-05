# Generated by Django 2.2 on 2019-04-21 14:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asso',
            fields=[
                ('idAsso', models.AutoField(primary_key=True, serialize=False)),
                ('nomAsso', models.CharField(max_length=100)),
                ('typeAsso', models.CharField(max_length=40)),
                ('description', models.TextField(null=True)),
                ('dateCreation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de creation')),
            ],
            options={
                'verbose_name': 'association',
                'ordering': ['idAsso'],
            },
        ),
    ]
