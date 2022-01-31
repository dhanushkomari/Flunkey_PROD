from RestaurantApp.models import Delivery, Table, Vist
from BotsApp.models import Bot
from rest_framework import serializers

#...  Delivery Serializers ....................................
class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'

class DeliveryStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ('food_delivered',)
#..............................................................


#...  Bot Serializers .........................................

class BotStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bot
        fields = ('avialable',)

class BotBatterySerializer(serializers.ModelSerializer):
    class Meta:
        model = Bot
        fields = ('battery',)

class VistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vist
        fields = '__all__'
#..............................................................

#... Table Serializers ........................................
class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ('avialable',)
#..............................................................




    
