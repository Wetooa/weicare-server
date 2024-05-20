from django.urls import path


from weicare_server.routes import notification, health_data, contact, device, user, send_sms

urlpatterns = [
    path("/user/get_profile/<int:user_id>", user.get_profile, name="get_profile"),
    path("/user/get_all_profiles", user.get_all_profiles, name="get_all_profiles"),
    path("/user/add_user", user.add_user, name="add_user"),

    path('/health-data/add/<int:user_id>/', health_data.add_health_data, name='add_health_data'),
    path('/health-data/add/<int:user_id>/elevated', health_data.add_elevated_health_data, name='add_elevated_health_data'),
    path('/health-data/recent/<int:user_id>/', health_data.get_recent_health_data, name='get_recent_health_data'),
    path('/health-data/all/<int:user_id>/', health_data.get_all_health_data, name='get_all_health_data'),

    path('/contacts/create/', contact.create_contact, name='create_contact'),
    path('/contacts/<int:user_id>/', contact.get_all_contacts, name='get_all_contacts'),
    path('/contacts/<int:user_id>/<int:contact_id>/', contact.get_single_contact, name='get_single_contact'),
    path('/contacts/update/<int:user_id>/<int:contact_id>/', contact.update_contact, name='update_contact'),
    path('/contacts/delete/<int:user_id>/<int:contact_id>/', contact.delete_contact, name='delete_contact'),   
    
    path('/device/create/', device.create_device, name='create_device'),
    path('/device/<int:user_id>/', device.get_all_devices, name='get_all_devices'),
    path('/device/<int:user_id>/<int:device_id>/', device.get_single_device, name='get_single_device'),
    path('/device/update/<int:user_id>/<int:device_id>/', device.update_device, name='update_device'),
    path('/device/delete/<int:user_id>/<int:device_id>/', device.delete_device, name='delete_device'),

    path('/notification/create/', notification.create_notification, name='create_notification'),
    path('/notification/<int:user_id>/', notification.get_all_notifications, name='get_all_notifications'),
    path('/notification/<int:user_id>/<int:notification_id>/', notification.get_single_notification, name='get_single_notification'),
    path('/notification/update/<int:user_id>/<int:notification_id>/', notification.update_notification, name='update_notification'),
    path('/notification/delete/<int:user_id>/<int:notification_id>/', notification.delete_notification, name='delete_notification'),


]



