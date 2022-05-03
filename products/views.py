from django.shortcuts import render
from rest_framework.permissions import AllowAny
from .serializers import PostCreateUpload
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from .models import Identified
# Create your views here.


class CreateImageInfo(APIView):
    queryset = Identified.object.all()
    serializer_class = PostCreateUpload
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
