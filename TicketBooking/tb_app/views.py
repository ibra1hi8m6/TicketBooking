from django.shortcuts import render
from .models import *
from django.contrib import messages
from . import models
#MainPage
def MainPage (request):
   return render (request,'tb_app/MainPage.html')

#LoginPage  

def LoginPage (request):
   if request.method == "POST":
      name = request.POST.get('username')
      password = request.POST.get('password')
      print('name= '+name + 'password ='+password)
      if name==password:
         messages.add_message(request, messages.INFO, 'Invalid data', extra_tags='Invalid data')
      else:
         messages.add_message(request, messages.INFO, 'Login successfully',extra_tags='login')
         data = CustomerLogin(  Password=password, UserName=name)
         data.save()
      


   return render (request,'tb_app/LoginPage.html') 


#SignupPage  

def SignupPage (request):
   if request.method == "POST":
      name = request.POST.get('name')
      email = request.POST.get('email')
      password = request.POST.get('password')
      password2 = request.POST.get('password2')
      if password!=password2:
         messages.add_message(request, messages.INFO, 'Password Does Not Match', extra_tags='Invalid data')
      else :
         messages.add_message(request, messages.INFO, 'Signed-up Successfully',extra_tags='login')
         data = CustomerSignup( Email=email, Password=password, UserName=name,Password2=password2) 
         data.save()
   return render (request,'tb_app/SignupPage.html') 

#Payment   

def Payment (request):
   if request.method == "POST":
         email = request.POST.get('email')
         numberCard = request.POST.get('numberCard')
         month = request.POST.get('month')
         NmaeOnCard = request.POST.get('NmaeOnCard')
         cvc=request.POST.get('cvc')
      
         messages.add_message(request, messages.INFO, 'Passwords  do not match')
      
         data = models.Payment( Emailcard=email, Cardnumber=numberCard, NameCard=NmaeOnCard,Expirycard=month ,CVVcard=cvc ) 
         data.save()
   return render (request,'tb_app/Payment.html')

#NFL
def NFLMainPage (request):
   return render (request,'tb_app/NFLMainPage.html')

def TicketPageNFL (request):
   return render (request,'tb_app/TicketPageNFL.html')
   
def NFLTicket1 (request):
   return render (request,'tb_app/NFL Ticket 1.html')   

def NFLTicket2 (request):
   return render (request,'tb_app/NFL Ticket 2.html') 

def NFLTicket3 (request):
   return render (request,'tb_app/NFL Ticket 3.html') 

def NFLTicket4 (request):
   return render (request,'tb_app/NFL Ticket 4.html') 

def NFLTicket5 (request):
   return render (request,'tb_app/NFL Ticket 5.html') 

def NFLTicket6 (request):
   return render (request,'tb_app/NFL Ticket 6.html') 
      

#MLB
def MLBMainPage (request):
   return render (request,'tb_app/MLBMainPage.html')    

def MLBTicket1 (request):
   return render (request,'tb_app/MLB Ticket 1.html') 

def MLBTicket2 (request):
   return render (request,'tb_app/MLB Ticket 2.html')    

def MLBTicket3 (request):
   return render (request,'tb_app/MLB Ticket 3.html') 

def MLBTicket4 (request):
   return render (request,'tb_app/MLB Ticket 4.html') 

def MLBTicket5 (request):
   return render (request,'tb_app/MLB Ticket 5.html')

def MLBTicket6 (request):
   return render (request,'tb_app/MLB Ticket 6.html')  


#Tennis
def TennisMainPage (request):
   return render (request,'tb_app/TennisMainPage.html')

def TennisTicket1 (request):
   return render (request,'tb_app/Tennis Ticket 1.html')

def TennisTicket2 (request):
   return render (request,'tb_app/Tennis Ticket 2.html')

def TennisTicket3 (request):
   return render (request,'tb_app/Tennis Ticket 3.html')

def TennisTicket4 (request):
   return render (request,'tb_app/Tennis Ticket 4.html')

def TennisTicket5 (request):
   return render (request,'tb_app/Tennis Ticket 5.html')

def TennisTicket6 (request):
   return render (request,'tb_app/Tennis Ticket 6.html')


#NBA
def NBAMainPage (request):
   return render (request,'tb_app/NBAMainPage.html')

def NBATicket1 (request):
   return render (request,'tb_app/NBA Ticket 1.html')

def NBATicket2 (request):
   return render (request,'tb_app/NBA Ticket 2.html')

def NBATicket3 (request):
   return render (request,'tb_app/NBA Ticket 3.html')

def NBATicket4 (request):
   return render (request,'tb_app/NBA Ticket 4.html')

def NBATicket5 (request):
   return render (request,'tb_app/NBA Ticket 5.html')

def NBATicket6 (request):
   return render (request,'tb_app/NBA Ticket 6.html')
   

