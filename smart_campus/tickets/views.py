from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django.views.decorators.cache import cache_page
from .models import Ticket
from .serializers import TicketSerializer
from django.core.cache import cache



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@cache_page(60)   # cache for 60 seconds
def ticket_list(request):

    if request.method == 'GET':

        tickets = Ticket.objects.all()

        #Filtering
        category = request.query_params.get('category')

        if category:
            tickets = tickets.filter(category=category)

        

        #Search
        search = request.query_params.get('search')
        if search:
            tickets = tickets.filter(title__icontains=search) | \
                      tickets.filter(description__icontains=search)

        #Ordering
        ordering = request.query_params.get('ordering')
        if ordering:
            tickets = tickets.order_by(ordering)

        #Pagination
        paginator = PageNumberPagination()
        paginator.page_size = 2
        paginated_tickets = paginator.paginate_queryset(tickets, request)

        serializer = TicketSerializer(paginated_tickets, many=True)

        return paginator.get_paginated_response(serializer.data)



    if request.method == 'POST':
        serializer = TicketSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            cache.clear()   #clear redis cache
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)



@api_view(['GET', 'PUT', 'POST','PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
@cache_page(60)
def ticket_detail(request, id):

    try:
        ticket = Ticket.objects.get(id=id)
    except Ticket.DoesNotExist:
        return Response({'error': 'Ticket not found'}, status=404)

    # GET
    if request.method == 'GET':
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)

    # PUT (Full Update)
    if request.method == 'PUT':
        serializer = TicketSerializer(ticket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache.clear()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    # PATCH (Partial Update)
    if request.method == 'PATCH':
        serializer = TicketSerializer(ticket, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            cache.clear()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    # DELETE
    if request.method == 'DELETE':
        ticket.delete()
        cache.clear()
        return Response({'message': 'Ticket deleted successfully'})