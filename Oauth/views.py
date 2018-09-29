from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import uuid

# Create your views here.

# @api_view(['GET',])
# def logout(request):
#     request.user.jwt_secret = uuid.uuid4()
#     request.user.save()
#     return Response({'status': 'ok'}, status=status.HTTP_200_OK)

class LogoutViewSet(viewsets.ViewSet):

    def logout(self, request):
        request.user.jwt_secret = uuid.uuid4()
        request.user.save()
        return Response({'status': 'ok'}, status=status.HTTP_200_OK)




