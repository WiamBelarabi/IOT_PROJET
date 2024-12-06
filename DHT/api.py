from .models import Dht11
from .serializers import DHT11Serializer
from rest_framework.decorators import api_view
from rest_framework import status, generics
from rest_framework.response import Response
from twilio.rest import Client
@api_view(["GET", "POST"])
def send_telegram_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    response = send_telegram_message.requests.post(url, data=payload)
    return response

class DhtCreateView(generics.CreateAPIView):
    queryset = Dht11.objects.all()
    serializer_class = DHT11Serializer

def Dlist(request):
    if request.method == "GET":
        all_data = Dht11.objects.all()
        data_ser = DHT11Serializer(all_data, many=True)  # Les données sont sérialisées en JSON
        return Response(data_ser.data)

    elif request.method == "POST":
        serial = DHT11Serializer(data=request.data)

        if serial.is_valid():
            serial.save()
            derniere_temperature = Dht11.objects.last().temp
            print(derniere_temperature)

            if serial.is_valid():
                serial.save()
                derniere_temperature = Dht11.objects.last().temp
                print(derniere_temperature)

                if derniere_temperature > 25:
                    # Alert WhatsApp
                    account_sid = 'AC976fb865e1ca0f789bd0f7d1f2c53152'
                    auth_token = '33ccc2d7e85397335ee5a1d064127a53'
                    client = Client(account_sid, auth_token)
                    message_whatsapp = client.messages.create(
                        from_='whatsapp:+14155238886',
                        body='La température dépasse le seuil de 25°C, veuillez intervenir immédiatement pour vérifier et corriger cette situation',
                        to='whatsapp:+212762374139'
                    )
                    # Alert Telegram
                    telegram_token = '7363928154:AAG2ZzinL2AUDbYXzxYVxlw_Vp_sPKFioqE'
                    chat_id = '6791282158'
                    telegram_message = 'La température dépasse le seuil de 25°C, veuillez intervenir immédiatement pour vérifier et corriger cette situation'
                    response=send_telegram_message(telegram_token, chat_id, telegram_message)

                return Response(serial.data, status=status.HTTP_201_CREATED)

            else:
                return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
