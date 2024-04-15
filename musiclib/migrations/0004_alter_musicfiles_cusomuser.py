# Generated by Django 5.0.3 on 2024-04-14 08:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musiclib', '0003_musicfiles_cusomuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicfiles',
            name='cusomuser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='musicfiles', to=settings.AUTH_USER_MODEL),
        ),
    ]
