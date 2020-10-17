from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import BasicAuthentication

from .serializers import FileUploadSerializer, FileSerializer, FileUpdateSerializer
from .permissions import IsFileOwner
from .models import File


class FileListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsFileOwner]
    authentication_classes = [JWTAuthentication]
    serializer_class = FileSerializer
    queryset = File.objects.all()


class FileDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsFileOwner]
    authentication_classes = [JWTAuthentication]
    queryset = File.objects.all()
    serializer_class = FileSerializer


class FileUploadView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = FileUploadSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FileUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsFileOwner]
    authentication_classes = [JWTAuthentication]
    serializer_class = FileUpdateSerializer
    queryset = File.objects.all()

    def perform_update(self, serializer, *args, **kwargs):
        serializer.instance.reset_flag_and_sensitivity() 
        serializer.save()


class FileDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsFileOwner]
    authentication_classes = [JWTAuthentication]
    queryset = File.objects.all()






