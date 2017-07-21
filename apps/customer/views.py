from django.contrib.auth.models import User
from apps.customer.forms import RegisterCustomerForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy


class RegisterCustomer(CreateView):
    model = User
    template_name = 'customer/register_customer.html'
    form_class = RegisterCustomerForm
    success_url = reverse_lazy('ticket:ticket_list')
