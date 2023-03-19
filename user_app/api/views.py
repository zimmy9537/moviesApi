from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user_app.api.serializers import RegistrationSerializer
from user_app import models


@api_view(['POST',])
def logout_view(request):
    if request.method=='POST':
        request.user.auth_token.delete()
        data={}
        data['response']='Successfully logged out!'
        return Response(data)

@api_view(['POST',])
def register_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)

        data={}


        if serializer.is_valid():
            serializer.save()

            data['response']="Registration successfull"
            data['username']=account.username
            data['email']=account.email

            token=Token.objects.get(user=account).key
            data['token']=token

        else:
            data=serializer.errors

            return Response(data)