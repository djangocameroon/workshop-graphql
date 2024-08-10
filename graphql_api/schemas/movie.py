import graphene
from graphene_django import DjangoObjectType

from graphql_api.models import Movie


class MovieSchema(DjangoObjectType):
    class Meta:
        model = Movie
        fields = "__all__"


class MovieSchemaInput(graphene.InputObjectType):
    title = graphene.String()
    release_date = graphene.Date()
    duration = graphene.Int()
    kind = graphene.String()
