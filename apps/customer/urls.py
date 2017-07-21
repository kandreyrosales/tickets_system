from django.conf.urls import url, include
from apps.customer.views import RegisterCustomer

urlpatterns = [
    url(r'^register/', RegisterCustomer.as_view(), name='register_customer'),
]
