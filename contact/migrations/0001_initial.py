# Generated by Django 3.2.23 on 2024-04-18 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('read', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-createdAt'],
            },
        ),
    ]
