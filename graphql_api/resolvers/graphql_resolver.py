import graphene

from graphql_api.resolvers.movie_resolver import (
    CreateMovieMutation, 
    MovieQuery,
)


class GraphQLQuery(MovieQuery):
    me = graphene.String()

    def resolve_me(self, info):
        return "Hello, World!"


class GraphQLMutation(graphene.ObjectType):
    create_movie = CreateMovieMutation.Field()


graphql_schema = graphene.Schema(query=GraphQLQuery, mutation=GraphQLMutation)
