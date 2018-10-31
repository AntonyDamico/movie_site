from rest_framework import serializers

class TokenSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=255)