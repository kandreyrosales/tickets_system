from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ticket/', include('apps.tickets.urls', namespace='ticket')),
    url(r'^customer/', include('apps.customer.urls', namespace='customer')),
    url(r'^agent/', include('apps.agents.urls', namespace='agent')),
    url(r'^$', login, {'template_name': 'index.html'}, name='login'),
]
