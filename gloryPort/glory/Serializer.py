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

class apiSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.caseapi
        fields="__all__"

class tagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields="__all__"

class taskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields="__all__"

class reportSerializer(serializers.ModelSerializer):
    createtime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    class Meta:
        model = models.Report
        fields="__all__"

class schedlerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SchedlerModel
        fields="__all__"

class detailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CaseResult
        fields="__all__"

class logSerializer(serializers.ModelSerializer):
    createtime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = models.logCase
        fields="__all__"


class numSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Num
        fields="__all__"

class gloabSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.gloadConfig
        fields="__all__"


class gloabKeySerializer(serializers.ModelSerializer):
    updatetime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = models.gloadCaseKey
        fields="__all__"

class envSerializer(serializers.ModelSerializer):
    createtime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = models.environment
        fields="__all__"

class statisticalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.statistical
        fields="__all__"