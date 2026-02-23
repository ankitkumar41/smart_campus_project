from django.urls import path
from . import views
urlpatterns = [
 path('tickets/', views.ticket_list),
    path('tickets/<int:id>/', views.ticket_detail),
]