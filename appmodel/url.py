from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^n1/', views.add_model),
]