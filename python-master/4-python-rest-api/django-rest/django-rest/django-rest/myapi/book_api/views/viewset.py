from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import Book, Author
from ..serializers import BookSerializer, AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=True)
    def author(self, request, *args, **kwargs):
        book = self.get_object()
        author = Author.objects.get(id=book.author_id)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)
