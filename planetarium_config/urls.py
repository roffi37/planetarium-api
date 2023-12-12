from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/planetarium/", include("planetarium.urls", namespace="planetarium")),
    path("api/user/", include("user.urls", namespace="user")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/doc/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"),
    path("api/doc/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("__debug__/", include("debug_toolbar.urls")),
]
