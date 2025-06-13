from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from posts.models import Post, Comment, Group

from .serializers import PostSerializer, CommentSerializer, GroupSerializer
from .permissions import IsOwnerOrReadOnlyPermission
from .mixins import PostFromURLMixin


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnlyPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]


class CommentViewSet(PostFromURLMixin, viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnlyPermission]

    def get_queryset(self):
        return Comment.objects.filter(post=self.get_post())

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())
