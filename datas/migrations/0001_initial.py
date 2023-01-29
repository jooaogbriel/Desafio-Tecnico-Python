# Generated by Django 4.1.5 on 2023-01-29 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_data', models.IntegerField()),
                ('date', models.DateField()),
                ('value', models.FloatField()),
                ('cpf', models.CharField(max_length=11)),
                ('card', models.CharField(max_length=12)),
                ('hour', models.TimeField()),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datas', to='storage.storage')),
            ],
        ),
    ]
