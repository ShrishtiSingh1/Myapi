from .models import Item
from .serializers import ItemSerializer

def get_all_items():
    return Item.objects.all()

def create_item(data):
    serializer = ItemSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return serializer
    return None
