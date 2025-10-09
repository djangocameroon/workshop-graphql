import graphene
from ..models import Movie
from ..schemas.movie import MovieType


class CreateMovie(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)

    movie = graphene.Field(MovieType)

    def mutate(self, info, title, description):
        movie = Movie(title=title, description=description)
        movie.save()
        return CreateMovie(movie=movie)


class UpdateMovie(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()
        description = graphene.String()

    movie = graphene.Field(MovieType)

    def mutate(self, info, id, title=None, description=None):
        movie = Movie.objects.get(pk=id)
        if title:
            movie.title = title
        if description:
            movie.description = description
        movie.save()
        return UpdateMovie(movie=movie)


class DeleteMovie(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        movie = Movie.objects.get(pk=id)
        movie.delete()
        return DeleteMovie(success=True)
