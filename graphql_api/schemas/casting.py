import graphene
from graphene_django import DjangoObjectType

from ..models import Casting


class CastingType(DjangoObjectType):
    class Meta:
        model = Casting
        fields = "__all__"
