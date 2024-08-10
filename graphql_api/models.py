from django.db import models

from graphql_api.utils.commons import generate_uuid


class Movie(models.Model):
    uuid = models.CharField(max_length=100, primary_key=True, default=generate_uuid)
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    duration = models.IntegerField()
    kind = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Actor(models.Model):
    uuid = models.CharField(max_length=100, primary_key=True, default=generate_uuid)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Casting(models.Model):
    uuid = models.CharField(max_length=100, primary_key=True, default=generate_uuid)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# ============================================================================================


class Chief(models.Model):
    uuid = models.CharField(max_length=100, primary_key=True, default=generate_uuid)
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Recipe(models.Model):
    uuid = models.CharField(max_length=100, primary_key=True, default=generate_uuid)
    title = models.CharField(max_length=100)
    chief = models.ForeignKey(Chief, on_delete=models.CASCADE)
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
