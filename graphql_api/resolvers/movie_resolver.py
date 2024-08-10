import graphene

from graphql_api.models import Movie
from graphql_api.schemas.movie import MovieSchema, MovieSchemaInput


class CreateMovieMutation(graphene.Mutation):
    movie = graphene.Field(MovieSchema)

    class Arguments:
        movie_in = MovieSchemaInput(required=True)

    def mutate(self, info, movie_in: MovieSchemaInput):
        created_movie = Movie.objects.create(
            title=movie_in.title,
            release_date=movie_in.release_date,
            duration=movie_in.duration,
            kind=movie_in.kind,
        )
        return CreateMovieMutation(movie=created_movie)
