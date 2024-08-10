from django.urls import path
from graphene_django.views import GraphQLView

from graphql_api.resolvers.graphql_resolver import graphql_schema


urlpatterns = [
    path(
        "graphql",
        GraphQLView.as_view(graphiql=True, schema=graphql_schema),
    ),
]
