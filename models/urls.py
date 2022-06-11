from django.urls import path

from models import views

urlpatterns = [
    path('api/user', views.myUsersList),
    path('api/user/<str:email>',views.userDetail),
    path('api/user/pass/<int:pk>', views.userPass),
    path('api/trip', views.tripList),
    path('api/trip/<int:pk>', views.tripDetail),
    path('api/trip/<str:country>', views.tripDetailCountry),
    path('api/journey', views.journeyList),
    path('api/journey/user/<int:id_user>', views.userJourneyDetail),
    path('api/trip/journey/<int:id_trip>', views.tripJourneyDetail),
    path('api/journey/<int:pk>', views.journeyDetail)
]