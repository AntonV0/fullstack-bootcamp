"""Views for the vendorEventRegister app."""

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from vendorEventRegister.models import Events
from vendorEventRegister.serializers import EventSerializer

class EventListShowCreate(APIView):
    """View to list all events and create a new event."""
    def get(self, request):
        """Get all events."""
        events = Events.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Create a new event."""
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SingleEventAccess(APIView):
    """View to access a single event."""
    def get_object(self, id):
        """Helper method to get the event object by id."""
        try:
            return Events.objects.get(id=id)
        except Events.DoesNotExist:
            return None

    def get(self, request, id):
        """Get a single event by id."""
        event = self.get_object(id)
        if event is None:
            return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = EventSerializer(event)
        return Response(serializer.data)

    def put(self, request, id):
        """Update a single event by id."""
        event = self.get_object(id)
        if event is None:
            return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        """Delete a single event by id."""
        event = self.get_object(id)
        if event is None:
            return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)

        event.delete()
        return Response({"message": "Event deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
