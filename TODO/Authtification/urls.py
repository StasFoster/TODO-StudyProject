from django.urls import path
from . import views

urlpatterns = [
    path('',views.enter, name="enter"),
    path('register/<string:mode>/', auth)
]
