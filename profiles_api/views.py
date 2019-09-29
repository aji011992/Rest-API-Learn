from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """returns a list of API View features"""
        an_apiview = [
            'uses HTTP method function (get, post, patch, put, delete)',
            'Is similar to a traidtional Django Views',
            'Gives you the most control over your application',
        ]

        return Response({'message': 'Hello!', 'an_apiview':an_apiview})
