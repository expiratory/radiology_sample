from django.db import models


class Sample(models.Model):
    MODALITY_CHOICES = (
        ("RG", "Rg"),
        ("CT", "CT"),
        ("MRI", "MRI"),
    )

    title = models.CharField(max_length=256, verbose_name='Заголовок описания',
                             blank=False, null=False)
    text = models.TextField(verbose_name='Текст описания', blank=False, null=False)
    datetime_of_creation = models.DateTimeField(auto_now_add=True)
    datetime_of_change = models.DateTimeField(auto_now=True)
    modality = models.CharField(max_length=3, choices=MODALITY_CHOICES,
                                default="", blank=False, null=False)
    region_of_interest = models.ForeignKey('RegionOfInterest', on_delete=models.DO_NOTHING)
    specialization = models.ForeignKey('Specialization', on_delete=models.DO_NOTHING)


class RegionOfInterest(models.Model):
    title = models.CharField(verbose_name='Название зоны исследования', max_length=50, blank=False, null=False)
    icon = models.FileField(verbose_name='Иконка зоны исследования', null=False, upload_to='region_of_interest')


class Specialization(models.Model):
    title = models.CharField(verbose_name='Название специализации', max_length=50, blank=False, null=False)

