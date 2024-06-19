from django.urls import path
from app.api import views

urlpatterns = [
    path('party/', views.PoliticalParty_list),
    path('mp/', views.MP_list),
    path('place/', views.place_list),
    path('sector/', views.sector_list),
    
]