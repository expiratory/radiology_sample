from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .serializers import SampleSerializer
from .models import Sample


class SampleViewSet(GenericViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer

    @action(methods=['get'], detail=False)
    def get_all_samples(self, request):
        samples = Sample.objects.all().values()
        return Response({'samples': samples})

    @action(methods=['get'], detail=True)
    def get_defined_sample(self, pk, request):
        try:
            defined_sample = Sample.objects.get(pk=pk)
            return Response({'defined_sample': SampleSerializer(defined_sample).data})
        except Sample.DoesNotExist as e:
            return Response({'message': 'fail', 'description': str(e)})

    @action(methods=['post'], detail=False)
    def add_sample(self, request):
        try:
            data = request.POST
            sample = Sample.objects.create(
                title=data['title'],
                text=data['text'],
                modality=data['modality'],
                region_of_interest=data['region_of_interest'],
                specialization=data['specialization'],
            )
            return Response({'sample': SampleSerializer(sample).data})
        except KeyError as e:
            return Response({'message': 'fail', 'description': str(e)})
        except ValueError as e:
            return Response({'message': 'fail', 'description': str(e)})
        except TypeError as e:
            return Response({'message': 'fail', 'description': str(e)})
        except Exception as e:
            return Response({'message': 'fail', 'description': str(e)})
