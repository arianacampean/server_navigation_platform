from rest_framework import serializers

from models.models import MyUser, Trip, Journey


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=MyUser
        fields=('id','first_name','last_name','email','password')



class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trip
        fields=('id','id_journey','latitude','longitude','city','country','name','visited')

class JourneySerializer(serializers.ModelSerializer):
    class Meta:
        model=Journey
        fields=('id','id_user','start_date','end_date')