## Views for accounts app
from django.db.models import Q
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import GenericAPIView
from rest_framework import status, serializers
from rest_framework.response import Response

from structure.accounts.models.base import User
from structure.accounts.models.employee import Employee
from structure.accounts.serializer import (
        LoginSerializer,
        RegisterSerializer
)


'''
Login view for API Authentication 
'''

class APILoginView(GenericAPIView):
    permission_classes = ()
    authentication_classes = ()
    serializer_class = LoginSerializer

    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        
        ## checking if ther user exists 
        ## user can input username or phone number
        match_user = User.objects.filter(
            Q(username=data['username']) |
            Q(employee__phone=data['username'])
        )
        if match_user.exists():
            user = authenticate(username=match_user.first().username, password=data['password'])
            if not user:
                raise serializers.ValidationError({'Error':'Password Mismatch'})
        else:
            raise serializers.ValidationError({'Error':'User doesn`t exists'})

        # generate token 
        refresh = RefreshToken.for_user(user)

        return Response({
            'access_token':str(refresh.access_token),
            'refresh_token':str(refresh)
        },status=status.HTTP_200_OK)


'''
Employee Register 
    fields 
    (
    Full Name , 
    Unique Phone Number,
    password ,
    confirm password 
    )
'''

class RegisterAPIView(GenericAPIView):
    permission_classes = ()
    authentication_classes = ()
    serializer_class =  RegisterSerializer
    queryset = Employee.objects.filter(is_active=True)

    def post(self,request):

        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"Success":"Employee Created Successfully !"})
        else:
            return Response(serializer.error_messages)

