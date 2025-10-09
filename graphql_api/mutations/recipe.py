import graphene
from ..models import Recipe, Chief
from ..schemas.recipe import RecipeType


class CreateRecipe(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        chief_id = graphene.ID(required=True)

    recipe = graphene.Field(RecipeType)

    def mutate(self, info, title, description, chief_id):
        chief = Chief.objects.get(pk=chief_id)
        recipe = Recipe(title=title, description=description, chief=chief)
        recipe.save()
        return CreateRecipe(recipe=recipe)


class UpdateRecipe(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()
        description = graphene.String()
        chief_id = graphene.ID()

    recipe = graphene.Field(RecipeType)

    def mutate(self, info, id, title=None, description=None, chief_id=None):
        recipe = Recipe.objects.get(pk=id)
        if title:
            recipe.title = title
        if description:
            recipe.description = description
        if chief_id:
            chief = Chief.objects.get(pk=chief_id)
            recipe.chief = chief
        recipe.save()
        return UpdateRecipe(recipe=recipe)


class DeleteRecipe(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        recipe = Recipe.objects.get(pk=id)
        recipe.delete()
        return DeleteRecipe(success=True)
