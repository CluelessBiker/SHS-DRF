# Generated by Django 3.2.23 on 2023-12-31 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('mon', 'Monday'), ('tue', 'Tuesday'), ('wed', 'Wednesday'), ('thu', 'Thursday'), ('fri', 'Friday'), ('sat', 'Saturday'), ('sun', 'Sunday')], default='mon', max_length=10)),
                ('open', models.TimeField()),
                ('close', models.TimeField()),
                ('info', models.CharField(blank=True, max_length=50, null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.location')),
            ],
        ),
    ]
