from django.conf.urls import url
from taxreductionapp import views

urlpatterns = [
    url(r'^properties/(?P<propertyID>[0-9]+)$', views.property_by_id),
    url(r'^properties/lookup$',
        views.property_by_address),
]
