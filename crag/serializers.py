from rest_framework import serializers

from .models.climb import Climb
from .models.comment import Comment

class ClimbSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Climb

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Comment

class CommentReadSerializer(CommentSerializer):
    climb = ClimbSerializer(source='climb_id')
    class Meta:
        model = Comment
        fields = ('climb', 'id')