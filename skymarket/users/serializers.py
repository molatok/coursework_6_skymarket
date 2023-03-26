from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from .models import User


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    phone = PhoneNumberField
    image = serializers.ImageField(required=False)
    role = serializers.CharField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'password', 'email', 'image', 'role']

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone=validated_data['phone'],
            role=validated_data['role'],
            password=validated_data['password']
        )
        user.image = validated_data.get('image', None)
        user.save()

        return user



class CurrentUserSerializer(serializers.ModelSerializer):
    pass
