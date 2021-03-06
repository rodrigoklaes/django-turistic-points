# Generated by Django 2.0.13 on 2021-06-26 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line1', models.CharField(max_length=150)),
                ('line2', models.CharField(blank=True, max_length=150, null=True)),
                ('city', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('lat', models.CharField(blank=True, max_length=100, null=True)),
                ('lng', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
