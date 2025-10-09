import graphene

from .queries.movie import MovieQuery
from .queries.actor import ActorQuery
from .queries.casting import CastingQuery
from .queries.chief import ChiefQuery
from .queries.recipe import RecipeQuery

from .mutations.movie import CreateMovie, UpdateMovie, DeleteMovie
from .mutations.actor import CreateActor, UpdateActor, DeleteActor
from .mutations.casting import CreateCasting, DeleteCasting
from .mutations.chief import CreateChief, UpdateChief, DeleteChief
from .mutations.recipe import CreateRecipe, UpdateRecipe, DeleteRecipe


class Query(MovieQuery, ActorQuery, CastingQuery, ChiefQuery, RecipeQuery, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    create_movie = CreateMovie.Field()
    update_movie = UpdateMovie.Field()
    delete_movie = DeleteMovie.Field()

    create_actor = CreateActor.Field()
    update_actor = UpdateActor.Field()
    delete_actor = DeleteActor.Field()

    create_casting = CreateCasting.Field()
    delete_casting = DeleteCasting.Field()

    create_chief = CreateChief.Field()
    update_chief = UpdateChief.Field()
    delete_chief = DeleteChief.Field()

    create_recipe = CreateRecipe.Field()
    update_recipe = UpdateRecipe.Field()
    delete_recipe = DeleteRecipe.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
