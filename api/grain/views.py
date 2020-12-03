from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.conf import	settings
from django.http import	HttpResponse
from django.template.loader import render_to_string
from django.conf import settings
from utils.image64 import encode_image
from utils.pdf_weasyprint import django_url_fetcher
import weasyprint

from .models import SampleGrain
from .models import SampleDetailGrain
from .models import AnalysisGrain
from .models import PercentageTypeGrain
from .models import TypeGrain

# Create your views here.
def var_dinamic(inp, val):
    inp = val
    return inp

def admin_analysis_pdf(request, sample_id):
    sample = get_object_or_404(SampleGrain, id=sample_id)
    detail_sample = list(SampleDetailGrain.objects.filter(sample=sample_id))
    c = 0
    detail = []
    one = []
    two = []
    for d in detail_sample:
        if c <= 11:
            one.append(d)
        elif c >= 11:
            two.append(d)
        c += 1
    if len(one):
        detail.append(one)
    if len(two):
        detail.append(two)

    analysis = get_object_or_404(AnalysisGrain, sample=sample_id)
    percent_grain = list(
            PercentageTypeGrain.objects.filter(analysis_percent_grain=analysis.id)
    )
    types = TypeGrain.objects.filter(status=True)
    dict_types = {}
    for t in types:
        name_type = t.name_type.replace(' ', '_').lower()
        dict_types[name_type] = 00.0

    for pg in percent_grain:
        name_type_sub = pg.percent_type_grain.name_type.replace(' ', '_').lower()
        dict_types[name_type_sub] = pg.percentage


    image_64 = encode_image(sample.image)
    
    html_str = render_to_string(
        'grain/pdf_grain.html', {
            'sample':sample, 'image': image_64, 'details': detail,
            'all_percents': dict_types,
        }
    )
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] ='filename=\"analysis_{}.pdf"'.format(
        sample.id
    )

    html = weasyprint.HTML(
        string=html_str, base_url=request.build_absolute_uri('/'),
        url_fetcher=django_url_fetcher
    )

    html.write_pdf(
        response,
        stylesheets=[
            weasyprint.CSS(settings.STATIC_ROOT + 'grain/pdf_intro.css')
        ]
    )

    return response
