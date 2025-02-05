from django.urls import path, include
from .views import service_list, service_detail, service_create, service_update, service_delete
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crm_app.urls')),
    path('services/', service_list, name='service_list'),
    path('services/<int:pk>/', service_detail, name='service_detail'),
    path('services/create/', service_create, name='service_create'),
    path('services/<int:pk>/edit/', service_update, name='service_update'),
    path('services/<int:pk>/delete/', service_delete, name='service_delete'),
]
