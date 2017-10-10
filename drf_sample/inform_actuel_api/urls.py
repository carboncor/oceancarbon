from django.conf.urls import url

from .views import (
    FichierAPIView, FichierDetailAPIView, FichierByIdAPIView,
    VideoAPIView, VideoByIdAPIView, VideoDetailAPIView,
    PhotoAPIView, PhotoByIdAPIView, PhotoDetailAPIView,
    PhotoByCategoryAPIView

)

urlpatterns = [
    url(r'^fichiers/$', FichierAPIView.as_view(), name='fichier_list'),
    url(r'^fichierById/$', FichierByIdAPIView.as_view(), name='fichier-ById'),
    url(r'^fichierById/(?P<pk>[0-9]+)/$', FichierDetailAPIView.as_view(), name='fichier-detail'),

    url(r'^videos/$', VideoAPIView.as_view(), name="video_list"),
    url(r'^videoById/$', VideoByIdAPIView.as_view(), name='video-ById'),
    url(r'^videoById/(?P<pk>\d+)$', VideoDetailAPIView.as_view(), name='video-detail'),

    url(r'^photos/$', PhotoAPIView.as_view(), name="movie_list"),
    url(r'^photoById/$', PhotoByIdAPIView.as_view(), name='movie-ById'),
    url(r'^photoById/(?P<pk>\d+)$', PhotoDetailAPIView.as_view(), name='movie-detail'),
    url(r'^photosByCategory/(?P<category>.+)/$', PhotoByCategoryAPIView.as_view(), name='photo-category'),

]


