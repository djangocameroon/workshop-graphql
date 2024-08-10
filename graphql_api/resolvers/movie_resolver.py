import graphene
from graphql import GraphQLError

from graphql_api.models import Movie
from graphql_api.schemas.movie import MovieSchema, MovieSchemaInput


class MovieQuery(graphene.ObjectType):
    movies = graphene.List(MovieSchema)
    
    get_movie = graphene.Field(
        MovieSchema, 
        movie_uuid=graphene.String(required=True)
    )

    def resolve_movies(self, info):
        return Movie.objects.all()
    
    def resolve_get_movie(self, info, movie_uuid: str):
        try:
            existing_movie = Movie.objects.get(
                uuid=movie_uuid
            )
        except:
            raise GraphQLError("Movie not found")
        return existing_movie


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
