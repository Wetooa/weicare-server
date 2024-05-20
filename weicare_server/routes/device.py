
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from weicare_server.models import Device, User
from django.shortcuts import get_object_or_404

@csrf_exempt
def create_device(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user = get_object_or_404(User, id=user_id)
        device = Device(
            user=user,
            name=request.POST.get('name'),
            is_active=bool(request.POST.get('is_active')),
        )
        device.save()
        return JsonResponse({'message': 'Device created successfully'}, status=201)
    return JsonResponse({'error': 'Unsupported request method'}, status=405)

def get_all_devices(request, user_id):
    user = get_object_or_404(User, id=user_id)
    devices = Device.objects.filter(user=user).values()
    return JsonResponse({'devices': list(devices)}, status=200)

def get_single_device(request, user_id, device_id):
    user = get_object_or_404(User, id=user_id)
    device = get_object_or_404(Device, id=device_id, user=user)
    data = {
        'name': device.name,
        'is_active': device.is_active,
        'created_at': device.created_at,
    }
    return JsonResponse(data, status=200)

@csrf_exempt
def update_device(request, user_id, device_id):
    if request.method == 'PUT':
        user = get_object_or_404(User, id=user_id)
        device = get_object_or_404(Device, id=device_id, user=user)
        device.name = request.POST.get('name')
        device.is_active = bool(request.POST.get('is_active'))
        device.save()
        return JsonResponse({'message': 'Device updated successfully'}, status=200)
    return JsonResponse({'error': 'Unsupported request method'}, status=405)

@csrf_exempt
def delete_device(request, user_id, device_id):
    if request.method == 'DELETE':
        user = get_object_or_404(User, id=user_id)
        device = get_object_or_404(Device, id=device_id, user=user)
        device.delete()
        return JsonResponse({'message': 'Device deleted successfully'}, status=200)
    return JsonResponse({'error': 'Unsupported request method'}, status=405)
