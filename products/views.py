
from xml.dom.minidom import Identified
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PostCreateUpload
import requests
from django.db import models
from rest_framework.parsers import MultiPartParser, FormParser
import os
from foodapi.settings import BASE_DIR
# Create your views here.


class CreateImageInfo(APIView):
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = PostCreateUpload

    def post(self, request, *args, **kwargs):
        headers = {'Authorization': 'Bearer ' +
                   '6833ec9e1b6fb4ce2bfce0e01adc084cac320a9a'}
        url = 'https://api.logmeal.es/v2/image/recognition/type/{model_version}'
        file = PostCreateUpload(data=request.FILES)
        if file.is_valid():
            file.save()
            image = file.data['image']
            resp = requests.post(
                url, files={'image': open(image, 'r')}, headers=headers)
            return Response(resp.data, status=status.HTTP_201_CREATED)

    # def post(self, request, *args, **kwargs):
    #     headers = {'Authorization': 'Bearer ' +
    #                '6833ec9e1b6fb4ce2bfce0e01adc084cac320a9a'}
    #     url = 'https://api.logmeal.es/v2/image/recognition/type/{model_version}'
    #     serializer = PostCreateUpload(data=request.FILES['image'])
    #     if serializer.is_valid():
    #         img = Identified(image=serializer)
    #         img.save()
            # resp = requests.post(
            #     url, files={'image': open(img, 'r')}, headers=headers)
    #         return Response(img.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def post(self, request, *args, **kwargs):
        # headers = {'Authorization': 'Bearer ' +
        #            'caab3974b560f34dddf03df4059e25711c83dd38'}
    #     url = 'https://api.logmeal.es/v2/image/recognition/type/'
    #     serializer_class = PostCreateUpload
    #     serializer = serializer_class(data=request.data['image'])
    #     if serializer.is_valid():
    #         resp = requests.post(url, serializer, headers=headers)
    #         serializer.save()

    #         return Response(resp.json, status=200)
#
# def post(self, request):
#     headers = {'Authorization': 'Bearer ' +
#                 'caab3974b560f34dddf03df4059e25711c83dd38'}
#     url = 'https://api.logmeal.es/v2/image/recognition/type/'
#     image = get_object_or_404(Identified, image=self)
#     serializer_class = PostCreateUpload
#     serializer = serializer_class(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save(parent=image)
#         res = requests.post(
#             url, files={'image': open(serializer, 'r')}, headers=headers)
#         return Response(res.data, status=200)
