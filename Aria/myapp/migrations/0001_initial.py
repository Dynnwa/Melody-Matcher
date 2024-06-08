# Generated by Django 5.0.6 on 2024-06-08 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SongItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
                ('length', models.IntegerField()),
                ('genre', models.CharField(max_length=100)),
                ('fingerprint', models.CharField(max_length=100)),
            ],
        ),
    ]
