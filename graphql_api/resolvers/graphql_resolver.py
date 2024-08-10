import graphene


class GraphQLQuery(graphene.ObjectType):
    pass



class GraphQLMutation(graphene.ObjectType):
    pass


graphql_schema = graphene.Schema(
    query=GraphQLQuery, mutation=GraphQLMutation
)
