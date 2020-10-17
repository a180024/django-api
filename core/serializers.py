from rest_framework import serializers
from .models import File


class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = (
            "file",
        ) 


class FileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = (
            "file",
        ) 


class FileSerializer(serializers.ModelSerializer):
    filename = serializers.ReadOnlyField()
    filepath = serializers.ReadOnlyField()
    filesize = serializers.ReadOnlyField()
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    last_updated = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

    class Meta:
        model = File
        fields = (
            'filename',
            'filepath',
            'filesize',
            'sensitivity_score',
            'flag',
            'created',
            'last_updated'
        ) 

    

        

