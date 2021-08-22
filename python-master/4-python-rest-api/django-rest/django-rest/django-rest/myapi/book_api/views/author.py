
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import *
from rest_framework.authentication \
    import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings

from ..models import Author
from ..serializers import AuthorSerializer


class AuthorAPIView(APIView):
    authentication_classes = \
        api_settings.DEFAULT_AUTHENTICATION_CLASSES
    permission_classes = [IsAuthenticated]

    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class AuthorDetailAPIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return Author.objects.get(id=id)
        except Author.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

    def get(self, request, id):
        author = self.get_object(id)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def put(self, request, id):
        author = self.get_object(id)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        author = self.get_object(id)
        author.delete()
        return Response(status=HTTP_204_NO_CONTENT)
