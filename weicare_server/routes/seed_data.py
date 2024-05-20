import random
from django.utils import timezone
from weicare_server.models import User, Contact, Device, HealthData, Notification, SexType, HeartClassificationType

def seed_users(num_users=10):
    for _ in range(num_users):
        user = User.objects.create(
            firstname='First' + str(random.randint(1, 100)),
            lastname='Last' + str(random.randint(1, 100)),
            address='Address' + str(random.randint(1, 100)),
            age=random.randint(18, 80),
            sex=random.choice([SexType.MALE, SexType.FEMALE]),
            weight=random.uniform(50, 100),
            height=random.uniform(150, 200),
            created_at=timezone.now()
        )
        # Call other seeder functions related to this user (e.g., seed_contacts, seed_devices, etc.)
        seed_contacts(user)
        seed_devices(user)
        seed_health_data(user)
        seed_notifications(user)

def seed_contacts(user, num_contacts=5):
    for _ in range(num_contacts):
        contact = Contact.objects.create(
            firstname='ContactFirst' + str(random.randint(1, 100)),
            lastname='ContactLast' + str(random.randint(1, 100)),
            age=random.randint(18, 80),
            address='ContactAddress' + str(random.randint(1, 100)),
            relationship='Relationship' + str(random.randint(1, 100)),
            numbers='1234567890',  # Sample phone number
            emails='contact@example.com',  # Sample email
            user=user,
            created_at=timezone.now()
        )

def seed_devices(user, num_devices=3):
    for _ in range(num_devices):
        device = Device.objects.create(
            name='Device' + str(random.randint(1, 100)),
            is_active=random.choice([True, False]),
            user=user,
            created_at=timezone.now()
        )

def seed_health_data(user, num_health_data=10):
    for _ in range(num_health_data):
        health_data = HealthData.objects.create(
            user=user,
            raw_troponin_readings=random.randint(1, 100),
            heart_rate=random.randint(60, 120),
            systolic_bp=random.randint(100, 150),
            diastolic_bp=random.randint(60, 100),
            heart_status='Normal',  # Sample heart status
            classification=random.choice([HeartClassificationType.GOOD, HeartClassificationType.RISK, HeartClassificationType.DANGER]),
            created_at=timezone.now()
        )

def seed_notifications(user, num_notifications=5):
    for _ in range(num_notifications):
        notification = Notification.objects.create(
            user=user,
            title='NotificationTitle' + str(random.randint(1, 100)),
            message='NotificationMessage' + str(random.randint(1, 100)),
            type=random.choice([HeartClassificationType.GOOD, HeartClassificationType.RISK, HeartClassificationType.DANGER]),
            is_read=random.choice([True, False]),
            created_at=timezone.now()
        )

def run_seeders():
    seed_users()
