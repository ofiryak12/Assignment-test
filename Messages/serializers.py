from rest_framework import serializers
from .models import Data_msg

class DataSerializer_readall(serializers.ModelSerializer):
    class Meta:
        model = Data_msg
        fields = ['id','sender','reciever','subject','message','read','creation_Date']

class DataSerializer_write(serializers.ModelSerializer):
    class Meta:
        model = Data_msg
        fields = ['reciever', 'subject', 'message', 'creation_Date']
    # sender = serializers.CharField(max_length=100)
    # reciever = serializers.CharField(max_length=100)
    # message = serializers.TextField()
    # subject = serializers.CharField(max_length=50)
    # creation_Date = serializers.DateTimeField()
    #
    # def create(self, validated_data):
    #     return Data.objects.create(validated_data)
    #
    # def update(self, instance, validated_data):
    #      instance.sender = validated_data.get('sender',instance.sender)
    #      instance.reciever = validated_data.get('reciever', instance.reciever)
    #      instance.message = validated_data.get('message', instance.message)
    #      instance.subject = validated_data.get('subject', instance.subject)
    #      instance.creation_Date = validated_data.get('creation_Date', instance.creation_Date)
    #      instance.save()
    #      return instance