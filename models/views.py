from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from models.models import MyUser, Trip, Journey
from models.serializers import MyUserSerializer, TripSerializer, JourneySerializer


#adaugare si luare de utilizatori
@api_view(['GET', 'POST'])
def myUsersList(request):
    if request.method == "GET":
        users = MyUser.objects.all()
        usersSerailizer = MyUserSerializer(users, many=True)
        return JsonResponse(usersSerailizer.data, safe=False)


    elif request.method == 'POST':
        user = JSONParser().parse(request)
        userSer = MyUserSerializer(data=user)

        if  userSer.is_valid():
            userSer.save()
            return JsonResponse( userSer.data, status=status.HTTP_201_CREATED)
        print( userSer.errors)
        return JsonResponse( userSer.errors, status=status.HTTP_400_BAD_REQUEST)

#luare utilizator in functie de email
@api_view(['GET'])
def userDetail(request, email):
    if request.method == 'GET':
        user = MyUser.objects.filter(email=email)
        usersSerailizer =MyUserSerializer(user, many=True)
        return JsonResponse(usersSerailizer.data, safe=False)





#actualizare utilizator in functie de id
@api_view(['PUT'])
def userPass(request, pk):
    try:
        user = MyUser.objects.get(id=pk)
    except user.DoesNotExist:
        return JsonResponse({'message': 'User does not exist!'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        new_user= JSONParser().parse(request)

        userserializer = MyUserSerializer(user,data=new_user)
        if userserializer.is_valid():
            userserializer.save()
            return JsonResponse(userserializer.data)
        return JsonResponse(userserializer.errors, status=status.HTTP_400_BAD_REQUEST)


#luare tripin functie de tara
@api_view(['GET'])
def tripDetailCountry(request, country):
    if request.method == 'GET':
        tr = Trip.objects.filter(country=country)
        tripSerailizer =TripSerializer(tr, many=True)
        return JsonResponse(tripSerailizer.data, safe=False)


#luare si adugare trip
@api_view(['GET','POST'])
def tripList(request):
    if request.method == "GET":
        trips= Trip.objects.all()
        tripsSerailizer = TripSerializer(trips, many=True)
        return JsonResponse(tripsSerailizer.data, safe=False)


    elif request.method == 'POST':
        trip = JSONParser().parse(request)
        print(trip)
        tripSer = TripSerializer(data=trip)
        if  tripSer.is_valid():
            tripSer.save()
            return JsonResponse( tripSer.data, status=status.HTTP_201_CREATED)
        print( tripSer.errors)
        return JsonResponse( tripSer.errors, status=status.HTTP_400_BAD_REQUEST)

#ia tripul dupa id
@api_view(['GET','DELETE', 'PUT'])
def tripDetail(request, pk):
    try:
        trip = Trip.objects.get(id=pk)
    except trip.DoesNotExist:
        return JsonResponse({'message': 'Trip does not exist!'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        tripSerailizer =TripSerializer(trip)
        print(tripSerailizer)
        return JsonResponse(tripSerailizer.data, safe=False)

    elif request.method == 'DELETE':
        trip.delete()
        return JsonResponse({'message': 'Trip was deleted succesfully!'},
                            status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        new_trip= JSONParser().parse(request)
        print(new_trip)
        tripserializer = TripSerializer(trip ,data=new_trip)
        if tripserializer.is_valid():
            tripserializer.save()
            return JsonResponse(tripserializer.data)
        return JsonResponse(tripserializer.errors, status=status.HTTP_400_BAD_REQUEST)


#ia toate tripurile dintr un jouney
@api_view(['GET'])
def tripJourneyDetail(request, id_trip):
    if request.method == 'GET':
        tr = Trip.objects.filter(id_journey=id_trip)
        tripSerailizer =TripSerializer(tr, many=True)
        return JsonResponse(tripSerailizer.data, safe=False)



#luare journy-urile in functie de id_user
@api_view(['GET'])
def userJourneyDetail(request, id_user):
    if request.method == 'GET':
        tr = Journey.objects.filter(id_user=id_user)
        tripSerailizer =JourneySerializer(tr, many=True)
        return JsonResponse(tripSerailizer.data, safe=False)




#luare si adugare jouney
@api_view(['GET','POST'])
def journeyList(request):
    if request.method == "GET":
        trips= Journey.objects.all()
        tripsSerailizer = JourneySerializer(trips, many=True)
        return JsonResponse(tripsSerailizer.data, safe=False)


    elif request.method == 'POST':
        trip = JSONParser().parse(request)
        print(trip)
        tripSer = JourneySerializer(data=trip)
        print(tripSer)
        if  tripSer.is_valid():
            tripSer.save()
            return JsonResponse( tripSer.data, status=status.HTTP_201_CREATED)
        print( tripSer.errors)
        return JsonResponse( tripSer.errors, status=status.HTTP_400_BAD_REQUEST)


#stergere,luare si actualizare jouney in functie de id
@api_view(['GET','DELETE', 'PUT'])
def journeyDetail(request, pk):
    try:
        trip = Journey.objects.get(id=pk)
    except trip.DoesNotExist:
        return JsonResponse({'message': 'Trip does not exist!'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        tripSerailizer =JourneySerializer(trip)
        print(tripSerailizer)
        return JsonResponse(tripSerailizer.data, safe=False)

    elif request.method == 'DELETE':
        trip.delete()
        return JsonResponse({'message': ' Trip was deleted succesfully!'},
                            status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        new_trip= JSONParser().parse(request)
        print(new_trip)
        tripserializer = JourneySerializer(trip ,data=new_trip)
        if tripserializer.is_valid():
            tripserializer.save()
            return JsonResponse(tripserializer.data)
        return JsonResponse(tripserializer.errors, status=status.HTTP_400_BAD_REQUEST)