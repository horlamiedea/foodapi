
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .serializers import PostCreateUpload
import requests
import json
from .models import Identified
# Create your views here.


class CreateImageInfo(APIView):
    serializer_class = PostCreateUpload

    # def post(self, request, *args, **kwargs):
    #     headers = {'Authorization': 'Bearer ' +
    #                'caab3974b560f34dddf03df4059e25711c83dd38'}
    #     url = 'https://api.logmeal.es/v2/image/recognition/type/'
    #     serializer_class = PostCreateUpload
    #     serializer = serializer_class(data=request.data['image'])
    #     if serializer.is_valid():
    #         resp = requests.post(url, serializer, headers=headers)
    #         serializer.save()

    #         return Response(resp.json, status=200)

    def post(self, request):
        headers = {'Authorization': 'Bearer ' +
                   'caab3974b560f34dddf03df4059e25711c83dd38'}
        url = 'https://api.logmeal.es/v2/image/recognition/type/'
        image = get_object_or_404(Identified, image=self)
        serializer_class = PostCreateUpload
        serializer = serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(parent=image)
            res = requests.post(
                url, files={'image': open(serializer, 'r')}, headers=headers)
            return Response(res.data, status=200)
