from .models import User,Deal,Message,Start
from rest_framework import serializers


class DealSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Deal
        fields = '__all__'

    def create(self, validated_data):
        return Deal.objects.create(**validated_data) 


class MessageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Message
        fields = '__all__'

    def create(self, validated_data):
        return Message.objects.create(**validated_data) 


class StartSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Start
        fields = '__all__'

    def create(self, validated_data):
        return Start.objects.create(**validated_data) 



class UserSerializer(serializers.ModelSerializer):
    
    class Meta: 

        model = User
        fields = ('id','Name', 'Email', 'Pass','Activate','Role') 
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return User.objects.filter(pk=instance).update(**validated_data)