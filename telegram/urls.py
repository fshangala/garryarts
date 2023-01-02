from django.urls import path
from telegram.views import GetUpdate

app_name="telegram"
urlpatterns = [
    path("get-update/",GetUpdate.as_view(),name="getUpdate")
]