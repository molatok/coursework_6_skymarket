from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/redoc-tasks/", include("redoc.urls")),
    path("api/shema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/shema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema")),
    path("", include('users.urls')),
    path("", include('ads.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)