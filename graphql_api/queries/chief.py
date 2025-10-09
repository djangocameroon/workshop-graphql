import graphene
from ..models import Chief
from ..schemas.chief import ChiefType


class ChiefQuery(graphene.ObjectType):
    chiefs = graphene.List(ChiefType)
    chief = graphene.Field(ChiefType, id=graphene.Int())

    def resolve_chiefs(self, info):
        return Chief.objects.all()

    def resolve_chief(self, info, id):
        return Chief.objects.get(pk=id)
