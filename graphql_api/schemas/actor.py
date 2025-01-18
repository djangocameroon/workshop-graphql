import graphene
from graphene_django import DjangoObjectType

from graphql_api.models import Actor


class ActorSchema(DjangoObjectType):
    class Meta:
        model = Actor
        fields = "__all__"


class CreateActorInputSchema(graphene.InputObjectType):
    first_name = graphene.String(required=True)
    last_name = graphene.String(required=True)
    birth_date = graphene.Date(required=True)


class UpdateActorInputSchema(graphene.InputObjectType):
    first_name = graphene.String(required=False)
    last_name = graphene.String(required=False)
