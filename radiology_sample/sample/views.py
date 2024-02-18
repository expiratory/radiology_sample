from rest_framework.decorators import action
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .serializers import SampleSerializer
from .models import Sample
from django.shortcuts import render
from .forms import SampleForm
from django_filters import rest_framework as filters
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated


class SampleFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    modality = filters.ChoiceFilter(choices=Sample.MODALITY_CHOICES)
    region_of_interest = filters.ChoiceFilter(choices=Sample.REGION_OF_INTEREST_CHOICES)
    specialization = filters.ChoiceFilter(choices=Sample.SPECIALIZATION_CHOICES)

    class Meta:
        model = Sample
        fields = ['title', 'modality', 'region_of_interest', 'specialization']


class SampleViewSet(mixins.ListModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SampleFilter
    search_fields = ('title',)

    @action(methods=['get'], detail=False)
    def get_all_samples(self, request):
        queryset = Sample.objects.all()
        title_search = request.GET.get('title_search', None)
        if title_search:
            title_search = title_search.lower()
        modality_filter = request.GET.get('modality_filter', None)
        region_of_interest_filter = request.GET.get('region_of_interest_filter', None)
        specialization_filter = request.GET.get('specialization_filter', None)
        if title_search:
            queryset = queryset.filter(title__icontains=title_search)
        if modality_filter:
            queryset = queryset.filter(modality=modality_filter)
        if region_of_interest_filter:
            queryset = queryset.filter(region_of_interest=region_of_interest_filter)
        if specialization_filter:
            queryset = queryset.filter(specialization=specialization_filter)
        ordering = request.GET.get('ordering', '')
        if ordering:
            queryset = queryset.order_by(ordering)
        samples = queryset.values()
        context = {
            'samples': samples,
            'MODALITY_CHOICES': Sample.MODALITY_CHOICES,
            'REGION_OF_INTEREST_CHOICES': Sample.REGION_OF_INTEREST_CHOICES,
            'SPECIALIZATION_CHOICES': Sample.SPECIALIZATION_CHOICES,
            'ordering': ordering,
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
