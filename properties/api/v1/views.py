from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

from properties.models import Property
from .serializers import PropertySerializer
from users.api.v1.permissions import IsHost


class PropertyView(GenericAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    @extend_schema(tags=["Properties"])
    def get(self, request):
        return Response(PropertySerializer(Property.objects.all(), many=True).data)

    @extend_schema(tags=["Properties"])
    def post(self, request):
        if request.user.userprofile.role != "Host":
            return Response({"error": "Only hosts can create property"}, status=403)

        serializer = PropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(host=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class PropertyDetailView(GenericAPIView):
    serializer_class = PropertySerializer

    def get_object(self, id):
        return Property.objects.get(id=id)

    @extend_schema(tags=["Properties"])
    def get(self, request, id):
        return Response(PropertySerializer(self.get_object(id)).data)

    @extend_schema(tags=["Properties"])
    def put(self, request, id):
        obj = self.get_object(id)
        serializer = PropertySerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @extend_schema(tags=["Properties"])
    def delete(self, request, id):
        obj = self.get_object(id)
        obj.delete()
        return Response(status=204)