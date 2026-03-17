"""Serializers for the vendorEventRegister app."""

from rest_framework import serializers
from vendorEventRegister.models import Events

class EventSerializer(serializers.ModelSerializer):
    """Serializer for the Events model."""
    class Meta:
        """Meta class for the EventSerializer."""
        model = Events
        fields = '__all__'
# Meta class will tell the serializer which model to use and which fields to include.
# In this case, we are including all fields from the Events model.

# A serializer in Django REST Framework is a way to convert complex data types, such
# as Django models, into native Python datatypes that can then be easily rendered into
# JSON, XML, or other content types. It also provides deserialization, allowing parsed
#  data to be converted back into complex types after being validated.
