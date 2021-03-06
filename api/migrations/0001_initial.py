# Generated by Django 4.0.2 on 2022-06-07 05:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('deviceId', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('deviceType', models.CharField(max_length=20)),
                ('lightStatus1', models.IntegerField(choices=[(0, 0), (1, 1)], default=0)),
                ('lightStatus2', models.IntegerField(choices=[(0, 0), (1, 1)], default=0)),
                ('lightStatus3', models.IntegerField(choices=[(0, 0), (1, 1)], default=0)),
                ('lightStatus4', models.IntegerField(choices=[(0, 0), (1, 1)], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.device')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
