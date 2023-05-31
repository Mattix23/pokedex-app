# Generated by Django 4.2.1 on 2023-05-31 16:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pokemon', '0005_pokemon_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='text',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='types',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pokemon', to=settings.AUTH_USER_MODEL),
        ),
    ]
