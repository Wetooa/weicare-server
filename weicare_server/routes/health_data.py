
from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from weicare_server.models import HealthData, User


def add_health_data(request, user_id):
    if request.method == 'POST':
        try:
            data = request.POST  
            user_id = int(data.get('user_id'))  
            user = User.objects.get(id=user_id) 

            raw_troponin_readings = int(data.get('raw_troponin_readings'))
            heart_rate = int(data.get('heart_rate'))
            systolic_bp = int(data.get('systolic_bp'))
            diastolic_bp = int(data.get('diastolic_bp'))

            heart_status = data.get('heart_status')
            classification = data.get('classification')

            new_health_data = HealthData(
                user=user, raw_troponin_readings=raw_troponin_readings, heart_rate=heart_rate,
                systolic_bp=systolic_bp,
                diastolic_bp=diastolic_bp,
                heart_status=heart_status,
                classification=classification,
            )

            new_health_data.save()

            return JsonResponse({'message': 'Health data created successfully'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Unsupported request method'}, status=405)

def add_elevated_health_data(request):
    if request.method == 'POST':
        try:
            data = request.POST  
            user_id = int(data.get('user_id'))  
            user = User.objects.get(id=user_id) 

            raw_troponin_readings = int(20)
            heart_rate = int(80)
            systolic_bp = int(80)
            diastolic_bp = int(120)

            heart_status = data.get('heart_status')
            classification = data.get('classification')

            new_health_data = HealthData(
                user=user,
                raw_troponin_readings=raw_troponin_readings,
                heart_rate=heart_rate,
                systolic_bp=systolic_bp,
                diastolic_bp=diastolic_bp,
                heart_status=heart_status,
                classification=classification,
            )

            new_health_data.save()

            return JsonResponse({'message': 'Health data created successfully'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Unsupported request method'}, status=405)

def get_recent_health_data(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        recent_data = HealthData.objects.filter(user=user).order_by('-created_at').first()
        if recent_data:
            data = {
                'raw_troponin_readings': recent_data.raw_troponin_readings,
                'heart_rate': recent_data.heart_rate,
                'systolic_bp': recent_data.systolic_bp,
                'diastolic_bp': recent_data.diastolic_bp,
                'heart_status': recent_data.heart_status,
                'classification': recent_data.classification,
                'created_at': recent_data.created_at,
            }
            return JsonResponse({"health_data": data}, status=200)
        else:
            return JsonResponse({'error': 'No recent health data found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


def get_all_health_data(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        all_data = HealthData.objects.filter(user=user).values()
        if all_data:
            return JsonResponse({'health_data': list(all_data)}, status=200)
        else:
            return JsonResponse({'error': 'No health data found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


