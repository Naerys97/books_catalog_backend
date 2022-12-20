from rest_framework.viewsets import ModelViewSet
from . import models, serializers


class BookViewSet(ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer


class AuthorViewSet(ModelViewSet):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer


class EditorialViewSet(ModelViewSet):
    queryset = models.Editorial.objects.all()
    serializer_class = serializers.EditorialSerializer


class GenreViewSet(ModelViewSet):
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer