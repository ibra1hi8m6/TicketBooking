from django.urls import path
from . import views
    #MainPage
urlpatterns = [ 
    path ('MainPage/', views.MainPage, name = ' main page' ),

    #LoginPage
    path ('LoginPage/', views.LoginPage, name = 'login page'),

    #SignupPage
    path ('SignupPage/', views.SignupPage, name = 'Signup page'),

    #Payment
    path ('Payment/', views.Payment, name = 'payment'),
    

    #NFL
    path ('MainPage/NFLMainPage/', views.NFLMainPage, name = ' NFL main page' ),
    path ('MainPage/NFLMainPage/NFLTicket1/', views.NFLTicket1, name = 'NFL Ticket 1'),
    path ('MainPage/NFLMainPage/NFLTicket2/', views.NFLTicket2, name = 'NFL Ticket 2'),
    path ('MainPage/NFLMainPage/NFLTicket3/', views.NFLTicket3, name = 'NFL Ticket 3'),
    path ('MainPage/NFLMainPage/NFLTicket4/', views.NFLTicket4, name = 'NFL Ticket 4'),
    path ('MainPage/NFLMainPage/NFLTicket5/', views.NFLTicket5, name = 'NFL Ticket 5'),
    path ('MainPage/NFLMainPage/NFLTicket6/', views.NFLTicket6, name = 'NFL Ticket 6'),


    #MLB
    path ('MainPage/MLBMainPage/', views.MLBMainPage, name = 'MLB main page'),
    path ('MainPage/MLBMainPage/MLBTicket1/', views.MLBTicket1, name = 'MLB Ticket 1'),
    path ('MainPage/MLBMainPage/MLBTicket2/', views.MLBTicket2, name = 'MLB Ticket 2'),
    path ('MainPage/MLBMainPage/MLBTicket3/', views.MLBTicket3, name = 'MLB Ticket 3'),
    path ('MainPage/MLBMainPage/MLBTicket4/', views.MLBTicket4, name = 'MLB Ticket 4'),
    path ('MainPage/MLBMainPage/MLBTicket5/', views.MLBTicket5, name = 'MLB Ticket 5'),
    path ('MainPage/MLBMainPage/MLBTicket6/', views.MLBTicket6, name = 'MLB Ticket 6'),


    #Tennis
    path ('MainPage/TennisMainPage/', views.TennisMainPage, name = 'TennisMainPage'),
    path ('MainPage/TennisMainPage/TennisTicket1/', views.TennisTicket1, name = 'Tennis Ticket 1'),
    path ('MainPage/TennisMainPage/TennisTicket2/', views.TennisTicket2, name = 'Tennis Ticket 2'),
    path ('MainPage/TennisMainPage/TennisTicket3/', views.TennisTicket3, name = 'Tennis Ticket 3'),
    path ('MainPage/TennisMainPage/TennisTicket4/', views.TennisTicket4, name = 'Tennis Ticket 4'),
    path ('MainPage/TennisMainPage/TennisTicket5/', views.TennisTicket5, name = 'Tennis Ticket 5'),
    path ('MainPage/TennisMainPage/TennisTicket6/', views.TennisTicket6, name = 'Tennis Ticket 6'),


    #NBA
    path ('MainPage/NBAMainPage/', views.NBAMainPage, name = 'NBAMainPage'),
    path ('MainPage/NBAMainPage/NBATicket1/', views.NBATicket1, name = 'NBA Ticket 1'),
    path ('MainPage/NBAMainPage/NBATicket2/', views.NBATicket2, name = 'NBA Ticket 2'),
    path ('MainPage/NBAMainPage/NBATicket3/', views.NBATicket3, name = 'NBA Ticket 3'),
    path ('MainPage/NBAMainPage/NBATicket4/', views.NBATicket4, name = 'NBA Ticket 4'),
    path ('MainPage/NBAMainPage/NBATicket5/', views.NBATicket5, name = 'NBA Ticket 5'),
    path ('MainPage/NBAMainPage/NBATicket6/', views.NBATicket6, name = 'NBA Ticket 6'),
    
]