from django.contrib import admin
from material.admin.decorators import register
from material.admin.sites import site
from django.utils.safestring import mark_safe

# from django.utils.translation import ugettext_lazy as _

from .models import Quinua
from .models import Sample

class SampleInline(admin.TabularInline):
    model = Sample
    extra = 0

@register(Quinua)
class QuinuaAdmin(admin.ModelAdmin):
    icon_name = 'bubble_chart'
    list_display = ('name', 'uuid', 'datetimer',)
    fields = ['name',]
    search_fields = ['name']
    inlines =[SampleInline, ]

@register(Sample)
class SampleAdmin(admin.ModelAdmin):
    icon_name='blur_on'
    list_display = ['quinua_name', 'uuid', 'broken_grain', 'damaged_grain', 'immature_grain',
    'coated_grain', 'germinated_grain', 'whole_grain',]
    readonly_fields = ('quinua_image',)
    fields = ['quinua', 'image', 'quinua_image','broken_grain', 'damaged_grain',
    'immature_grain', 'coated_grain', 'germinated_grain', 'whole_grain', 'total',]

    def quinua_name(self, obj):
        return obj.quinua.name
    quinua_name.short_description = 'Quinua'
    quinua_name.admin_order_field = 'quinua__name'

    def quinua_image(self, obj):
        return mark_safe('<img class="responsive-img" src="{url}" width="{width}" height={height} />'.format(
            url = obj.image.url,
            width=obj.image.width,
            height=obj.image.height,
            )
    ) 
