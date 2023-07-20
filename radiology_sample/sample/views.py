from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .serializers import SampleSerializer
from .models import Sample
from django.shortcuts import render


class SampleViewSet(GenericViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer

    @action(methods=['get'], detail=False)
    def get_all_samples(self, request):
        samples = Sample.objects.all().values()
        return render(request, 'sample/get_all_samples.html', {'samples': samples})

    @action(methods=['get'], detail=True)
    def get_defined_sample(self, request, pk):
        try:
            defined_sample = Sample.objects.get(pk=pk)
            return render(request, 'sample/get_defined_sample.html',
                          {'defined_sample': SampleSerializer(defined_sample).data})
        except Exception as e:
            return render(request, 'sample/error.html', {'message': 'fail', 'description': str(e)})

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
            return render(request, 'sample/add_sample.html', {'sample': SampleSerializer(sample).data})
        except Exception as e:
            return render(request, 'sample/error.html', {'message': 'fail', 'description': str(e)})
