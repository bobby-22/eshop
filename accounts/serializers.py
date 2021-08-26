from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        min_length=3,
        max_length=20,
        required=True
        )
    email = serializers.EmailField(
        required=True
        )
    password1 = serializers.CharField(
        label="Password",
        style={'input_type': 'password'},
        min_length=4,
        max_length=128,
        write_only=True,
        required=True
        )
    password2 = serializers.CharField(
        label="Confirm password",
        style={'input_type': 'password'},
        min_length=4,
        max_length=128,
        write_only=True,
        required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2"
            )
    
    def validate(self, attrs):
        if User.objects.filter(username=attrs["username"]).exists():
            raise serializers.ValidationError("This username is already taken")
        if User.objects.filter(email=attrs["email"]).exists():
            raise serializers.ValidationError("This e-mail is already used")
        if attrs["password1"] != attrs["password2"]:
            raise serializers.ValidationError("Passwords didn't match")
        return super().validate(attrs)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password2'])
        user.save()
        return user
    
class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        min_length=3,
        max_length=20,
        required=True
        )
    password1 = serializers.CharField(
        style={'input_type': 'password'},
        min_length=4,
        max_length=128,
        write_only=True,
        required=True
    )
