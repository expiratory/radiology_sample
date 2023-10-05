from rest_framework.decorators import action
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .serializers import SampleSerializer
from .models import Sample
from django.shortcuts import render
from .forms import SampleForm


class SampleViewSet(GenericViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer

    @action(methods=['get'], detail=False)
    def get_all_samples(self, request):
        samples = Sample.objects.all().values()
        context = {
            'samples': samples,
            'MODALITY_CHOICES': Sample.MODALITY_CHOICES,
            'REGION_OF_INTEREST_CHOICES': Sample.REGION_OF_INTEREST_CHOICES,
            'SPECIALIZATION_CHOICES': Sample.SPECIALIZATION_CHOICES,
        }
        return render(request, 'sample/get_all_samples.html', context)

    @action(methods=['get'], detail=True)
    def get_defined_sample(self, request, pk):
        defined_sample = Sample.objects.get(pk=pk)
        return render(request, 'sample/get_defined_sample.html',
                      {'defined_sample': SampleSerializer(defined_sample).data})

    @action(detail=False, methods=['get', 'post'], renderer_classes=[TemplateHTMLRenderer])
    def add_sample(self, request):
        if request.method == 'POST':
            form = SampleForm(request.POST)
            if form.is_valid():
                form.save()
                return Response({"message": "Описание успешно добавлено!"},
                                template_name='rest_framework/success_template.html')
        else:
            form = SampleForm()

        return Response({'form': form}, template_name='rest_framework/sample_form.html')
