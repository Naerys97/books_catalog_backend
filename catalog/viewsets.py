import json

from django.db import transaction
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers


class BookViewSet(ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    parser_classes = (MultiPartParser, FormParser)
    #
    # data = {'title': 'Daddy Long Legs',
    #         'amount': 2, 'description': 'Papaito',
    #         'language': 'English', 'details': 'Shiny New',
    #         'quality': 'good', 'genres': [16],
    #         'authors': [{'name': 'Jean Webster'}]}

    # < QueryDict: {'csrfmiddlewaretoken': ['oyP6T2iFfpg5OL25r52rnkr0Itcvb8dTnafO8OgL3r53NGsjfHed7OABQucEIrhx'],
    #               'title': ['Hello World'], 'amount': ['3'], 'description': ["Judy's letters to Jervis"],
    #               'quality': ['good'], 'details': ['Brand new'], 'language': ['English'],
    #               'cover': [ < InMemoryUploadedFile: Annotation
    # 2022 - 11 - 18
    # 081126.
    # png(image / png) >]} >

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        # print(request.data)
        # breakpoint()
        data = request.data
        # json.loads(data.pop('authors')[0])
        newAuthors = [{'name': author} for author in data['authors'] if type(author) is str]
        existingAuthors = [author for author in data['authors'] if type(author) is int]
        genres = request.data['genres']
        editorial = request.data['editorial']
        data['authors'] = newAuthors
        serialized_book = self.get_serializer(data=data)
        if serialized_book.is_valid():
            serialized_book.save(existingAuthors=existingAuthors, genres=genres, editorial=editorial)
            return Response(data=serialized_book.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serialized_book.errors, status=status.HTTP_400_BAD_REQUEST)

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        data = request.data
        instance = self.get_object()
        newAuthors = [{'name': author} for author in data['authors'] if type(author) is str]
        existingAuthors = [author for author in data['authors'] if type(author) is int]
        genres = request.data['genres']
        editorial = request.data['editorial']
        data['authors'] = newAuthors
        serialized_book = self.get_serializer(instance=instance, data=data)
        if serialized_book.is_valid():
            serialized_book.save(existingAuthors=existingAuthors, genres=genres, editorial=editorial)
            return Response(data=serialized_book.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serialized_book.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorViewSet(ModelViewSet):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer


class EditorialViewSet(ModelViewSet):
    queryset = models.Editorial.objects.all()
    serializer_class = serializers.EditorialSerializer


class GenreViewSet(ModelViewSet):
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer
