from rest_framework import serializers
from.models import user,user2,log,food,accepting


    #  donar
class userserializer(serializers.ModelSerializer):
    class Meta:
        model=user
        fields='__all__'
    def Create (self,validated_data):
        return user.objects.Create(**validated_data)

    #   receiver     
class userserializers(serializers.ModelSerializer):
    class Meta:
        model=user2
        fields='__all__'
    def Create (self,validated_data):
        return user.objects.Create(**validated_data)
    
class logserializer(serializers.ModelSerializer):
    class Meta:
        model=log
        fields='__all__'
    def Create (self,validated_data):
        return log.objects.Create(**validated_data)
    

class foodserializer(serializers.ModelSerializer):
    class Meta:
        model=food
        fields='__all__'
    def Create (self,validated_data):
        return food.objects.Create(**validated_data)   
    

class acceptingserializer(serializers.ModelSerializer):
    class Meta:
        model=accepting
        fields='__all__'
    def Create (self,validated_data):
        return accepting.objects.Create(**validated_data)