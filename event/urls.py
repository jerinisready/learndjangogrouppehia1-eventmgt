from django.http import HttpResponse
from django.urls import path

from event.views import homepage, private_view

urlpatterns = [
    path('', homepage, name="home"),
    path('private-view/', private_view, name="private_view")
]
