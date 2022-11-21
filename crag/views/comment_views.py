from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ..models.comment import Comment
from ..serializers import CommentSerializer, CommentReadSerializer

class Comments(APIView):
    def get(self, request):
        """Index request"""
        comments = Comment.objects.all()[:10]
        data = CommentReadSerializer(comments, many=True).data
        return Response(data)

    def post(self, request):
        """Post request"""
        comment = CommentSerializer(data=request.data['comment'])
        if comment.is_valid():
            saved_apt = comment.save()
            return Response(comment.data, status=status.HTTP_201_CREATED)
        else:
            return Response(comment.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetail(APIView):
    def get(self, request, pk):
        """Show Request"""
        comment = get_object_or_404(Comment, pk=pk)
        data = CommentReadSerializer(comment).data
        return Response(data)

    def patch(self, request, pk):
        """Update request"""
        comment = get_object_or_404(Comment, pk=pk)
        updated_apt = CommentSerializer(comment, data=request.data['comment'])
        if updated_apt.is_valid():
            updated_apt.save()
            data = updated_apt.data
            # OR: Find the object we just created & serialize it to return book & borrower objects
            # got_apt = get_object_or_404(Comment, pk=updated_apt.data['id'])
            # data = CommentReadSerializer(get_apt).data
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(comment.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete Request"""
        comment = get_object_or_404(Comment, pk=pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)