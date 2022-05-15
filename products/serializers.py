
import os
from django.conf import settings
from rest_framework import serializers
from .models import Identified


class PostCreateUpload(serializers.ModelSerializer):
    class Meta():
        model = Identified
        fields = ('timestamp', 'image')

    # def create(self, validated_data):
    #     return Identified.objects.create(**validated_data)

    # def clean_image(self, value):
    #     initial_path = value.path
    #     new_path = settings.MEDIA_ROOT + value.name
    #     os.rename(initial_path, new_path)
    #     return value
