import graphene

from graphql_api.resolvers.actor_resolver import (
    ActorQuery,
    CreateActorMutation,
    UpdateActorMutation,
)


class GraphQLQuery(ActorQuery):
    pass


class GraphQLMutation(graphene.ObjectType):
    create_actor = CreateActorMutation.Field()
    update_actor = UpdateActorMutation.Field()


graphql_schema = graphene.Schema(
    query=GraphQLQuery, mutation=GraphQLMutation
)
