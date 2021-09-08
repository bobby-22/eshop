from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        min_length=3,
        max_length=20,
        error_messages={
            "blank": "Username cannot be empty",
            "min_length": "Username must be between 3 and 20 characters",
        },
    )

    email = serializers.EmailField(
        error_messages={
            "blank": "Email cannot be empty",
        },
    )

    password1 = serializers.CharField(
        label="Password",
        style={"input_type": "password"},
        min_length=4,
        max_length=128,
        write_only=True,
        error_messages={
            "blank": "Password cannot be empty",
            "min_length": "Password must be between longer than 4 characters",
        },
    )
    password2 = serializers.CharField(
        label="Confirm password",
        style={"input_type": "password"},
        min_length=4,
        max_length=128,
        write_only=True,
        error_messages={
            "blank": "Password confirmation cannot be empty",
            "min_length": "Password must be longer than 4 characters",
        },
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def validate(self, attrs):
        if attrs["username"] == "" or attrs["username"] is None:
            raise serializers.ValidationError("Username is required")
        if User.objects.filter(username=attrs["username"]).exists():
            raise serializers.ValidationError("This username is already taken")
        if User.objects.filter(email=attrs["email"]).exists():
            raise serializers.ValidationError("This email is already used")
        if attrs["password1"] != attrs["password2"]:
            raise serializers.ValidationError("Passwords didn't match")
        return super().validate(attrs)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
        )
        user.set_password(validated_data["password2"])
        user.save()
        return user


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        error_messages={
            "blank": "Username cannot be empty",
        },
    )
    password1 = serializers.CharField(
        style={"input_type": "password"},
        write_only=True,
        error_messages={
            "blank": "Password cannot be empty",
        },
    )


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        data["username"] = self.user.username
        data["user_id"] = self.user.id
        return data
