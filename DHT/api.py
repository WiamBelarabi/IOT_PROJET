from .models import Dht11
from .serializers import DHT11Serializer
from rest_framework.decorators import api_view
from rest_framework import status, generics
from rest_framework.response import Response
from twilio.rest import Client
@api_view(["GET", "POST"])
class DhtCreateView(generics.CreateAPIView):
    queryset = Dht11.objects.all()
    serializer_class = DHT11Serializer

def Dlist(request):
    if request.method == "GET":
        all_data = Dht11.objects.all()
        data_ser = DHT11Serializer(all_data, many=True)  # Serialize all data in JSON
        return Response(data_ser.data)

    elif request.method == "POST":
        serial = DHT11Serializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)


# Alertwhatsapp
account_sid = 'AC976fb865e1ca0f789bd0f7d1f2c53152'
auth_token = '33ccc2d7e85397335ee5a1d064127a53'
client = Client(account_sid, auth_token)
message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='La température dépasse le seuil,veuillez intervenir immédiatement',
    to='whatsapp:+212762374139'
)

