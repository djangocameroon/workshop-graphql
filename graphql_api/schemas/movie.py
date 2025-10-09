import graphene
from graphene_django import DjangoObjectType

from ..models import Movie


class MovieType(DjangoObjectType):
    class Meta:
        model = Movie
        fields = "__all__"
