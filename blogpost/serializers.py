from rest_framework import serializers
from .models import BlogPost, Author
from django.contrib.auth import authenticate


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        # read_only_fields = ['username']

    def create(self, validated_data):
        return Author.objects.create_user(**validated_data)

class BlogPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
        ordering = ['-created_at']

class LoginSerializers(serializers.Serializer):
    username = serializers.CharField(max_length = 150, required=True)
    password = serializers.CharField(max_length=128, write_only=True, required=True)

    # def validate(self, data):
    #     user = authenticate(username=data.get('username'), password=data.get('password'))
    #     if user is None:
    #         raise serializers.ValidationError('Invalid username or password')
    #     if not user.is_active:
    #         raise serializers.ValidationError('User account has been disabled')
    #     data['user'] = user
    #     return data

