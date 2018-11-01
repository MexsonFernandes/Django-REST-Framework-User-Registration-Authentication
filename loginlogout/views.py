from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from .models import Users
from .serializers import UserSerializer, UserLoginSerializer


class Record(generics.ListCreateAPIView):
    # get method handler
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class Login(generics.GenericAPIView):
    # get method handler
    queryset = Users.objects.all()
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer_class = UserLoginSerializer(data=data)
        if serializer_class.is_valid(raise_exception=True):
            new_data = serializer_class.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)