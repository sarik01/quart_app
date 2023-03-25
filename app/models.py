from tortoise.models import Model
from tortoise import fields

class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=255, unique=True, null=False)
    email = fields.CharField(max_length=255, unique=True, null=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    posts: fields.ReverseRelation["Post"]

    def format(self):
        return {
            'posts': self.posts,
            'username': self.username,
            'created_at': self.created_at
        }

class Post(Model):
    name = fields.CharField(max_length=255, unique=True, null=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    user_id = fields.ForeignKeyField(
        "models.User", related_name="posts", null=True
    )

    def format(self):
        return {
            'name': self.name,
            'created_at': self.created_at,
            'user_id': self.user_id
        }