from django.db import models
from django.utils import timezone

class SexType(models.TextChoices):
    MALE = 'male', 'Male'
    FEMALE = 'female', 'Female'

class HeartClassificationType(models.TextChoices):
    GOOD = 'good', 'Good'
    RISK = 'risk', 'Risk'
    DANGER = 'danger', 'Danger'

class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    address = models.TextField()

    age = models.IntegerField()
    sex = models.CharField(max_length=10, choices=SexType.choices)
    weight = models.FloatField()
    height = models.FloatField()

    created_at = models.DateTimeField(default=timezone.now)

class Contact(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField()
    address = models.TextField()
    relationship = models.CharField(max_length=255)

    numbers = models.CharField(max_length=20)
    emails = models.EmailField()

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')

    created_at = models.DateTimeField(default=timezone.now)

class Device(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='devices')

    created_at = models.DateTimeField(default=timezone.now)

class HealthData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='health_data')

    # TODO: temp lang muna
    raw_troponin_readings = models.IntegerField()
    heart_rate = models.IntegerField()

    systolic_bp = models.IntegerField()
    diastolic_bp = models.IntegerField()

    heart_status = models.CharField(max_length=255)
    classification = models.CharField(max_length=10, choices=HeartClassificationType.choices)

    created_at = models.DateTimeField(default=timezone.now)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')

    title = models.CharField(max_length=255)
    message = models.TextField()

    type = models.CharField(max_length=10, choices=HeartClassificationType.choices)
    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(default=timezone.now)



