from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views import View
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import GenericAPIView
from rest_framework import status, serializers
from rest_framework.response import Response

from structure.accounts.models.base import User
from structure.accounts.models.profile import Profile
from structure.accounts.serializer import LoginSerializer


## Login view to our system 

class LoginView(View):
    
    def get(self,request):
        return render(request,'user/login.html')

    def post(self,request):
        # getting data from client 
        username = request.POST.get('username',None)
        password =request.POST.get('password',None)

        ## checking if ther user exists 
        ## user can input username or phone number
        match_user = User.objects.filter(
            Q(username=username) |
            Q(profile__phone=username)
        )
        if match_user.exists():
            user = authenticate(request,username=match_user.first().username,password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                # message
                messages.warning(request,'Sorry Password didn`t match')
                return redirect('login')
        ## if user not exists to our system , return Error
        else:
            # message
            messages.warning(request,'User Not Found')
            return redirect('login')
            



# Logout View  of our system 
class LogoutView(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self,request):
        logout(request)
        return redirect('/')        


## User register view of our system 
class RegisterView(View):

    def get(self,request):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request,'user/sign-up.html')

    def post(self,request):
        # getting data from client 
        full_name = request.POST.get('fullname',None)
        phone_number = request.POST.get('phone',None)
        password = request.POST.get('password1',None)
        confirm_password = request.POST.get('password2',None)

        ## Checking if phone number Already exists 
        ## if exists , return the error else proceed further
        if Profile.objects.filter(phone=phone_number).exists():
            messages.warning(request,"Phone Number Already Exists !!")
            return redirect('register')
        else:
            ## Creating The User Instance first 
            create_user = User(
                username = f"{full_name.split()[0]}##{phone_number}",
                password = make_password(password),
                confirm_password = make_password(confirm_password)
            )
            create_user.save()

            ## Creating the Profie along with the User instance 
            save_profile = Profile(
                user = create_user,
                full_name = full_name,
                phone = phone_number
            )
            save_profile.save()
            messages.success(request,"Account Created Successfully! \nPlease Login to Continue")
            return redirect('login')


## Response of Phone number checking using HTMX 
## when user enter his/her phone number 
## HTMX will check if the phone number exists or not by this URL end 

class CheckPhoneNumber(View):
    def post(self,request):
        phone_number = request.POST.get('phone')
        
        if Profile.objects.filter(phone=phone_number).exists():
            return HttpResponse("<div style='color:red; padding:2px;'>The Phone Number is Already Exists !</div>")
        else:
            return HttpResponse("<div style='color:green; padding:2px;'>The Phone Number is Available</div>")
            

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
            Q(profile__phone=data['username'])
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


