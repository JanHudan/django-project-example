from django.urls import path, include, re_path
# from django.views.generic import TemplateView

urlpatterns = [
    path('', include(('frontend.urls', 'frontend'), namespace='frontend')),
    path('api/', include(('api.urls', 'api'), namespace='api')),
]

# urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]
