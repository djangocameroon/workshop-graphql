import graphene
from graphene_django import DjangoObjectType

from ..models import Actor


class ActorType(DjangoObjectType):
    class Meta:
        model = Actor
        fields = "__all__"
