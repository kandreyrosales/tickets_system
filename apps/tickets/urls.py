from django.conf.urls import url, include
from apps.tickets.views import index, ticket_new, ticket_list, ticket_agent_list, change_status_ticket, TicketDetailView, ticket_detail_view, ticket_update
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^new/', login_required(ticket_new), name='ticket_new'),
    url(r'^list/', login_required(ticket_list), name='ticket_list'),
    url(r'^agent_list/', login_required(ticket_agent_list), name='ticket_agent_list'),
    url(r'^change_status_ticket/', change_status_ticket, name='change_status_ticket'),
    url(r'^detail/(?P<pk>\d+)$', ticket_detail_view, name='ticket_detail'),
    url(r'^update/(?P<pk>\d+)$', ticket_update, name='ticket_update')
]
