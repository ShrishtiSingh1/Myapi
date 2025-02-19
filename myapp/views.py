from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .services import get_all_items, create_item
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the homepage of the API!")

@api_view(['GET', 'POST'])
def item_list(request):
    if request.method == 'GET':
        items = get_all_items()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = create_item(request.data)
        if serializer:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)
