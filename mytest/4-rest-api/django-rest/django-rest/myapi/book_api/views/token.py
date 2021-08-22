from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators \
    import api_view, authentication_classes, permission_classes
from rest_framework.status import *
from rest_framework.authtoken.models import Token


@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def create_token(request):
    if request.method == 'POST':
        token = Token.objects.create(user=request.user)
        return JsonResponse({'token': token.key}, safe=False)
