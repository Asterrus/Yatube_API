from posts.models import Comment, Group, Post
from rest_framework.filters import SearchFilter
from rest_framework.mixins import (CreateModelMixin, ListModelMixin,
                                   RetrieveModelMixin)
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import (GenericViewSet, ModelViewSet,
                                     ReadOnlyModelViewSet)

from .permissions import IsAuthorOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class GroupViewSet(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all().select_related('author').only(
        'id', 'text', 'pub_date', 'image', 'group', 'author__username')
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination
    page_size = 10

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_id'])

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user, post_id=self.kwargs['post_id'])


class FollowViewSet(CreateModelMixin, ListModelMixin,
                    RetrieveModelMixin, GenericViewSet):
    serializer_class = FollowSerializer
    filter_backends = [SearchFilter, ]
    search_fields = ['user__username', 'following__username']

    def get_queryset(self):
        return self.request.user.followings.all().select_related(
            'following').only('id', 'user__username', 'following__username')
