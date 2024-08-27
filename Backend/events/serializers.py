from rest_framework.fields import CharField,ListField
from rest_framework.serializers import ModelSerializer
from .models import Event

class EventSerializer(ModelSerializer):
    attendee = ListField(child=CharField(required=False), required=False)

    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'start_at', 'end_at', 'location', 'attendee',)
        extra_kwargs = {'attendees': {'required': False, "allow_null": True}}