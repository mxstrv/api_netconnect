from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Post, Group, Follow, User
from rest_framework.validators import UniqueTogetherValidator


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('author', 'post')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')
        validators = [UniqueTogetherValidator(
            queryset=Follow.objects.all(),
            fields=('user', 'following'),
            message="You can't follow the same person twice")]

    def validate(self, data):
        if self.context['request'].user == data['following']:
            raise serializers.ValidationError("You can't follow yourself")
        return data
