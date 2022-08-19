from rest_framework import serializers
from users.models import CustomUser
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

class RegisterUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=68,
        write_only=True,
        validators = [validate_password],
    )
    password2 = serializers.CharField(
        write_only=True, 
        required=True
    )

    class Meta:
        model = CustomUser
        fields = ('nickname', 'username', 'password', 'password2')
    
    def validate(self, instance):
        if instance['password'] != instance['password2']:
            raise serializers.ValidationError(
                {"password": 'Password fields didnt match'}
            )
        return instance
    
    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

    

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=68, write_only=True)

    nickname = serializers.CharField(max_length=255, read_only=True)
    tokens = serializers.CharField(max_length=68, read_only = True)

    class Meta:
        model = CustomUser
        fields = ['nickname', 'username', 'password', 'tokens']

    def validate(self, instance):
        username = instance.get('username','')
        password = instance.get('password','')

        user = auth.authenticate(username=username, password=password)

        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        

        return {
            'username' : user.username,
            'nickname' : user.nickname,
            'tokens' : user.tokens
        }
        


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {
        'bad_token': ('Token is expired or invalid')
    }

    def validate(self, instance):
        self.token = instance['refresh']
        return instance

    def save(self, **kwargs):

        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
            self.fail('bad_token')


# class ChangePasswordSerializer(serializers.ModelSerializer):
    
#     old_password = serializers.CharField(max_length=68, write_only=True, required=True)
#     new_password = serializers.CharField(max_length=68, write_only=True, required=True, validators=[validate_password])
#     new_password2 = serializers.CharField(max_length=68, write_only=True, required=True)
    

#     class Meta:
#         model = CustomUser
#         fields = ('old_password', 'new_password', 'new_password2')

#     def validate(self, instance):
#         if instance['new_password'] != instance['new_password2']:
#             raise serializers.ValidationError({"password": "Password fields didn't match."})

#         return instance


class ChangePasswordSerializer(serializers.Serializer):
    
    model = CustomUser

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(max_length=68, write_only=True, required=True)
    new_password2 = serializers.CharField(max_length=68, write_only=True, required=True)

    
    def validate(self, instance):
        if instance['new_password'] != instance['new_password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return instance