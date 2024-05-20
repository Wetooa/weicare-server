
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from weicare_server.models import Notification, User
from django.shortcuts import get_object_or_404

@csrf_exempt
def create_notification(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user = get_object_or_404(User, id=user_id)
        notification = Notification(
            user=user,
            title=request.POST.get('title'),
            message=request.POST.get('message'),
            type=request.POST.get('type'),
            is_read=bool(request.POST.get('is_read')),
        )
        notification.save()
        return JsonResponse({'message': 'Notification created successfully'}, status=201)
    return JsonResponse({'error': 'Unsupported request method'}, status=405)

def get_all_notifications(request, user_id):
    user = get_object_or_404(User, id=user_id)
    notifications = Notification.objects.filter(user=user).values()
    return JsonResponse({'notifications': list(notifications)}, status=200)

def get_single_notification(request, user_id, notification_id):
    user = get_object_or_404(User, id=user_id)
    notification = get_object_or_404(Notification, id=notification_id, user=user)
    data = {
        'title': notification.title,
        'message': notification.message,
        'type': notification.type,
        'is_read': notification.is_read,
        'created_at': notification.created_at,
    }
    return JsonResponse(data, status=200)

@csrf_exempt
def update_notification(request, user_id, notification_id):
    if request.method == 'PUT':
        user = get_object_or_404(User, id=user_id)
        notification = get_object_or_404(Notification, id=notification_id, user=user)
        notification.title = request.POST.get('title')
        notification.message = request.POST.get('message')
        notification.type = request.POST.get('type')
        notification.is_read = bool(request.POST.get('is_read'))
        notification.save()
        return JsonResponse({'message': 'Notification updated successfully'}, status=200)
    return JsonResponse({'error': 'Unsupported request method'}, status=405)

@csrf_exempt
def delete_notification(request, user_id, notification_id):
    if request.method == 'DELETE':
        user = get_object_or_404(User, id=user_id)
        notification = get_object_or_404(Notification, id=notification_id, user=user)
        notification.delete()
        return JsonResponse({'message': 'Notification deleted successfully'}, status=200)
    return JsonResponse({'error': 'Unsupported request method'}, status=405)
