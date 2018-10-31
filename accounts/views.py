from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings

from .serializers import TokenSerializer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

@csrf_exempt
@permission_classes((permissions.AllowAny,))
@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        serializer = TokenSerializer(data={
            "token": jwt_encode_handler(
                jwt_payload_handler(user)
            )
        })
        serializer.is_valid()
        return Response(serializer.data)
    return Response(status=status.HTTP_401_UNAUTHORIZED)
        


