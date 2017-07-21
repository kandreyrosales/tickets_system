from django.shortcuts import render, redirect
from apps.tickets.forms import TicketForm, TicketUpdateForm
from apps.tickets.models import Ticket
from django.shortcuts import get_object_or_404, Http404
from django.http.response import JsonResponse
from django.db.models import Q
from django.views.generic import View, DetailView
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy


def index(request):
    return render(request, 'ticket/index.html')


def ticket_new(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('ticket:ticket_list')
    else:
        form = TicketForm()
    return render(request, 'ticket/tickets_form.html', {'form': form})


def ticket_list(request):
    tickets = Ticket.objects.filter(created_by=request.user)
    return render(request, 'ticket/ticket_list.html', {'tickets': tickets})


def ticket_agent_list(request):
    group_list = request.user.groups.values_list('name', flat=True)
    group_user = ""
    if "agent" in group_list:
        group_user = "agent"
    if "customer" in group_list:
        group_user = "customer"
    tickets = Ticket.objects.filter(Q(agent__isnull=True)|Q(agent=request.user))
    return render(request, 'ticket/ticket_agent_list.html', {'tickets':tickets, 'group_user': group_user})


def change_status_ticket(request):
    status = False
    if request.is_ajax() and request.GET:
        ticket_id = request.GET.get('id_ticket')
        try:
            tck = get_object_or_404(Ticket, id=ticket_id)
            tck.status = 'IP'
            tck.agent = request.user
            tck.save()
            status = True
        except:
            status = False

    return JsonResponse({"status": status})


def ticket_detail_view(request, pk):
    try:
        ticket_id = Ticket.objects.get(pk=pk)
    except Ticket.DoesNotExist:
        raise Http404("Book does not exist")

    return render(
        request,
        'ticket/ticket_detail.html',
        context={'ticket': ticket_id, }
    )


class TicketDetailView(DetailView):
    model = Ticket


def ticket_update(request, pk, template_name='ticket/ticket_update.html'):
    ticket = get_object_or_404(Ticket, pk=pk)
    print(ticket)
    form = TicketUpdateForm(request.POST or None, instance=ticket)
    if form.is_valid():
        form.save()
        return redirect('ticket:ticket_agent_list')
    return render(request, template_name, {'form':form})



