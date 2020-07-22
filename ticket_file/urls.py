from django.urls import path
from ticket_file import views

urlpatterns = [
    path('ticket_create/', views.ticketcreation),
    path('ticket_submit/<int:id>/', views.submissionview, name="submitpage"),
    path('profile/<int:id>/', views.userview),
    path('ticket_create/edit/<int:id>/', views.ticket_edit),
    path('in_progress/<int:id>/', views.in_progress_view),
    path('done/<int:id>/', views.doneview),
    path('invalid/<int:id>/', views.invalidview)
]