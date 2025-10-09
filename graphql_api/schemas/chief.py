import graphene
from graphene_django import DjangoObjectType

from ..models import Chief


class ChiefType(DjangoObjectType):
    class Meta:
        model = Chief
        fields = "__all__"
