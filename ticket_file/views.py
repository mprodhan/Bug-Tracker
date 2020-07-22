from django.shortcuts import render, reverse, HttpResponseRedirect, HttpResponse
from ticket.models import Ticket
from custom_user.models import BugUser
from ticket_file.forms import TicketSubmit
from django.contrib.auth.decorators import login_required

# @login_required
def ticketcreation(request):
    if request.method == "POST":
        form = TicketSubmit(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ticket_submit = BugUser.objects.get(id=request.user.id)
            ticket = Ticket.objects.create(
                username = ticket_submit,
                title = data["title"],
                bug = data["bug"]
            )
            return HttpResponseRedirect(reverse("submitpage", kwargs={"id": ticket.id}))
    form = TicketSubmit()
    return render(request, "generic_form.html", {"form": form})

# @login_required
def in_progress_view(request, id):
    ticket = Ticket.objects.get(id=id)
    ticket.assigned_user = request.user
    ticket.completed_by = None
    ticket.ticket_status = "IP"
    ticket.save()
    return HttpResponseRedirect(reverse("homepage"))

# @login_required
def doneview(request, id):
    ticket = Ticket.objects.get(id=id)
    ticket.assigned_user = None
    ticket.completed_by = request.user
    ticket.ticket_status = "DO"
    ticket.save()
    return HttpResponseRedirect(reverse("homepage"))

# @login_required
def invalidview(request, id):
    ticket = Ticket.objects.get(id=id)
    ticket.assigned_user = None
    ticket.completed_by = None
    ticket.ticket_status = "IN"
    ticket.save()
    return HttpResponseRedirect(reverse("homepage"))


# This function will view the ticket submission from ticketcreation fucntion.
# This is also the ticketdetail page.
# @login_required
def submissionview(request, id):
    buguser = BugUser.objects.filter(id=request.user.id)
    data = Ticket.objects.get(id=id)
    return render(request, "submitview.html", {"buguser": buguser, "data": data})

# This is the profile of the user and the tickets that they filed, worked and resolved.
# @login_required
def userview(request, id):
    username = BugUser.objects.get(id=id)
    data = Ticket.objects.filter(username=username)
    return render(request, "profile.html", {"username": username, "data": data})

# This view edits the tickets.
# @login_required
def ticket_edit(request, id):
    ticket = Ticket.objects.get(id=id)
    if request.method == "POST":
        form = TicketSubmit(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ticket.title = data["title"],
            ticket.bug = data["bug"],
            ticket.save()
            return HttpResponseRedirect(reverse('submitpage', args=(id,)))
    form = TicketSubmit(initial={
        'title': ticket.title,
        'bug': ticket.bug,
    })
    return render(request, "generic_form.html", {"form": form})
