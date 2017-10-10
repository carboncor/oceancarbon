from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer, FichierSerializer, VideoSerializer, PhotoSerializer
from inform_actuel.models import Fichier, Video, Photo
from django.contrib.auth.models import User


class SafeMethodsOnlyPermission(permissions.BasePermission):
    """Only can access non-destructive methods (like GET and HEAD)"""

    def has_permission(self, request, view):
        return self.has_object_permission(request, view)

    def has_object_permission(self, request, view, obj=None):
        return request.method in permissions.SAFE_METHODS


class FichierAPIView(APIView):
    def get(self, request, format=None):
        fichiers = Fichier.objects.all()
        serializer = FichierSerializer(fichiers, many=True)
        return Response(serializer.data)


class FichierByIdAPIView(APIView):
    def get(self, request, format=None):
        fichier = Fichier.objects.all().order_by('id')
        serializer = FichierSerializer(fichier, many=True)
        return Response(serializer.data)


class FichierDetailAPIView(APIView):
    def get(self, request, pk, format=None):
        fichier = Fichier.objects.get(id=pk)
        serializer = FichierSerializer(fichier)
        return Response(serializer.data)


class VideoAPIView(APIView):
    def get(self, request, format=None):
        videos = Video.objects.all().order_by('id')
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)


class VideoByIdAPIView(APIView):
    def get(self, request, format=None):
        video = Video.objects.all().order_by('id')
        serializer = VideoSerializer(video, many=True)
        return Response(serializer.data)


class VideoDetailAPIView(APIView):
    def get(self, request, pk, format=None):
        video = Video.objects.get(pk=pk)
        serializer = VideoSerializer(video)
        return Response(serializer.data)


class PhotoAPIView(APIView):
    def get(self, request, format=None):
        photos = Photo.objects.all().order_by('id')
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)


class PhotoByIdAPIView(APIView):
    def get(self, request, format=None):
        photo = Photo.objects.all().order_by('id')
        serializer = VideoSerializer(photo, many=True)
        return Response(serializer.data)


class PhotoDetailAPIView(APIView):
    def get(self, request, pk, format=None):
        photo = Photo.objects.get(pk=pk)
        serializer = PhotoSerializer(photo)
        return Response(serializer.data)


class PhotoByCategoryAPIView(APIView):
    def get(self, request, category, format=None):
        photo = Photo.objects.filter(category=category)
        serializer = PhotoSerializer(photo, many=True)
        return Response(serializer.data)

# class MovieActeurList(generics.ListAPIView):
#     model = Acteur
#     queryset = Acteur.objects.all()
#     serializer_class = ActeurSerializer
#
#     def get_queryset(self):
#         queryset = super(MovieActeurList, self).get_queryset()
#         return queryset.filter(movie=self.kwargs.get('pk'))
