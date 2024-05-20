
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from weicare_server.models import Contact, User
from django.shortcuts import get_object_or_404

@csrf_exempt
def create_contact(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user = get_object_or_404(User, id=user_id)
        contact = Contact(
            user=user,
            firstname=request.POST.get('firstname'),
            lastname=request.POST.get('lastname'),
            age=int(request.POST.get('age')),
            address=request.POST.get('address'),
            relationship=request.POST.get('relationship'),
            numbers=request.POST.get('numbers'),
            emails=request.POST.get('emails'),
        )
        contact.save()
        return JsonResponse({'message': 'Contact created successfully'}, status=201)
    return JsonResponse({'error': 'Unsupported request method'}, status=405)


def get_all_contacts(request, user_id):
    user = get_object_or_404(User, id=user_id)
    contacts = Contact.objects.filter(user=user).values()
    return JsonResponse({'contacts': list(contacts)}, status=200)


def get_single_contact(request, user_id, contact_id):
    user = get_object_or_404(User, id=user_id)
    contact = get_object_or_404(Contact, id=contact_id, user=user)
    data = {
        'firstname': contact.firstname,
        'lastname': contact.lastname,
        'age': contact.age,
        'address': contact.address,
        'relationship': contact.relationship,
        'numbers': contact.numbers,
        'emails': contact.emails,
    }
    return JsonResponse(data, status=200)


@csrf_exempt
def update_contact(request, user_id, contact_id):
    if request.method == 'PUT':
        user = get_object_or_404(User, id=user_id)
        contact = get_object_or_404(Contact, id=contact_id, user=user)
        contact.firstname = request.POST.get('firstname')
        contact.lastname = request.POST.get('lastname')
        contact.age = int(request.POST.get('age'))
        contact.address = request.POST.get('address')
        contact.relationship = request.POST.get('relationship')
        contact.numbers = request.POST.get('numbers')
        contact.emails = request.POST.get('emails')
        contact.save()
        return JsonResponse({'message': 'Contact updated successfully'}, status=200)
    return JsonResponse({'error': 'Unsupported request method'}, status=405)

@csrf_exempt
def delete_contact(request, user_id, contact_id):
    if request.method == 'DELETE':
        user = get_object_or_404(User, id=user_id)
        contact = get_object_or_404(Contact, id=contact_id, user=user)
        contact.delete()
        return JsonResponse({'message': 'Contact deleted successfully'}, status=200)
    return JsonResponse({'error': 'Unsupported request method'}, status=405)


