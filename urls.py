from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ServiceViewSet, AdvertisingCampaignViewSet, PotentialClientViewSet,
    ContractViewSet, ActiveClientViewSet
)
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
)
from rest_framework.routers import DefaultRouter
from .views import (
    ServiceViewSet, AdvertisingCampaignViewSet, PotentialClientViewSet,
    ContractViewSet, ActiveClientViewSet
)



urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', include('crm.urls')),
]


router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'campaigns', AdvertisingCampaignViewSet)
router.register(r'potential_clients', PotentialClientViewSet)
router.register(r'contracts', ContractViewSet)
router.register(r'active_clients', ActiveClientViewSet)

]
