from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import AutomationView, HomeView, SobreView, PrivacyPolicyView, DataDeletionView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('automacao/', AutomationView.as_view(), name='automacao'),
    path('politica-de-privacidade/', PrivacyPolicyView.as_view(), name='politica-de-privacidade'),
    path('exclusao-de-dados/', DataDeletionView.as_view(), name='exclusao-de-dados'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

