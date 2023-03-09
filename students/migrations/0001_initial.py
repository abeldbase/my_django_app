# Generated by Django 4.1.5 on 2023-03-03 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField(null=True)),
                ('phone', models.IntegerField()),
                ('city', models.CharField(blank=True, null=True, max_length=255)),
                ('zip', models.IntegerField(blank=True, null=True)),
                ('state', models.CharField(max_length=255)),
                ('graduation', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('year', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), (
                    'JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], default='FR', max_length=255)),
            ],
        ),
    ]
