from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import SimpleRouter
from django.views.decorators.csrf import csrf_exempt
from . import views
from . import apiviews

app_name="home"
urlpatterns = [
    path('',views.HomeView.as_view(),name="home"),
    path('place-art-order/',views.PlaceOrderView.as_view(),name="place-art-order"),
    path('version/',views.GetVersion.as_view(),name="version")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
