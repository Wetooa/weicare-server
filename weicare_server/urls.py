from django.urls import path


from weicare_server.routes import notification, health_data, contact, device, user, send_sms

urlpatterns = [
    path("/user/get_profile/<int:user_id>", user.get_profile, name="get_profile"),
    path("/user/get_all_profiles", user.get_all_profiles, name="get_all_profiles"),
    path("/user/add_user", user.add_user, name="add_user"),

    path('health-data/add/<int:user_id>/', health_data.add_health_data, name='add_health_data'),
    path('health-data/add/<int:user_id>/elevated', health_data.add_elevated_health_data, name='add_elevated_health_data'),

    path('health-data/recent/<int:user_id>/', health_data.get_recent_health_data, name='get_recent_health_data'),
    path('health-data/all/<int:user_id>/', health_data.get_all_health_data, name='get_all_health_data'),
    #
    # path("/contact", contact.index, name="index"),
    #
    # path("/notification", device.idnex, name="index"),
    #
    # path("/device", user.index, name="index"),
    #
    # path("/send_sms", send_sms.index, name="index"),
]



