from rest_framework.viewsets import ModelViewSet
from post.models import Post
from post.api.serializers import PostSerializers

class PostApiViewSet(ModelViewSet):
    serializer__class = PostSerializer
    queryset = Post.objects.all()