from django.contrib import admin
from .models import Sample, RegionOfInterest, Specialization


@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    pass


@admin.register(RegionOfInterest)
class RegionOfInterestAdmin(admin.ModelAdmin):
    pass


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    pass
