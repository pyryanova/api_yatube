from django.shortcuts import get_object_or_404

from posts.models import Post


class PostFromURLMixin:
    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))
