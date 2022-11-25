'''
Acccounts App serializer 
'''

from rest_framework import serializers
from structure.accounts.models.employee import Employee
from structure.accounts.models.base import User
from django.contrib.auth.hashers import make_password


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True,style={'input_type': 'password'})


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,style={'input_type': 'password'})
    confirm_password = serializers.CharField(write_only=True,style={'input_type': 'password'})

    class Meta:
        model = Employee
        fields = ['full_name','phone','password','confirm_password'] 


    def create(self,validated_data):
        # getting Password and confirm password
        password1 = validated_data.pop('password')
        password2 = validated_data.pop('confirm_password')
        phone = validated_data.pop('phone')


        if Employee.objects.filter(phone=phone).exists():
            raise serializers.ValidationError("Phone Number Already Exists !!")
        
        elif password1 != password2:
            raise serializers.ValidationError("Password & Confirm Password Mismatch")
        else: 

            # creatng the User first then assing to customer instance
            auth_info = {
                'password':make_password(password1),
                'confirm_password':make_password(password2)
            }
            userobj = User(**auth_info)
            userobj.save()
            
            ## Assigning the user to Employee instance and save 
            employee_obj = Employee.objects.create(**validated_data)
            employee_obj.phone = phone
            employee_obj.user = userobj
            employee_obj.save()

            # Creating Username after Employee creation 
            # username is combined wiht Full name and phone Number
            employee_obj.user.username = f"{employee_obj.full_name}_{phone}"
            employee_obj.user.save()
            
            return employee_obj
        