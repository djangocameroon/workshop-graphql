import graphene
from ..models import Movie
from ..schemas.movie import MovieType


class MovieQuery(graphene.ObjectType):
    movies = graphene.List(MovieType)
    movie = graphene.Field(MovieType, id=graphene.Int())

    def resolve_movies(self, info):
        return Movie.objects.all()

    def resolve_movie(self, info, id):
        return Movie.objects.get(pk=id)
