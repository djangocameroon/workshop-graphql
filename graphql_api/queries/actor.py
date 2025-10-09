import graphene
from ..models import Actor
from ..schemas.actor import ActorType


class ActorQuery(graphene.ObjectType):
    actors = graphene.List(ActorType)
    actor = graphene.Field(ActorType, id=graphene.Int())

    def resolve_actors(self, info):
        return Actor.objects.all()

    def resolve_actor(self, info, id):
        return Actor.objects.get(pk=id)
