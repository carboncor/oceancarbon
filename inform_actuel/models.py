
from django.db import models
from django.utils import timezone


from django.contrib.auth.models import  User


class Profil(models.Model):
    user = models.OneToOneField(User)  # La liaison OneToOne vers le modèle User
    Adresse = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")
    telephone = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return "Profil de {0}".format(self.user.username)


class Document(models.Model):
    titre_doc = models.CharField(max_length=255)
    date_create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return u"{0} [{1}]".format(self.titre_doc, self.date_create)


class Fichier(models.Model):
    nom_fic = models.CharField(max_length=255, blank=True, null=True)
    url_fic = models.FileField(upload_to="fichiers/", null=True, blank=True)
    content_doc = models.TextField(null=True)
    document = models.ForeignKey('Document')

    class Meta:
        ordering = ['nom_fic']

    def __str__(self):
        return u"{0} [{1}]".format(self.nom_fic, self.url_fic)


class Video(models.Model):
    titre_video = models.CharField(max_length=50, blank=True, null=True)
    url_video = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return "{0}".format(self.titre_video)


class CategoryPhoto(models.Model):
    titre_cp = models.CharField(max_length=255)

    def __str__(self):
        return "{0}".format(self.titre_cp)


class Photo(models.Model):
    titre_photo = models.CharField(max_length=50, blank=True, null=True)
    url_photo = models.ImageField(upload_to="photos/", null=True)
    category = models.ForeignKey('CategoryPhoto', null=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return "{0}".format(self.titre_photo)





        # class Comment(models.Model):
        #     author = models.ForeignKey(User)
        #     movie = models.ForeignKey('Movie')
        #     content = models.TextField(blank=True)
        #     created_date = models.DateTimeField(
        #         default=timezone.now)
        #
        #     def __str__(self):
        #         return "{0}".format(self.content)
        #
        #
        # class Panier(models.Model):
        #     utilisateur = models.ForeignKey(User)
        #     movie = models.ForeignKey('Movie')
        #     valide = models.BooleanField(default=False)
        #     created_date = models.DateTimeField(
        #         default=timezone.now)
        #
        #     def __str__(self):
        #         return "{0}".format(self.movie)
        #
        #
        # class Movie(models.Model):
        #     LONG_METRAGE = 'LONG METRAGE'
        #     SERIE = 'SERIE'
        #     MOVIE_TYPE = (
        #         (LONG_METRAGE, 'Long metrage'),
        #         (SERIE, 'Serie'),
        #     )
        #
        #     code = models.CharField(max_length=10, null=True, blank=True, unique=True)
        #     titre = models.CharField(max_length=100)
        #     resume = models.TextField()
        #     duree = models.CharField(max_length=10)
        #     url_trailer = models.URLField(blank=True, null=True)
        #     date_sortie = models.DateField()
        #     exclu = models.BooleanField()
        #     url_detail = models.URLField(blank=True, null=True)
        #     date_publication = models.DateTimeField(default=timezone.now)
        #     photo = models.ImageField(upload_to="photos/", null=True)
        #
        #     acteurs = models.ManyToManyField("Acteur", related_name="Movie")
        #     realisateurs = models.ManyToManyField("Realisateur", related_name="Movie")
        #     genre = models.ForeignKey('Genre')
        #     type = models.CharField(
        #         max_length=15,
        #         choices=MOVIE_TYPE,
        #         default=LONG_METRAGE,
        #     )
        #
        #     def is_upperclass(self):
        #         return self.type in (self.LONG_METRAGE, self.SERIE)
        #
        #     class Meta:
        #         permissions = (
        #
        #             ("commenter_movie", "Commenter un film"),
        #
        #             ("louer_movie", "Louer des films"),
        #
        #         )
        #         ordering = ['code']
        #
        #     def __str__(self):
        #         return u"{0} [{1}]".format(self.titre, self.date_sortie)
        #
        #
        # # class Photo(models.Model):
        # #     movie = models.ForeignKey(Movie, related_name='photos')
        # #     image = models.ImageField(upload_to="%Y/%m/%d")
        #
        #
        #
        # class Acteur(models.Model):
        #     MONSIEUR = 'MR'
        #     MADAME = 'MME'
        #     GENDER_TYPE = (
        #         (MONSIEUR, 'Monsieur'),
        #         (MADAME, 'Madame'),
        #     )
        #
        #     code_act = models.CharField(max_length=10, unique=True)
        #     nom_act = models.CharField(max_length=50)
        #     prenom_act = models.CharField(max_length=150)
        #     date_naissance_act = models.DateField()
        #     gender_act = models.CharField(
        #         max_length=3,
        #         choices=GENDER_TYPE,
        #         default=MONSIEUR,
        #     )
        #
        #
        #     def is_upperclass(self):
        #         return self.gender_real in (self.MONSIEUR, self.MADAME)
        #
        #     class Meta:
        #         ordering = ['nom_act']
        #
        #     def __str__(self):
        #         return u"{0} [{1}]".format(self.nom_act, self.prenom_act)
        #
        #
        # class Realisateur(models.Model):
        #     MONSIEUR = 'MR'
        #     MADAME = 'MME'
        #     GENDER_TYPE = (
        #         (MONSIEUR, 'Monsieur'),
        #         (MADAME, 'Madame'),
        #     )
        #
        #     code_real = models.CharField(max_length=10, unique=True)
        #     nom_real = models.CharField(max_length=50)
        #     prenom_real = models.CharField(max_length=150)
        #     date_naissance_real = models.DateField()
        #     gender_real = models.CharField(
        #         max_length=3,
        #         choices=GENDER_TYPE,
        #         default=MONSIEUR,
        #     )
        #
        #     def is_upperclass(self):
        #         return self.gender_real in (self.MONSIEUR, self.MADAME)
        #
        #     class Meta:
        #         ordering = ['nom_real']
        #
        #     def __str__(self):
        #         return u"{0} [{1}]".format(self.nom_real, self.prenom_real)
        #
        #
        # class Genre(models.Model):
        #     code_gen = models.CharField(max_length=6, unique=True)
        #     description_gen = models.CharField(max_length=25)
        #
        #
        #     class Meta:
        #         ordering = ['description_gen']
        #
        #     def __str__(self):
        #         return u"{0} [{1}]".format(self.code_gen, self.description_gen)
