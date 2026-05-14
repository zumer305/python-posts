from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def signup(request):

    username = request.data['username']
    password = request.data['password']

    user = User.objects.create_user(
        username=username,
        password=password
    )

    return Response({
        "message": "User created successfully"
    })