from rest_framework import serializers
from glory import models

class projectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.project
        fields="__all__"

class modelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.modelse
        fields="__all__"
