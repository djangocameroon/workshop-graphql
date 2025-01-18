from datetime import datetime

import graphene
from graphql import GraphQLError

from graphql_api.models import Actor
from graphql_api.schemas.actor import ActorSchema, CreateActorInputSchema, UpdateActorInputSchema


class ActorQuery(graphene.ObjectType):
    list_actors = graphene.List(
        ActorSchema,
        description="List all actors",
    )
    
    get_actor = graphene.Field(
        ActorSchema,
        actor_uuid=graphene.String(),
        description="Get actor by uuid",
    )
    
    def resolve_list_actors(self, info):
        all_actors = Actor.objects.all()
        return all_actors

    def resolve_get_actor(self, info, actor_uuid: str):
        try:
            actor = Actor.objects.get(uuid=actor_uuid)
        except:
            raise GraphQLError("Actor not found !")
        
        return actor


class CreateActorMutation(graphene.Mutation):
    
    actor = graphene.Field(ActorSchema)
    
    class Arguments:
        create_actor_in = CreateActorInputSchema(required=True)
    
    def mutate(self, info, create_actor_in: CreateActorInputSchema):
        if Actor.objects.filter(
            first_name=create_actor_in.first_name, last_name=create_actor_in.last_name
        ).exists():
            raise GraphQLError("Actor already exists !")
        
        created_actor = Actor.objects.create(
            first_name=create_actor_in.first_name,
            last_name=create_actor_in.last_name,
            birth_date=create_actor_in.birth_date,
        )
        return CreateActorMutation(actor=created_actor)


class UpdateActorMutation(graphene.Mutation):
    
    message = graphene.String()
    
    class Arguments:
        actor_uuid = graphene.String(required=True)
        update_actor_in = UpdateActorInputSchema(required=True)
    
    def mutate(self, info, actor_uuid: str, update_actor_in: UpdateActorInputSchema):
        try:
            existing_actor = Actor.objects.get(uuid=actor_uuid)
        except:
            raise GraphQLError("Actor not found !")
        
        if not update_actor_in.first_name and not update_actor_in.last_name:
            raise GraphQLError("At least one field must be provided !")
        
        updated = False
        if update_actor_in.first_name:
            existing_actor.first_name = update_actor_in.first_name
            updated = True
        
        if update_actor_in.last_name:
            existing_actor.last_name = update_actor_in.last_name
            updated = True
        
        if updated:
            existing_actor.save()
        
        return UpdateActorMutation(message=f"Actor {existing_actor.uuid} updated successfully !")
