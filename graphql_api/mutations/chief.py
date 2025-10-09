import graphene
from ..models import Chief
from ..schemas.chief import ChiefType


class CreateChief(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    chief = graphene.Field(ChiefType)

    def mutate(self, info, name):
        chief = Chief(name=name)
        chief.save()
        return CreateChief(chief=chief)


class UpdateChief(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()

    chief = graphene.Field(ChiefType)

    def mutate(self, info, id, name=None):
        chief = Chief.objects.get(pk=id)
        if name:
            chief.name = name
        chief.save()
        return UpdateChief(chief=chief)


class DeleteChief(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        chief = Chief.objects.get(pk=id)
        chief.delete()
        return DeleteChief(success=True)
