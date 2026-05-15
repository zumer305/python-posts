from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Post


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):

    post = Post.objects.create(
        title=request.data['title'],
        content=request.data['content'],
        author=request.user
    )

    return Response({"message": "Post created"})


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_post(request, pk):

    post = Post.objects.get(id=pk)

    if post.author != request.user:
        return Response({"error": "You are not allowed to edit this post"})

    post.title = request.data['title']
    post.content = request.data['content']
    post.save()

    return Response({"message": "Post updated"})