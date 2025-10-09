import graphene
from ..models import Casting
from ..schemas.casting import CastingType


class CastingQuery(graphene.ObjectType):
    castings = graphene.List(CastingType)
    casting = graphene.Field(CastingType, id=graphene.Int())

    def resolve_castings(self, info):
        return Casting.objects.all()

    def resolve_casting(self, info, id):
        return Casting.objects.get(pk=id)
