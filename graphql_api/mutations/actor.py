import graphene
from ..models import Actor
from ..schemas.actor import ActorType


class CreateActor(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    actor = graphene.Field(ActorType)

    def mutate(self, info, name):
        actor = Actor(name=name)
        actor.save()
        return CreateActor(actor=actor)


class UpdateActor(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()

    actor = graphene.Field(ActorType)

    def mutate(self, info, id, name=None):
        actor = Actor.objects.get(pk=id)
        if name:
            actor.name = name
        actor.save()
        return UpdateActor(actor=actor)


class DeleteActor(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        actor = Actor.objects.get(pk=id)
        actor.delete()
        return DeleteActor(success=True)
