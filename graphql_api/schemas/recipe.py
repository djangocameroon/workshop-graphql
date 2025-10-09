import graphene
from graphene_django import DjangoObjectType

from ..models import Recipe


class RecipeType(DjangoObjectType):
    class Meta:
        model = Recipe
        fields = "__all__"
