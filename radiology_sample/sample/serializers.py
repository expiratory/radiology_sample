from rest_framework import serializers
from .models import Sample


class SampleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sample
        fields = ('title', 'text', 'datetime_of_creation', 'datetime_of_change',
                  'modality', 'region_of_interest', 'specialization', 'image',
                  'additional_image')
