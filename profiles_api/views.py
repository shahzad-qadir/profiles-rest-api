from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import HelloSerializer


class HelloApiView(APIView):

    serializer_class = HelloSerializer

    def get(self, request):
        features = [
            'REST Framework is good',
            'It can help you create APIs',
            'Lovely, as it sounds.'
        ]
        return Response({'message': 'Hello', 'features': features})

    def post(self, request):
        """Create a hello message with name provided"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello, {name}"
            return Response({'message': message})

        return Response(
            serializer.errors,
            status.HTTP_400_BAD_REQUEST
        )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request):
        """Delete an object"""
        return Response({'method': 'DELETE'})
