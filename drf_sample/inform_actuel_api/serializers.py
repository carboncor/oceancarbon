from rest_framework import serializers

from inform_actuel.models import Document, Fichier, Video, Photo, CategoryPhoto
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id", "username"
        )


class FichierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fichier
        fields = (
            "id", "nom_fic", "url_fic", "content_doc", "document"
        )


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = (
            "id", "titre_video", "url_video"
        )


class CategoryPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryPhoto
        fields = (
            "id", "titre_cp"
        )


class PhotoSerializer(serializers.ModelSerializer):
    category = CategoryPhotoSerializer(required=False)

    class Meta:
        model = Photo
        fields = (
            "id", "titre_photo", "url_photo", "category"
        )
