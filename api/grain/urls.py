from django.urls import path

from .views import admin_analysis_pdf

app_name = 'grain'

urlpatterns = [
    path('analysis/<uuid:sample_id>/', 
        admin_analysis_pdf, name='admin_sample_pdf'
    ), 
]   
