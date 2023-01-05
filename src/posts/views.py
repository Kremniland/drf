from rest_framework import viewsets


from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    '''permisions остаются из settings: AllowAny'''
    queryset = Post.objects.all()
    serializer_class = PostSerializer

