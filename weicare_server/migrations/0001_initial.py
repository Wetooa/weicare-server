# Generated by Django 3.2.12 on 2024-05-16 14:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('age', models.IntegerField()),
                ('sex', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('weight', models.FloatField()),
                ('height', models.FloatField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('type', models.CharField(choices=[('good', 'Good'), ('risk', 'Risk'), ('danger', 'Danger')], max_length=10)),
                ('is_read', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='weicare_server.user')),
            ],
        ),
        migrations.CreateModel(
            name='HealthData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('troponin_level', models.IntegerField()),
                ('heart_rate', models.IntegerField()),
                ('blood_pressure', models.CharField(max_length=20)),
                ('heart_status', models.CharField(max_length=255)),
                ('classification', models.CharField(choices=[('good', 'Good'), ('risk', 'Risk'), ('danger', 'Danger')], max_length=10)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='health_data', to='weicare_server.user')),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='weicare_server.user')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('address', models.TextField()),
                ('relationship', models.CharField(max_length=255)),
                ('numbers', models.CharField(max_length=20)),
                ('emails', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='weicare_server.user')),
            ],
        ),
    ]