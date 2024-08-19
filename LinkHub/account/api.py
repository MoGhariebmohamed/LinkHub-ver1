from django.http import JsonResponse
from rest_framework.decorators import  permission_classes, authentication_classes ,api_view
from . forms import SingupForm

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def singup(request):
    data = request.data
    message = f"Hello, {data['user']}! Your account has been created."

    form = SingupForm({
        'email':data.get('email'),
        'name':data.get('name'),
        'password1':data.get('password1'),
        'password2':data.get('password2'),
        })
    if form.is_valid():
        form.save()

        # Send verification email later
    else:
        message = "Error: Account could not be created."
    return JsonResponse({'staus': message})