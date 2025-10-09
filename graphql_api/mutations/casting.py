import graphene
from ..models import Casting, Movie, Actor
from ..schemas.casting import CastingType


class CreateCasting(graphene.Mutation):
    class Arguments:
        movie_id = graphene.ID(required=True)
        actor_id = graphene.ID(required=True)
        role = graphene.String(required=True)

    casting = graphene.Field(CastingType)

    def mutate(self, info, movie_id, actor_id, role):
        movie = Movie.objects.get(pk=movie_id)
        actor = Actor.objects.get(pk=actor_id)
        casting = Casting(movie=movie, actor=actor, role=role)
        casting.save()
        return CreateCasting(casting=casting)


class DeleteCasting(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        casting = Casting.objects.get(pk=id)
        casting.delete()
        return DeleteCasting(success=True)
