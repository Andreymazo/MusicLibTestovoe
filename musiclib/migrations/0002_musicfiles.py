# Generated by Django 5.0.3 on 2024-04-13 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musiclib', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MusicFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='название произведения')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]
