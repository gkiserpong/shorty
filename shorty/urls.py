from django.urls import path

from shorty.views import DefaultView, RedirectView


app_name = "shorty"

urlpatterns = [
    path("<slug:short>/", RedirectView.as_view(), name="index"),
    path("", DefaultView.as_view(), name="default"),
    ]