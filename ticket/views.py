from django.shortcuts import render
from ticket.models import Ticket
from django.contrib.auth.decorators import login_required

# @login_required
def index(request):
    data = Ticket.objects.filter(ticket_status="NE")
    assigned = Ticket.objects.filter(ticket_status="IP")
    done = Ticket.objects.filter(ticket_status="DO")
    invalid = Ticket.objects.filter(ticket_status="IN")
    return render(request, "index.html", {"data": data, "assigned": assigned,
        "done": done, "invalid": invalid})
