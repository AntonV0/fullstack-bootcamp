"""vendorEventRegister URL Configuration"""

from django.urls import path
from . import views

urlpatterns = [
    path("events/", views.EventListShowCreate.as_view(), name="event-show-post"),
    path("events/<int:id>/", views.SingleEventAccess.as_view(), name="event-single-access"),
]
