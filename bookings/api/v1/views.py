from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

from bookings.models import Booking
from .serializers import BookingSerializer


class BookingView(GenericAPIView):

    @extend_schema(tags=["Bookings"])
    def get(self, request):
        return Response(BookingSerializer(Booking.objects.all(), many=True).data)

    @extend_schema(tags=["Bookings"])
    def post(self, request):
        if request.user.userprofile.role != "Guest":
            return Response({"error": "Only guests can book"}, status=403)

        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(guest=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)