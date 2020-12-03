from django.contrib import admin
from django.utils.safestring import mark_safe
from django.urls import reverse
from material.admin.sites import site
from material.admin.decorators import register

from .models import Grain
from .models import CategoryGrain
from .models import TypeGrain
from .models import SampleGrain
from .models import SampleDetailGrain
from .models import AnalysisGrain
from .models import PercentageTypeGrain

class PercentageTypeGrainInline(admin.TabularInline):
    model = PercentageTypeGrain
    extra = 0

class AnalysisGrainInline(admin.TabularInline):
    model = AnalysisGrain
    extra = 0

class TypeGrainInline(admin.TabularInline):
    model = TypeGrain
    extra = 0

class SampleDetailGrainInline(admin.TabularInline):
    model = SampleDetailGrain
    extra = 0



@register(SampleGrain)
class SampleGrainAdmin(admin.ModelAdmin):
    icon_name = 'track_changes'
    inlines = [AnalysisGrainInline, SampleDetailGrainInline, ]
    list_display = ('name_sample', 'analysis_pdf', )
    # fields = []                    
    # readonly_fields = ()                              
    # search_fields = []

    def analysis_pdf(self, obj):
        return mark_safe('<a href="{}">PDF</a>'.format(
            reverse('grain:admin_sample_pdf', args=[obj.id])
        ))

@register(SampleDetailGrain)
class SampleDetailGrainAdmin(admin.ModelAdmin):
    icon_name = 'bubble_chart'

    list_display = ('name_seed', 'sample', )
    readonly_fields = ('grain_image',)

    def grain_image(self, obj):
        return mark_safe(
            '<img class="responsive-img" src="{url}" width="{width}" height={height} />'.format(
                url = obj.image_result.url,
                width = obj.image_result.width,
                height = obj.image_result.height,
            )
        )

@register(Grain)
class GrainAdmin(admin.ModelAdmin):
    icon_name='grain'
    inlines = [TypeGrainInline, ]

@register(CategoryGrain)
class CategoryGrainAdmin(admin.ModelAdmin):
    icon_name='blur_circular'

@register(TypeGrain)
class TypeGrainAdmin(admin.ModelAdmin):
    icon_name='blur_circular'

@register(AnalysisGrain)
class AnalysisGrainAdmin(admin.ModelAdmin):
    icon_name='search'
    inlines = [ PercentageTypeGrainInline, ]

# site.register(Grain)
# site.register(TypeGrain)
# site.register(SampleGrain)
# site.register(AnalysisGrain)


