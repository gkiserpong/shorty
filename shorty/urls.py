from django.urls import path

from shorty.views import RedirectView


app_name = "shorty"

urlpatterns = [
    path("<slug:short>/", RedirectView.as_view(), name="index")
    ]