from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include
from jokes import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('users/', include('jokes.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('api/random/', views.random_number_api, name='random_number_api'),

]
