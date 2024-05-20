
from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from weicare_server.models import User


def get_profile(request, user_id):
    if request.method == "GET":
        user = User.objects.get(id = user_id)
        return JsonResponse( status=200, data = {"user": user  },  safe = False)


def add_user(request) :
    if request.method == 'POST':
        try:
            data = request.POST 
            firstname = data.get('firstname')
            lastname = data.get('lastname')
            address = data.get('address')
            age = int(data.get('age'))
            sex = data.get('sex')
            weight = float(data.get('weight'))
            height = float(data.get('height'))

            new_user = User(
                firstname=firstname,
                lastname=lastname,
                address=address,
                age=age,
                sex=sex,
                weight=weight,
                height=height,
            )

            new_user.save()

            return JsonResponse({'message': 'User created successfully'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Unsupported request method'}, status=405)


def get_all_profiles(request):
    if request.method == "GET":
        users = User.objects.get()
        return JsonResponse(status = 200, data= {"users" : users}, safe = False)

