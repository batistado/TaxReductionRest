from django.conf.urls import url
from taxreductionapp import views

urlpatterns = [
    url(r'^properties/(?P<pk>[0-9]+)$', views.property_detail),
]
