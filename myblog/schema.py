from graphene_django import DjangoObjectType
from . import models
import graphene

class PostType(DjangoObjectType):
    class Meta:
        model = models.Post

class CommentType(DjangoObjectType):
    class Meta:
        model = models.Comment

class Query (graphene.ObjectType):
    all_posts = graphene.List(PostType)
    post_by_slug = graphene.Field(PostType, slug= graphene.String())
    
    def resolve_all_posts (root,info):
        return (
            models.Post.objects.all().filter(status='published')
        )

    def resolve_post_by_slug(root,info,slug):
        return (
            models.Post.objects.get(slug=slug)
        )

schema = graphene.Schema(query=Query)