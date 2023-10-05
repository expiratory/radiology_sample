from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Sample


class SampleViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.sample_data = {
            'title': 'Test Title',
            'text': 'Test Text',
            'modality': 'RG',
            'region_of_interest': 'HEAD',
            'specialization': 'TRAUMA'
        }
        self.sample = Sample.objects.create(**self.sample_data)

    def test_get_all_samples(self):
        response = self.client.get('/api/v1/sample/get_all_samples/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.context['samples']), 1)

    def test_add_sample(self):
        new_sample_data = {
            'title': 'New Test Title',
            'text': 'New Test Text',
            'modality': 'CT',
            'region_of_interest': 'NECK',
            'specialization': 'PHYSICIAN'
        }
        response = self.client.post('/api/v1/sample/add_sample/', new_sample_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Sample.objects.count(), 2)

    def test_get_defined_sample(self):
        response = self.client.get('/api/v1/sample/1/get_defined_sample/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.context['defined_sample']['title'], self.sample_data['title'])

    def test_filters(self):
        Sample.objects.create(title='Another Title', text='Another Text', modality='MRI', region_of_interest='THORAX',
                              specialization='NEUROLOGY')

        response = self.client.get('/api/v1/sample/get_all_samples/', {'title_search': 'Another Title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.context['samples']), 1)

        response = self.client.get('/api/v1/sample/get_all_samples/', {'modality_filter': 'MRI'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.context['samples']), 1)

        response = self.client.get('/api/v1/sample/get_all_samples/', {'region_of_interest_filter': 'THORAX'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.context['samples']), 1)

        response = self.client.get('/api/v1/sample/get_all_samples/', {'specialization_filter': 'NEUROLOGY'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.context['samples']), 1)
