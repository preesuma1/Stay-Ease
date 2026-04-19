from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

from users.models import UserProfile
from .serializers import UserProfileSerializer


class UserProfileView(GenericAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    @extend_schema(tags=["Users"])
    def get(self, request):
        qs = UserProfile.objects.all()
        return Response(UserProfileSerializer(qs, many=True).data)

    @extend_schema(tags=["Users"])
    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class UserProfileDetailView(GenericAPIView):
    serializer_class = UserProfileSerializer

    def get_object(self, id):
        return UserProfile.objects.get(id=id)

    @extend_schema(tags=["Users"])
    def get(self, request, id):
        obj = self.get_object(id)
        return Response(UserProfileSerializer(obj).data)

    @extend_schema(tags=["Users"])
    def put(self, request, id):
        obj = self.get_object(id)
        serializer = UserProfileSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @extend_schema(tags=["Users"])
    def delete(self, request, id):
        obj = self.get_object(id)
        obj.delete()
        return Response(status=204)