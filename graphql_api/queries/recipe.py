import graphene
from ..models import Recipe
from ..schemas.recipe import RecipeType


class RecipeQuery(graphene.ObjectType):
    recipes = graphene.List(RecipeType)
    recipe = graphene.Field(RecipeType, id=graphene.Int())

    def resolve_recipes(self, info):
        return Recipe.objects.all()

    def resolve_recipe(self, info, id):
        return Recipe.objects.get(pk=id)
